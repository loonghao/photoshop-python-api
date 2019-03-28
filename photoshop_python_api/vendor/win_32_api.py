# Copyright (c) 2017 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
A minimal set of win32 functions to manage toolkit dialogs under Windows.
"""
import ctypes
from ctypes import wintypes

############################################################################
# user32.dll

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool,
                                     ctypes.POINTER(ctypes.c_int),
                                     ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
SendMessage = ctypes.windll.user32.SendMessageW
SendMessageTimeout = ctypes.windll.user32.SendMessageTimeoutW
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
SetParent = ctypes.windll.user32.SetParent
RealGetWindowClass = ctypes.windll.user32.RealGetWindowClassW
EnableWindow = ctypes.windll.user32.EnableWindow
IsWindowEnabled = ctypes.windll.user32.IsWindowEnabled
GetWindowLong = ctypes.windll.user32.GetWindowLongW
SetWindowLong = ctypes.windll.user32.SetWindowLongW

############################################################################
# kernal32.dll

CloseHandle = ctypes.windll.kernel32.CloseHandle
CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
Process32First = ctypes.windll.kernel32.Process32FirstW
Process32Next = ctypes.windll.kernel32.Process32NextW

############################################################################
# globals

TH32CS_SNAPPROCESS = 0x00000002
WM_GETTEXT = 0x000D
SMTO_ABORTIFHUNG = 0x0002
SMTO_BLOCK = 0x0001
GWL_EXSTYLE = -20
WS_EX_NOPARENTNOTIFY = 0x00000004
WS_EX_NOINHERITLAYOUT = 0x00100000


############################################################################
# structures

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes.DWORD),
        ("cntUsage", ctypes.wintypes.DWORD),
        ("th32ProcessID", ctypes.wintypes.DWORD),
        ("th32DefaultHeapID", ctypes.POINTER(ctypes.c_ulong)),
        ("th32ModuleID", ctypes.wintypes.DWORD),
        ("cntThreads", ctypes.wintypes.DWORD),
        ("th32ParentProcessID", ctypes.wintypes.DWORD),
        ("pcPriClassBase", ctypes.c_long),
        ("dwFlags", ctypes.wintypes.DWORD),
        ("szExeFile", ctypes.c_wchar * ctypes.wintypes.MAX_PATH),
    ]


############################################################################
# functions

def find_parent_process_id(process_id):
    """
    Find the parent process id for a given process

    :param int process_id: ID of the process to find the parent of.

    :returns: The parent process id or None if a parent isn't found.
    """
    parent_process_id = None

    try:
        h_process_snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)

        pe = PROCESSENTRY32()
        pe.dwSize = ctypes.sizeof(PROCESSENTRY32)
        ret = Process32First(h_process_snapshot, ctypes.byref(pe))

        while ret:
            if pe.th32ProcessID == process_id:
                parent_process_id = pe.th32ParentProcessID
                break

            ret = Process32Next(h_process_snapshot, ctypes.byref(pe))
    except Exception, e:
        pass
    else:
        CloseHandle(h_process_snapshot)

    return parent_process_id


def safe_get_window_text(hwnd):
    """
    Safely get the window text (title) of a specified window.

    :param hwnd: Window handle to get the text of.

    :returns: Window title, if found, otherwise an empty string.
    """
    title = ""

    try:
        buffer_sz = 1024
        unicode_buffer = ctypes.create_unicode_buffer(buffer_sz)
        result = SendMessageTimeout(
            hwnd,
            WM_GETTEXT,
            buffer_sz,
            ctypes.byref(unicode_buffer),
            SMTO_ABORTIFHUNG | SMTO_BLOCK,
            100,
            0,
        )

        if result != 0:
            title = unicode_buffer.value
    except Exception, e:
        pass

    return title


def find_windows(process_id=None, class_name=None, window_text=None,
                 stop_if_found=True):
    """
    Find top-level windows matching certain criteria.

    :param int process_id: Only match windows that belong to this process id if specified.
    :param str class_name: Only match windows that match this class name if specified.
    :param str window_text: Only match windows that match this window text if specified.
    :param bool stop_if_found: Stop as soon as a match is found.

    :returns: List of window handles found by search
    """
    found_hwnds = []

    # sub-function used to actually enumerate the windows in EnumWindows
    def enum_windows_proc(hwnd, lparam):
        # try to match process id:
        matches_proc_id = True
        if process_id != None:
            win_process_id = ctypes.c_long()
            GetWindowThreadProcessId(hwnd, ctypes.byref(win_process_id))
            matches_proc_id = (win_process_id.value == process_id)
        if not matches_proc_id:
            return True

        # try to match class name:
        matches_class_name = True
        if class_name != None:
            buffer_len = 1024
            unicode_buffer = ctypes.create_unicode_buffer(buffer_len)
            RealGetWindowClass(hwnd, unicode_buffer, buffer_len)
            matches_class_name = (class_name == unicode_buffer.value)
        if not matches_class_name:
            return True

        # try to match window text:
        matches_window_text = True
        if window_text != None:
            hwnd_text = safe_get_window_text(hwnd)
            matches_window_text = (window_text in hwnd_text)
        if not matches_window_text:
            return True

        # found a match    
        found_hwnds.append(hwnd)

        return not stop_if_found

    # enumerate all top-level windows:
    EnumWindows(EnumWindowsProc(enum_windows_proc), None)

    return found_hwnds


def qwidget_winid_to_hwnd(winid):
    """
    Convert the winid for a QWidget to an HWND.

    :param int winid: The QWidget winid to convert.

    :returns: Window handle
    """
    # Setup arguments and return types.
    ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
    ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]

    # Convert PyCObject to a void pointer.
    hwnd = ctypes.pythonapi.PyCObject_AsVoidPtr(winid)

    return hwnd

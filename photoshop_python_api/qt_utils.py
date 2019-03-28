# Import built-in modules
import logging

# Import local modules
from photoshop_python_api.vendor import win_32_api


def _get_photoshop_main_hwnd():
    """Windows specific method to find the main Photoshop window handle (HWND).

    Returns:
        Widget: find a HWND Widget or None.

    """
    found_hwnds = win_32_api.find_windows(class_name="Photoshop",
                                          stop_if_found=True)
    if found_hwnds:
        return found_hwnds[0]


def render_photoshop_widget(widget):
    """Parented Qt widget to the main Photoshop application.

    Windows-specific method to get the proxy window that will 'own' all
    dialogs. This will be parented to the main photoshop application.

    Args:
        widget (QWidgets.QWidget): The Qt widgets that need to be changed.

    Returns:
        QWidgets.QWidget: A QWidget that has been parented to Photoshop's
            window.

    """
    logger = logging.getLogger(__name__)
    ps_hwnd = _get_photoshop_main_hwnd()
    proxy_win_hwnd = None

    if ps_hwnd:
        proxy_win_hwnd = win_32_api.qwidget_winid_to_hwnd(
            widget.winId())
    else:
        logger.warning("Unable to determine the HWND of Photoshop it. "
                       "This means that we can't properly setup window "
                       "parenting for apps.")

    # Parent to the Photoshop application window if we found everything
    # we needed. If we didn't find our proxy window for some reason, we
    # will return None below. In that case, we'll just end up with no
    # window parenting, but apps will still launch.
    if proxy_win_hwnd is None:
        logger.warning("Unable setup window parenting properly. Dialogs "
                       "shown will not be parented to Photoshop, but they "
                       "will still function properly otherwise.")
    else:
        # Set the window style/flags. We don't need or want our Python
        # dialogs to notify the Photoshop application window when they're
        # opened or closed, so we'll disable that behavior.
        win_ex_style = win_32_api.GetWindowLong(proxy_win_hwnd,
                                                win_32_api.GWL_EXSTYLE)
        win_32_api.SetWindowLong(
            proxy_win_hwnd,
            win_32_api.GWL_EXSTYLE,
            win_ex_style | win_32_api.WS_EX_NOPARENTNOTIFY,
        )
        win_32_api.SetParent(proxy_win_hwnd, ps_hwnd)
    return widget

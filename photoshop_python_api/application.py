# Import third-party modules
import pywintypes
from win32com.client import Dispatch, GetActiveObject


class Application(object):
    object_name = 'Application'
    _root = 'Photoshop'

    def __init__(self, ps_version='2017'):
        self._version_id_mappings = {
            '2018': '120',
            '2017': '110',
            'cs6': '60'
        }
        self.version = ps_version
        self.app_id = self._version_id_mappings.get(self.version)
        self.progress_id = self._get_name(
            [self._root, self.object_name, self.app_id])
        try:
            self.app = GetActiveObject(self.progress_id)
        except pywintypes.com_error:
            self.app = Dispatch(self.progress_id)

    @property
    def document(self):
        return self.app.Document

    @property
    def active_document(self):
        return self.app.ActiveDocument

    @property
    def active_layer(self):
        return self.app.ArtLayer

    def active_layer_set(self):
        return self.app.LayerSets

    @property
    def preferences(self):
        return self.app.Preferences

    def open(self, *args, **kwargs):
        self.app.Open(*args, **kwargs)

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)

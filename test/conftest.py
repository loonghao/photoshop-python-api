import os

import pytest


@pytest.fixture()
def photoshop_app():
    from photoshop.api import Application

    app = Application()
    app.documents.add(name="UnitTest")
    yield app
    app.activeDocument.close()


@pytest.fixture()
def data_root():
    return os.path.join(os.path.dirname(__file__), "test_data")


@pytest.fixture()
def psd_file(data_root):
    def _get_psd_file(name):
        return os.path.join(data_root, f"{name}.psd")

    return _get_psd_file

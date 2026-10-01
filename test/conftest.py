# Import built-in modules
import os

# Import third-party modules
import pytest

# Scripts, not tests: they execute their side effects at import time (launching
# Photoshop and running every file under examples/), so collecting them would run
# them on every pytest invocation.
collect_ignore_glob = ["*/manual_test_all_examples.py", "*/manual_test_enum_values.py"]


@pytest.fixture()
def photoshop_app():
    # Import local modules
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

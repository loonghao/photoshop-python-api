import pytest


@pytest.yield_fixture
def photoshop_app():
    from photoshop.application import Application

    app = Application()
    app.documents.add(name="UnitTest")
    yield app
    app.activeDocument.close()

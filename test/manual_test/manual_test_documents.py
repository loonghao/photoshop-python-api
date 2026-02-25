from math import isclose

import pytest

from photoshop.api.application import Application


class TestNewDocument:
    """Test various parts of the API in a new document."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for current test."""
        self.app = Application()
        self.docs = self.app.documents

    def test_create_document(self):
        doc_name = "test_document"
        w = 22.3
        h = 47
        res = 55.8
        doc = self.docs.add(22.3, 47, resolution=55.8, name=doc_name)
        try:
            assert doc.name == doc_name
            assert doc.width == int(w)
            assert doc.height == h
            assert isclose(doc.resolution, res, abs_tol=0.01)
        finally:
            doc.close()

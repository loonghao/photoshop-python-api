from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from photoshop import Session
from photoshop.api._artlayer import ArtLayer
from photoshop.api._document import Document
from photoshop.api._layerSet import LayerSet
from photoshop.api.enumerations import LayerKind


class TestNewDocument:
    """Test various parts of the API in a new document."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for current test."""
        self.session = Session(action="new_document", auto_close=True)
        self.session.run_action()
        self.app = self.session.app
        self.doc = self.session.active_document
        yield
        self.session.close()

    def test_active_layer(self):
        layer_1 = self.doc.artLayers.add()
        layer_2 = self.doc.artLayers.add()
        self.doc.activeLayer = layer_1
        assert layer_1.id == self.doc.activeLayer.id
        self.doc.activeLayer = layer_2
        assert layer_2.id == self.doc.activeLayer.id

    def test_channel_histogram(self):
        channel = self.doc.activeChannels[0]
        assert isinstance(channel.histogram, tuple)

    def test_document_info_keywords(self):
        doc_info = self.doc.info
        assert doc_info.keywords is None
        doc_info.keywords = ["foo", "bar"]
        assert isinstance(doc_info.keywords, tuple)
        assert doc_info.keywords == ("foo", "bar")
        tuple_keywords = ("key", "word", "?")
        doc_info.keywords = tuple_keywords
        assert doc_info.keywords == tuple_keywords

    def test_selection(self):
        self.doc.resizeImage(500, 500)
        assert self.doc.width == 500
        assert self.doc.height == 500
        selection = self.doc.selection
        # If the selection touches the document's borders it might not get contracted
        selection.select(((10, 10), (200, 10), (200, 200), (10, 200)))
        bounds = selection.bounds
        assert isinstance(bounds, tuple)
        assert isinstance(bounds[0], float)
        selection.contract(20.5)
        contracted_bounds = selection.bounds
        assert bounds[0] < contracted_bounds[0]
        selection.expand(10)
        expanded_bounds = selection.bounds
        assert expanded_bounds[0] < contracted_bounds[0]

    def test_paths(self):
        with TemporaryDirectory(prefix="photoshop_python_api_") as tmpdir:
            doc_path = Path(tmpdir, "test_doc.psd")
            self.doc.saveAs(str(doc_path))
            assert isinstance(self.doc.saved, bool)
            assert self.doc.saved
            assert self.doc.fullName == doc_path

    def test_layer_kind(self):
        background_layer = self.doc.artLayers[0]
        assert isinstance(background_layer, ArtLayer)
        layer_kind = background_layer.kind
        layer_set_1 = self.doc.layerSets.add()
        self.doc.activeLayer = layer_set_1

        # This used to fail in version 0.24.1
        assert background_layer.kind == layer_kind

        layer_1 = self.doc.artLayers.add()
        layer_1.kind = LayerKind.TextLayer
        assert layer_1.kind == LayerKind.TextLayer

    def test_layer_iteration(self):
        layer_set = self.doc.layerSets.add()
        layers = list(self.doc.layers)
        assert any((layer for layer in layers if isinstance(layer, LayerSet)))
        assert any((layer for layer in layers if isinstance(layer, ArtLayer)))

        layer_set.artLayers.add()
        layer_set.layerSets.add()
        assert any((layer for layer in layer_set if isinstance(layer, LayerSet)))
        assert any((layer for layer in layer_set if isinstance(layer, ArtLayer)))

    def test_layer_parent(self):
        layer_set = self.doc.layerSets.add()
        assert isinstance(layer_set.parent, Document)
        sub_layer = layer_set.artLayers.add()
        assert isinstance(sub_layer.parent, LayerSet)

    def test_layer_access(self):
        for collection in (self.doc.artLayers, self.doc.layerSets):
            names = ("l_1", "l_2")
            layers: list[ArtLayer | LayerSet] = []
            for name in names:
                layer = collection.add()
                layer.name = name
                layers.append(layer)
            for name, layer in zip(names, layers):
                assert collection[name].id == layer.id
                got_layer = collection.getByName(name)
                assert got_layer
                assert got_layer.id == layer.id

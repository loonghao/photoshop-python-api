# Import third-party modules
import pytest

# Import local modules
from photoshop import Session


class TestLayerComps:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for current test."""
        self.session = Session(action="new_document", auto_close=True)
        self.session.run_action()
        self.app = self.session.app
        self.doc = self.session.active_document
        layer = self.doc.artLayers.add()
        self.doc.activeLayer = layer
        self.layer_comps = self.doc.layerComps
        self.n = 2
        for i in range(self.n):
            self.layer_comps.add(str(i))
        yield
        self.session.close()

    def test_layer_comps_len(self):
        assert self.layer_comps.length == self.n

    def test_get_by_name(self):
        name = "1"
        layer = self.layer_comps[name]
        assert layer.name == name

    def test_get_by_index(self):
        idx = 0
        layer = self.layer_comps[0]
        assert layer.name == str(idx)

    def test_loop_layers(self):
        for layer in self.layer_comps:
            assert layer.name

    def test_add_layer_comp(self):
        name = "new_layer"
        comment = "test"
        layer = self.layer_comps.add(name, comment)
        assert layer.name == name
        assert layer.comment == comment

    def test_delete_layer_comp(self):
        layer = self.layer_comps[0]
        name = layer.name
        layer.remove()
        layer = self.layer_comps.getByName(name)
        assert layer is None

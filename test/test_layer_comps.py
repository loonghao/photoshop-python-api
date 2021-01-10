""""""
import pytest
from photoshop import Session


class TestTextItem:
    """Test the solidColor."""

    # pylint: disable=attribute-defined-outside-init
    @pytest.fixture(autouse=True)
    def setup(self, psd_file):
        """Setup for current test."""
        self.session = Session(
            file_path=psd_file("layer_comps"), action="open", auto_close=True
        )
        self.session.run_action()
        doc = self.session.active_document
        self.layer_compse = doc.layerComps  # -> TextItem
        yield
        self.session.close()

    def test_length(self):
        assert self.layer_compse.length == 2

    def test_getByName(self):
        layer = self.layer_compse.getByName("layer1")
        assert layer.name == "layer1"

    def test_loop_layers(self):
        for layer in self.layer_compse:
            assert layer.name

    def test_add_a_layer(self):
        self.layer_compse.add("new_layer", "test")
        assert self.layer_compse.length == 3

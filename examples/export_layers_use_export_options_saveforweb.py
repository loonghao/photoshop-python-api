"""Export every layer as a .png file use `ExportOptionsSaveForWeb`."""
# Import built-in modules
import os

# Import third-party modules
import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session

PSD_FILE = psd.get_psd_files()


def hide_all_layers(layers):
    for layer in layers:
        layer.visible = False


def main():
    psd_file = PSD_FILE["export_layers_as_png.psd"]
    with Session(psd_file, action="open") as ps:
        doc = ps.active_document
        options = ps.ExportOptionsSaveForWeb()
        layers = doc.artLayers
        for layer in layers:
            hide_all_layers(layers)
            layer.visible = True
            layer_path = os.path.join(doc.path, layer.name)
            print(layer_path)
            if not os.path.exists(layer_path):
                os.makedirs(layer_path)
            image_path = os.path.join(layer_path, f"{layer.name}.png")
            doc.exportDocument(image_path, exportAs=ps.ExportType.SaveForWeb, options=options)
        ps.alert("Task done!")
        ps.echo(doc.activeLayer)


if __name__ == "__main__":
    main()

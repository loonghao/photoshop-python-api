"""Export every layer as a .png file."""
import os

from photoshop import Session


def hide_all_layers(layers):
    for layer in layers:
        layer.visible = False


def main():
    psd_file = os.path.join(os.path.dirname(__file__), "export_layers_as_png.psd")
    with Session(psd_file, action="open") as ps:
        doc = ps.active_document
        options = ps.PNGSaveOptions()
        layers = doc.artLayers
        for layer in layers:
            hide_all_layers(layers)
            layer.visible = True
            layer_path = os.path.join(doc.path, layer.name)
            print(layer_path)
            if not os.path.exists(layer_path):
                os.makedirs(layer_path)
            image_path = os.path.join(layer_path, f"{layer.name}.png")
            doc.saveAs(image_path, options, True)
        ps.alert("Task done!")
        ps.echo(doc.activeLayer)


if __name__ == "__main__":
    main()

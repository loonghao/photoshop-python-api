"""This example demonstrates how to export a document with different formats.

References:
    https://github.com/loonghao/photoshop-python-api/issues/368
"""

# Import built-in modules
import os

# Import third-party modules
from photoshop import Session
from photoshop.api.enumerations import DitherType
from photoshop.api.enumerations import ExportType
from photoshop.api.enumerations import SaveDocumentType
from photoshop.api.save_options.png import PNGSaveOptions
from photoshop.api.save_options.jpg import JPEGSaveOptions
from photoshop.api.save_options.png import ExportOptionsSaveForWeb


def main():
    """Export document with different formats."""
    psd_file = os.path.join(os.path.dirname(__file__), "files", "export_layers_as_png.psd")
    if not os.path.exists(psd_file):
        raise FileNotFoundError(
            f"File not found: {psd_file}"
        )

    # Start a new photoshop session
    with Session(psd_file, "open") as ps:
        doc = ps.active_document

        # Export as PNG-24
        png_path = os.path.join(os.path.dirname(__file__), "exported_png24.png")
        png_options = PNGSaveOptions()
        png_options.interlaced = False  # Disable interlacing for better quality
        png_options.compression = 0  # Set compression to 0 for maximum quality
        doc.saveAs(png_path, png_options, True)  # True for saving as copy
        print(f"Exported PNG-24: {png_path}")

        # Export as JPEG with high quality
        jpg_path = os.path.join(os.path.dirname(__file__), "exported_jpeg.jpg")
        jpg_options = JPEGSaveOptions()
        jpg_options.quality = 12  # Set quality to maximum (12)
        jpg_options.embedColorProfile = True  # Preserve color profile
        jpg_options.formatOptions = 1  # Use standard baseline format
        jpg_options.scans = 3  # Enable progressive scanning
        jpg_options.matte = 1  # No background color (matte)
        doc.saveAs(jpg_path, jpg_options, True)  # True for saving as copy
        print(f"Exported JPEG: {jpg_path}")

        # Export as GIF using Save for Web
        gif_path = os.path.join(os.path.dirname(__file__), "exported_gif.gif")
        gif_options = ExportOptionsSaveForWeb()
        gif_options.format = SaveDocumentType.CompuServeGIFSave  # Set format to GIF
        gif_options.colors = 256  # Use maximum number of colors (256)
        gif_options.dither = DitherType.NoDither  # Disable dithering for sharper edges
        gif_options.transparency = True  # Preserve transparency in the GIF
        doc.exportDocument(gif_path, ExportType.SaveForWeb, gif_options)
        print(f"Exported GIF: {gif_path}")


if __name__ == "__main__":
    main()

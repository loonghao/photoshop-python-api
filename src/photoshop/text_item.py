from photoshop._core import Photoshop


class TextItem(Photoshop):
    object_name = 'Application'

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def contents(self):
        """str:"""
        return self.app.contents

    @contents.setter
    def contents(self, text):
        self.app.contents = text

    @property
    def position(self):
        return self.app.position

    @position.setter
    def position(self, array):
        """The position of the origin for the text.

        The array must contain two values. Setting this property is basically
        equivalent to clicking the text tool at a point in the documents to
        create the point of origin for text.

        """
        self.app.position = array

    @property
    def size(self):
        return self.app.size

    @size.setter
    def size(self, value):
        self.app.size = value

    @property
    def color(self):
        return self.app.color

    @color.setter
    def color(self, color_value):
        """

        Args:
            color_value (photoshop_python_api.SolidColor):

        Returns:

        """
        self.app.color = color_value

    def capitalization(self):
        return self.app.capitalization

    def alternateLigatures(self):
        return self.app.alternateLigatures

    @property
    def name(self):
        return self.app.name

from photoshop.artlayer import ArtLayer


def hello_world():

    artlayer = ArtLayer()

    # attrs = [
    #     # "build",
    #     "colorSettings",
    #     "currentTool",
    #     "displayDialogs",
    #     "documents.name"
    # ]
    # for attr in attrs:
    #     print("app.{}".format(attr), _getattr(app, attr))
    print(artlayer.fillOpacity)


if __name__ == '__main__':
    hello_world()

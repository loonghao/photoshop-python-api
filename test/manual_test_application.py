from photoshop import Application


def hello_world():
    app = Application()

    # attrs = [
    #     # "build",
    #     "colorSettings",
    #     "currentTool",
    #     "displayDialogs",
    #     "documents.name"
    # ]
    # for attr in attrs:
    #     print("app.{}".format(attr), _getattr(app, attr))
    # print(app.build)
    # print(app.colorSettings)
    # print(app.currentTool)
    # print(app.displayDialogs)
    # print(app.macintoshFileTypes)
    # print(app.fonts)
    # print(app.foregroundColor.cmyk.black)
    # print(app.freeMemory)
    # print(app.locale)
    # print(app.measurementLog.exportMeasurements("d:/test.text"))
    # print(app.preferencesFolder)
    # print(app.recentFiles)
    # print(app.version)
    # print(app.beep())
    # print(app.bringToFront())
    # app.changeProgressText("a")
    # print(app.charIDToTypeID("jsCt"))
    # app.doForcedProgress("test", 'alert ("dasdads")')
    # app.doProgress("tes1t", 'alert ("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")')
    # app.doProgressSegmentTask(50, 100, 100,
    #                           'alert("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")')
    # app.doProgressSubTask(20, 100, 'alert("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")')
    # app.doProgressTask(20, 'alert("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")')

    # app.updateProgress(100, 2)
    # app.showColorPicker()
    # app.refreshFonts()
    app.purge(0)
    print(app.isQuicktimeAvailable())
    app.doJavaScript('alert', ['aasdasd'], 1)


if __name__ == '__main__':
    hello_world()

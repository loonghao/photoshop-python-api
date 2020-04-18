from photoshop import Session

psDisplayNoDialogs = 3
with Session() as ps:
    app = ps.app
    for index, x in enumerate(range(50)):
        # Execute an existing action from action palette.
        idPly = app.charIDToTypeID("Ply ")
        desc8 = ps.ActionDescriptor()
        idnull = app.charIDToTypeID("null")
        ref3 = ps.ActionReference()
        idActn = app.charIDToTypeID("Actn")
        ref3.putName(idActn, "Sepia Toning (layer)")
        idASet = app.charIDToTypeID("ASet")
        ref3.PutName(idASet, "Default Actions")
        desc8.putReference(idnull, ref3)
        app.executeAction(idPly, desc8, ps.DialogModes.DisplayNoDialogs)

        # Create solid color fill layer.
        idMk = app.charIDToTypeID("Mk  ")
        desc21 = ps.ActionDescriptor()
        idNull = app.charIDToTypeID("null")
        ref12 = ps.ActionReference()
        idContentLayer1 = app.stringIDToTypeID("contentLayer")
        ref12.putClass(idContentLayer1)
        desc21.putReference(idNull, ref12)
        idUsng = app.charIDToTypeID("Usng")
        desc22 = ps.ActionDescriptor()
        idType = app.charIDToTypeID("Type")
        desc23 = ps.ActionDescriptor()
        idClr = app.charIDToTypeID("Clr ")
        desc24 = ps.ActionDescriptor()
        idRd = app.charIDToTypeID("Rd  ")
        desc24.putDouble(idRd, index)
        idGrn = app.charIDToTypeID("Grn ")
        desc24.putDouble(idGrn, index)
        idBl = app.charIDToTypeID("Bl  ")
        desc24.putDouble(idBl, index)
        idRGBC = app.charIDToTypeID("RGBC")
        desc23.putObject(idClr, idRGBC, desc24)
        idSolidColorLayer = app.StringIDToTypeID("solidColorLayer")
        desc22.putObject(idType, idSolidColorLayer, desc23)
        idContentLayer2 = app.StringIDToTypeID("contentLayer")
        desc21.putObject(idUsng, idContentLayer2, desc22)
        app.executeAction(idMk, desc21, psDisplayNoDialogs)

        # Select mask.
        idSlct = app.charIDToTypeID("slct")
        desc38 = ps.ActionDescriptor()
        idNull1 = app.charIDToTypeID("null")
        ref20 = ps.ActionReference()
        idChnl1 = app.charIDToTypeID("Chnl")
        idChnl2 = app.charIDToTypeID("Chnl")
        idMsk = app.charIDToTypeID("Msk ")
        ref20.putEnumerated(idChnl1, idChnl2, idMsk)
        desc38.putReference(idNull1, ref20)
        idMkVs = app.charIDToTypeID("MkVs")
        desc38.putBoolean(idMkVs, False)
        app.executeAction(idSlct, desc38, psDisplayNoDialogs)

        app.activeDocument.activeLayer.invert()

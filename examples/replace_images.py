"""
var idplacedLayerReplaceContents = stringIDToTypeID( "placedLayerReplaceContents" );
    var desc93 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    desc93.putPath( idnull, new File( "C:\\Users\\hao.long\\Pictures\\HAL-1.png" ) );
executeAction( idplacedLayerReplaceContents, desc93, DialogModes.NO );
"""

from photoshop import Session

with Session() as ps:
    idplacedLayerReplaceContents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
    desc = ps.ActionDescriptor
    idnull = ps.app.charIDToTypeID("null")
    desc.putPath(idnull, "your/image/path.jpg")
    ps.app.executeAction(idplacedLayerReplaceContents, desc)
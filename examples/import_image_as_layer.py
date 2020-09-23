"""
function replaceContents (newFile) {  
// =======================================================  
var idplacedLayerReplaceContents = stringIDToTypeID( "placedLayerReplaceContents" );  
    var desc3 = new ActionDescriptor();  
    var idnull = charIDToTypeID( "null" );  
    desc3.putPath( idnull, new File( newFile ) );  
    var idPgNm = charIDToTypeID( "PgNm" );  
    desc3.putInteger( idPgNm, 1 );  
executeAction( idplacedLayerReplaceContents, desc3, DialogModes.NO );  
return app.activeDocument.activeLayer  
};  

"""

from photoshop import Session

with Session(action="new_document") as ps:
    desc = ps.ActionDescriptor
    desc.putPath(ps.app.charIDToTypeID("null"), "your/image/path")
    event_id = ps.app.charIDToTypeID("Plc ")  # `Plc` need one space in here.
    ps.app.executeAction(ps.app.charIDToTypeID("Plc "), desc)

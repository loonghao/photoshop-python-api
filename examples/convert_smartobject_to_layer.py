"""Convert Smart object to artLayer."""

# Import built-in modules
from textwrap import dedent

# Import local modules
from photoshop import Session
import photoshop.api.action_manager as am


# example 1
with Session() as ps:
    js = dedent(
        """
        var idplacedLayerConvertToLayers = stringIDToTypeID( "placedLayerConvertToLayers" );
        executeAction( idplacedLayerConvertToLayers, undefined, DialogModes.NO );
    """
    )
    ps.app.doJavaScript(js)

# example 2
with Session() as ps:
    # The event id used in executeAction differs across Photoshop versions.
    # Look up eventid list or record with ScriptListener Plug-in to decide which eventid to use.
    ps.app.executeAction(am.str2id("placedLayerConvertToLayers"), None)

"""A examples to show you how to operation layerSet."""

from photoshop import Session

with Session(action="new_document") as ps:
    docRef = ps.active_document
    # Add a new layerSet.
    new_layer_set = docRef.layerSets.add()
    # Print the layerSet count.
    ps.echo(docRef.layerSets.length)
    ps.echo(len(docRef.layerSets))
    # Rename the layerSet.
    docRef.layerSets[0].name = "New Name"
    ps.echo(new_layer_set.name)

    # Change the layerSet opacity
    new_layer_set.opacity = 90
    ps.echo(new_layer_set.opacity)

    # Duplicate the layerSet.
    duplicate_layer_set = new_layer_set.duplicate()
    # Add a new artLayer in current active document.
    layer = docRef.artLayers.add()
    # Move the artLayer under the duplicate layerSet.
    layer.move(duplicate_layer_set, ps.ElementPlacement.INSIDE)
    # Merge the layerSet.
    merged_layer = duplicate_layer_set.merge()
    ps.echo(merged_layer.name)

    # Set visible.
    new_layer_set.visible = False

    merged_layer.remove()

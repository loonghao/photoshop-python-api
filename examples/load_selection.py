# This script will demonstrate how to load a selection from a saved alpha
# channel.

from photoshop import Session

with Session() as ps:
    doc_ref = ps.app.documents.add(320, 240)
    start_ruler_units = ps.app.preferences.rulerUnits
    if start_ruler_units is not ps.Units.Pixels:
        ps.app.Preferences.RulerUnits = ps.Units.Pixels
    # Save a rectangular selection area offset by 50 pixels from the image
    # border into an alpha channel.
    offset = 50
    selBounds1 = (
        (offset, offset),
        (doc_ref.Width - offset, offset),
        (doc_ref.Width - offset, doc_ref.Height - offset),
        (offset, doc_ref.Height - offset),
    )
    doc_ref.selection.select(selBounds1)
    selAlpha = doc_ref.channels.Add()
    doc_ref.selection.store(selAlpha)

    # Now create a second wider but less tall selection.
    selBounds2 = ((0, 75), (doc_ref.Width, 75), (doc_ref.Width, 150), (0, 150))
    doc_ref.selection.select(selBounds2)

    # Load the selection from the just saved alpha channel, combining it with
    # the active selection.
    doc_ref.selection.load(selAlpha, ps.SelectionType.ExtendSelection, False)

    # Set ruler back to where it was.
    ps.app.Preferences.RulerUnits = start_ruler_units

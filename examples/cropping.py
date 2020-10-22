"""A cropping example."""

from photoshop import Session

with Session(action="new_document") as ps:
    ps.active_document.crop(bounds=[100, 12, 354, 246],
                            width=1920,
                            height=1080)

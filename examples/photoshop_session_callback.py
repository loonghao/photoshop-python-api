from photoshop import Session


def do_something():
    print("Do something.")


with Session(callback=do_something) as ps:
    ps.echo(ps.active_document.name)
    ps.alert(ps.active_document.name)

from photoshop import Session


def do_something(photoshop_api):
    print(photoshop_api.active_document)
    print("Do something.")


with Session(callback=do_something) as ps:
    ps.echo(ps.active_document.name)
    ps.alert(ps.active_document.name)

import click
from ..PythonInterface.main import HolaTESE

@click.command()
@click.option(
    '--busqueda', default=''
)
@click.option(
    '--msgbox', default=None
)
def cli(busqueda, msgbox):
    if not msgbox:
        for a in HolaTESE(busqueda):
            print(a)
    else:
        from ..CInterface import message_box
        message_box(msgbox)

import os
import click
from processaImagem import ProcessaImagem

@click.command()
@click.option('--figure', '-f', required=True, help='Figure name for contour extraction.')
def cli(figure):
    """Simple program that greets NAME for a total of COUNT times."""
    if not os.path.isfile(figure):
        click.echo('Invalid path for --figure/ -f: ' + figure)
        quit()
    pi = ProcessaImagem(figure)
    pi.extrai_contorno()
    pi.mostra_imagem()


if __name__ == '__main__':
    cli()

# Biblioteca para comandos do sistema
import os
# Biblioteca para verificação de paths
import ntpath
# Biblioteca para CLI
import click

from processaMalha import ProcessaMalha


@click.command()
@click.option('--inputfile', '-f', required=True, help='file name for mesh generation.')
@click.option('--dx', '-dx', required=True, help='Set the interval between each point on X axis.')
@click.option('--dy', '-dy', required=True, help='Set the interval between each point on Y axis.')
@click.option('--output', '-o', help='Output file name for contour export.')
@click.option('-dftoffset', '-do',is_flag=True, help='Set the offset as the minimum values from input arrays.')
@click.option('--xoffset', '-xo', default=0, help='X axis offset from start.')
@click.option('--yoffset', '-yo', default=0, help='Y axis offset from start.')
@click.option('--verbose', '-v', is_flag=True, help='Runs the program with verbosity. Good for debugging.')

def cli(inputfile, output, dx, dy, xoffset, yoffset, dftoffset, verbose):
    if not os.path.isfile(inputfile):
        click.echo('Invalid path for --input/ -f: ' + inputfile)
        quit()
    xarray = []
    yarray = []
    f = open(inputfile,'r')
    for line in f.readlines():
        aux = line.split()
        xarray.append(float(aux[0]))
        yarray.append(float(aux[1]))
    f.close()
    malha = ProcessaMalha(xarray, yarray, dftoffset, xoffset, yoffset, float(dx), float(dy))
    malha.criar_malha()
    if output == None:
        output = path_leaf(inputfile)[:-4] + '-data.txt'
    malha.exporta_coords_malha(output)


# Função responsável pela extração do nome do arquivo dentro de um path


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


"""
Função main para rodar o código do CLI
"""
if __name__ == '__main__':
    cli()

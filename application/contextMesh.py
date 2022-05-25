# Biblioteca para comandos do sistema
import os
# Biblioteca para verificação de paths
import ntpath
# Biblioteca para CLI
import click

from processaMalha import ProcessaMalha


@click.command()
@click.option('--inputfile', '-f', required=True, help='file name for mesh generation.')
@click.option('--dx', '-dx', default=0.0, help='Set the interval between each point on X axis.')
@click.option('--dy', '-dy', default=0.0, help='Set the interval between each point on Y axis.')
@click.option('--nx', '-nx', default=0, help='Set the number of nodes on X axis.')
@click.option('--ny', '-ny', default=0, help='Set the number of nodes on Y axis.')
@click.option('--output', '-o', help='Output file name for contour export.')
@click.option('--xmin', '-xm', default=0, help='X axis minimum value.')
@click.option('--ymin', '-ym', default=0, help='Y axis minimum value.')

def cli(inputfile, output, dx, dy, nx, ny, xmin, ymin):
    if not os.path.isfile(inputfile):
        click.echo('Invalid path for --input/ -f: ' + inputfile)
        quit()
    if dx == 0 and nx == 0:
        click.echo('Missing argument --dx ou --nx')
        quit()
    if dy == 0 and ny == 0:
        click.echo('Missing argument --dy ou --ny')
        quit()
    xarray = []
    yarray = []
    f = open(inputfile,'r')
    for line in f.readlines():
        aux = line.split()
        xarray.append(float(aux[0]))
        yarray.append(float(aux[1]))
    f.close()
    malha = ProcessaMalha(xarray, yarray, xmin, ymin, int(nx), int(ny), float(dx), float(dy))
    malha.criar_malha()
    if output == None:
        output = path_leaf(inputfile)[:-4] + '-data.txt'
    malha.exporta_coords_malha(output)


# Função responsável pela extração do nome do arquivo dentro de um path


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


#Função para escrever um vetor em um arquivo

def export_point(path, l):
    try:
        with open(path, "w") as dataFile:
            content = ''
            for i in l:
                if type(i) is list:
                    aux = ' '.join([str(elem) for elem in i])
                else:
                    aux = str(i)
                content = content + aux + "\n"
            dataFile.write(content)
    except:
        print('Path does not exist for export')
        return

"""
Função main para rodar o código do CLI
"""
if __name__ == '__main__':
    cli()

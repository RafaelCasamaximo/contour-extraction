# Biblioteca para comandos do sistema
import os
# Biblioteca para verificação de paths
import ntpath
# Biblioteca para CLI
import click

from processaMalhaNIE import ProcessaMalhaNIE


@click.command()
@click.option('--inputfile', '-f', required=True, help='File name for mesh generation.')
@click.option('--output', '-o', help='Output file name for contour export.')
@click.option('--rangesfile', '-r', required=True, help='File name for critical regions of the mesh.')
@click.option('--irregular', '-ir', is_flag=True, help='Set the mesh mode as irregular')

def cli(inputfile, output, rangesfile, irregular):
    if not os.path.isfile(inputfile):
        click.echo('Invalid path for --inputfile/ -f: ' + inputfile)
        quit()
    if not os.path.isfile(inputfile):
        click.echo('Invalid path for --rangesfile/ -r: ' + inputfile)
        quit()
    xarray = []
    yarray = []
    f = open(inputfile,'r')
    for line in f.readlines():
        aux = line.split()
        xarray.append(float(aux[0]))
        yarray.append(float(aux[1]))
    f.close()
    malha = ProcessaMalhaNIE(xarray, yarray)
    r = open(rangesfile, 'r')
    for line in r.readlines():
        aux = line.split()
        nx = int(aux[0])
        ny = int(aux[1])
        if aux[2] == "min":
            xi = min(xarray)
        else:
            xi = float(aux[2])
        if aux[3] == "min":
            yi = min(yarray)
        else:
            yi = float(aux[3])
        if aux[4] == "max":
            xf = max(xarray)
        else:
            xf = float(aux[4])
        if aux[5] == "max":
            yf = max(yarray)
        else:
            yf = float(aux[5])
        malha.addRange(xi, yi, xf, yf, nx, ny)
    r.close()
    if output == None:
        output = path_leaf(inputfile)[:-4] + '-data.txt'
    if irregular:
        malha.criar_malha_irregular()
        malha.export_ranges(output[:-4] + '-ranges.txt')
    else:
        malha.criar_malha()
        export_point(output[:-4] + '-dx.txt',  malha.dx)
        export_point(output[:-4] + '-dy.txt',  malha.dy)
    export_point(output, malha.mesh)


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
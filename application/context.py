# Biblioteca para comandos do sistema
import os
# Biblioteca para verificação de paths
import ntpath
# Biblioteca para CLI
import click
# Classe para Processamento de Imagens
from processaImagem import ProcessaImagem
# Classe para a interface gráfica
from interface import Interface


"""
Essa parte do código é responsável pelo funcionamento dos orgumentos do programa
use python main.py --help para ver informações ou use a documentação
"""


@click.command()
@click.option('--figure', '-f', help='Figure name for contour extraction.')
@click.option('--output', '-o', help='Output file name for contour export.')
@click.option('--width', '-w', default=-1, help='Max width of boundary set.')
@click.option('--height', '-h', default=-1, help='Max height of boundary set.')
@click.option('--xoffset', '-xo', default=-1, help='X axis offset from start.')
@click.option('--yoffset', '-yo', default=-1, help='Y axis offset from start.')
@click.option('--interval', '-i', default=0, help='Set the interval between each point of the output.')
@click.option('--matlab', '-m', is_flag=True, help='Convert to matlab boundary.')
@click.option('--metadata', '-md', is_flag=True, help='Generates a metadata file as [output]-metada.json showing the configurations and other usefull info about the boundary and the file.')
@click.option('--graphical', '-gui', is_flag=True, help='Runs the program in the GUI mode (In Development).')
@click.option('--verbose', '-v', is_flag=True, help='Runs the program with verbosity. Good for debugging.')
def cli(figure, output, width, height, xoffset, yoffset, interval, matlab, metadata, graphical, verbose):
    """A program that get the boundary of a binary-colored figure."""

    if graphical:
        gui = Interface()

    # Verifica se o path passado como figura é válido e existe. Sai do programa se não foi válido.
    if figure != None:
        click.echo('--figure/ -f: required' + figure)
        quit()
    if not os.path.isfile(figure):
        click.echo('Invalid path for --figure/ -f: ' + figure)
        quit()
    # Cria um objeto ProcessaImagem, necessário para a realização do algoritmo. O parâmetro figure é o path da figura que irá passar pelo algoritmo.
    pi = ProcessaImagem(figure)

    # Extrai o contorno da figura e salva nos atributos de ProcessaImagem
    pi.extrai_contorno()
    # Converte para o formato matlab como descrito na descrição do comando
    if matlab:
        pi.converte_matlab()
    # Altera a escala do conjunto de pontos extraidos do contorno. Para cada parâmetro -1 (default), o contorno não é alterado naquele quesito
    pi.altera_escala(width, height, xoffset, yoffset)
    # Caso o usuário tenha passado o nome do arquivo desejado, será gerado um novo arquivo de texto com o nome. Caso não seja especificado o nome do arquivo de dados será:
    # [nome-do-arquivo-figure]-data.txt
    if output == None:
        output = path_leaf(figure)[:-4] + '-data.txt'
        outputConfig = path_leaf(figure)[:-4] + '-metadata.json'
    # Calcula a área
    pi.calcula_area()
    # Cria um arquivo de configuração quando exporta o txt mostrando informações uteis sobre o arquivo
    pi.exporta_metadata(outputConfig, width, height, xoffset, yoffset)
    # Cria um novo arquivo com o output
    pi.exporta_contorno(output, interval)

# Função responsável pela extração do nome do arquivo dentro de um path


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


"""
Função main para rodar o código do CLI
"""
if __name__ == '__main__':
    cli()

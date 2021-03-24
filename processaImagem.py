import cv2
from pixel import Pixel
from pprint import pprint

class ProcessaImagem:

    """
    Constructor da classe ProcessaImagem
    Path é o caminho até a imagem desejada
    A imagem (por enquanto) deve ser em preto em branco. Caso seja uma imagem colorida o programa converterá automaticamente para preto e branco UTILIZANDO APENAS O CANAL BLUE,
    resultado do formato BGR

    path: caminho de entrada da imagem
    img: 3d array que guarda valor BGR da imagem [x][y][BGR]
    yTotal: valor total de linhas que tem (pixeis de altura)
    xTotal: valor total de colunas que tem (pixeis de largura)
    bidimensional_image: 2d array com [x][y] e do mesmo tamanho que img, o valor de cada posição é o valor B da img 
    MOORE_OFFSET: coordenadas que representam os 8 pontos adjascentes do ponto atual, representandos por (x, y)
    """
    def __init__(self, path):
        self.path = path
        self.img = cv2.imread(path, cv2.COLOR_BGR2GRAY)
        self.yTotal = self.img.shape[0]
        self.xTotal = self.img.shape[1]
        self.bidimensional_image = [[0] * self.xTotal for i in range(self.yTotal)]
        """
        |4|5|6|
        |3|P|7|
        |2|1|8|
        """
        self.MOORE_OFFSET = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

    """
    Imprime uma certa imagem na tela e espera até o usuário apertar uma tecla para continuar a execução do código
    Indepentente da imagem ser transformada em uma unica coloração posteriormente, quando a imagem é impressa ela aparece com todas as cores em seu tamanho original.
    """
    def mostra_imagem(self):
        cv2.imshow('image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    """
    Utiliza o pprint (pretty print) para imprimir de forma elegante os valores de um array, independente das dimensões
    """
    def imprime_coords(self):
        pprint(self.img, width=10)

    """
    
    """
    def extrai_contorno(self):
        contorno = []
        #Converte imagem RGB para imagem PB
        self.convert_3d_to_2d_image_array()
        #Encontra o primeiro pixel branco
        startPixel = self.encontra_ponto_inicial()
        contorno.append(startPixel)
        pixel = startPixel
        
        backtrackIndexStart = 0 #(0, -1)
        countourPixel, backtrackIndexStart = self.moore_neighborhood(pixel, backtrackIndexStart)

        #for i in range(2000):
        while countourPixel != startPixel:
            countourPixel, backtrackIndexStart = self.moore_neighborhood(countourPixel, backtrackIndexStart)
            contorno.append(countourPixel)

        with open("output.txt", "w") as dataFile:
            dataFile.write(self.converte_pixelArray_to_string(contorno))

        cv2.imshow('image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()





    """
    A partir de uma certa imagem em 3 dimensões, dada pelo openCv no formato de cores BGR, em valores que alternam entre 0 e 255 (min e max),
    essa função converte para uma imagem somente em 2 dimensões [x][y] no qual o valor cas posições é dado através do canal B entre 0 e 255
    """
    def convert_3d_to_2d_image_array(self):
        for i in range(self.yTotal):
            for j in range(self.xTotal):
                self.bidimensional_image[i][j] = self.img[i][j][1]

    def encontra_ponto_inicial(self):
        for i in range(self.yTotal - 1, -1, -1):
            for j in range(self.xTotal):
                if self.bidimensional_image[i][j] == 255:
                    pixel = Pixel(i, j, 255)
                    return pixel

    def moore_neighborhood(self, p, backtrackIndex):
        for i in range(8):
            index = (i + backtrackIndex) % 8
            neighborX = p.x + self.MOORE_OFFSET[index][0]
            neighborY = p.y + self.MOORE_OFFSET[index][1]
            neighborValue = self.bidimensional_image[neighborX][neighborY]
            neighborPixel = Pixel(neighborX , neighborY , neighborValue)
            if neighborPixel.value == 255:
                self.img[neighborX][neighborY] = [255, 0, 0]
                return neighborPixel, index -1 

    def converte_pixelArray_to_string(self, array):
        content = ''
        for element in array:
            content = content + str(element.x) + "," + str(element.y) + "\n"
        return content
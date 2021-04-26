import cv2
from PIL import Image
from PIL import ImageTk
from pixel import Pixel

class AnalisaImagem:

    @staticmethod
    def cria_mascara(hsva_threshold, filename):
        #Tem que fazer uma nova imagem com o threshold certo em preto e pranco e retornar essa imagem

        min_values = (hsva_threshold['min_hue'], hsva_threshold['min_satur'], hsva_threshold['min_value'])
        max_values = (hsva_threshold['max_hue'], hsva_threshold['max_satur'], hsva_threshold['max_value'])

        alpha = hsva_threshold['opacity'] / 100
        beta = 1 - alpha

        #Lê a imagem e converte ela no formato HSV
        image = cv2.imread(filename)
        frame_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #Faz o Threshold
        frame_threshold = cv2.inRange(frame_HSV, min_values, max_values)

        frame_threshold = cv2.cvtColor(frame_threshold, cv2.COLOR_GRAY2BGR)
        frame_threshold = cv2.bitwise_not(frame_threshold)
        frame_threshold = cv2.addWeighted(image, beta, frame_threshold, alpha, 0.0)
        
        image = ImageTk.PhotoImage(Image.fromarray(frame_threshold))

        return image

import numpy as np

class ProcessaMalha:

    def __init__(self, xarray, yarray, defaultofsset, xoffset, yoffset, dx, dy):
        self.x = xarray
        self.y = yarray
        if(defaultofsset):
            self.xmin = min(xarray)
            self.ymin = min(yarray)
        else:
            self.xmin = xoffset
            self.ymin = yoffset
        self.dx = dx
        self.dy = dy
        self.mesh = []
    

    def setdx(self, dx):
        self.dx = dx


    def setdx(self, dy):
        self.dy = dy


    def setxmin(self, xmin):
        self.xmin = xmin


    def setymin(self, ymin):
        self.ymin = ymin

    def getNode(self, xpoint, ypoint):
       point = []
       point.append((xpoint - self.xmin)//self.dx * self.dx + self.xmin)
       point.append((ypoint - self.ymin)//self.dy * self.dy + self.ymin)
       return point

    def criar_malha(self):
        prevpoint = self.getNode(self.x[0], self.y[0]) 
        self.mesh.append(prevpoint)
        flagx = 0
        flagy = 0
        tam = len(self.x)
        for i in range(1,tam):
            point = self.getNode(self.x[i], self.y[i])
            if point[0] != prevpoint[0] or point[1] != prevpoint[1]:
                if flagx and point[1] == prevpoint[1]:
                    self.mesh[-1][0] = point[0]
                    self.mesh[-1][1] = point[1]
                elif flagy and point[0] == prevpoint[0]:
                    self.mesh[-1][0] = point[0]
                    self.mesh[-1][1] = point[1]
                else:
                    self.mesh.append(point)
                flagx = 0
                flagy = 0
                if point[0] == self.mesh[-2][0]:
                    flagx = 1
                elif point[1] == self.mesh[-2][1]:
                    flagy = 1
                prevpoint = point
        point = self.mesh[0]
        if flagx:
            if point[1] == prevpoint[1]:
                self.mesh[-1][0] = point[0]
                self.mesh[-1][1] = point[1]
        elif flagy:
            if point[0] == prevpoint[0]:
                self.mesh[-1][0] = point[0]
                self.mesh[-1][1] = point[1]
        elif point[0] != prevpoint[0] or point[1] != prevpoint[1]:
            self.mesh.append(point)
    
    def converte_pointArray_to_string(self, array):
        content = ''
        i = 0
        while i < len(array):
            element = array[i]
            content = content + str(element[0]) + " " + str(element[1]) + "\n"
            i += 1
        return content

    def exporta_coords_malha(self, path):
        try:
            with open(path, "w") as dataFile:
                resultado = self.converte_pointArray_to_string(
                    self.mesh)
                dataFile.write(resultado)
        except:
            print('Path does not exist for boundary export')
            return

    def calcula_area(self):
        area = 0
        i = 0
        j = 0
        for index in range(0, (len(self.boundary)) - 1):
            auxI = self.boundary[index]
            auxJ = self.boundary[index + 1]
            area += auxI[1] * auxJ[0] - auxI[0] * auxJ[1]
        auxI = self.boundary[len(self.boundary) - 1]
        auxJ = self.boundary[0]
        area += auxI[1] * auxJ[0] - auxI[0] * auxJ[1]
        area = area / 2
        return area
    
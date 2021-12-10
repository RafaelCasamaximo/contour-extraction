class ProcessaMalha:

    """
    Constructor da classe ProcessaMalha
    x e y são vetores que representam as coordenadas que representam a figura que será representada na malha
    xmin e ymin são os valores mínimos da malha
    defaultmin define se os valores mínimos são informados ou calculados automaticamente
    nx e ny são os números de nós da malha em cada eixo
    dx e dy são os tamanhos do nó da malha em cada eixo
    é necessário que pelo menos o tamanho ou número de nós seja informado
    mesh é onde as coordenadas dos nós da malha gerada serão armazenadas
    """

    def __init__(self, xarray, yarray, defaultmin, xmin, ymin, nx, ny, dx, dy):
        self.x = xarray
        self.y = yarray
        if(defaultmin):
            self.xmin = min(xarray)
            self.ymin = min(yarray)
        else:
            self.xmin = xmin
            self.ymin = ymin
        if dx == 0:
            self.dx = (max(xarray) - self.xmin)/(nx - 1)
        else:
            self.dx = dx
        if dy == 0:
            self.dy = (max(yarray) - self.ymin)/(ny - 1)
        else:
            self.dy = dy
        if nx == 0:
            self.nx = int((max(xarray) - self.xmin)//dx) + 1
        else:
            self.nx = nx
        if ny == 0:
            self.ny = int((max(yarray) - self.ymin)//dy) + 1
        else:
            self.ny = ny
        self.mesh = []


    """
    Atualiza o valor de nx
    """

    def setnx(self, nx):
        self.nx = nx

    """
    Atualiza o valor de ny
    """
    
    def setny(self, ny):
        self.ny = ny


    """
    Atualiza o valor de dx
    """
    
    def setdx(self, dx):
        self.dx = dx


    """
    Atualiza o valor de dy
    """

    def setdy(self, dy):
        self.dy = dy


    """
    Atualiza o valor de xmin
    """

    def setxmin(self, xmin):
        self.xmin = xmin


    """
    Atualiza o valor de ymin
    """

    def setymin(self, ymin):
        self.ymin = ymin


    """
    Retorna a coordenada do nó da malha onde o ponto informado está 
    """

    def getNode(self, xpoint, ypoint):
       point = []
       point.append((xpoint - self.xmin)//self.dx * self.dx + self.xmin)
       point.append((ypoint - self.ymin)//self.dy * self.dy + self.ymin)
       return point


    """
    Percore x e y, obtendo os nós da malha para cada ponto com a função getNode, 
    e removendo nós irrelevantes
    """

    def criar_malha(self):
        self.mesh = []
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
    

    """
    Essa função é utilizada para converter o array das coordenadas em uma string para ser impressa no arquivo de texto. Retorna a string.
    """

    def converte_pointArray_to_string(self, array):
        content = ''
        i = 0
        while i < len(array):
            element = array[i]
            content = content + str(element[0]) + " " + str(element[1]) + "\n"
            i += 1
        return content

    """
    Essa função retorna uma string com informações sobre a malha, os valores mínimos, números de nós e tamanho dos nós
    """

    def converte_meshInfo_to_string(self):
        content = ''
        content = content + str(self.nx) + " " + str(self.ny) + "\n"
        content = content + str(self.xmin) + " " + str(self.ymin) + "\n"
        content = content + str(self.dx) + " " + str(self.dy) + "\n"
        return content

    """
    Função responsável por exportar as coordenadas dos nós da malha em um arquivo path
    """

    def exporta_coords_malha(self, path):
        try:
            with open(path, "w") as dataFile:
                resultado = self.converte_meshInfo_to_string() + self.converte_pointArray_to_string(
                    self.mesh)
                dataFile.write(resultado)
        except:
            print('Path does not exist for mesh export')
            return


    """
    Utiliza um método descrito por Gauss para o cálculo da área de um poligono irregular convexo
    Utiliza como base: https://www.thecivilengineer.org/education/calculation-examples/item/1319-calculation-example-three-point-resection
    Para esse algoritmo funcionar ele precisa de uma lista ordenada de pontos. No caso, a própria lista de pontos que foi adquirida a partir da extração de contorno
    """

    def calcula_area(self):
        area = 0
        i = 0
        j = 0
        for index in range(0, (len(self.mesh)) - 1):
            auxI = self.mesh[index]
            auxJ = self.mesh[index + 1]
            area += auxI[1] * auxJ[0] - auxI[0] * auxJ[1]
        auxI = self.mesh[len(self.mesh) - 1]
        auxJ = self.mesh[0]
        area += auxI[1] * auxJ[0] - auxI[0] * auxJ[1]
        area = area / 2
        return area
    

    """
    Retorna a malha em forma de matriz
    """

    def get_mesh_mat(self):
        mat = [[0 for col in range(self.nx)] for row in range(self.ny)]
        for node in self.mesh:
            j = int((node[0] - self.xmin) // self.dx)
            i = int((node[1] - self.ymin) // self.dy)
            mat[i][j] = 1
        return mat


    """
    Remove da malha linhas e colunas repetitivas
    """

    def filter_mesh(self, mDx, mDy):
        mat = self.get_mesh_mat()
        dx = [self.xmin]
        dy = [self.ymin]
        aux = 1
        for i in range(1, self.ny):
            if all([x == y for x,y in zip(mat[i - 1], mat[i])]):
                aux += 1
                if aux == mDy:
                    dy.append(dy[-1] + self.dy * aux)
                    aux = 1
            else:
                dy.append(dy[-1] + self.dy * aux)
                aux = 1
        for i in range(1, self.nx):
            col1 = [x[i - 1] for x in mat]
            col2 = [x[i] for x in mat]
            if all([x == y for x,y in zip(col1, col2)]):
                aux += 1
                if aux == mDx:
                    dx.append(dx[-1] + self.dx * aux)
                    aux = 1
            else:
                dx.append(dx[-1] + self.dx * aux)
                aux = 1
        mesh = []
        for node in self.mesh:
            if node[0] in dx and node[1] in dy:
                mesh.append([node[0],node[1]])
        if mesh[0][0] != mesh[-1][0] or mesh[0][1] != mesh[-1][1]:
            mesh.append([node[0],node[1]])
        return mesh, dx, dy
    
    
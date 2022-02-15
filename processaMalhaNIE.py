class ProcessaMalhaNIE:

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

    def __init__(self, xarray, yarray):
        self.x = xarray
        self.y = yarray
        self.mesh = []
        self.ranges = []
        self.dx = []
        self.dy = []

    
    """
    Adiciona informações da região da malha
    """

    def addRange(self, xmin, ymin, xmax, ymax, nx, ny):
        if len(self.ranges) == 0:
            dx = (xmax - xmin)/(nx - 1)
            dy = (ymax - ymin)/(ny - 1)
        else:
            r = self.ranges[0]
            xmin = (xmin - r["xi"]) // r["dx"] * r["dx"] + r["xi"]
            ymin = (ymin - r["yi"]) // r["dy"] * r["dy"] + r["yi"]
            xmax = (xmax - r["xi"]) // r["dx"] * r["dx"] + r["xi"]
            ymax = (ymax - r["yi"]) // r["dy"] * r["dy"] + r["yi"]
            dx = r["dx"]/nx
            dy = r["dy"]/ny
            nx = int((xmax - xmin)//dx) + 1
            ny = int((ymax - ymin)//dy) + 1
        aux = {
            "nx" : nx,
            "ny" : ny,
            "xi" : xmin,
            "yi" : ymin,
            "xf" : xmax,
            "yf" : ymax,
            "dx" : dx,
            "dy" : dy
        }
        self.ranges.append(aux)

    """
    Obtem os intervalos da malha
    """

    def setIntervals(self):
        self.dx = []
        self.dy = []

        xaux = sorted(self.ranges, key = lambda value: value["dx"])
        aux = []
        for r in xaux:
            for i in range(r["nx"]):
                x = r["xi"] + i * r["dx"]
                if all([x < a or x > b for a,b in aux]):
                    self.dx.append(x)
            aux.append([r["xi"], r["xf"]])

        yaux = sorted(self.ranges, key = lambda value: value["dy"])
        aux = []
        for r in yaux:
            for i in range(r["ny"]):
                y = r["yi"] + i * r["dy"]
                if all([y < a or y > b for a,b in aux]):
                    self.dy.append(y)
            aux.append([r["yi"], r["yf"]])
        
        self.dx.sort()
        self.dy.sort()




    """
    Retorna o valor de x da coordenada do nó da malha onde o ponto informado está 
    """

    def getXNode(self, xpoint):
        for i in range(len(self.dx) - 1):
            if xpoint >= self.dx[i] and xpoint < self.dx[i + 1]:
                return self.dx[i] 
        if xpoint == self.dx[-1]:
            return self.dx[-1]
        print("A figura é maior que os limites da malha")
        quit(1)

    
    """
    Retorna o valor de y da coordenada do nó da malha onde o ponto informado está 
    """
    
    def getYNode(self, ypoint):
        for i in range(len(self.dy) - 1):
            if ypoint >= self.dy[i] and ypoint < self.dy[i + 1]:
                return self.dy[i] 
        if ypoint == self.dy[-1]:
            return self.dy[-1]
        print("A figura é maior que os limites da malha")
        print(ypoint)
        quit(1)

    
    """
    Percore x e y, obtendo os nós da malha para cada ponto com a função getNode, 
    e removendo nós irrelevantes.
    """

    def criar_malha(self):
        self.setIntervals()
        self.mesh = []
        prevpoint = [self.getXNode(self.x[0]), self.getYNode(self.y[0])] 
        self.mesh.append(prevpoint)
        flagx = 0
        flagy = 0
        tam = len(self.x)
        for i in range(1,tam):
            point = [self.getXNode(self.x[i]), self.getYNode(self.y[i])]
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
    Retorna a coordenada do nó da malha onde o ponto informado está 
    """

    def getNode(self, xpoint, ypoint):
        auxX = xpoint
        auxY = ypoint
        flag = 0
        for r in self.ranges:
            if r["xi"] <= xpoint <= r["xf"] and r["yi"] <= ypoint <= r["yf"]:
                auxX = (xpoint - r["xi"]) // r["dx"] * r["dx"] + r["xi"]
                auxY = (ypoint - r["yi"]) // r["dy"] * r["dy"] + r["yi"]
                flag = 1
            elif auxX == r["xf"] and r["yi"] < auxY < r["yf"]:
                auxY = (ypoint - r["yi"]) // r["dy"] * r["dy"] + r["yi"]
            elif r["xi"] < auxX < r["xf"] and auxY == r["yf"]:
                auxX = (xpoint - r["xi"]) // r["dx"] * r["dx"] + r["xi"]
        if flag:
            return[auxX, auxY] 
        print("A figura é maior que os limites da malha")
        quit(1)



    """
    Percore x e y, obtendo os nós da malha irregular para cada ponto com a função getNode, 
    e removendo nós irrelevantes.
    """

    def criar_malha_irregular(self):
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
    Adiciona as informações das regiões da malha em um arquivo
    """

    def export_ranges(self, path):
        try:
            with open(path, "w") as dataFile:
                content = ''
                for i in self.ranges:
                    aux = ' '.join([str(elem) for elem in i.values()])
                    content = content + aux + "\n"
                dataFile.write(content)
        except:
            print('Path does not exist for export')
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
    


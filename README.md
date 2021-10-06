# Extração de Conjuntos de Contornos a Partir de Figuras  🐍🔍
---
#### Um script em Python para a extração de um conjunto de pontos que formam um objeto em uma figura.
#### Esse repositório foi criado como continuação do Projeto de Iniciação Científica: "Reconhecimento de Malhas".

#### Python scripts  
##### Conjuntos de comandos que podem ser executados no CMD ou Bash.  
`main.py` - Programa inicial.  
`malha.py` - Cria malha com base no contorno gerado.  
##### Flags de `main.py`
`--help` - Parâmetro que mostra todos os outros parâmetros do projeto e suas descrições.  
`--figure/ -f` **OBRIGATORIO** - Parâmetro de entrada para a figura desejada.  
`--output/ -o` Parâmetro para definir o nome do arquivo de saída. Caso não exista o arquivo será `[figure]-data.txt`.  
`--width/ -w` - Parâmetro para definir a largura máxima do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--height/ -h` - Parâmetro para definir a altura máxima do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--xoffset/ -xo` - Parâmetro para definir o deslocamento no eixo X (direita) do mínimo valor possivel do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--yoffset/ -yo` - Parâmetro para definir o deslocamento no eixo Y (baixo) do mínimo valor possivel do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--interval/ -i` - Define um intervalo entre cada ponto no output.  
`--matlab/ -m` - Parâmetro para definir se os pontos serão exportados no formato MATLAB, com origem (0, 0) no canto inferior esquerdo.  
`-metadata/ -md` - Parâmetro para exportar um arquivo de metadata contendo as informações executadas no projeto em questão, gerando um arquivo `[output/figure]-metadata.json`.  
`--graphical/ -gui` **EM DESENVOLVIMENTO** - Roda o programa com a interface de usuário experimental.  
`--verbose` **EM DESENVOLVIMENTO** - Parâmetro para habilitar o modo verboso (detalhes de comandos e procedimentos).  

##### Flags de `malha.py`
`--help` - Parâmetro que mostra todos os outros parâmetros do projeto e suas descrições.  
`--inputfile/ -f` **OBRIGATORIO** - Parâmetro de entrada para as coordenadas do contorno da figura.  
`--output/ -o` Parâmetro para definir o nome do arquivo de saída. Caso não exista o arquivo será `[inputfile]-data.txt`.    
`--xmin/ -xo` - Parâmetro para definir o mínimo valor possivel do eixo x na malha. Caso não seja inserido seu valor será 0.  
`--ymin/ -yo` - Parâmetro para definir o mínimo valor possivel do eixo y na malha. Caso não seja inserido seu valor será 0.  
`--defaultmin/ -dm` - Parâmetro para definir que `--xmin/ -xo` e `--ymin/ -yo` serão os valores mínimos do conjunto de pontos do contorno da figura.   
`--dx/ -dx` - Tamanho do nó da malha em relação ao eixo x. Caso não seja inserido seu valor será obtido utizando os parâmetros `--nx/ -nx` e `--xmin/ -xo`.   
`--dy/ -dy` - Tamanho do nó da malha em relação ao eixo y. Caso não seja inserido seu valor será obtido utizando os parâmetros `--ny/ -ny` e `--ymin/ -yo`.   
`--nx/ -nx` - Número de nós da malha em relação ao eixo x. Caso não seja inserido seu valor será obtido utizando os parâmetros `--dx/ -dx` e `--xmin/ -xo`.  
`--ny/ -ny` - Número de nós da malha em relação ao eixo y. Caso não seja inserido seu valor será obtido utizando os parâmetros `--dy/ -dy` e `--ymin/ -yo`.  

É necessário que pelo menos o tamanho ou número de nós seja informado para cada eixo.

##### Dependências  
`python3` - Linguagem de Programação  
`pip install click` - Utilizado para o CLI  
`pip install opencv-python` - Utilizado para o Processamento de Imagens  
`pip install Pillow` - Utilizado para a integração da Interface Gráfica com o OpenCv  

##### Exemplos de Execução  
`python main.py -f "./tests/basicTest/basicTest1.png"`  
`python main.py -f ./tests/basicTest/basicTest1.png`  
`python main.py --figure //.../tests/basicTest/basicTest1.png`  
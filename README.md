# Extração de Conjuntos de Contornos a Partir de Figuras  🐍🔍
---
#### Um script em Python para a extração de um conjunto de pontos que formam um objeto em uma figura.
#### Esse repositório foi criado como continuação do Projeto de Iniciação Científica: "Reconhecimento de Malhas".

#### Python scripts  
##### Conjuntos de comandos que podem ser executados no CMD ou Bash.  
`main.py` - Programa inicial.  
##### Flags  
`--help` - Parâmetro que mostra todos os outros parâmetros do projeto e suas descrições.  
`--figure/ -f` **OBRIGATORIO** - Parâmetro de entrada para a figura desejada.  
`--output/ -o` Parâmetro para definir o nome do arquivo de saída. Caso não exista o arquivo será `[figure]-data.txt`.
`--width/ -w` - Parâmetro para definir a largura máxima do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--height/ -h` - Parâmetro para definir a altura máxima do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--xoffset/ -xo` - Parâmetro para definir o deslocamento no eixo X (direita) do mínimo valor possivel do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--yoffset/ -yo` - Parâmetro para definir o deslocamento no eixo Y (baixo) do mínimo valor possivel do conjunto de pontos. Caso não seja inserido ou seja -1 o comando será ignorado.  
`--matlab/ -m` - Parâmetro para definir se os pontos serão exportados no formato MATLAB, com origem (0, 0) no canto inferior esquerdo.  
`-metadata/ -md` - Parâmetro para exportar um arquivo de metadata contendo as informações executadas no projeto em questão, gerando um arquivo `[output/figure]-metadata.json`. 
`--verbose` **EM DESENVOLVIMENTO** - Parâmetro para habilitar o modo verboso (detalhes de comandos e procedimentos).  

##### Dependências  
`python3` - Linguagem de Programação  
`pip install click` - Utilizado para o CLI  
`pip install opencv-python` - Utilizado para o Processamento de Imagens  

##### Exemplos de Execução  
`python main.py -f "./tests/basicTest/basicTest1.png"`  
`python main.py -f ./tests/basicTest/basicTest1.png`  
`python main.py --figure //.../tests/basicTest/basicTest1.png`  
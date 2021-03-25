# Extração de Conjuntos de Contornos a Partir de Figuras  🐍🔍
---
#### Um script em Python para a extração de um conjunto de pontos que formam um objeto em uma figura.
#### Esse repositório foi criado como continuação do Projeto de Iniciação Científica: "Reconhecimento de Malhas".

#### Python scripts
###### Conjuntos de comandos que podem ser executados no CMD ou Bash.
`main.py` - Programa inicial.
###### Flags
`-f figure/ --figure figure` **OBRIGATORIO** - Parâmetro de entrada para a figura desejada.
`--verbose` **EM DESENVOLVIMENTO** - Parâmetro para habilitar o modo verboso (detalhes de comandos e procedimentos).

###### Dependências
`python3` - Linguagem de Programação
`pip install click` - Utilizado para o CLI
`pip install opencv-python` - Utilizado para o Processamento de Imagens

###### Exemplos de Execução
`python main.py -f "./tests/basicTest/basicTest1.png"`
`python main.py -f ./tests/basicTest/basicTest1.png`
`python main.py --figure C:/.../tests/basicTest/basicTest1.png`
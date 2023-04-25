# Sumário
*******
Tabelas de conteúdo 
 1. [Objetivo](#objetivo)
 2. [Imagens](#imagens)
 3. [Funcionalidades](#funcionalidades)
 4. [Guia de Instalação](#guia-de-instalacao)

*******
<div id= 'objetivo'>

# Objetivo

Este projeto consiste em desenvolver um jogo que simula uma batalha de robos. Projeto este, que é de carater avaliativo, para conclusão do primeiro modulo de treinamento em python para o processo seletivo da **Jala University**.

<div id= 'imagens'>

# Imagens

### Pagina Inicial

```python
##################################################################################################
##                                                                                              ##   
##       888888b.          d8888 88888888888        d8888 888      888    888        d8888      ## 
##       888  "88b        d88888     888           d88888 888      888    888       d88888      ##
##       888  .88P       d88P888     888          d88P888 888      888    888      d88P888      ## 
##       8888888K.      d88P 888     888         d88P 888 888      8888888888     d88P 888      ## 
##       888  "Y88b    d88P  888     888        d88P  888 888      888    888    d88P  888      ##
##       888    888   d88P   888     888       d88P   888 888      888    888   d88P   888      ##     
##       888   d88P  d8888888888     888      d8888888888 888      888    888  d8888888888      ##
##       8888888P"  d88P     888     888     d88P     888 88888888 888    888 d88P     888      ##                                                                      
##                                                                                              ## 
##                                                                                              ##                                              
##                                      8888888b.  8888888888                                   ##
##                                      888  "Y88b 888                                          ##
##                                      888    888 888                                          ##
##                                      888    888 8888888                                      ##
##                                      888    888 888                                          ##
##                                      888    888 888                                          ##
##                                      888  .d88P 888                                          ##
##                                      8888888P"  8888888888                                   ##
##                                                                                              ##
##                                                                                              ##
##                                                                                              ##
##                     8888888b.   .d88888b.  888888b.    .d88888b.   .d8888b.                  ##
##                      888   Y88b d88P" "Y88b 888  "88b  d88P" "Y88b d88P  Y88b                ##
##                      888    888 888     888 888  .88P  888     888 Y88b.                     ##
##                      888   d88P 888     888 8888888K.  888     888  "Y888b.                  ##
##                      8888888P"  888     888 888  "Y88b 888     888     "Y88b.                ##    
##                      888 T88b   888     888 888    888 888     888       "888                ##
##                      888  T88b  Y88b. .d88P 888   d88P Y88b. .d88P Y88b  d88P                ##
##                      888   T88b  "Y88888P"  8888888P"   "Y88888P"   "Y8888P"                 ##
##                                                                                              ##        
##                                                                                              ##
##                                                                                              ##
##                                                                                              ##
##                                                                                              ##
##                                                                                              ## 
##                                                                                              ##        
################################# |                      | #######################################       

                                🤖 | PRESSIONE QUALQUER TECLA!
```

### Robo 🤖

```python
MEU NOME É ROBOT
EU TENHO 100 % DE ENERGIA
 .
      0: CABEÇA
      ESTA DISPONIVEL: False
      ATAQUE: 5                              
      DEFESA: 10
      CONSUMO DE ENERGIA: 5
                  ^
                  |                  |1: ARMA
                  |                  |ESTA DISPONIVEL: True
                                     |ATAQUE: 15
                             ------> |DEFESA: 0
                _____                |CONSUMO DE ENERGIA: 10
               X_____\
       .-^-.  ||_| |_||  .-^-.
      /_\_/_\_|  |_|  |_/_\_/_\             |2: BRAÇO_ESQUERDO
      ||(_)| __\_____/__ |(_)||             |ESTA DISPONIVEL: False
      \/| | |::|\```/|::| | |\/             |ATAQUE: 3
      /`---_|::|-+-+-|::|_---'\             |DEFESA: 17
     / /  \ |::|-|-|-|::| /  \ \            |CONSUMO DE ENERGIA: 10
    /_/   /|`--'-+-+-`--'|\   \_\  ----->   |  
    | \  / |===/_\ /_\===| \  / |           |3: BRAÇO_DIREITO
    |  \/  /---/-/-\-\  o\  \/  |           |ESTA DISPONIVEL: False
    | ||| | O / /   \ \   | ||| |           |ATAQUE: 6
    | ||| ||-------------|o|||| |           |DEFESA: 5
    | ||| ||----\ | /----|o|||| |           |CONSUMO DE ENERGIA: 10
    | _|| ||-----|||-----|o|||_ |    
    \/|\/  |     |||     |o|\/|\/    |4: PERNA_ESQUERDA
    \_o/   |----|||||----|-' \o_/    |ESTA DISPONIVEL: False
           |##  |   |  ##|           |ATAQUE: 4
           |----|   |----|           |DEFESA: 20
           ||__ |   | __||           |CONSUMO DE ENERGIA: 15
          [|'  `|] [|'  `|]  ---->   | 
          [|`--'|] [|`--'|]          |5: PERNA_DIREITA
          /|__| |\ /| |__|\          |ESTA DISPONIVEL: False
          ||  | || ||    ||          |ATAQUE: 8
          ||__|_|| ||_|__||          |DEFESA: 13
          ||    || ||    ||          |CONSUMO DE ENERGIA: 15
          \|----|/ \|----|/    
          /______\ /______\
          |__||__| |__||__|


PARABÉNS, ROBO: Elias VOCÊ GANHOU!!

```
<div id= 'funcionalidades'>

# Funcionalidades

* Jogador vs Maquina
* Multiplayer - PVP
* Modo Torre - > Estilo Mortal Kombat
* Ranking

<div id= 'guia-de-instalacao'>

# Guia de instalação

Este guia tem como objetivo ajudar a configurar o ambiente para que possa ser executado localmente.

### Instalando Modulos

##### Requests - Trabalhar com requisições HTTP

`$ pip install requests`

##### IPython - Modulo para usilização de metodo de limpar a tela do console

`$ pip install IPython`


##### Executar o programa!

`$ python3 app.py`



# Autores

- Diego Nascimento
- Elias Junior

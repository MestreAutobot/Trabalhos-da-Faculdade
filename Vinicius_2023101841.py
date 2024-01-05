######################################################
# Programção I / Programação Funcional (2023/1)
# EP2 - Jogo da Velha
# Nome: Vinícius Constâncio de Moura Maia
# Matrícula:2023101841
######################################################

import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2023101841" 



def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Vinícius Constâncio de Moura Maia" 



def limpaTela(): 
    """
    função responsavel por limpar o terminal tanto no linux quanto no windows
    
    parâmetros:
            não existe valor de parâmetros
    retorno:
        Função não retorna nada
    """
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 



def jogadaComputador(listaTab,robo,opcao = 2,jogador="x"):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    listaTab: lista de tamanho 10 representando o tabuleiro
    robo: letra do computador
    opcao: opção de dificuldade da maquina
    jogador: letra do jogador 

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia: 
    a estratégia do modo normal consiste em sortear posições aleatórias que não foram escolhidas.

    a estratégia do modo difícil consiste em não deixar o jogador ganhar, fazendo com que sempre
    a maquina jogue em posições vantajosas atrapalhando o jogador, assim dando o resultado de empate 
    para o jogo na maioria dos casos. Porém se ela estiver faltando uma posição pra ganhar, e for 
    no turno da mesma ela jogará nessa posição que está faltando, assim ganhando. 
    """
    if opcao ==1:
        listaTab[0:]
        return jogadaComputadorFacil(listaTab,robo)
    elif opcao ==2:
        listaTab[0:]
        return escolherMovimento(listaTab,jogador,robo)
        


def escolherMovimento(listaTab,jogador,robo):
    '''
    função responsavel por sortear uma posição aleatoria entre [1,3,5,7,9] e retornar essa posição, caso a maquina inicie, 
    e se a maquina não iniciar primeiro ela retorna a função analisarjogo para verificar o estado do tabuleiro
    
    Parâmetros:
        listatab: lista de tamanho 10 representando o tabuleiro
        robo: letra do computador
        jogador: letra do jogador 

    Retorno:
    posicção de [1,3,5,7,9] caso a maquina começe, se não ela retorna uma posição (entre 1 e 9) para o tabuleiro
    '''
    
    if listaTab == [" "," "," "," "," "," "," "," "," "," "]:
        aleatorio = random.choice([1,3,5,7,9])
        return aleatorio
    else:
        return AnalisarJogo(listaTab,jogador,robo)



def AnalisarJogo(tab,jogador,robot):
    '''
    função responsavel por implementar a estratégia geral da máquina para analisar 
    o estado atual do jogo e decidir a melhor jogada do computador naquele turno.
    Fazendo com que a maquina esteja mais perto da vitória
    
    Parâmetros:
    tab: lista de tamanho 10 representando o tabuleiro
    robot: letra do computador
    jogador: letra do jogador 

    Retorno:
    Posição (entre 1 e 9) para o tabuleiro 
    '''
    
    vitoria = [(tab[1],tab[2],tab[3]),(tab[4],tab[5],tab[6]),(tab[7],tab[8],tab[9]),(tab[1],tab[5],tab[9]),(tab[3],tab[5],tab[7]),(tab[1],tab[4],tab[7]),(tab[2],tab[5],tab[8]),(tab[3],tab[6],tab[9])] 
    ######finalizacao######
    
    if vitoria[0][0] == " " and vitoria [0][1] == robot and vitoria[0][2] == robot:
        tab[1] = robot
        return 1
    elif vitoria[0][0] == robot and vitoria [0][1] == " " and vitoria[0][2] == robot:
        tab[2] = robot
        return 2
    elif vitoria[0][0] == robot and vitoria [0][1] == robot and vitoria[0][2] == " ":
        tab[3] = robot
        return 3
    
    elif vitoria[1][0] == " " and vitoria [1][1] == robot and vitoria[1][2] == robot:
        tab[4] = robot
        return 4
    elif vitoria[1][0] == robot and vitoria [1][1] == " " and vitoria[1][2] == robot:
        tab[5] = robot
        return 5
    elif vitoria[1][0] == robot and vitoria [1][1] == robot and vitoria[1][2] == " ":
        tab[6] = robot
        return 6
    
    elif vitoria[2][0] == " " and vitoria [2][1] == robot and vitoria[2][2] == robot:
        tab[7] = robot
        return 7
    elif vitoria[2][0] == robot and vitoria [2][1] == " " and vitoria[2][2] == robot:
        tab[8] = robot
        return 8
    elif vitoria[2][0] == robot and vitoria [2][1] == robot and vitoria[2][2] == " ":
        tab[9] = robot
        return 9
    
    elif vitoria[3][0] == " " and vitoria [3][1] == robot and vitoria[3][2] == robot:
        tab[1] = robot
        return 1
    elif vitoria[3][0] == robot and vitoria [3][1] == " " and vitoria[3][2] == robot:
        tab[5] = robot
        return 5
    elif vitoria[3][0] == robot and vitoria [3][1] == robot and vitoria[3][2] == " ":
        tab[9] = robot
        return 9
    
    elif vitoria[4][0] == " " and vitoria [4][1] == robot and vitoria[4][2] == robot:
        tab[3] = robot
        return 3
    elif vitoria[4][0] == robot and vitoria [4][1] == " " and vitoria[4][2] == robot:
        tab[5] = robot
        return 5
    elif vitoria[4][0] == robot and vitoria [4][1] == robot and vitoria[4][2] == " ":
        tab[7] = robot
        return 7
    
    elif vitoria[5][0] == " " and vitoria [5][1] == robot and vitoria[5][2] == robot:
        tab[1] = robot
        return 1
    elif vitoria[5][0] == robot and vitoria [5][1] == " " and vitoria[5][2] == robot:
        tab[4] = robot
        return 4
    elif vitoria[5][0] == robot and vitoria [5][1] == robot and vitoria[5][2] == " ":
        tab[7] = robot
        return 7
    
    elif vitoria[6][0] == " " and vitoria [6][1] == robot and vitoria[6][2] == robot:
        tab[2] = robot
        return 2
    elif vitoria[6][0] == robot and vitoria [6][1] == " " and vitoria[6][2] == robot:
        tab[5] = robot
        return 5
    elif vitoria[6][0] == robot and vitoria [6][1] == robot and vitoria[6][2] == " ":
        tab[8] = robot
        return 8
    
    elif vitoria[7][0] == " " and vitoria [7][1] == robot and vitoria[7][2] == robot:
        tab[3] = robot
        return 3
    elif vitoria[7][0] == robot and vitoria [7][1] == " " and vitoria[7][2] == robot:
        tab[6] = robot
        return 6
    elif vitoria[7][0] == robot and vitoria [7][1] == robot and vitoria[7][2] == " ":
        tab[9] = robot
        return 9
    ########defesa#########
    elif vitoria[0][0] == " " and vitoria [0][1] == jogador and vitoria[0][2] == jogador:
        tab[1] = robot
        return 1
    elif vitoria[0][0] == jogador and vitoria [0][1] == " " and vitoria[0][2] == jogador:
        tab[2] = robot
        return 2
    elif vitoria[0][0] == jogador and vitoria [0][1] == jogador and vitoria[0][2] == " ":
        tab[3] = robot
        return 3
    
    elif vitoria[1][0] == " " and vitoria [1][1] == jogador and vitoria[1][2] == jogador:
        tab[4] = robot
        return 4
    elif vitoria[1][0] == jogador and vitoria [1][1] == " " and vitoria[1][2] == jogador:
        tab[5] = robot
        return 5
    elif vitoria[1][0] == jogador and vitoria [1][1] == jogador and vitoria[1][2] == " ":
        tab[6] = robot
        return 6
   
    elif vitoria[2][0] == " " and vitoria [2][1] == jogador and vitoria[2][2] == jogador:
        tab[7] = robot
        return 7
    elif vitoria[2][0] == jogador and vitoria [2][1] == " " and vitoria[2][2] == jogador:
        tab[8] = robot
        return 8
    elif vitoria[2][0] == jogador and vitoria [2][1] == jogador and vitoria[2][2] == " ":
        tab[9] = robot
        return 9
    
    elif vitoria[3][0] == " " and vitoria [3][1] == jogador and vitoria[3][2] == jogador:
        tab[1] = robot
        return 1
    elif vitoria[3][0] == jogador and vitoria [3][1] == " " and vitoria[3][2] == jogador:
        tab[5] = robot
        return 5
    elif vitoria[3][0] == jogador and vitoria [3][1] == jogador and vitoria[3][2] == " ":
        tab[9] = robot
        return 9
    
    elif vitoria[4][0] == " " and vitoria [4][1] == jogador and vitoria[4][2] == jogador:
        tab[3] = robot
        return 3
    elif vitoria[4][0] == jogador and vitoria [4][1] == " " and vitoria[4][2] == jogador:
        tab[5] = robot
        return 5
    elif vitoria[4][0] == jogador and vitoria [4][1] == jogador and vitoria[4][2] == " ":
        tab[7] = robot
        return 7

    elif vitoria[5][0] == " " and vitoria [5][1] == jogador and vitoria[5][2] == jogador:
        tab[1] = robot
        return 1
    elif vitoria[5][0] == jogador and vitoria [5][1] == " " and vitoria[5][2] == jogador:
        tab[4] = robot
        return 4
    elif vitoria[5][0] == jogador and vitoria [5][1] == jogador and vitoria[5][2] == " ":
        tab[7] = robot
        return 7
    
    elif vitoria[6][0] == " " and vitoria [6][1] == jogador and vitoria[6][2] == jogador:
        tab[2] = robot
        return 2
    elif vitoria[6][0] == jogador and vitoria [6][1] == " " and vitoria[6][2] == jogador:
        tab[5] = robot
        return 5
    elif vitoria[6][0] == jogador and vitoria [6][1] == jogador and vitoria[6][2] == " ":
        tab[8] = robot
        return 8
    
    elif vitoria[7][0] == " " and vitoria [7][1] == jogador and vitoria[7][2] == jogador:
        tab[3] = robot
        return 3
    elif vitoria[7][0] == jogador and vitoria [7][1] == " " and vitoria[7][2] == jogador:
        tab[6] = robot
        return 6
    elif vitoria[7][0] == jogador and vitoria [7][1] == jogador and vitoria[7][2] == " ":
        tab[9] = robot
        return 9
    
    elif tab[5] == jogador:
        return jogadameio(tab,jogador,robot)
    
    elif tab[1] == jogador and tab [9] == jogador or tab[3] == jogador and tab[7]==jogador:
        PosicaoRandom = random.choice([2,4,6,8])
        if tab[PosicaoRandom] == " ":
            tab[PosicaoRandom] = robot
            return PosicaoRandom
        else:
            return AnalisarJogo(tab,jogador,robot)
    elif tab[4] == jogador and tab [9] == jogador:
        if tab[7]== " ":
            tab[7] = robot
            return 7

    elif tab[6] == jogador and tab [7] == jogador:
        if tab[9]== " ":
            tab[9] = robot
            return 9
        
    elif vitoria[0][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[0][2] == " ":
            tab[3] = robot
            return 3
        elif vitoria[0][1] == " ":
            tab[2] = robot
            return 2
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[0][1] == jogador:
        if vitoria[0][0] == " ":
            tab[1] = robot
            return 1
        elif vitoria[0][2] == " ":
            tab[3] = robot
            return 3
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[0][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[0][0] == " ":
            tab[1] = robot
            return 1
        elif vitoria[0][1] == " ":
            tab[2] = robot
            return 2
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[1][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[1][2] == " ":
            tab[6] = robot
            return 6
        elif vitoria[1][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[1][1] == jogador:
        if vitoria[1][0] == " ":
            tab[4] = robot
            return 4
        elif vitoria[1][2] == " ":
            tab[6] = robot
            return 6
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[1][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[1][0] == " ":
            tab[4] = robot
            return 4
        elif vitoria[1][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[2][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[2][2] == " ":
            tab[9] = robot
            return 9
        elif vitoria[2][1] == " ":
            tab[8] = robot
            return 8
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[2][1] == jogador:
        if vitoria[2][0] == " ":
            tab[7] = robot
            return 7
        elif vitoria[2][2] == " ":
            tab[9] = robot
            return 9
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[2][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[2][0] == " ":
            tab[7] = robot
            return 7
        elif vitoria[2][1] == " ":
            tab[8] = robot
            return 8
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[3][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[3][2] == " ":
            tab[9] = robot
            return 9
        elif vitoria[3][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[3][1] == jogador:
        if vitoria[3][0] == " ":
            tab[1] = robot
            return 1
        elif vitoria[3][2] == " ":
            tab[9] = robot
            return 9
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[3][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[3][0] == " ":
            tab[1] = robot
            return 1
        elif vitoria[3][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[4][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[4][2] == " ":
            tab[7] = robot
            return 7
        elif vitoria[4][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[4][1] == jogador:
        if vitoria[4][0] == " ":
            tab[3] = robot
            return 3
        elif vitoria[4][2] == " ":
            tab[7] = robot
            return 7
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[4][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[4][0] == " ":
            tab[3] = robot
            return 3
        elif vitoria[4][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[5][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[5][2] == " ":
            tab[7] = robot
            return 7
        elif vitoria[5][1] == " ":
            tab[4] = robot
            return 4
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[5][1] == jogador:
        if vitoria[5][0] == " ":
            tab[1] = robot
            return 1
        elif vitoria[5][2] == " ":
            tab[7] = robot
            return 7
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[5][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[5][0] == " ":
            tab[1] = robot
            return 1
        elif vitoria[5][1] == " ":
            tab[4] = robot
            return 4
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[6][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[6][2] == " ":
            tab[8] = robot
            return 8
        elif vitoria[6][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[6][1] == jogador:
        if vitoria[6][0] == " ":
            tab[2] = robot
            return 2
        elif vitoria[6][2] == " ":
            tab[8] = robot
            return 8
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[6][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[6][0] == " ":
            tab[2] = robot
            return 2
        elif vitoria[6][1] == " ":
            tab[5] = robot
            return 5
        else:
            jogadaAleatoria(tab,robot)
    
    elif vitoria[7][0] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[7][2] == " ":
            tab[9] = robot
            return 9
        elif vitoria[7][1] == " ":
            tab[6] = robot
            return 6
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[7][1] == jogador:
        if vitoria[7][0] == " ":
            tab[3] = robot
            return 3
        elif vitoria[7][2] == " ":
            tab[9] = robot
            return 9
        else:
            jogadaAleatoria(tab,robot)
    elif vitoria[7][2] == jogador:
        if tab [5]  == " ":
            tab[5] = robot
            return 5
        if vitoria[7][0] == " ":
            tab[3] = robot
            return 3 
        elif vitoria[7][1] == " ":
            tab[6] = robot
            return 6
        else:
            jogadaAleatoria(tab,robot)



def jogadameio(tab,jogador,robot):
    '''
    função responsavel pela estratégia da maquina caso o jogador jogue na posição tab[5]
    
    parâmetros:
                Tab: lista de tamanho 10 representando o tabuleiro
                robot: letra do computador
                jogador: letra do jogaddor
    retorno:
            Posição (entre 1 e 9) para o tabuleiro 
    '''

    if tab[5] and tab[1] == jogador and tab[9] == robot:
        if tab[3] == " ":
            tab[3] = robot
            return 3
        elif tab[6] == " ":
            tab[6] = robot
            return 6
    if tab[5] and tab[3] == jogador and tab[7] == robot:
        if tab[1] == " ":
            tab[1] = robot
            return 1
        elif tab[4] == " ":
            tab[4] = robot
            return 4
    if tab[5] and tab[7] == jogador and tab[3] == robot:
        if tab[1] == " ":
            tab[1] = robot
            return 1
        if tab[4] == " ":
            tab[4] = robot
            return 4
    if tab[5] and tab[9] == jogador and tab[1] == robot:
        if tab[3] == " ":
            tab[3] = robot
            return 3
        if tab[6] == " ":
            tab[6] = robot
            return 6
    if tab[5] and tab[9] == jogador:
        if tab[1] == " ":
            tab[1] = robot
            return 1
    if tab[5] and tab[7] == jogador:
        if tab[3] == " ":
            tab[3] = robot
            return 3
    if tab[5] and tab[3] == jogador:
        if tab[7] == " ":
            tab[7] = robot
            return 7
    if tab[5] and tab[1] == jogador:
        if tab[9] == " ":
            tab[9] = robot
            return 9
    elif tab[5] == jogador:
        diagonalRandom = random.choice([1,3,7,9])
        if tab[diagonalRandom] == " ":
            tab[diagonalRandom] = robot
            return diagonalRandom
        elif tab[diagonalRandom] != " ":
            return AnalisarJogo(tab,jogador,robot)
        else:
            jogadaAleatoria(tab,robot)
    else:
        return jogadaAleatoria(tab,robot)



def jogadaAleatoria(tab,robot):
    '''
    função responsavel por escolher uma opção aleatoria do tabuleiro caso a maquina
    não saiba a onde jogar, e se a função escolher uma opção onde já tenha um simbolo 
    ela vai entrar em recursão 
    
    parâmetros:
                Tab: lista de tamanho 10 representando o tabuleiro
                robot: letra do computador
    retorno:
            Posição (entre 1 e 9) para o tabuleiro
    '''
    aleatorio = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if tab[aleatorio] == " ":
        tab[aleatorio] = robot
        return aleatorio
    else:
        return jogadaAleatoria(tab,robot)



def jogadaComputadorFacil(listaTab, robo):
    '''
    função responasvel pela dificuldade normal do jogo, onde ela vai sortear um número de 0 a 9 para ser marcado no tabuleiro.
    Se o espaço escolhido já tiver algum simbolo diferente do [" "] ele entra em recursão se não ele marca no local
    
    parâmetros:
                listaTab: lista de tamanho 10 representando o tabuleiro
                robo: letra do computador
    retorno:
            Posição (entre 1 e 9) para o tabuleiro
    '''
    aleatorio = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    if aleatorio == 0:
        return jogadaComputadorFacil(listaTab, robo)
    if listaTab[aleatorio] == " ":
        listaTab[aleatorio] = robo
        return aleatorio
    else:
        return jogadaComputadorFacil(listaTab, robo)



def telaAbertura():
    """
    função responsavel pela tela de abertura do programa, que só vai ser realmente iniciado quando for precionado uma tecla
    
    parâmetros:
            não existe valor de parâmetros
    retorno:
         a função não retorna nada

    """
    print()
    print("                                                     /$$                 /$$    /$$          /$$ /$$                      ")
    print("                                                    | $$                | $$   | $$         | $$| $$                      ")
    print("       /$$  /$$$$$$   /$$$$$$   /$$$$$$         /$$$$$$$  /$$$$$$       | $$   | $$ /$$$$$$ | $$| $$$$$$$   /$$$$$$       ")
    print("      |__/ /$$__  $$ /$$__  $$ /$$__  $$       /$$__  $$ |____  $$      |  $$ / $$//$$__  $$| $$| $$__  $$ |____  $$      ")
    print("       /$$| $$  \ $$| $$  \ $$| $$  \ $$      | $$  | $$  /$$$$$$$       \  $$ $$/| $$$$$$$$| $$| $$  \ $$  /$$$$$$$      ")
    print("      | $$| $$  | $$| $$  | $$| $$  | $$      | $$  | $$ /$$__  $$        \  $$$/ | $$_____/| $$| $$  | $$ /$$__  $$      ")
    print("      | $$|  $$$$$$/|  $$$$$$$|  $$$$$$/      |  $$$$$$$|  $$$$$$$         \  $/  |  $$$$$$$| $$| $$  | $$|  $$$$$$$      ")
    print("      | $$ \______/  \____  $$ \______/        \_______/ \_______/          \_/    \_______/|__/|__/  |__/ \_______/      ")
    print(" /$$  | $$           /$$  \ $$                                                                                            ")
    print("|  $$$$$$/          |  $$$$$$/                                                                                            ")
    print(" \______/            \______/                                                                                             ")
    print()                                                                                                                                                                                                                                                                             
    input("Precione uma tecla para continuar...")



def score(vitoriaJ,vitoriaR,empate):
    '''
    função responsavel por imprimir o score
    
    parâmetros:
            vitoriaJ: quantidade de pontos do jogador
            vitoriaR: quantidade de pontos da maquina
            empate:   quantidade de pontos de empate
    retorno:
         a função não retorna nada
    '''
    print("+"+"="*49+"+")
    print(f"| Jogador score: {vitoriaJ}"+32*" "+"|")
    print(f"| Maquina score: {vitoriaR}"+32*" "+"|")
    print(f"| Empate score:  {empate}"+32*" "+"|")
    print("+"+"="*49+"+")



def foto():
    """
    função imprimi o criador o criador do jogo da velha
    
    parâmetros:
             a função não tem parâmetros
    retorno:
             a função não retorna nada
    """
    print("+"+"="*69+"+")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣴⣿⡿⠋⠈⠻⣮⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡿⠋⠀⠀⠀⠀⠙⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠿⠿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   |")
    print("| ⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⣀⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⠀⠀   |")
    print("| ⢀⣤⣾⡿⠟⠛⠛⢿⣿⣶⣾⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣦⣀⣀⣤⣶⣿⡿⠿⢿⣿⡀⠀   |")
    print("| ⣿⣿⠏⠀⢰⡆⠀⠀⠉⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⡿⠟⠋⠁⠀⠀⢸⣿⠇⠀   |")
    print("| ⣿⡟⠀⣀⠈⣀⡀⠒⠃⠀⠙⣿⡆⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀   |")
    print("| ⣿⡇⠀⠛⢠⡋⢙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀   |")
    print("| ⣿⣧⠀⠀⠀⠓⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠀⠀⢸⣧⣤⣤⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⠀   |")
    print("| ⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠻⣷⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠁⠀⠀   |")
    print("| ⠈⠛⠻⠿⢿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⢿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡄⠀⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⢿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡄⠀   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⣿⣷⣶⣶⣤⣤⣀⡀⠀⠀⠀⢀⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡿⣄   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⣿⣷⣶⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣹   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⢸⣧   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣆⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣾⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⣿   |")
    print("| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣻⣷⣶⣾⣿⣿⡿⢯⣛⣛⡋⠁⠀⠀⠉⠙⠛⠛⠿⣿⣿⡷⣶⣿   |")
    print("+"+"="*69+"+")
    print("|"+" "*22+":3 Programador_Meowson ;3"+" "*22+"|")
    print("+"+"="*69+"+")



def Tutorial():
    """
    função responsavel por imprimir o tutorial
    
    parâmetros:
                nenhum
    retorno:
                nenhum 
    """
    limpaTela()
    print(" "*31+"ᓚᘏᗢ")
    print("+"+"="*61+"+")
    print("|"+" "*27+"Tutorial"+" "*26+"|")
    print("+"+"="*61+"+")
    print("|"+"- O tabuleiro  é uma matriz  de três linhas por três colunas."+"|")
    print("+"+"="*61+"+")
    print("|"+"- Dois jogadores escolhem uma marcação cada um, geralmente um"+"|") 
    print("|"+" círculo (o) e um xis (x)."+" "*35+"|")
    print("+"+"="*61+"+")
    print("|"+"- Os jogadores jogam alternadamente, uma marcação por vez em"+" "*1+"|")
    print("|"+" uma lacuna que esteja vazia."+" "*32+"|")
    print("+"+"="*61+"+")
    print("|"+" - O objectivo é conseguir três círculos ou três xis em "+" "*5+"|")
    print("|"+" linha, quer horizontal, vertical ou diagonal , e ao mesmo"+" "*3+"|")
    print("|"+" tempo, quando possível, impedir o adversário de ganhar na"+" "*3+"|")
    print("|"+" próxima jogada. Pronto para jogar?"+" "*26+"|")
    print("+"+"="*61+"+")



def verificaEscolha():
    '''
    função responsavel pela escolha de simbolo que o jogador quer selecionar
    
    parâmetros:
            nenhum
    retorno:
            a função retorna o simbolo que o jogador quer ser,e o simbolo da maquina
    '''
    escolha = input("Você quer ser 'X' ou 'O'?")
    if len(escolha) > 0:
        if escolha != "X" and escolha != "O" and escolha != "x" and escolha != "o":
            return verificaEscolha()
        elif escolha == "X" or escolha == "x":
            escolhaBot = "O"
            return "X", escolhaBot
        elif  escolha == "O" or escolha == "o":
            escolhaBot = "X"
            return "O", escolhaBot
    else:
        return verificaEscolha()



def leValor(funcaoConversao, msgInput="", msgErro="ERRO: Valor inválido"):
    """
    função é responsável por converter um valor digitado pelo usuário de acordo com o tipo de conversão especificado (como float, int, etc.). 
    Caso a conversão não seja possível, a função imprime uma mensagem de erro e entra em uma recursão, continuando a pedir um novo valor até que 
    o valor correto seja digitado.
    
    parâmetros:
            funcaoConversao: recebe o tipo de conversão float, int, etc.
            msgInput: recebe um string que vai aparecer na mensagem do input da função
            msgErro: recebe um string que vai imprimir a mensagem de erro   
    retorno:
        a função retorna funcaoConversao(input(msgInput)), caso o valor da conversão esteja correto, caso não esteja começa o passo de recursão até o cliente digitar o valor certo
    """
    try:  
        return funcaoConversao(input(msgInput))
    except:  
        print(msgErro)
        return leValor(funcaoConversao, msgInput, msgErro)



def maquina():
    '''
    a função maquina é responsável por exibir o menu do jogo da velha 
    e permitir que o usuário escolha entre as opções disponíveis.
    
    Parâmetros:
            nenhum
    retorno:
            não retorna nada
    '''
    print("+"+"="*49+"+")
    print("|"+" "*5+"bem vindo ao clássico Jogo da Velha :)"+6*" "+"|")
    print("+"+"="*49+"+")
    print("|"+"[1]jogar"+41*" "+"|")
    print("|"+"[2]tutorial"+38*" "+"|")
    print("|"+"[3]créditos"+38*" "+"|")
    print("|"+"[4]sair"+42*" "+"|")
    print("+"+"="*49+"+")
    opcao = leValor(int,"digite uma opção: ","A opção deve ser um inteiro")
    limpaTela()
    if opcao == 1:
        opcaoJogo()
    elif opcao == 2:
        Tutorial()
    elif opcao ==3:
        foto()
    elif opcao ==4:
        print("Desligando ;-;")
        exit()
    else:
        print("Opção inválida!")
    input("--> Enter para continuar...")
    limpaTela()
    maquina()



def opcaoJogo(PontosJogador=0,Pontosmaquina=0,PontosEmpate=0):
    '''
    função que armazena a quantidade de vitorias tanto do jogador,quanto a maquina e a quantidade de empates 
    além de imprimir um menu escolhendo escolhendo a dificuldade da maquina

    Parâmetros:
            PontosJogador: pontuação do jogador 
            PontosMaquina: pontuação da máquina 
            PontosEmpate: quantidade de empates 
    retorno:
            não retorna nada
    '''
    listaTab = [" "," "," "," "," "," "," "," "," "," "]
    print("+"+"="*49+"+")
    print("|"+" "*19+"Dificuldade"+19*" "+"|")
    print("+"+"="*49+"+")
    print("|"+"[1]Normal"+40*" "+"|")
    print("|"+"[2]Difícil"+39*" "+"|")
    print("+"+"="*49+"+")
    opcao = leValor(int,"digite a dificuldade: ","A opção deve ser um inteiro")
    if opcao != 1 and opcao != 2:
        limpaTela()
        opcaoJogo()
    elif opcao == 1:
        quemInicia = primeiraJogada()
        jogador, robo = verificaEscolha()
        limpaTela()
        jogo(opcao,listaTab,jogador,robo,quemInicia,PontosJogador,Pontosmaquina,PontosEmpate)
    elif opcao == 2:
        quemInicia = primeiraJogada()
        jogador, robo = verificaEscolha()
        limpaTela()
        jogo(opcao,listaTab,jogador,robo,quemInicia,PontosJogador,Pontosmaquina,PontosEmpate)



def PosicaoJogada(tabuleiro,opJogador,opBot):
    """
    Função destinada a escolher em qual posição o jogador irá jogar.

    Parâmetros:
            tabuleiro: lista de tamanho 10 representando o tabuleiro
            opJogador: a opção escolhida pelo jogador ('X' ou 'O')
            opBot: a opção do bot (a opção oposta à escolhida pelo jogador)
    Retorna:
        A posição escolhida pelo jogador para fazer sua jogada, caso seja escolhido uma posição errada ou já ocupada 
        com um simbolo a função entra em recursão.
    """
    jogada = leValor(int,"digite a posição: ","A opção deve ser um inteiro")
    if jogada <= 9 and jogada>=1:
        if jogada == 1 and tabuleiro[1] == " ":
            return jogada
        elif jogada == 2 and tabuleiro[2] == " ":
            return jogada
        elif jogada == 3 and tabuleiro[3] == " ":
            return jogada
        elif jogada == 4 and tabuleiro[4] == " ":
            return jogada
        elif jogada == 5 and tabuleiro[5] == " ":
            return jogada
        elif jogada == 6 and tabuleiro[6] == " ":
            return jogada
        elif jogada == 7 and tabuleiro[7] == " ":
            return jogada
        elif jogada == 8 and tabuleiro[8] == " ":
            return jogada
        elif jogada == 9 and tabuleiro[9] == " ":
            return jogada
        else:
            limpaTela()
            tabu(tabuleiro,opJogador,opBot)
            print("Jogada inválida")
            return PosicaoJogada(tabuleiro,opJogador,opBot)       
    else:
        limpaTela()
        tabu(tabuleiro,opJogador,opBot)
        print("Jogada inválida")
        return PosicaoJogada(tabuleiro,opJogador,opBot)



def jogo (op,listaTabuleiro,opJogador,opBot,quemInicia,PontosJogador,Pontosmaquina,PontosEmpate):
    '''
    função responsavel por gerir o fluxo de informações do jogo da velha, alternando entre a vez 
    do jogador e a vez da máquina, verificando se houve vitória ou empate e atualizando os pontos do 
    jogador, máquina e empate.
     Parâmetros:
        op            : opção de dificuldade da maquina
        listaTabuleiro: lista de tamanho 10 representando o tabuleiro
        opJogador     : opção escolhida pelo jogador ('X' ou 'O')
        opBot         : opção do bot (a opção oposta à escolhida pelo jogador)
        quemInicia    : variável que dita quem inicia 
        PontosJogador : quantidade de pontos do jogador
        Pontosmaquina : quantidade de pontos da maquina
        PontosEmpate  : quantidade de pontos de empate
    
    Retorno:
            a função retorna a função opcaoJogo() caso o jogador queira jogar novamente, com o estoque atualizado de pontos.
            e também retorna ela mesma caso o jogo não tenha acabado diminuindo em -1 ou +1 para mudar entre jogador e maquina
    '''
    listaTabuleiro[0:]
    if quemInicia == 1:
        tabu(listaTabuleiro,opJogador,opBot)
        print("A vez do jogador")
        jogadaPlayer = PosicaoJogada(listaTabuleiro,opJogador,opBot)
        listaTabuleiro[jogadaPlayer] = opJogador
        limpaTela()
        tabu(listaTabuleiro,opJogador,opBot)
        vitoriaPlayer(listaTabuleiro,opJogador)
        if vitoriaPlayer(listaTabuleiro,opJogador) == True: 
            score(PontosJogador+1,Pontosmaquina,PontosEmpate)
            print("Parábens você ganhou!!!")
            x = tentarNovamente()
            if x == "S" or x == "s":
                limpaTela()
                return opcaoJogo(PontosJogador+1,Pontosmaquina,PontosEmpate)
                
        else:
            empate(listaTabuleiro)
            if empate(listaTabuleiro)== True:
                score(PontosJogador,Pontosmaquina,PontosEmpate+1)
                print("O jogo terminou empatado!!!")
                x = tentarNovamente()
                if x == "S" or x == "s":
                    limpaTela()
                    return opcaoJogo(PontosJogador,Pontosmaquina,PontosEmpate+1)
            else:
                limpaTela()
                return jogo(op,listaTabuleiro,opJogador,opBot,quemInicia-1,PontosJogador,Pontosmaquina,PontosEmpate)      
    else:
        tabu(listaTabuleiro,opJogador,opBot)
        print("A vez da maquina")
        jogadaComputador(listaTabuleiro,opBot,op,opJogador)
        limpaTela()
        tabu(listaTabuleiro,opJogador,opBot)
        vitoriaPc(listaTabuleiro,opBot)
        if vitoriaPc(listaTabuleiro,opBot) == True:
            score(PontosJogador,Pontosmaquina+1,PontosEmpate)
            print("Que pena :( Tente melhor na proxima vez...")
            x = tentarNovamente()
            if x == "S" or x == "s":
                limpaTela()
                return opcaoJogo(PontosJogador,Pontosmaquina+1,PontosEmpate)
        else:
            empate(listaTabuleiro)
            if empate(listaTabuleiro)== True:
                score(PontosJogador,Pontosmaquina,PontosEmpate+1)
                print("O jogo terminou empatado!!!")
                x = tentarNovamente()
                if x == "S" or x == "s":
                    limpaTela()
                    return opcaoJogo(PontosJogador,Pontosmaquina,PontosEmpate+1)
            else:
                limpaTela()
                return jogo(op,listaTabuleiro,opJogador,opBot,quemInicia+1,PontosJogador,Pontosmaquina,PontosEmpate)



def tentarNovamente():
    '''
    função responsavel por perguntar ao jogador caso ele queira jogar novamente caso seja escrito algo fora de "s" ou "n" 
    a função entra em recursão 
    Parâmetros:
        nenhum 
    Retorno:
    retorna jogarNovamente caso o jogador queira tentar jogar de novo
    '''
    jogarNovamente = input("Deseja jogar novamente (S/N)? ")
    if jogarNovamente == "S" or jogarNovamente == "s":
        return jogarNovamente
    elif jogarNovamente == "n" or jogarNovamente == "N":
        limpaTela()
        print("Obrigado por jogar, e até outra hora :3")
        exit()
    else:
        limpaTela()
        print("Comando inválido!")
        return tentarNovamente()



def vitoriaPlayer(tabuleiro,player):
    '''
    função verifica se o jogador ganhou 
    
    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    player: letra do jogador 

    Retorno:
    retorna True se ganhou e false caso ainda não tenha ganhado 

    '''
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == player:
        return True
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == player:
        return True
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == player:
        return True
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == player:
        return True
    elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7] == player:
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == player:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == player:
        return True
    elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == player:
        return True
    else:
        return False



def empate(tabuleiro):
    """
    Função que verifica se houve empate ou não
    
    parâmetros:
            tabuleiro: lista de tamanho 10 representando o tabuleiro
    retorno:
            True se houve empate e False caso não houve 
    """
    if tabuleiro[1] != " " and tabuleiro[2] != " " and tabuleiro[3] != " " and tabuleiro[4] != " " and tabuleiro[5] != " " and tabuleiro[6] != " " and tabuleiro[7] != " " and tabuleiro[8] != " " and tabuleiro[9] != " ":
        return True
    else:
       return False



def vitoriaPc(tabuleiro,robot):   
    '''
    função verifica se a maquina ganhou 
    
    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    robot: letra da maquina 

    Retorno:
    retorna True se ganhou e false caso ainda não tenha ganhado 
    '''
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == robot:
        return True
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == robot:
        return True
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == robot:
        return True
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == robot:
        return True
    elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7] == robot:
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == robot:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == robot:
        return True
    elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == robot:
        return True
    else:
        return False



def tabu(tabuleiro,jogador,maquina):
    """
    Função que imprime o tabuleiro

    parâmetros:
            tabuleiro: lista de tamanho 10 representando o tabuleiro
            jogador: letra do jogador 
            maquina: letra do computador
    retorno:
        não retorna nada
    """
    print(" "*23+"ᓚᘏᗢ")
    print('=' * 51)
    print(' '*3+'MAPA DO JOGO '+' '*16 +'JOGO EM ANDAMENTO')
    print('=' * 51)
    print('+-----+-----+-----+', '          ', '+-----+-----+-----+')
    print('│  7  │  8  │  9  │', '          ', f'│  {tabuleiro[7]}  │  {tabuleiro[8]}  │  {tabuleiro[9]}  │')
    print('+-----+-----+-----+', '          ', '+-----+-----+-----+')
    print('│  4  │  5  │  6  │', '          ', f'│  {tabuleiro[4]}  │  {tabuleiro[5]}  │  {tabuleiro[6]}  │')
    print('+-----+-----+-----+', '          ', '+-----+-----+-----+')
    print('│  1  │  2  │  3  │', '          ', f'│  {tabuleiro[1]}  │  {tabuleiro[2]}  │  {tabuleiro[3]}  │')
    print('+-----+-----+-----+', '          ', '+-----+-----+-----+')
    print('+'+'=' * 49 +'+')
    print(f'| jogador:{jogador}'+' '* 39 +'|')
    print(f'| maquina:{maquina}'+' '* 39 +'|')
    print('+'+'=' * 49 +'+')



def primeiraJogada():
    """
    Função responsável por escolher aleatoriamente quem vai iniciar o jogo.
    parâmetros:
        não tem parâmetros
    retorno:
        retorna o número entre(0 e 1)
    """
    numeros = [0, 1]
    resultado = random.choice(numeros)
    return resultado



def main():
    '''
    função responsável por iniciar o programa
    parâmetros:
        não tem parâmetros
    retorno:
        não retorna nada
    '''
    limpaTela()
    telaAbertura()
    limpaTela()
    maquina()

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()

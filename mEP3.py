
def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """

    if p1 != "x" and p1 != "o" and p1 != " ":
        return False
    if p2 != "x" and p2 != "o" and p2 != " ":
        return False
    if p3 != "x" and p3 != "o" and p3 != " ":
        return False
    if p4 != "x" and p4 != "o" and p4 != " ":
        return False
    if p5 != "x" and p5 != "o" and p5 != " ":
       return False
    if p6 != "x" and p6 != "o" and p6 != " ":
        return False
    if p7 != "x" and p7 != "o" and p7 != " ":
        return False
    if p8 != "x" and p8 != "o" and p8 != " ":
        return False
    if p9 != "x" and p9 != "o" and p9 != " ":
        return False
    else:
        return True
       

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.
    Retorna True se a jogada for válida e False, caso contrário
    """
    valorX = 0
    valorO = 0
    if p1 == "x":
        valorX += 1
    if p1 == "o":
        valorO += 1
    if p2 == "x":
        valorX += 1
    if p2 == "o":
        valorO += 1
    if p3 == "x":
        valorX += 1
    if p3 == "o":
        valorO += 1
    if p4 == "x":
        valorX += 1
    if p4 == "o":
        valorO += 1
    if p5 == "x":
        valorX += 1
    if p5 == "o":
        valorO += 1
    if p6 == "x":
        valorX += 1
    if p6 == "o":
        valorO += 1
    if p7 == "x":
        valorX += 1
    if p7 == "o":
        valorO += 1
    if p8 == "x":
        valorX += 1
    if p8 == "o":
        valorO += 1
    if p9 == "x":
        valorX += 1
    if p9 == "o":
        valorO +=1
    if valorX > valorO:
        if (valorX - valorO) >= 2:
            return False
        else:
            return True
    if valorO > valorX:
        if (valorO - valorX) >= 2:
            return False
        else:
            return True  

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ("x" ou "o") venceu a jogada. 
    """
    valorvazio= 0
    
    if p1 == p2 == p3:
        if p1 == p2 == p3 == " ":
            return False
        else:
            print(f"O jogador '{p1}' venceu!")
            return True
    if p4 == p5 == p6:
        if p4 == p5 == p6 == " ":
            return False
        else:
            print(f"O jogador '{p4}' venceu!")
            return True
    if p7 == p8 == p9:
        if p7 == p8 == p9 == " ":
            return False
        else:
            print(f"O jogador '{p7}' venceu!")
            return True
    if p1 == p4 == p7:
        if p1 == p4 == p7 == " ":
            return False
        else:
            print(f"O jogador '{p1}' venceu!")
            return True
    if p2 == p5 == p8:
        if p2 == p5 == p8 == " ":
            return False
        else:
            print(f"O jogador '{p2}' venceu!")
            return True
    if p3 == p6 == p9:
        if p3 == p6 == p9 == " ":
            return False
        else:
            print(f"O jogador '{p3}' venceu!")
            return True
    if p1 == p5 == p9:
        if p1 == p5 == p9 == " ":
            return False
        else:
            print(f"O jogador '{p1}' venceu!")
            return True
    if p3 == p5 == p7:
        if p3 == p5 == p7 == " ":
            return False
        else:
            print(f"O jogador '{p3}' venceu!")
            return True
    if p1 == " ":
        valorvazio += 1
    if p2 == " ":
        valorvazio += 1
    if p3 == " ":
        valorvazio += 1
    if p4 == " ":
        valorvazio += 1
    if p5 == " ":
        valorvazio += 1
    if p6 == " ":
        valorvazio += 1    
    if p7 == " ":
        valorvazio += 1
    if p8 == " ":
        valorvazio += 1
    if p9 == " ":
        valorvazio += 1
    
    if valorvazio >= 1:
        print("O jogo nao terminou!") 
    else:
        print("Empate!")
        return False
    
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()

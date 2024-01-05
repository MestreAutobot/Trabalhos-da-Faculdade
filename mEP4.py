######################################################
# Programção I / Programação Funcional (2023/1)
# miniEP4 - Desenhando objetos geométricos simples
# Nome: vinícius constâncio de moura maia
# Matrícula:
######################################################

def verificarForma(a):
    if a != "R" and a != "P" and a != "TE"  and a != "TRE" and a != "TRD":
        return False
    else: 
        return True
    
def verificaMedida(c, b):
    try:
        c = int(c)
        b = int(b)  
        if c >= 0 and b>= 0 :
            return True
        else: 
            return False
    except ValueError:
        return False


def imprimeLinhaCheia(simbolo, largura):

    print(simbolo * largura)

def imprimeLinhaVazada2(simbolo, vezes, nEspacos, espaco2 = 0):
    
    if vezes != 0:
        espaco2 = espaco2 + 1
        print((" " * espaco2)+simbolo+(" " * (nEspacos - 2))+simbolo)
        imprimeLinhaVazada2(simbolo, vezes - 1, nEspacos, espaco2)
    elif vezes == 0:
        return

def imprimeLinhaVazada(simbolo, vezes, nEspacos):
    if vezes != 0:
        print(simbolo+(" " * (nEspacos - 2))+simbolo)
        imprimeLinhaVazada(simbolo, vezes - 1, nEspacos)
    elif vezes == 0:
        return

def imprimeRetangulo(simbolo, largura, altura):
    largura = int(largura)
    altura = int(altura)
    if largura == 1 and altura == 1:
        return simbolo
    imprimeLinhaCheia(simbolo, largura)
    imprimeLinhaVazada(simbolo, altura - 2, largura)
    imprimeLinhaCheia(simbolo, largura)   

def imprimeParalelogramo(simbolo, largura, altura):
    largura = int(largura)
    altura = int(altura)
    if largura == 1 and altura == 1:
        return simbolo
    deslocamentoFinal = altura - 1
    imprimeLinhaCheia(simbolo, largura)
    imprimeLinhaVazada2(simbolo, altura - 2, largura)
    print(" "*deslocamentoFinal+(simbolo * largura))

def trianguloRetanguloE(altura, simbolo, linha=1):
    altura = int(altura)
    if linha > altura:
        return
    espacos = altura - linha
    if linha == 1 or linha == altura:
        print(simbolo * linha)
    else:
        print(simbolo + ' ' * (linha - 2) + simbolo)
    trianguloRetanguloE(altura, simbolo, linha + 1)

def trianguloequilatero(altura, simbolo, linha=1):
    altura = int(altura)
    if linha > altura:
        return
    espacos = altura - linha
    if linha == 1 or linha == altura:
        print(' ' * espacos + simbolo * (2 * linha - 1))
    else:
        print(' ' * espacos + simbolo + ' ' * (2 * linha - 3) + simbolo)
    trianguloequilatero(altura, simbolo, linha + 1)


def trianguloRetanguloD(altura, simbolo, linha=1):
    altura = int(altura)
    espaco = altura - linha
    asteriscos = (linha-2)
    if linha > altura:
        return
    elif linha == 1:
        print(f"{espaco*' '}{simbolo}")
    elif linha == altura:
        print(simbolo * linha)
        return
    else:
        print(F"{' '* espaco}{simbolo}{' '* asteriscos}{simbolo}")
    trianguloRetanguloD(altura, simbolo, linha + 1)


def main():
    forma = input("Digite uma forma: ")
    if forma != "TE" and forma != "TRE" and forma != "TRD":
        lar = input("Digite a largura: ")
        alt = input("Digite a altura: ")
    else:
        lar = 0
        alt = input()
    sim = input("Digite o simbolo:")

    if verificarForma(forma) == False:
        print("Objeto invalido. escolha uma dessas 5 formas:R/P/TE/TRD/TRE")
    elif verificaMedida(alt, lar) == False:
        print("Medida invalida.")
    else:
        if forma == "R":
            imprimeRetangulo(sim, lar, alt)
        if forma == "P":
            imprimeParalelogramo(sim, lar, alt)
        if forma == "TE":
            trianguloequilatero(alt, sim)
        if forma == "TRE":
            trianguloRetanguloE(alt, sim)
        if forma ==  "TRD":
            trianguloRetanguloD(alt, sim)

main()

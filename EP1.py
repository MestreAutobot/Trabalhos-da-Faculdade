from os import system, name

def limparTela():
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



def telaAbertura():
    """
    função responsavel pela tela de abertura do programa, que só vai ser realmente iniciado quando for precionado uma tecla
    
    parâmetros:
            não existe valor de parâmetros
    retorno:
         a função não retorna nada

    """
    
    print("Seja bem-vindo a Pizzaria_Meow ᓚᘏᗢ")
    input("Precione uma tecla para continuar...")



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



def informaçõesInternas(qtmeow, qtlasa, qtMini,qt20 = 1, qt10=1, qt5=1, qt2=1, qt1=1, qtmeio=1, faturamento=0):
    """
    função responsável por imprimir o estoque de alimentos, notas/moedas e o faturamento da maquina

    parâmetros:
            qtmeow: estoque do produto "Meow_Italiana"
            qtlasa: estoque do produto "Lasagna_Garfield"
            qtMini: estoque do produto "MiniPizza_Cat"
            qt20: estoque de notas de  "R$20,00"
            qt10: estoque de notas de  "R$10,00"
            qt5: estoque de notas de  "R$05,00"
            qt2: estoque de notas de  "R$02,00"
            qt1: estoque de moedas de  "R$01,00"
            qtmeio: estoque de moedas de  "R$00,50"
            faturamento: valor do faturamento
    retorno:
        a função não retorna nada

    """
    
    print("+"+"-"*49+"+")
    print("|"+" "*15+"informações_Internas"+" "*14+"|")
    print("+"+"-"*49+"+")
    print("|","Meow_Italiana",f":    {qtmeow} un"," "*24+"|")
    print("|","Lasagna_Garfield",f": {qtlasa} un"," "*24+"|")
    print("|","MiniPizza_Cat",f":    {qtMini} un"," "*24+"|")
    print("+"+"-"*49+"+")
    print("|","Notas_de_R$20,00",f" : {qt20}"," "*26+"|")
    print("|","Notas_de_R$10,00",f" : {qt10}"," "*26+"|")
    print("|","Notas_de_R$05,00",f" : {qt5}"," "*26+"|")
    print("|","Notas_de_R$02,00",f" : {qt2}"," "*26+"|")
    print("|","Moedas_de_R$01,00",f": {qt1}"," "*26+"|")
    print("|","Moedas_de_R$00,50",f": {qtmeio}"," "*26+"|")
    print("+"+"-"*49+"+")
    print("|","faturamento",f": {faturamento:.2f}"," "*29+"|")
    print("+"+"-"*49+"+")



def adicionarRetirar(op,Me,La,Mi):
    """
    função responsavel por descontar uma unidade do alimento escolhido pelo usuário, e retorna o valor atualizado para a maquina  

    parâmetros:
            op: produto escolhido pelo usuário
            Me: estoque do produto "Meow_Italiana"
            La: estoque do produto "Lasagna_Garfield"
            Mi: estoque do produto "MiniPizza_Cat"

    retorno:    
        retorna (Me, La, Mi) diminuindo em -1 uma das três variaveis dependendo da escolha do produto que o usuário escolheu
    """ 
    if op == 1:
        return Me -1, La, Mi
    elif op == 2:
        return Me , La-1, Mi
    elif op == 3:
        return Me , La, Mi-1



def foto():
    """
    função imprimi o criador da Pizzaria_Meow
    
    parâmetros:
        a função não tem parâmetros
    retorno:
        a função não retorna nada
    """
    print("+"+"-"*69+"+")
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
    print("+"+"-"*69+"+")
    print("|"+" "*24+"<%) Chefe_Meowson <%)"+" "*24+"|")
    print("+"+"-"*69+"+")



def adcionar_credito(op,x=0,dindin=0,qt20 = 1, qt10=1, qt5=1, qt2=1, qt1=1, qtmeio=1):
    """
    função responsável por calcular o troco, e adicionar as notas/moedas inseridas pelo usuário na maquina de vendas  


    parâmetros:
        op:  produto escolhido pelo usuário
        x: preço do produto escolhido pelo usuário
        dindin: contadora de notas/moedas inserida pelo usuário
        qt20: estoque de notas de "R$20,00"
        qt10: estoque de notas de "R$10,00"
        qt5: estoque de notas de  "R$05,00"
        qt2: estoque de notas de  "R$02,00"
        qt1: estoque de moedas de "R$01,00"
        qtmeio: estoque de moedas de "R$00,50"
        
    retorno:
        a função retorna  várias informações atualizadas,  incluindo o troco (dindin-x), o valor que atualiza 
        o faturamento (x) e as quantidades atualizadas de cada nota/moeda além do valor somado inserido pelo usuário.
        
    """    
    if op ==1:
        x = 3.00
    elif op ==2:
        x = 2.50
    elif op ==3:
        x = 4.50
    else:
        print("error")
    if dindin >= x:
        return dindin-x, x, qt20, qt10, qt5, qt2, qt1, qtmeio,dindin
    else:
        valorInserido = leValor(float,"insira o dinheiro na maquina:R$ ","error valor não identificado")
        if valorInserido != 20 and valorInserido != 10 and valorInserido != 5 and valorInserido != 2 and valorInserido != 1 and valorInserido != 0.5:
            print("nota não identificada")
            return adcionar_credito(op,x,dindin,qt20, qt10, qt5, qt2, qt1, qtmeio)
        else:
            if valorInserido == 20:
                qt20+=1
            elif valorInserido == 10:
                qt10+=1
            elif valorInserido == 5:
                qt5+=1
            elif valorInserido == 2:
                qt2+=1
            elif valorInserido == 1:
                qt1+=1
            elif valorInserido == 0.5:
                qtmeio+=1
            valorDepositado = dindin+valorInserido
            return adcionar_credito(op,x,valorDepositado,qt20, qt10, qt5, qt2, qt1, qtmeio)



def Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio):
    """
    função responsável por calcular o troco, atualizar as quantidades de notas/moedas disponíveis no estoque e imprimir o troco nota por nota


    parâmetros:
        troco: O valor do troco a ser calculado
        quantidade20: estoque de notas de "R$20,00"  
        quantidade10: estoque de notas de "R$10,00" 
        quantidade5:  estoque de notas de "R$05,00"  
        quantidade2:  estoque de notas de "R$02,00" 
        quantidade1:  estoque de notas de "R$01,00"
        quantidademeio:estoque de notas de "R$00,50"
        
    retorno:
        A função retorna uma tupla contendo o troco restante e as quantidades atualizadas de notas/moedas disponíveis no estoque. No primeiro caso 
        se todas as quantidades de notas/moedas disponíveis no estoque forem iguais a zero, significa que não há mais notas/moedas para dar como troco. 
        com isso, a função retorna o troco restante e as quantidades de notas/moedas inalteradas. O segundo caso se o troco for igual a zero, significa 
        que o troco foi dado por completo e não tem mais notas/moedas para dar. Nesse caso, a função retorna o troco restante e as quantidades de notas/moedas atualizadas.
        O resto são as recursões para que o troco chegue a zero, e se nenhuma das condições anteriores for atendida, significa que não há notas/moedas disponíveis para dar 
        o troco restante. Nesse caso, a função retorna o troco restante e as quantidades de notas/moedas inalteradas, ou atualizadas dependendo se o cliente vai optar por pegar o produto ou não.
    """
    
    
    if quantidade20 == 0 and quantidade10 == 0 and quantidade5 == 0 and quantidade2 == 0 and quantidade1 == 0 and quantidademeio == 0:
        return troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio
    
    if troco == 0:
        return troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio
    
    if troco >= 20 and quantidade20 > 0:
        print("R$ 20.00")
        return Calculartroco(troco - 20, quantidade20 - 1, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
    
    if troco >= 10 and quantidade10 > 0:
        print("R$ 10.00")
        return Calculartroco(troco - 10, quantidade20, quantidade10 - 1, quantidade5, quantidade2, quantidade1, quantidademeio)
    
    if troco >= 5 and quantidade5 > 0:
        print("R$ 05.00")
        return Calculartroco(troco - 5, quantidade20, quantidade10, quantidade5 - 1, quantidade2, quantidade1, quantidademeio)
    
    if troco >= 2 and quantidade2 > 0:
        print("R$ 02.00")
        return Calculartroco(troco - 2, quantidade20, quantidade10, quantidade5, quantidade2 - 1, quantidade1, quantidademeio)
    
    if troco >= 1 and quantidade1 > 0:
        print("R$ 01.00")
        return Calculartroco(troco - 1, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1 - 1, quantidademeio)
    
    if troco >= 0.5 and quantidademeio > 0:
        print("R$ 00.50")
        return Calculartroco(troco - 0.5, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio - 1)
    
    return troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio

def Calculartroco2(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio):
    """
    função responsável por calcular o troco e atualizar as quantidades de notas/moedas disponíveis no estoque


    parâmetros:
        troco: O valor do troco a ser calculado
        quantidade20: estoque de notas de "R$20,00"  
        quantidade10: estoque de notas de "R$10,00" 
        quantidade5:  estoque de notas de "R$05,00"  
        quantidade2:  estoque de notas de "R$02,00" 
        quantidade1:  estoque de notas de "R$01,00"
        quantidademeio:estoque de notas de "R$00,50"
        
    retorno:
        A função retorna uma tupla contendo o troco restante e as quantidades atualizadas de notas/moedas disponíveis no estoque. No primeiro caso 
        se todas as quantidades de notas/moedas disponíveis no estoque forem iguais a zero, significa que não há mais notas/moedas para dar como troco. 
        com isso, a função retorna o troco restante e as quantidades de notas/moedas inalteradas. O segundo caso se o troco for igual a zero, significa 
        que o troco foi dado por completo e não tem mais notas/moedas para dar. Nesse caso, a função retorna o troco restante e as quantidades de notas/moedas atualizadas.
        O resto são as recursões para que o troco chegue a zero, e se nenhuma das condições anteriores for atendida, significa que não há notas/moedas disponíveis para dar 
        o troco restante. Nesse caso, a função retorna o troco restante e as quantidades de notas/moedas inalteradas, ou atualizadas dependendo se o cliente vai optar por pegar o produto ou não.
    """
    
    if quantidade20 == 0 and quantidade10 == 0 and quantidade5 == 0 and quantidade2 == 0 and quantidade1 == 0 and quantidademeio == 0:
        return troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio
    
    if troco == 0:
        return troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio
    
    if troco >= 20 and quantidade20 > 0:
        return Calculartroco2(troco - 20, quantidade20 - 1, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
    
    if troco >= 10 and quantidade10 > 0:
        return Calculartroco2(troco - 10, quantidade20, quantidade10 - 1, quantidade5, quantidade2, quantidade1, quantidademeio)
    
    if troco >= 5 and quantidade5 > 0:
        return Calculartroco2(troco - 5, quantidade20, quantidade10, quantidade5 - 1, quantidade2, quantidade1, quantidademeio)
    
    if troco >= 2 and quantidade2 > 0:
        return Calculartroco2(troco - 2, quantidade20, quantidade10, quantidade5, quantidade2 - 1, quantidade1, quantidademeio)
    
    if troco >= 1 and quantidade1 > 0:
        return Calculartroco2(troco - 1, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1 - 1, quantidademeio)
    
    if troco >= 0.5 and quantidademeio > 0:
        return Calculartroco2(troco - 0.5, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio - 1)
    
    return troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio

def poucoTroco(Meow, Lasa, Mini,opcao,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento):
    """
    função responsável por verificar se o usuário deseja completar ou não a transação.
        
    parâmetros:
        Meow: estoque do produto "Meow_Italiana"
        Lasa: estoque do produto "Lasagna_Garfield"
        Mini: estoque do produto "MiniPizza_Cat"
        opcao: produto escolhido pelo usuário
        qt20: estoque de notas de "R$20,00"     
        qt10: estoque de notas de "R$10,00"
        qt5: estoque de notas de "R$05,00"
        qt2: estoque de notas de "R$02,00" 
        qt1: estoque de notas de "R$01,00"
        qtmeio: estoque de notas de "R$00,50"
        faturamento: faturamento da maquina
    retorno:
        a função retorna True se o usuário deseja completar a transação, ou False caso o usuário desejar o dinheiro de volta, 
        Caso o usuário digite uma opção inválida, a função chama recursivamente a si mesma com os mesmos parâmetros, esperando 
        que o usuário digite uma resposta válida.  
    """
    x = input("você gostaria ainda de completar a transação?S/N:")
    if x =="S":
        return True
    elif x=="N":
        return False
    else:
        return poucoTroco(Meow, Lasa, Mini,opcao,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento)



def compra(Meow, Lasa, Mini,opcao,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento):
    """
    função responsável por realizar a compra do produto que o usuário escolheu 


    parâmetros:
        Meow: estoque do produto "Meow_Italiana"
        Lasa: estoque do produto "Lasagna_Garfield"
        Mini: estoque do produto "MiniPizza_Cat"
        opcao: produto escolhido pelo usuário
        qt20: estoque de notas de "R$20,00"     
        qt10: estoque de notas de "R$10,00"
        qt5: estoque de notas de "R$05,00"
        qt2: estoque de notas de "R$02,00" 
        qt1: estoque de notas de "R$01,00"
        qtmeio: estoque de notas de "R$00,50"
        faturamento: faturamento da maquina
        
    retorno:
        a função retorna os valores atualizados dos produtos, das notas e do faturamento para a função maquina e imprimi o troco para o cliente, caso tenha troco o suficente, caso não tenha  
        vai ser perguntado se o cliente vai querer receber o troco só que com um valor menor possivel de ser devolvido, caso ele queira a função vai retornar a maquina normalmente, 
        mas se ele não querer a copra é cancelada, e o dinheiro é retornado nota por nota 
        
    """
    print("+"+"-"*32+"+")
    print("|░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░|")
    print("|░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░|")
    print("|░░░░░░█░█░▀░░░░░▀░░▀░░░░█░█░░░░░|")
    print("|░░░░░░█░█░░░░░░░░▄▀▀▄░▀░█░█▄▀▀▄░|")
    print("|█▀▀█▄░█░█░░▀░░░░░█░░░▀▄▄█▄▀░░░█░|")
    print("|▀▄▄░▀██░█▄░▀░░░▄▄▀░░░░░░░░░░░░▀▄|")
    print("|░░▀█▄▄█░█░░░░▄░░█░░░▄█░░░▄░▄█░░█|")
    print("|░░░░░▀█░▀▄▀░░░░░█░██░▄░░▄░░▄░███|")
    print("|░░░░░▄█▄░░▀▀▀▀▀▀▀▀▄░░▀▀▀▀▀▀▀░▄▀░|")
    print("|░░░░█░░▄█▀█▀▀█▀▀▀▀▀▀█▀▀█▀█▀▀█░░░|")
    print("|░░░░▀▀▀▀░░▀▀▀░░░░░░░░▀▀▀░░▀▀░░░░|")
    print("+"+"-"*32+"+")
    if opcao == 1:
        print("|"+" "*3+"Você_escolheu_Meow_Italiana"+" "*2+"|")
        print("|   preço:R$03.00"+" "*16+"|")
    if opcao == 2:
        print("|"+" "*1+"Você_escolheu_Lasagna_Garfield"+" "*1+"|")
        print("|   preço:R$02.50"+" "*16+"|")
    if opcao == 3:
        print("|"+" "*2+"Você_escolheu_MiniPizza_Cat"+" "*3+"|")
        print("|   preço:R$04.50"+" "*16+"|")
    print("+"+"-"*32+"+")
    
    dinheiro = 0

    troco,fat,quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio,dindin=adcionar_credito(opcao,faturamento,dinheiro,qt20, qt10, qt5, qt2, qt1, qtmeio)
    print("+"+"-"*32+"+")
    print(f"|valor_pago:R${dindin:.2f}"+" "*15+"|")
    print(f"|troco:R${troco:.2f}"+" "*20+"|")
    print("+"+"-"*32+"+")
        
    tr,q20,q10,q5,q2,q1,qmeio=Calculartroco2(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
    faturamento_total=faturamento+fat
    if tr == 0:
        tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
        print("<3 obrigado pela compra ᓚᘏᗢ <3")
        Meow, Lasa, Mini=adicionarRetirar(opcao,Meow,Lasa,Mini)
        return Meow, Lasa, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
    else:
        print(f"não temos troco para {troco:.2f}")
        resultado = poucoTroco(Meow,Lasa,Mini,opcao,q20,q10,q5,q2,q1,qmeio,faturamento_total)
        if resultado and opcao==1:
            if troco == tr: 
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {troco:.2f}")
                return Meow-1, Lasa, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
            elif tr < troco:
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {tr:.2f}")
                return Meow-1, Lasa, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
            else:
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {troco- tr:.2f}")
                return Meow-1, Lasa, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
        if resultado and opcao==2:
            if troco == tr: 
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {troco:.2f}")
                return Meow, Lasa-1, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
            elif tr < troco:
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {tr:.2f}")
                return Meow, Lasa-1, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
            else:
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {troco-tr:.2f}")
                return Meow, Lasa-1, Mini, q20,q10,q5,q2,q1,qmeio,faturamento_total
        if resultado and opcao==3:
            if troco == tr: 
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {troco:.2f}")
                return Meow, Lasa, Mini-1, q20,q10,q5,q2,q1,qmeio,faturamento_total
            elif tr < troco:
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {tr:.2f}")
                return Meow, Lasa, Mini-1, q20,q10,q5,q2,q1,qmeio,faturamento_total
            else:
                tr,q20,q10,q5,q2,q1,qmeio=Calculartroco(troco, quantidade20, quantidade10, quantidade5, quantidade2, quantidade1, quantidademeio)
                print(f"ficamos te devendo {troco-tr:.2f}")
                return Meow, Lasa, Mini-1, q20,q10,q5,q2,q1,qmeio,faturamento_total
        else:
            impressao(quantidade20-qt20,quantidade10-qt10,quantidade5-qt5,quantidade2-qt2,quantidade1-qt1,quantidademeio-qtmeio)
            return Meow, Lasa, Mini,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento

def impressao(q20,q10,q5,q2,q1,qmeio):
    """
    função responsável por devolver o crédito inserido pelo usuário

    parâmetros:
        q20: estoque de notas de "R$20,00"     
        q10: estoque de notas de "R$10,00"
        q5: estoque de notas de "R$05,00"
        q2: estoque de notas de "R$02,00" 
        q1: estoque de notas de "R$01,00"
        qmeio: estoque de notas de "R$00,50"
        
    retorno:
        a função não retorna nada
        
    """
    if q20 and q10 and q5 and q2 and q1 and qmeio == 0:
        return
    if q20 >0:  
        print("R$20.00")
        impressao(q20-1,q10,q5,q2,q1,qmeio)
    elif q10 >0:
        print("R$10.00")
        impressao(q20,q10-1,q5,q2,q1,qmeio)
    elif q5 >0:
        print("R$05.00")
        impressao(q20,q10,q5-1,q2,q1,qmeio)
    elif q2 >0:
        print("R$02.00")
        impressao(q20,q10,q5,q2-1,q1,qmeio)
    elif q1 >0:
        print("R$01.00")
        impressao(q20,q10,q5,q2,q1-1,qmeio)
    elif qmeio >0:
        print("R$00.50")
        impressao(q20,q10,q5,q2,q1,qmeio-1)
        
    


def maquina(Meow = 5,Lasa = 5,Mini= 5,qt20 = 0, qt10=0, qt5=0, qt2=0, qt1=0, qtmeio=0, faturamento=0):
    """
    função responsável por imprimir o cardapio,realizar as vendas,armazenar o faturamento e controlar o estoque dos produtos e notas/moedas.

    parâmetros:
        Meow: estoque do produto "Meow_Italiana"
        Lasa: estoque do produto "Lasagna_Garfield"
        Mini: estoque do produto "MiniPizza_Cat"
        qt20: estoque de notas de "R$20,00"     
        qt10: estoque de notas de "R$10,00"
        qt5: estoque de notas de "R$05,00"
        qt2: estoque de notas de "R$02,00" 
        qt1: estoque de notas de "R$01,00"
        qtmeio: estoque de notas de "R$00,50"
        faturamento: faturamento da maquina
        
    retorno:
        a função não retorna nada
    """
    
    limparTela()
    print("+"+"-"*49+"+")
    print("|"+" "*18+"Pizzaria_Meow"+" "*18+"|")
    print("|"+" "*21+"ฅ^•ﻌ•^ฅ"+" "*21+"|")
    print("|"+" "*22+"Carta"+" "*22+"|")
    print("+"+"-"*49+"+")
    print("|"+" "*16+"Comidas_Italianas"+" "*16+"|")
    if Meow <= 0:
        print("|","1 - Meow_Italiana"+"_"*18+"Esgotado ;-;","|")
    else:
        print("|","1 - Meow_Italiana"+"_"*23+"R$03,00","|")
    if Lasa <= 0:
        print("|","2 - Lasagna_Garfield"+"_"*15+"Esgotado ;-;","|")
    else:
        print("|","2 - Lasagna_Garfield"+"_"*20+"R$02,50","|")
    if Mini <= 0:
        print("|","3 - MiniPizza_Cat"+"_"*18+"Esgotado ;-;","|")
    else:
        print("|","3 - MiniPizza_Cat"+"_"*23+"R$04,50","|")
    print("+"+"-"*49+"+")
    print("|"+" "*18+"Outras_Opções"+" "*18+"|")
    print("|","4 - Informações_Internas"+" "*24+"|")
    print("|","5 - Imagem do Chefe"+" "*29+"|")
    print("|","6 - Finalizar"+" "*35+"|")
    print("+"+"-"*49+"+")
    if qt20  == 0 and qt10 == 0 and qt5 == 0 and qt2 == 0 and qt1 == 0 and qtmeio == 0:
        print("|"+" "*10+"ATENÇÃO: MAQUINA_SEM_TROCO!!!"+" "*10+"|")
        print("+"+"-"*49+"+")
    opcao = leValor(int,"digite uma opção: ","A opção deve ser um inteiro")
    limparTela()  # Limpar o terminal antes de processar a opção selecionada
    
    if opcao == 1:
        if Meow <= 0:
            print("esgotado")
        else:
           Meow, Lasa, Mini,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento = compra(Meow, Lasa, Mini,opcao,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento)
           
    elif opcao == 2:
        if Lasa <= 0:
            print("esgotado")
        else:
            Meow, Lasa, Mini,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento = compra(Meow, Lasa, Mini,opcao,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento)
            
    elif opcao == 3:
        if Mini <= 0:
            print("esgotado")
        else:
            Meow, Lasa, Mini,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento = compra(Meow, Lasa, Mini,opcao,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento)
            
    elif opcao == 4:
        limparTela()
        informaçõesInternas(Meow, Lasa, Mini,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento)
    elif opcao == 5:
        limparTela()
        foto()
    elif opcao == 6:
        print("Volte sempre :3!!!")
        exit()
    else:
        print("Opção inválida!")
    input("--> Enter para continuar...")
    maquina(Meow, Lasa, Mini,qt20, qt10, qt5, qt2, qt1, qtmeio, faturamento)

def main():
    """
    função responsável por iniciar o programa
    parâmetros:
        não tem parâmetros
    retorno:
        não retorna nada
    """
    
    limparTela()
    telaAbertura()
    limparTela()
    maquina()
main()

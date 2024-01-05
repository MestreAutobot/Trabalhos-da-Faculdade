flag = True
peso = float(input())
idade = int(input())
if idade == 16 or idade == 17:
    documento = input()
boasaude = input()
drogas = input()
primeiradoacao = input()
if primeiradoacao == "N":
    tempodaultimadoacao = int(input())
    ultimo12meses = int(input())
sexo = input()
if sexo == "F":
    gravidez = input()
    amamentando = input()
    if amamentando == "S":
        idadebebe = int(input())
print(f"Peso: {peso}")
print(f"Idade: {idade}")
if idade == 16 or idade == 17:
    print(f"Documento de autorizacao: {documento}")
print(f"Boa saude: {boasaude}")
print(f"Uso de drogas injetaveis: {drogas}")
print(f"Primeira doacao: {primeiradoacao}")
if primeiradoacao == "N":
    print(f"Meses desde ultima doacao: {tempodaultimadoacao}")
    print(f"Doacoes nos ultimos 12 meses: {ultimo12meses}")
print(f"Sexo biologico: {sexo}")
if sexo == "F":
    print(f"Gravidez: {gravidez}")
    print(f"Amamentando: {amamentando}")
    if amamentando == "S":
        print(f"Meses bebe: {idadebebe}")

if peso < 50.0:
    print("Impedimento: abaixo do peso minimo.")
    flag = False
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    flag = False
if idade == 16 or idade == 17:
    if documento == "N":
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
        flag = False
if idade > 60 and primeiradoacao == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    flag = False
if idade > 69:
    print("Impedimento: maior de 69 anos.")
    flag = False
if boasaude == "N":
    print("Impedimento: nao esta em boa saude.")
    flag = False
if drogas == "S":
    print("Impedimento: uso de drogas injetaveis.")
    flag = False
if sexo == "M" and primeiradoacao == "N":   
    if tempodaultimadoacao < 2: 
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        flag = False
    if ultimo12meses >= 4:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        flag = False
if sexo == "F" and primeiradoacao == "N":
    if tempodaultimadoacao < 3:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        flag = False
    if ultimo12meses >= 3:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")    
        flag = False
if sexo == "F": 
    if gravidez == "S":
        print("Impedimento: gravidez.")
        flag = False
    if amamentando == "S" and idadebebe < 12:
        print("Impedimento: amamentacao.")
        flag = False
if flag == True:
    print("Procure um hemocentro.")
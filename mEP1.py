x = float (input ("coloque o primeiro número:"))
op = input("coloque a operação:")
y = float (input ("coloque o segundo número:"))

if op == "+":
    print(f'{x} {op} {y} =', (x+y))
elif op == "-":
    print(f'{x} {op} {y} =', (x-y))
elif op ==  "*":
    print(f'{x} {op} {y} =', (x*y))
elif op == "**":
    print(f'{x} {op} {y} =', (x**y))
elif op == "//":
    if y == 0:
        print("Divisao por 0!")
    else:
        print(f'{x} {op} {y} =', (x//y))
elif op == "%":
    if y == 0:
        print("Divisao por 0!")
    else:
        print(f'{x} {op} {y} =', (x%y))
elif op == "/":
    if y == 0:
        print("Divisao por 0!")
    else:
        print(f'{x} {op} {y} =', (x/y))
else:
    print("Operacao nao reconhecida!")

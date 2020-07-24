import operadores

print('Escolha as operações a baixo:')
print('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

escolha = int(input("Digite sua escolha: "))

if (escolha == 1):
    print('***Adição***')
    operadores.adicao()
elif (escolha == 2):
    print('***Subtração***')
    operadores.subtracao()
elif (escolha == 3):
    print('***Multiplicação***')
    operadores.subtracao()
elif (escolha == 4):
    print('***Divisão***')
    operadores.divisao()
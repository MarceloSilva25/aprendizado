# EXERCÍCIO 2
numero_1 = input("digite um número inteiro: ")

if numero_1.isdigit():
    entrada = int(numero_1)
    par_impar = entrada % 2 == 0 
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f"o número {entrada} é {par_impar_texto}")

else:
    print("você não digitou um número")
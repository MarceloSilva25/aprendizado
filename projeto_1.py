#EXERCÍCIO 1 : Codigo feito para testar operadores aprendidos. 

nome = input("Digite seu nome: ")
idade = input("digie sua idade: ")
if nome and idade: 
    print(f"Seu nome é: {nome}" )
   
    print(f"Seu nome invertido é: {nome [:: -1]}")
   
    print(f"seu nome contém {len (nome)} letras")

    if  ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    print(f"A primeira letra do seu nome é: {nome [0]}")
   
    print(f"a ultima letra do seu nome é: {nome [-1]}")
else: 
    print("Desculpe, vc deixou campos em branco")
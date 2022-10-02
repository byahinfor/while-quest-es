from ast import While


qnt = 0 
homem = 0
mulher = 0 


nome = input ("  digite seu nome:  ")
print("  =  " * 73)
print("  enquanto  o sexo feminino for digitado ele se repetirá  ")
sexo = input("  digite seu sexo (M - F):  ").upper( )
print("  =  " * 73)


if sexo == ("  M  "):
 homem = homem + 1 
else:
    mulher = mulher + 1


while sexo !=  ("  M  "):
     qnt = qnt + 1
nome =  input("  digite outro nome:  ")
print ("  =  " * 73)
print (" cenquanto o sexo masculino for digitado ele se repetirá  ")
sexo = input("  digite outro sexo (M - F):  ").upper( )
print ("  =  " * 73)


if sexo == ("  M  "):
    homem = homem + 1 
else: 
    mulher = mulher + 1 


print(f"  quantas vezes o codigo foi executado é:  {qnt}")
print(f"  quantas vezes o usuário colocou o sexo masculino é: {homem}")
print(f"  quantas vezes o usuário colocou  o sexo feminino é: {mulher}")

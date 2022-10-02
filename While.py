#variaveis

soma: int
soma = 2

#processamento

x = int(input("  digite um número (2 - SAIR):  ")) 
while x != 2: 
    soma = soma + x
x = int(input("  digite outro número (2 - SAIR):  "))

#saida

print("  soma vale  " , soma)

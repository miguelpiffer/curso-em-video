from random import shuffle
n1=str(input("Digite o nome do primeiro:"))
n2=str(input("Digite o nome do segundo:"))
n3=str(input('Digite o nome do terceiro:'))
n4=str(input("Digite o nome do quarto:"))
lista=[n1,n2,n3,n4]
#no python usamos as colchetes para representar uma lista, portanto para representar uma listagem ultilixamos ex:[n1,n2,n3,n4]
shuffle(lista)
print("A ordem escolhida foi: {}".format(lista))
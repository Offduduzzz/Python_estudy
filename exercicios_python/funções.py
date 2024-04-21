from random import randint

print('Introdução a função em python')

lista_nomes = ['Dudu', 'Maria', 'Patricia', 'Louyse']

def exibir():
    for x in lista_nomes:
        print(x)

def escolha_num():
    print(randint(0, 50))



exibir()
escolha_num()
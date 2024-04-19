"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    opcao = input('[i]nserir, [a]pagar e [l]istar: ').lower()
    if opcao == 'i':
        inserir = input('Digite o que deseja inserir na lista: ').lower()
        lista.append(inserir)
        indice = 0
        for elementos in lista:
            print(indice, elementos)
            indice += 1
    elif opcao == 'a':
        indice = 0
        for elementos in lista:
            print(indice, elementos)
            indice += 1
        remover = input('Digite o nome do elemento que deseje apagar: ')
        remover_str = ''
        try:
            remover_str = str(remover)
            if remover_str in lista:
                lista.remove(remover_str)
                print(f'Parabéns, você removeu o elemento: "{remover_str}" da sua lista.')
            else:
                print('Esse elemento não está na lista.')
        except ValueError:
            print('Você não digitou o nome do elemento.')

    elif opcao == 'l':
        print('Essa é sua lista de elementos: ')
        print('-='*30)
        indice = 0
        for elementos in lista:
            print(indice, elementos)
            indice += 1
    else:
        print('Você não digitou nenhuma das opções.')
        continue

lista = []
#   1 - loop infinito
while True: 
    print('Selecione uma opção: ')
    print('[i]nserir  [a]pagar [l]ista ')
    opcao = input('--> ')

    if opcao == 'i':
        print('i')
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        print('l')
    else:
        print('Digite [i], [a] ou [l].')
print('Exiba os índices da lista.')

lista = []

indice = -1

while True:
    nomes = input('Digite nome de cada vez para adicionar na lista: [PARA PARAR DIGITE: SAIR]').lower()
    if 'sair' in nomes:
        lista.append(nomes)
        break
    else:
        continue

lista = [nomes]

for nome in lista:
    indice += 1
    print(f'{indice}', end=' ')
    print(f'{nome}')
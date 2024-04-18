print('Analisando')

dado = input('Digite algo: ')

print(f'Tipo primitivo: {type(dado)}')
print(f'Tamanho: {len(dado)}') #fatiamento
print(f'Tem espaço? {dado.isspace()}')
print(f'É um número: {dado.isnumeric()}')
print(f'Está em maiúsculo: {dado.isupper()}')
print(f'Está em minúsculo: {dado.islower()}')

#.isnumeric()
#.isalpha()
#.islower()
#.isupper()
#.isspace()
#.isalnum()
#.istitle() 
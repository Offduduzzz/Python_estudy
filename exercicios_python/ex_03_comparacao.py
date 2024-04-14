print('Comparação de números.')
print('-'*40)
#   variable
valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')
print('='*40)
#   comparation
if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}.')
elif valor2 > valor1:
    print(f'{valor2} é maior que {valor1}.')
else:
    print(f'{valor1} é igual a {valor2}.')
print('-'*40)
#   end
print('FIM DO PROGRAMA')
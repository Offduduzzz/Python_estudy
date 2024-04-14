#   start of code 
print('Calculo do IMC')
print('-='*30)
#   variable
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = ( peso / altura ** 2 )
#   show
print(f'O seu IMC é: {imc:.2f}.')
# end
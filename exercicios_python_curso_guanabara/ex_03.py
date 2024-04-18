print('Somando dois números.')

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
try:
    num1_int = int(num1)
    num2_int = int(num2)

    soma = num1_int + num2_int

    print(f'A soma de {num1_int} + {num2_int} é {soma}.')

except ValueError:
    print('Você não digitou um número.')
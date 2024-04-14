#   input -> número
#   informe se o número é par ou ímpar
#   caso o usuário não digite um número inteiro -> denuncie a situação para o usuário

num = input('Digite um número inteiro: ')
#   checagem de variável
try:
    inteiro = int(num)
    # analisando o número digitado pelo o usuário
    if inteiro % 2 == 0:
        print(f'O número {inteiro} é par.')
    else:
        print(f'O número {inteiro} é ímpar.')
except ValueError:
    print('O valor digitado não é um inteiro.')

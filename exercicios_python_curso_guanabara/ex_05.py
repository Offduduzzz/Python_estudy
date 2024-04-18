print('Sucessor e Antecessor')

while True:
    num = input('Digite um número: ')

    try:
        num_int = int(num)

        s =  num_int + 1
        a =  num_int - 1

        print(f'O sucessor de {num_int} é {s}, enquanto o antecessor de {num_int} é {a}.')
        break
    except ValueError:
        print('Você não digitou um número.')
        continue
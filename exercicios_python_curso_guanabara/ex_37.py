print('Converção de números para binário, hexadecimal e binário.')
while True:
    num_usuario = input('Informe o número desejado: ')
    try:
        int_num_usuario = int(num_usuario)
        print('[1] binário \n[2] octal \n[3] hexadecimal')
        escolha_usuario  = input('Qual a conversão desejada: ')
        try:
            int_escolha_usuario = int(escolha_usuario)
            if int_escolha_usuario == 1:
                    num_binario = bin(int_num_usuario)
                    print(num_binario)
                    break
            elif int_escolha_usuario == 2:
                    num_octal = oct(int_num_usuario)
                    print(num_octal)
                    break
            elif int_escolha_usuario == 3:
                    num_hexadecimal = hex(int_num_usuario)
                    print(num_hexadecimal)
                    break
            else:
                    print('Não é pra chegar aqui.')
        except ValueError:
            print('Essa informação não pode ser aceita.')
    except ValueError:
        print('Essa informação não pode ser aceita.')
print('FIM')
#   input -> nome do usuário
#   4 letras ou menos -> print -> nome curto
#   entre 5 e 6 letras -> print -> nome normal
#   mais que 6 letras  -> print -> nome grande

nome_do_usuario = input('Digite seu nome: ')

#   checagem se a informação inserida é uma string
try: 
    #   validação se é uma string
    str_nome_do_usuario = str(nome_do_usuario)
    #   quantidade de letras 
    quantidade_de_letras = len(str_nome_do_usuario)
    #   classificação de acordo com a quantidade de letras
    if quantidade_de_letras <= 4:
        print('Seu nome é curto.')
    elif quantidade_de_letras >= 5 and quantidade_de_letras <= 6:
        print('Seu nome é normal.')
    elif quantidade_de_letras > 6:
        print('Seu nome é grande')
except ValueError:
    print('Você não digitou um nome.')

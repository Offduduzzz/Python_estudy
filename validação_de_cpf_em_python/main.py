'''Anotações
        0 1 2 3 4 5 6 7 8 9 10
        1 1 1 4 4 4 7 7 7 3 5
      -11 10 9 8 7 6 5 4 3 2 1
      '''


print('Validação de CPF')

cpf = []
cpf_copia = cpf.copy()

#   loop infinito
while True:
    cpf = input('Digite seus primeiros 9 digitos do CPF (EX.: 111444777) : ')
    cpf_int = 0
    #   checagem do número degitado
    try:
        cpf_int = int(cpf)
        list.cpf = cpf_int
        #   amostrar do dígitos do cpf e seus respectivos indices
        for i in cpf_int:
            print(f'{i}')
        #   ato da validação

        print(cpf[0]*2)
        print(cpf[1]*3)
        print(cpf[2]*4)
        print(cpf[3]*5)
        print(cpf[4]*6)
        print(cpf[5]*7)
        print(cpf[6]*8)
        print(cpf[7]*9)
        print(cpf[8]*10)


    except ValueError:
        print('Você não digitou um CPF. Digite novamente!')


print('Empréstimo bancário')

while True:
    valor_casa = input('Qual é o valor da casa? ')
    salario_comprador = input('Qual é seu salário? ')
    ano_pagamento = input('Em quantos anos deseja pagar? ')
    try:
        int_valor_casa = float(valor_casa)
        int_salario_comprador = float(salario_comprador)
        int_ano_pagamento = int(ano_pagamento)

        #   valor da casa / ano de pagamento

        meses_pagamento = int_ano_pagamento * 12

        prestacao = int_valor_casa / meses_pagamento

        salario_comprador_porcentagem = int_salario_comprador * 30 / 100

        if prestacao > salario_comprador_porcentagem:
            print('Empréstimo negado!')
            break
        else:
            print('Empréstimo concedido.')
            break
    except ValueError:
        print('Essa informação não pode ser aceita.')
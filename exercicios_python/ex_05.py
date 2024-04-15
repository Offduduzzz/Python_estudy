#   input -> horário
#   bom dia -> 0 - 11
#   boa tarde -> 12 - 17
#   boa noite -> 18 - 23

horario = input('Digite horário de agora: ')

#   checagem
try:
    horario_float = float(horario)
    #   saudação conforme o horário informado pelo usuário
    if horario_float >= 0 and horario_float <= 11:
        print('Bom Dia!!')
    elif horario_float >= 12 and horario_float <= 17:
        print('Boa Tarde!!')
    elif horario_float >= 18 and horario_float <= 23:
        print('Boa Noite!!')
except ValueError:
    print('O que você digitou não é um horário.')
'''Anotações
        0 1 2 3 4 5 6 7 8 9 10
        1 1 1 4 4 4 7 7 7 3 5
      -11 10 9 8 7 6 5 4 3 2 1
      '''
#    cpf: 54565323010
#    Primeiro digito
cpf_usuario = input('Digite o CPF: ')
nove_digitos_1 = cpf_usuario[:9]

contador_regresivo_1 = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos_1:
    resultado_digito_1 += int(digito_1) * contador_regresivo_1
    contador_regresivo_1 -= 1
digito_1 = resultado_digito_1 % 11
if digito_1 < 2:
    digito_1 = 0
else:
    digito_1 = (11 - digito_1)

#    Segundo digito

dez_digitos_2 = cpf_usuario[:10]

contador_regresivo_2 = 11
resultado_digito_2 = 0

for digito_2 in dez_digitos_2:
    resultado_digito_2 += int(digito_2) * contador_regresivo_2
    contador_regresivo_2 -= 1
digito_2 = resultado_digito_2 % 11
if digito_2 < 2:
    digito_2 = 0
else:
    digito_2 = (11 - digito_2)

cpf_gerado_pelo_calculo = f'{nove_digitos_1}{digito_1}{digito_2}'

if cpf_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_usuario} é válido')
else:
    print('CPF inválido')

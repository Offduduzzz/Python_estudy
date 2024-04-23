from random import randint

print('Acerte o número da maquina [Para sair digite "EXIT"].')
print('O número está entre 0 e 100.')

#   Número da máquina
num_maquina = randint(0, 100)

#   tentativas do usuário
tentativas_usuario = 0

while True:
    num_usuario = input('Digite um número: ').lower()
    tentativas_usuario += 1
    #   analisando os números
    if num_usuario == num_maquina:
        print('PARABÉNS!! Você acertou.')
        print(f'Até acerta você errou {tentativas_usuario} vezes.')
    elif num_usuario == 'exit':
        print(f'Você desistiu após tentar {tentativas_usuario} vezes.')
        print('Programa finalizado.')
        break
    else:
        print('Não foi dessa vez, tente novamente.')
        print(f'Essa já é sua {tentativas_usuario} tentativa.')



print('PALAVRA SECRETA')

print('Tente acertar a palavra secreta.')

#   variáveis
palavra_secreta = 'python'
palavras_acertadas = ''
tentativas = 0

#   lógica do jogo
while True:
    usuario_letra  = input('Digite uma letra: ')
    tentativas += 1

    if len(usuario_letra) > 1:
        print('Digite apenas uma letra.')
        continue
        
    if usuario_letra in palavra_secreta:
        palavras_acertadas += usuario_letra
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!!')
        print(f'A palavra secreta era {palavra_secreta}.')
        print(f'Total de tentativas: {tentativas}.')
        palavras_acertadas = ''
        tentativas = 0


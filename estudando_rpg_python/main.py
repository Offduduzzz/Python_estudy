from random import randint

lista_npcs = []

def criar_npc():
    
    level_monstro = randint(0, 100)
    
    novo_npc = {
        'name': f'monstro {level_monstro}',
        'level': level_monstro,
        'dano': 5 * level_monstro,
        'hp': 100 * level_monstro,
    }

    return novo_npc

def exibir_npcs():
    for npc in lista_npcs:
        print(f'Nome: {npc['name']} // Level: {npc['level']} // Dano {npc['dano']} // Hp: {npc['hp']}')


def gerar_npcs(n_npcs):

    for x in range(n_npcs):
        novo_npc = criar_npc()
        lista_npcs.append(novo_npc)

gerar_npcs(5)
exibir_npcs()

#   Criando players


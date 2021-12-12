# imports
from datetime import datetime
import random


# retorna o horário defino no sistema do usuário
def retorna_hora():
    hora = datetime.now()
    hora_format = hora.strftime('%H:%M')
    return hora_format


horario = retorna_hora()


# retorna a saldação de acordo com o horário definido do usuário
def retorna_saldacao():
    if horario < '12':
        return 'Bom dia'
    elif horario < '18':
        return 'Boa Tarde'
    else:
        return 'Boa noite'


saldacao = retorna_saldacao()


# Abertura do jogo
def abertura():
    print('-' * 25)
    print('{} - {}\nBem-vindo ao jogo Jokenpô!'.format(saldacao, horario))
    print('-' * 25)


abertura()


# Randomiza os números que representam papel, pedra e tesoura
def randomiza_num():
    num_random = random.randint(1, 3)
    return num_random


numero = randomiza_num()


# Pede para o usuario um chute
def pede_chute():
    print('(1)Papel (2)Pedra (3)Tesoura')
    chute = int(input('Insira um número: '))
    if chute < 1 or chute > 3:
        print('Por favor insira corretamente!')
    return chute


chute_usuario = pede_chute()


# Retorna a escolha do usuário e pc
def retorna_escolha(a, b):
    lista = ['papel', 'pedra', 'tesoura']
    usuario, pc = lista[a - 1], lista[b - 1]
    print('Jogador: {} | PC: {}'.format(usuario, pc))


# definições gerais do jogo
ganha1 = chute_usuario == 1 and numero == 2
ganha2 = chute_usuario == 2 and numero == 3
empate = chute_usuario == numero


# Define ganhador/perdedor
def retorna_ganhador():
    if ganha1 or ganha2:
        retorna_escolha(chute_usuario, numero)
        print('Você ganhou!')
    elif empate:
        retorna_escolha(chute_usuario, numero)
        print('Empate')
    else:
        retorna_escolha(chute_usuario, numero)
        print('você perdeu!')


retorna_ganhador()

# ----------------------------------------- #

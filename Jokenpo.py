# Jogo de Jokenpo - PEDRA PAPEL TESOURA #

from random import randint    # para escolher um int aleatório dentro da lista #

def jokenpo():
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)              #
    print('Vamos jogar Jokenpo?! Vamos!')
    print('''Escolha uma opção:\n
    [ 0 ] - Pedra
    [ 1 ] - Papel 
    [ 2 ] - Tesoura\n''')
    jogador = int(input('Qual a sua jogada? '))
    print('*' * 30)
    print('O Computador escolheu {}'.format(itens[computador]))
    print('O Player 1 escolheu {}'.format(itens[jogador]))
    if computador == 0:                     # COMPUTADOR JOGOU PEDRA
        if jogador == 0:                    # PEDRA
            print('Empatou!')
        elif jogador == 1:                  # PAPEL
            print('Jogador venceu!')
        elif jogador == 2:                  # TESOURA
            print('Vc Perdeu!')

    elif computador == 1:                   # COMPUTADOR JOGOU PAPEL
        if jogador == 0:                    # PEDRA
            print('Computador venceu!')
        elif jogador == 1:                  # PAPEL
            print('Empatou!')
        elif jogador == 2:                  # TESOURA
            print('Jogador Venceu!')
            
    elif computador == 2:                   # COMPUTADOR JOGOU TESOURA
        if jogador == 0:                    # PEDRA
            print('Jogador Venceu!')
        elif jogador == 1:                  # PAPEL
            print('Computador Venceu!')
        elif jogador == 2:                  # TESOURA
            print('Empatou!')
    else:
        print('Jogada Invalida!')
    
    again()

def again():
    executar_novo = input("Quer jogar novamente: [S] Sim ou [N] Não: \n")
    if executar_novo.upper().strip()[0] == "S" or executar_novo.upper() == 'SIM':
        jokenpo()   
        # nome da função principal
    elif executar_novo.upper().strip()[0] == "N" or executar_novo.upper() == 'NÃO':
        print("Até mais tarde!!!")
    else:
        again()

jokenpo()

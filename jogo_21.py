import random
import os

def obter_score_total_jogador (nome):
    deseja_continuar = True
    total_jogador = 0
    while deseja_continuar and total_jogador < 21:
        os.system('cls')
        numero_sorteado = random.randrange(1, 10)
        total_jogador = total_jogador + numero_sorteado
        print("jogador:", nome,"\nO número sorteado foi:", numero_sorteado, "\n A sua pontuação total, por enquanto é:", total_jogador)
        if total_jogador <= 21:
            deseja_continuar = input ("Deseja sortear mais um número? s/n ") == "s"
    if total_jogador > 21:
        print("VOCÊ PERDEU, PORQUE PASSOU DE 21")
    return total_jogador

jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = input("Digite o nome do segundo jogador: ")

total_jogador1 = obter_score_total_jogador(jogador1)
total_jogador2 = obter_score_total_jogador(jogador2)

if total_jogador1 < 21 and total_jogador2 < 21:
    if total_jogador1 == total_jogador2:
        print("Como o total dos dois jogadores foi igual, então temos um empate!")
    elif total_jogador2 > total_jogador1:
        print("Jogador: ", jogador2, "Você ganhou, com o total de ", total_jogador2, "pontos!")
    else:
        print("Jogador: ", jogador1, "Você ganhou, com o total de ", total_jogador1, "pontos!")



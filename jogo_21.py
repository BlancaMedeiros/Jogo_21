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
        input("Você perdeu, pois passou de 21, aperte enter para continuar")
    return total_jogador

numero_jogadores = int(input("Quantos jogadores vão participar: "))
lista_jogadores = [] * numero_jogadores
lista_jogadores_zerado = [] * numero_jogadores

for indice_jogador in range(numero_jogadores):
    nome = input("Digite o nome do jogador:")
    lista_jogadores.append(nome)

for indice_jogador in range(numero_jogadores):
    nome_jogador = lista_jogadores[indice_jogador]
    Total_jogador = obter_score_total_jogador(nome_jogador)
    lista_jogadores_zerado.append(Total_jogador)
     


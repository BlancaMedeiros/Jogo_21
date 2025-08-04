import random
import os

jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = input("Digite o nome do segundo jogador: ")

total_jogador1 = 0 
total_jogador2 = 0 
deseja_continuar = True

while deseja_continuar and total_jogador1 < 21:
    os.system('cls')
    numero_sorteado = random.randrange(1, 10)
    total_jogador1 = total_jogador1 + numero_sorteado
    print("jogador:", jogador1,"\nO número sorteado foi:", numero_sorteado, "\n A sua pontuação total, por enquanto é:", total_jogador1)
    if total_jogador1 < 21:
        deseja_continuar = input ("Deseja sortear mais um número? s/n ") == "s"
if total_jogador1 > 21:
    print("VOCÊ PERDEU, PORQUE PASSOU DE 21")
else:
    deseja_continuar = True
    while deseja_continuar and total_jogador2 < 21:
        os.system('cls')
        numero_sorteado = random.randrange(1, 10)
        total_jogador2 = total_jogador2 + numero_sorteado
        print("jogador:", jogador2, "\nO número sorteado foi:", numero_sorteado, "\n A sua pontuação total, por enquanto é:", total_jogador2)
        if total_jogador2 < 21:
            deseja_continuar = input ("Deseja sortear mais um número? s/n ") == "s" 
    if total_jogador2 > 21:
        print("VOCÊ PERDEU, PORQUE PASSOU DE 21")




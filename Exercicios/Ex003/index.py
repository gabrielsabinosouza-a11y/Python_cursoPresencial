import random

numero_aleatorio = random.randint(1, 10);

escolha_jogador = int(input("digite um numero de 1 a 10: "));
tentativa = 0;


while escolha_jogador != numero_aleatorio and tentativa < 5:
    tentativa += 1
    if escolha_jogador > numero_aleatorio:
        print("voce errou, o numero e menor")
    elif escolha_jogador < numero_aleatorio:
        print("voce errou, o numero e maior")
    escolha_jogador = int(input("digite um numero de 1 a 10: "))

if escolha_jogador == numero_aleatorio:
    print("voce acertou!")
else:
    print(f"voce perdeu! o numero era {numero_aleatorio}")
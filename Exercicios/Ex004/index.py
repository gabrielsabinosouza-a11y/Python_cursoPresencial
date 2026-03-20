import random
from random import randint
cores = {
    "limpa": "\033[m",
    'vermelho': "\033[31m",
    'verde': "\033[32m",
    'amarelo': "\033[33m",
    'azul': "\033[34m",
    'roxo': "\033[35m",
    'ciano': "\033[36m",
    'cinza': "\033[37m",
    'pretoebranco': '\033[7;30m'
}

estilos = {
    "negrito": "\033[1m",
    "reset": "\033[0m"
}

frase = "atividade do Lucao👍"


print(f"{estilos['negrito']}{cores['azul']}{'==='*4}{cores['cinza']}jogo de adivinhacao{cores['verde']}{'==='*4}{cores['limpa']}")
print(f"{cores['cinza']}{estilos['negrito']}{frase.center(42)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{'='*43}{cores['limpa']}")


numeroSecreto = randint(1, 100)

max_tentativas = 12  
falhas = 0

tentativa = int(input(f"{cores['cinza']}{estilos['negrito']}Digite um número entre 1 e 100: {cores['limpa']}"))


while tentativa != numeroSecreto and falhas < max_tentativas - 1:
    falhas += 1
    if tentativa > numeroSecreto:
        print(f"{cores['amarelo']}{estilos['negrito']}O número secreto é menor que {tentativa}.{cores['limpa']}")
    else:
        print(f"{cores['azul']}{estilos['negrito']}O número secreto é maior que {tentativa}.{cores['limpa']}")
    tentativa = int(input(f"{cores['cinza']}{estilos['negrito']}Tentativa {falhas + 1} de {max_tentativas}. Digite outro número: {cores['limpa']}"))

if tentativa == numeroSecreto:
    print(f"{cores['verde']}{estilos['negrito']}Parabéns! Você acertou o número secreto {numeroSecreto} em {falhas + 1} tentativas.{cores['limpa']}")
else:
    print(f"{cores['vermelho']}{estilos['negrito']}Você perdeu! O número secreto era {numeroSecreto}.{cores['limpa']}")

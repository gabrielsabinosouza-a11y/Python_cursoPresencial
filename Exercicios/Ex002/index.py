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

fundo = {
    "branco": "\033[40m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m",
    'vermelho_claro': '\033[101m',
    'verde_claro': '\033[102m',
    'amarelo_claro': '\033[103m',
    'azul_claro': '\033[104m',
    'roxo_claro': '\033[105m',
    'ciano_claro': '\033[106m',
    'cinza_claro': '\033[107m'
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}
frase = "atividade do Lucao👍"

print(f"{estilos['negrito']}{cores['azul']}{"==="*4}{cores['cinza']}jogo de adivinhacao{cores['verde']}{"==="*4}{cores['limpa']}")
print(f"{cores['cinza']}{estilos['negrito']}{frase.center(42)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*14+"="}{cores['limpa']}") 

numeroSecreto = randint(1, 50)

tentativa = int(input(f"{cores['cinza']}{estilos['negrito']}Digite um numero: "))

falhas = 0
while tentativa != numeroSecreto:
    falhas += 1
    if tentativa > numeroSecreto:
        print(f"{cores['amarelo']}{estilos['negrito']}O numero secreto e menor que {tentativa}{cores['limpa']}")
    elif tentativa < numeroSecreto:
        print(f"{cores['azul']}{estilos['negrito']}O numero secreto e maior que {tentativa}{cores['limpa']}")
    tentativa = int(input(f"{cores['cinza']}{estilos['negrito']}Digite um numero: "))

print(f"{cores['verde']}{estilos['negrito']}Parabens voce acertou o numero secreto que era {numeroSecreto}{cores['limpa']}")
    
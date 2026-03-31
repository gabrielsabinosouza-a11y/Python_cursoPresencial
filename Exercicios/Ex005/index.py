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

frase = "atividade do Gabrielcio"

print(f"{estilos['negrito']}{cores['azul']}{'==='*4}{cores['cinza']}atividade 5{cores['verde']}{'==='*5}{cores['limpa']}")
print(f"{cores['cinza']}{estilos['negrito']}{frase.center(42)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{'==='*13}{cores['limpa']}") 

nome = input(f"{estilos['negrito']}{cores['cinza']}digite seu nome: ")
print(f"seu nome é {cores['azul']}{estilos['sublinhado']}{nome}{cores['limpa']}")

idade = int(input(f"{estilos['negrito']}{cores['cinza']}qual a sua idade: "))
print(f"sua idade é {cores['verde']}{estilos['sublinhado']}{idade}{cores['limpa']}")

if idade >= 18:
    print(f"{estilos['negrito']}{cores['ciano']}você é maior de idade{cores['limpa']}")
else:
    print(f"{estilos['negrito']}{cores['amarelo']}você é menor de idade{cores['limpa']}")

def soma(num1, num2):
   adicao = (num1 + num2)
   return adicao

print(f"A soma entre 2 e 1 é {cores['amarelo']}{estilos['sublinhado']}{estilos['negrito']}{soma(2, 1)}{cores['limpa']}")

num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))

def divisao(num1, num2):
    resto = (num1 % num2)
    return resto

print(f"{estilos['negrito']}{cores['cinza']}o resto da divisao entre {cores['azul']}{num1}{cores['cinza']} e {cores['vermelho']}{num2} {cores['cinza']}é {cores['verde']}{divisao(num1, num2)}{cores['cinza']}")

def cadastrar_cliente():
    cliente = {}
    cliente['nome'] = input(f"{estilos['negrito']}{cores['cinza']}Digite o {cores['azul']}nome {cores['cinza']}do cliente: ")
    cliente['telefone'] = input(f"{estilos['negrito']}{cores['cinza']}Digite o {cores['vermelho']}telefone {cores['cinza']}do cliente: ")
    cliente['endereco'] = input(f"{estilos['negrito']}{cores['cinza']}Digite o {cores['verde']}endereço {cores['cinza']}do cliente: ")
    cliente['email'] = input(f"{estilos['negrito']}{cores['cinza']}Digite o {cores['roxo']}email {cores['cinza']}do cliente: ")
    return cliente

def mostrar_cliente(cliente):
    frase = "dados do cliente"  
    print(f"{estilos['negrito']}{cores['azul']}{'==='*6}{cores['cinza']}{cores['verde']}{'==='*6}{cores['limpa']}")
    print(f"{cores['cinza']}{estilos['negrito']}{frase.center(42)}{cores['limpa']}")
    print(f"{estilos['negrito']}{cores['vermelho']}{'==='*12}{cores['limpa']}") 
    print(f"Nome: {cores['azul']}{cliente['nome']}")
    print(f"{cores['cinza']}Telefone: {cores['vermelho']}{cliente['telefone']}")
    print(f"{cores['cinza']}Endereço: {cores['verde']}{cliente['endereco']}")
    print(f"{cores['cinza']}Email: {cores['roxo']}{cliente['email']}{cores['cinza']}")

cliente = cadastrar_cliente()
mostrar_cliente(cliente)

idade = int(input('digite sua idade: '))

if idade <= 13:
    print("voce eh uma crianca")
elif idade <= 17:
    print("voce eh um adolescente")
elif idade <= 59:
    print("voce e um adulto")
else: 
    print("voce eh idoso")
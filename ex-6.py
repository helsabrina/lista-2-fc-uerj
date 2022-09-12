
valor = list(input(str("Digite sua palavra/sequencia: ")))

len_valor = len(valor)
print(len_valor)

if(len_valor < 2):
    print(len_valor)
    while(len_valor < 2):
        print(len_valor)
        valor = list(input(str("A palavra/sequencia contém apenas um dígito, por favor, digite algo válido: ")))

def palindromo(palavra):
    reverso = palavra[::-1]

    if(palavra == reverso):
        return True
    else:
        return False

resultado = palindromo(valor)
print(resultado)


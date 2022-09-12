def palindromo(palavra):
    nova_palavra = palavra.replace(" ", "")
    lis_palavra = list(nova_palavra)
    reverso = lis_palavra[::-1]

    if(lis_palavra == reverso):
        return True
    else:
        return False
    
valor = input(str("Digite sua palavra/sequencia: ")).lower()
len_valor = len(valor)

while(len_valor < 2):
    valor = input(str("A palavra/sequencia contém apenas um dígito, por favor, digite uma frase/palavra válida: ")).lower()
    len_valor = len(valor)

resultado = palindromo(valor)
print(resultado)


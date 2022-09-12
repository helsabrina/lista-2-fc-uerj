
quantVogais = 0

frase = str(input("Digite uma frase: ")).lower()

for i in frase:
    if (i == "a"
        or i == "á"
        or i == "ã"
        or i == "â"
        or i == "à"
        or i == "e"
        or i == "é"
        or i == "ê"
        or i == "i"
        or i == "í"
        or i == "o"
        or i == "ô"
        or i == "õ"
        or i == "ó"
        or i == "u"
        or i == "ú"
        or i == "û"):

        quantVogais += 1


semEspaco = frase.replace(" ", "")
totalEspaco = len(frase) - len(semEspaco)


print("O total de vogais é:", quantVogais)
print('O total de brancos é:', totalEspaco)
print('O total do restoé:', len(semEspaco))

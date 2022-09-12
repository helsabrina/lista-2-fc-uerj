
tempC = 0
tempF = 0
somaTempC = 0
somaTempF = 0
arrF = []
maioresTempF = []

for i in range(1, 51):
    numero = str(i)
    
    tempC = float(input('Digite o ' + numero + 'º número: '))
    somaTempC += tempC
    
    tempF = tempC * 1.8 + 32
    somaTempF += tempF
    arrF.append(tempF)

mediaTempC = somaTempC / 50
mediaTempF = somaTempF / 50

for n in arrF:
    if(n > mediaTempF):
        maioresTempF.append(n)
        
print('A média das temperaturas em C é:', mediaTempC)
print('A média das temperaturas em F é:', mediaTempF)
print('Temperaturas acima da média em F são:', maioresTempF)

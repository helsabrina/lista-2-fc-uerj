
numeros = []

while(len(numeros) < 31):
    try:
        numero = int(input('Digite um número inteiro: '))
        numeros.append(numero)
    except:
        print("Erro! O número precisa ser inteiro.")


num_count = int(input("Digite o número de comparação: "))
count = 0

for i in numeros:
    if(i == num_count):
        count += 1
        
    
print(f"A quantidade de vezes que o número {num_count} aparece: {count}.")


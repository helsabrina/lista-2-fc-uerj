
vetor_orig = []

for i in range(1, 17):
        valor = (input("Digite o valor desejado: "))
        vetor_orig.append(valor)

primeiros = vetor_orig[0:8]
ultimos = vetor_orig[8:16]

novo_vetor = ultimos + primeiros

print(f"O vetor original é: {vetor_orig}")
print(f"O novo vetor é: {novo_vetor}")

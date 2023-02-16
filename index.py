# Definindo o código  hamming a ser usado
hamCode = [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]


# Calcular K1
contador = 2
k1 = hamCode[0]
while contador < len(hamCode):
    if (k1 == hamCode[contador]):
        k1 = 0
    else:
        k1 = 1
    contador += 2


# Calcular K2
contador = 2
controller = 1
k2 = hamCode[1]
while contador < len(hamCode):
    if (k2 == hamCode[contador]):
        k2 = 0
    else:
        k2 = 1
    if (controller % 2 == 0):
        contador += 1
    else:
        contador += 3
    controller += 1


# Calcular K3
contador = 4
k3 = hamCode[3]
while contador < len(hamCode):
    if (k3 == hamCode[contador]):
        k3 = 0
    else:
        k3 = 1

    if (contador == 7):
        contador += 4
    else:
        contador += 1


# Calcular K4
contador = 8
k4 = hamCode[7]
while contador < len(hamCode):
    if (k4 == hamCode[contador]):
        k4 = 0
    else:
        k4 = 1
    contador += 1


# Adicionando valores de K em um array
values = []
values.append(k4)
values.append(k3)
values.append(k2)
values.append(k1)


# Calculando erro
contador = 0
soma = []
while contador < len(values):
    if (values[contador] == 1):
         if (contador == 0):
            soma.append(8)
         elif (contador == 1):
           soma.append(4)
         elif (contador == 2):
             soma.append(2)
         elif (contador == 3):
             soma.append(1)
    contador += 1

errPosition = sum(soma)

# Resultados
print(f'K4, K3, K2, K1 = {values}')

if (errPosition != 0): 
    # A posição é contadada no array a partir de um
    print(f'O código possui erro no bit de posição: {errPosition}')
else:
    print('O código não possui erros')





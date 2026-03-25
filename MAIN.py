rango = int(input("Cuantos numeros deseas ingresar?: "))

lista_original = []
for i in range(1,rango+1):
    num = int(input(f"Ingrese el numero {i}: "))
    lista_original.append(num)

print(f"lista original: {lista_original}")
for i in range(len(lista_original)-1):
    if lista_original[i] > lista_original[i+1]:
        lista_original[i], lista_original[i+1] = lista_original[i+1], lista_original[i]
    for i2 in range(len(lista_original)-1):
        if lista_original[i2] > lista_original[i2+1]:
            lista_original[i2], lista_original[i2+1] = lista_original[i2+1], lista_original[i2]
        
print(f"lista ordenada: {lista_original}")








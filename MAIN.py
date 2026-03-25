rango = int(input("Cuantos numeros deseas ingresar?: "))

ls = []
for i in range(1,rango+1):
    num = int(input(f"Ingrese el numero {i}: "))
    ls.append(num)

print(f"lista original: {ls}")
for i in range(len(ls)-1):
    for i2 in range(len(ls)-1):
        if ls[i2] > ls[i2+1]:
            ls[i2], ls[i2+1] = ls[i2+1], ls[i2]

print(f"lista ordenada: {ls}")








# Bubble Sort en Python

# Nombre del estudiante
Jose Quintana

# Descripción
Este programa permite al usuario ingresar una cantidad de números por teclado, guardar esos números en una lista y luego ordenarlos de menor a mayor usando el algoritmo Bubble Sort.

El algoritmo Bubble Sort funciona comparando elementos adyacentes de la lista, es como comparar un elemento con el siguiente, y si el elemento de la izquierda es mayor que el de la derecha, se intercambian de posición. Este proceso se repite varias veces hasta que toda la lista queda ordenada.

## Como funciona:
1. Se pide al usuario cuántos números desea ingresar.
2. Se leen los números uno por uno y se guardan en una lista.
3. Se muestra la lista original.
4. Se recorre la lista varias veces.
5. En cada recorrido se comparan elementos vecinos.
6. Si el de la izquierda es mayor que el de la derecha, se intercambian.
7. Al final se muestra la lista ordenada

## Complejidad Computacional

*¿Cuál es la complejidad Big O de la solución?*
La complejidad temporal de esta solución es O(n²).
Tiene complejidad O(n²) porque el algoritmo utiliza dos bluces for anidados:

- El primer `for` controla la cantidad de pasadas acorde a cuantos numeros pidio el usario.
- y el segundo `for` recorre la lista comparando elementos adyacentes.

Si la lista tiene n elementos, en el peor caso se realizan muchas comparaciones repetidas entre ellos, aproximadamente del orden de n × n.

*¿tiempo de ejecución de 10 elementos vs 100 elementos?*
Si la lista tiene 10 elementos, el programa realiza pocas comparaciones y termina rápido, encambio Si la lista tiene 100 elementos, el número de comparaciones aumenta muchísimo, porque no crece de forma lineal sino cuadrática. Es decir, al aumentar la cantidad de elementos, el tiempo de ejecución crece bastante más.

## Ejemplo de ejecución

¿Cuantos numeros deseas ingresar?: 5
Ingrese el numero 1: 3
Ingrese el numero 2: 4
Ingrese el numero 3: 1
Ingrese el numero 4: 5
Ingrese el numero 5: 2

lista original: [3 ,4 ,1 ,5 ,2]
lista ordenada: [1, 2, 3, 4, 5]
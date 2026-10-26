#aprendendo quicksort com o livro "entendendo algoritmos"

import random 

def quicksort(array):
    #caso-base
    if len(array) < 2:
        return array
    #caso indução
    if len(array) == 2:
        if array[0] > array[1]:
            array = [array[1], array[0]]
        return array

    #dividir o array em dois
    #escolhe número aleatório dentro do array
    pivo = array.pop(random.choice(range(len(array))))
    #numeros menores que o pivo e numeros maiores que o pivo
    menores = []
    maiores = []
    for numero in array:
        if numero <= pivo:
            menores = menores + [numero]
        else:
            maiores = maiores + [numero]
    return quicksort(menores) + [pivo] + quicksort(maiores)


array = quicksort([5,3,1,2,4])

print(array)
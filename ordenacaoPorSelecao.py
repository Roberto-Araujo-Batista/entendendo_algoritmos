#ordenação por seleção do menor ao maior


def busca_menor(array):
    indice_menor = 0 #indice do menor número
    menor = array[indice_menor]
    
    pos = 0
    while pos < len(array):
        numero = array[pos]
        if numero < menor:
            menor = numero
            indice_menor = pos

        pos = pos +1

    return indice_menor        

def ordenacaoPorSelecao(array):
    lista_ordenada = []
    while len(array) > 0:
        indice_menor = busca_menor(array)
        lista_ordenada.append(array.pop(indice_menor))
    
    return lista_ordenada

lista = [1,5,48,6,7115,236,4]

print(ordenacaoPorSelecao(lista))

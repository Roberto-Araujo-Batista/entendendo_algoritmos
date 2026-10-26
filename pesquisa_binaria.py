#LIVRO: Entendendo algoritmos de Aditya Bhargava
#algoritmo: pesquisa binária

def pesquisa_binaria(lista, item):
    #demarcam início e fim do alcance da pesquisa
    baixo = 0
    alto  = len(lista) -1

    while baixo <= alto: #em algum momento eles serão iguais.
        meio  = (baixo + alto) //2
        chute = lista[meio]
        if chute == item:
            return item
        if chute > item: #chute alto
            alto = meio - 1
        else:   #chute baixo
            baixo = meio + 1
    return None

#para teste
minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 9))
print(pesquisa_binaria(minha_lista, 10))

lista_mil = []
numero = 1

while numero <= 1000:
    lista_mil = lista_mil + [numero]
    numero = numero + 1

print(pesquisa_binaria(lista_mil, 500))
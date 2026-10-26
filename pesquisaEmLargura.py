#pesquisa em largura utilizando grafos


grafo = {}

grafo['roberto'] = ['daniel', 'william', 'wallace']
grafo['daniel'] = ['isaac', 'galileu']
grafo['william'] = ['debora', 'margareth']
grafo['wallace'] = ['debora', 'robson']

grafo['isaac'] = []
grafo['galileu'] = []
grafo['debora'] = []
grafo['margareth'] = []
grafo['robson'] = []

#verificar se é vendedor de manga
def vendedorManga(nome):
    if nome == 'margareth':
        return True
    return False

#encontrar o vendedor de mangar
def pesquisaLargura(grafo):
    fila_pesquisa = []
    fila_pesquisa = fila_pesquisa + grafo['roberto']
    fila_pesquisa.pop(0)

    #evitar repetição:
    pessoas_verificadas = []

    while not fila_pesquisa == []:        
        pessoa = fila_pesquisa.pop(0)

        if pessoa in pessoas_verificadas:
            pass
        
        if vendedorManga(pessoa) == True:
            return pessoa

        if (vendedorManga(pessoa) == False):
            pessoas_verificadas = pessoas_verificadas + [pessoa]
            fila_pesquisa = fila_pesquisa + grafo[pessoa]
        
    return False

print(pesquisaLargura(grafo))

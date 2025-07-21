lista1 = [] # Adicionar à lista dos id.
lista2 = [] # Adicionar à lista dos titulos.
lista3 = [] # Adicionar à lista dos autores.
lista4 = [] # Adicionar à lista dos ids dos livros emprestados.
lista5 = [] # Adicionar à lista dos titulos dos livros emprestados.
lista6 = [] # Adicionar à lista dos autores dos livros emprestados.

opcao = ('1,2,3,4,5,6')

biblioteca = [lista1, lista2, lista3]
emprestados = [lista4, lista5, lista6]

while True:
    print("""
    _________________________________
    |          BIBLIOTECA           |
    |-------------------------------|
    |   [1] - Adicionar um Livro.   |
    |   [2] - Remover um Livro.     |
    |   [3] - Emprestar um Livro.   |
    |   [4] - Devolver um Livro.    |
    |   [5] - Ver a Biblioteca.     |
    |   [6] - Sair                  |
    |_______________________________|
    """)

    resposta = input('Digite uma opção: ')

    if resposta in opcao:
        if resposta == '1': # Adicionar um Livro.
            adicionar_livro(lista1, lista2, lista3)

        if resposta == '2': # Remover um Livro.
            remover_livro(lista1, lista2, lista3)

        if resposta == '3': # Emprestar um Livro.
            emprestar_livro(lista1, lista2, lista3, lista4, lista5, lista6)

        if resposta == '4': # Devolver um Livro.
            devolver_livro(lista1, lista2, lista3, lista4, lista5, lista6)

        if resposta == '5': # Ver a Biblioteca.
            ver_livro(biblioteca)

        if resposta == '6': # Sair.
            print('O menu foi fechado!')

            break

    else: # Repetir o programa.
            print('Essa opção não é válida.')

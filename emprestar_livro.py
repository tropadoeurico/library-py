def emprestar_livro(lista1, lista2, lista3, lista4, lista5, lista6):

    biblioteca = [lista1, lista2, lista3]
    emprestados = [lista4, lista5, lista6]

    print('Emprestar Livro: (ID, Titulo, Autor)')
    flag = False
    print('ID: ')
    id = int(input())       # Guarda o id para alterar.
    print('Titulo: ')
    titulo = input()        # Guarda o título para alterar.
    print('Autor: ')
    autor = input()         # Guarda o autor para alterar.

    if id in lista1:
        if titulo in lista2:
            if autor in lista3:
                lista1.remove(id)
                lista2.remove(titulo)
                lista3.remove(autor)

                lista4.append(id)
                lista5.append(titulo)
                lista6.append(autor)

                flag = True
                print('O livro foi emprestado!')

    if flag == False:
        print('Não é possível emprestar esse livro.')

    return (lista1, lista2, lista3, lista4, lista5, lista6)

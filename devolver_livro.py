def devolver_livro(lista1, lista2, lista3, lista4, lista5, lista6):

    biblioteca = [lista1, lista2, lista3]
    emprestados = [lista4, lista5, lista6]

    print('Devolver Livro: (ID, Titulo, Autor)')
    flag = False
    print('ID: ')
    id = int(input())       # Guarda o id para alterar.
    print('Titulo: ')
    titulo = input()        # Guarda o título para alterar.
    print('Autor: ')
    autor = input()         # Guarda o autor para alterar.

    if id in lista4:
        if titulo in lista5:
            if autor in lista6:
                lista4.remove(id)
                lista5.remove(titulo)
                lista6.remove(autor)

                lista1.append(id)
                lista2.append(titulo)
                lista3.append(autor)

                flag = True
                print('O livro foi devolvido!')

    if flag == False:
        print('Não é possível devolver esse livro.')

    return (lista1, lista2, lista3, lista4, lista5, lista6)
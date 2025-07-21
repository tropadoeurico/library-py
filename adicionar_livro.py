def adicionar_livro(lista1, lista2, lista3):

    biblioteca = [lista1, lista2, lista3]

    flag = False
    print('Adicionar livro: (id, nome, autor)')
    print('ID: ')
    id = int(input())   # Guarda o id.

    if id < 0:
        print('Não é possível adicionar ids negativos à biblioteca.')

    if id > 0:
        print('Titulo: ')
        titulo = input()    # Guarda o título.
        print('Autor: ')
        autor = input()     # Guarda o autor.

        if id:
            if titulo:
                if autor:
                    lista1.append(id)
                    lista2.append(titulo)
                    lista3.append(autor)
                    flag = True
                    print('O livro foi adicionado!')


            if flag == False:
                    print('Não é possível adicionar à biblioteca.')

        return (lista1,lista2,lista3)
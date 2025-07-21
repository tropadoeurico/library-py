def add_book(list1, list2, list3):

    biblioteca = [list1, list2, list3]

    flag = False
    print('Add Book: (id, nome, autor)')
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
                    list1.append(id)
                    list2.append(titulo)
                    list3.append(autor)
                    flag = True
                    print('O livro foi adicionado!')


            if flag == False:
                    print('Não é possível adicionar à biblioteca.')

        return (list1,list2,list3)

def remover_livro(lista1, lista2, lista3):

    biblioteca = [lista1, lista2, lista3]

    print('Remover Livro: (ID, Titulo, Autor)')
    flag = False
    print('ID: ')
    id = int(input())           # Guarda o id para remover.
    print('Titulo: ')
    titulo = input()            # Guarda o título para remover.
    print('Autor: ')
    autor = input()             # Guarda o autor para remover.


    if id in lista1:
        if titulo in lista2:
            if autor in lista3:
                lista1.remove(id)
                lista2.remove(titulo)
                lista3.remove(autor)
                flag = True

    if flag == False:
        print('Não é possível remover nada da biblioteca.')

    return (lista1, lista2, lista3)
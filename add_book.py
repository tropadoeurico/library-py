def add_book(list1, list2, list3):

    biblioteca = [list1, list2, list3]

    flag = False
    print('Add Book: (id, name, author)')
    print('ID: ')
    id = int(input())   # Save the id.

    if id < 0:
        print('Cannot add negative ids to the library.')

    if id > 0:
        print('Title: ')
        titulo = input()    # Save the title.
        print('Author: ')
        autor = input()     # Save the author.

        if id:
            if titulo:
                if autor:
                    list1.append(id)
                    list2.append(title)
                    list3.append(author)
                    flag = True
                    print('The book has been added!')


            if flag == False:
                    print('Unable to add to library.')

        return (list1,list2,list3)

def add_book(list1, list2, list3):

    library = [list1, list2, list3]

    flag = False
    print('Add Book: (id, title, author)')
    print('ID: ')
    id = int(input())   # Save the id.

    if id < 0:
        print('Cannot add negative ids to the library.')

    if id > 0:
        print('Title: ')
        title = input()    # Save the title.
        print('Author: ')
        author = input()     # Save the author.

        if id:
            if title:
                if author:
                    list1.append(id)
                    list2.append(title)
                    list3.append(author)
                    flag = True
                    print('The book has been added!')


            if flag == False:
                    print('Unable to add to library.')

        return (list1,list2,list3)

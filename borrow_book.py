def borrow_book(list1, list2, list3, list4, list5, list6):

    library = [list1, list2, list3]
    borrowed = [list4, list5, list6]

    print('Borrow book: (ID, Title, Author)')
    flag = False
    print('ID: ')
    id = int(input())       # Save the id to change.
    print('Title: ')
    title = input()        # Save the title to change.
    print('Author: ')
    author = input()         # Save the author to change.

    if id in list1:
        if title in list2:
            if author in list3:
                list1.remove(id)
                list2.remove(title)
                list3.remove(author)

                list4.append(id)
                list5.append(title)
                list6.append(author)

                flag = True
                print('The book was borrowed!')

    if flag == False:
        print('It is not possible to lend this book.')

    return (list1, list2, list3, list4, list5, list6)

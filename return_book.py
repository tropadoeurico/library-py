def return_book(list1, list2, list3, list4, list5, list6):

    library = [list1, list2, list3]
    borrowed = [list4, list5, list6]

    print('Return Book: (ID, Title, Author)')
    flag = False
    print('ID: ')
    id = int(input())       # Save the id to change.
    print('Title: ')
    title = input()        # Save the title to change.
    print('Author: ')
    author = input()         # Save the author to change.

    if id in list4:
        if title in list5:
            if author in lista6:
                list4.remove(id)
                list5.remove(title)
                list6.remove(author)

                list1.append(id)
                list2.append(title)
                list3.append(author)

                flag = True
                print('The book has been returned!')

    if flag == False:
        print('This book cannot be returned.')

    return (list1, list2, list3, list4, list5, list6)

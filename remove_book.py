def remove_book(list1, list2, list3):

    library = [list1, list2, list3]

    print('Remove a book: (ID, Title, Author)')
    flag = False
    print('ID: ')
    id = int(input())           # Store the id to remove.
    print('Title: ')
    title = input()            # Save the title to remove.
    print('Author: ')
    author = input()             # Save the author to remove.


    if id in list1:
        if title in list2:
            if author in list3:
                list1.remove(id)
                list2.remove(title)
                list3.remove(author)
                flag = True

    if flag == False:
        print('You cannot remove anything from the library.')

    return (list1, list2, list3)

list1 = [] # Add to list of ids.
list2 = [] # Add to list of titles.
list3 = [] # Add to authors list.
list4 = [] # Add to list of borrowed book IDs.
list5 = [] # Add to list of borrowed book titles.
list6 = [] # Add to the list of authors of borrowed books.

option = ('1,2,3,4,5,6')

library = [list1, list2, list3]
borrowed = [list4, list5, list6]

while True:
    print("""
    _________________________________
    |            LIBRARY            |
    |-------------------------------|
    |   [1] - Add a book.           |
    |   [2] - Remove a book.        |
    |   [3] - Borrow a book.        |
    |   [4] - Return a book.        |
    |   [5] - View the library.     |
    |   [6] - Leave.                |
    |_______________________________|
    """)

    resposta = input('Enter an option: ')

    if resposta in opcao:
        if resposta == '1': # Add a Book.
            add_book(list1, list2, list3)

        if resposta == '2': # Remove a Book.
            remove_book(list1, list2, list3)

        if resposta == '3': # Borrow a Book.
            borrowed_book(list1, list2, list3, list4, list5, list6)

        if resposta == '4': # Return a Book.
            return_book(list1, list2, list3, list4, list5, list6)

        if resposta == '5': # View the Library.
            view_book(library)

        if resposta == '6': # Leave.
            print('The menu has been closed!')

            break

    else: # Repeat the program.
            print('This option is not valid.')

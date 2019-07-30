book_name = input("Enter name of the book (say 'done' if done) ")
books = []

while book_name:
    if book_name == 'done':
        break

    books.append(book_name)
    book_name = input()

print(books)

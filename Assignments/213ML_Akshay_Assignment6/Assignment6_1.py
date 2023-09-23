class BookStore:
    noOfBooks = 0
    def __init__(self) -> None:
        self.name = ''
        self.author = ''

    def display(self):
        print('Book `{}` is written by author `{}`'. format(self.name, self.author))
        print('Author `{}` has written total `{}` no. of books'. format(self.author, BookStore.noOfBooks))

    def accept(self):
        self.name = str(input('Enter name of book : '))
        self.author = str(input('Enter name of author : '))
        BookStore.noOfBooks = int(input('Enter No. of books written by auther : '))

def main():
    print('Book Store')
    print('--------------------------')
    store1 = BookStore()
    store2 = BookStore()
    store1.accept()
    store2.accept()
    print('--------------------------')
    
    store1.display()
    print('--------------------------')
    store2.display()

if (__name__ == '__main__'):
    main()

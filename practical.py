print("Welcome to the Library Book Management System\n ")
class Book:
    def __init__(self,book_id,title,author,copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
    def display(self):
        print(f"Book ID:{self.book_id},Title: {self.title},Author: {self.author},Copies:{self.copies}",sep = " | ")

books = {}
while True:
    choice = int(input(" 1.Add a new book\n 2.View all books\n 3.Update book information\n 4.Remove a book\n 5.Search for a book\n 6.Sort and display books\n 7.Display Statistics\n 8.Exit\n \nEnter your choice: "))
    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        copies = int(input("Enter the Number of Copies: "))
        m = Book(book_id,title,author,copies)
        books[book_id] = m
        print("\nBook added successfully !\n")
        add_book = input("Do you want to continue? (y/n): ")
        print(add_book)
        if add_book == "y":
            option=int(input(" 1.Add a new book\n 2.View all books\n \nEnter your choice: "))
            if option == 1:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                copies = int(input("Enter the Number of Copies: "))
                m = Book(book_id,title,author,copies)
                books[book_id] = m
                print("\nBook added successfully !\n")
            elif option == 2:
                for book in books.values():
                    book.display()
            else:
                print("You have entered wrong option !")                
    
    elif choice == 2:
        for book in books.values():
            book.display()
    
    elif choice == 3:  
        book_id = int(input("Enter the Book ID to update: "))
        if book_id in books:
            book = books[book_id]
            print("1. Update Title\n2. Update Author\n3. Update Copies")
            update_choice = int(input("Choose what you want to update: "))
            if update_choice == 1:
                book.title = input("Enter the updated title: ")
            elif update_choice == 2:
                book.author = input("Enter the updated author: ")
            elif update_choice == 3:
                book.copies = int(input("Enter the updated number of copies: "))
            else:
                print("Invalid option.")
            print("\nBook information updated successfully!\n")
        else:
            print("Book ID not found.\n")

    elif choice == 4:
        ID = int(input("\nEnter the Book ID which you want to update: "))
        del books[ID]
        print("\nThe Book has been removed !\n")
    
    elif choice == 5:
        book_id = int(input("Enter the Book ID to update: "))
        if book_id in books:
            books[book_id].display()
 
    elif choice == 6:
        sorted_books = sorted(books.values(), key=lambda x: x.title)
        for book in sorted_books:
            book.display()

    elif choice == 7:
        total_books = len(books)
        total_copies = sum(book.copies for book in books.values())
        print(f"Total Books: {total_books}, Total Copies: {total_copies}\n")
   
    elif choice == 8:
        print("\nExiting the programm.\n \nGoodbye !")
        break
    
    else:
        print("\nYou have Entered the Wrong Choice ! \n")



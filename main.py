from library import Library

def main():
    print("Welcome to the Library Management System")
    print("1. Login as Librarian")
    print("2. Login as User")
    choice = input("Please select an option (1/2): ")

    if choice == '1':
        librarian_interface()
    elif choice == '2':
        user_interface()
    else:
        print("Invalid choice. Please select 1 or 2.")
        main()

def librarian_interface():
    print("\nLibrarian Menu")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Generate Reports")
    choice = input("Please select an option (1/2/3/4): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        search_book()
    elif choice == '4':
        generate_reports()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        librarian_interface()

def add_book():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="brian",
        password="apple123",
        database="mydatabase"
        )
        
        Title = input("Enter book title: ")
        Author = input("Enter book author: ")
        Genre = input("Enter book genre: ")
        Release_Year = input("Enter book release year: ")

        sql = """INSERT INTO library (Title, Author, Genre, Release_Year)
                 VALUES (%s, %s, %s, %s)"""
        values = (Title, Author, Genre, Release_Year)
        
        mycursor = mydb.cursor()
        mycursor.execute(sql, values)
        mydb.commit()
        print("Book added successfully!")

    except:
        print("Book added unsuccessfully")
    pass

def remove_book():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="brian",
        password="apple123",
        database="mydatabase"
        )
        
        Title = input("Enter book title: ")
        Author = input("Enter book author: ")
        Genre = input("Enter book genre: ")
        Release_Year = input("Enter book release year: ")
        
        sql = """DELETE FROM Library (Title, Author, Genre, Release_Year)
             VALUES (%s, %s, %s, %s)"""
        values = (Title, Author, Genre, Release_Year)
        
        mycursor = mydb.cursor()
        mycursor.execute(sql, values)
        mydb.commit()
        print("Book deleted successfully!")
        
    except:
        print("Book Not Found!")
    pass

def search_book():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="brian",
        password="apple123",
        database="mydatabase"
        )
        
        Book = input("Enter book title: ")
        
        sql = "SELECT id FROM Library WHERE Title = Book"
        
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)

        mydb.commit()
    
    except:
        print("Book Not Found!")
        
    pass

def generate_reports():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="brian",
        password="apple123",
        database="mydatabase"
        )
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Library WHERE availability LIKE 'YES")
        books_available = mycursor.fetchall()
        
        for x in books_available:
            print(f"Books available: {x}")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Library WHERE availability != 'YES")
        books_borrowed = mycursor.fetchall()
        
        for y in books_borrowed:
            print(f"Books borrowed: {y}")
            
        mydb.commit()
   
    except:
        print("Error")
        
    pass

def user_interface():
    print("\nUser Menu")
    print("1. Check-in a Book")
    print("2. Check-out a Book")
    print("3. Search for a Book")
    choice = input("Please select an option (1/2/3): ")

    if choice == '1':
        check_in_book()
    elif choice == '2':
        check_out_book()
    elif choice == '3':
        search_book()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        user_interface()




def check_in_book():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="brian",
        password="apple123",
        database="mydatabase"
        )
        
        book = input("Enter book title: ")
        sql = "UPDATE Library SET availability = 'YES' WHERE Title = book;"
        
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        
    
        mydb.commit()
        print("Book returned successfully!")
    
    except:
        print("Book Not Found!")
    
    pass

def check_out_book():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="brian",
        password="apple123",
        database="mydatabase"
        )
        
        book = input("Enter book title: ")
        sql = "UPDATE Library SET availability = 'NO' WHERE Title = book;"
        
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        
        mydb.commit()
        print("Book borrowed successfully!")
    
    except:
        print("Book Not Found!")
    
    pass


if __name__ == "__main__":
    main()

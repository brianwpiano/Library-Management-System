import mysql.connector
from datetime import datetime, timedelta

def sqlfunction():
    mydb = mysql.connector.connect(
    host="localhost",
    user="brian",
    password="apple123",
    database="mydatabase"
    )
    
    return mydb

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
    while True:
        print("\nLibrarian Menu")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Generate Reports")
        print("5. Logout")
        choice = input("Please select an option (1/2/3/4/5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            generate_reports()
        elif choice == '5':
            main()
        else:
            print("Invalid choice. Please select 1, 2, 3, 4 or 5.")
            librarian_interface()

def add_book():
    try:
        mydb = sqlfunction()
        
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
        print("Error Connection in MySQL Server for add_book Function")
        raise TypeError

def remove_book():
    try:
        mydb = sqlfunction()
        
        Title = input("Enter book title: ")
        Author = input("Enter book author: ")
        Genre = input("Enter book genre: ")
        Release_Year = input("Enter book release year: ")

        sql = '''
            DELETE FROM Library Where Title = %s AND Author = %s AND Genre = %s AND Release_Year = %s
        '''
            
        values = (Title, Author, Genre, Release_Year, )
        
        mycursor = mydb.cursor()
        mycursor.execute(sql, values)
        mydb.commit()
        print("Book deleted successfully!")
        
    except:
        print("Error Connection in MySQL Server for remove_book Function")
        raise TypeError
        
def search_book():
    try:
        mydb = sqlfunction()
        
        book = input("Enter book title: ")
        
        mycursor = mydb.cursor()
        
        sql = "SELECT id, Title, Author, Genre, Availability, Release_Year FROM Library WHERE Title = %s"
        cond = (book, )
        
        mycursor.execute(sql, cond)
        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)

        mydb.commit()
    
    except:
        print("Error Connection in MySQL Server for search_book Function")
        raise TypeError

def generate_reports():
    try:
        mydb = sqlfunction()
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Library WHERE availability LIKE 'YES")
        books_available = mycursor.fetchall()
        
        for x in books_available:
            print(f"Books available: {x}")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Library WHERE availability != 'YES'")
        books_borrowed = mycursor.fetchall()
        
        for y in books_borrowed:
            print(f"Books borrowed: {y}")
            
        mydb.commit()
   
    except:
        print("Error Connection in MySQL Server for generate_reports Function")
        raise TypeError

def user_interface():
    while True:
        print("\nUser Menu")
        print("1. Check-in a Book")
        print("2. Check-out a Book")
        print("3. Search for a Book")
        print("4. Logout")
        choice = input("Please select an option (1/2/3): ")

        if choice == '1':
            check_in_book()
        elif choice == '2':
            check_out_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            main()
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            user_interface()


def check_in_book():
    try:
        mydb = sqlfunction()
        
        book = input("Enter book title: ")
        return_date = datetime.now()
        sql = """
        UPDATE Library 
        SET availability = 'YES', Return_Date = %s WHERE Title = %s;"""
        values = (return_date.date(), book)
        
        mycursor = mydb.cursor()
        mycursor.execute(sql, values)
        
        mydb.commit()
        print("Book returned successfully!")
    
    except:
        print("Error Connection in MySQL Server for check_in_book Function")
        raise TypeError

def check_out_book():
    try:
        mydb = sqlfunction()
        
        book = input("Enter book title: ")
        check_out_date = datetime.now()
        due_date = check_out_date + timedelta(days=30)
        
        sql_update = """
        UPDATE Library
        SET Availability = 'NO', Check_Out_Date = %s, Due_Date = %s WHERE Title = %s;"""
                 
        values_update = (check_out_date.date(), due_date.date(), book)
        
        mycursor = mydb.cursor()
        mycursor.execute(sql_update, values_update)
        
        mydb.commit()
        print(f"Book borrowed successfully! Due date is {due_date.date()}")
    
    except:
        print("Error Connection in MySQL Server for check_out_book Function")
        raise TypeError

if __name__ == "__main__":
    main()

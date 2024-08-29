import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="brian",
password="apple123",
)

print (mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("DROP DATABASE IF EXISTS mydatabase")

mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("USE mydatabase")


mycursor.execute("""
CREATE TABLE IF NOT EXISTS Library(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    Title VARCHAR(255) NOT NULL UNIQUE, 
    Author VARCHAR(255) NOT NULL, 
    Genre VARCHAR(100),
    Availability ENUM('YES', 'NO') DEFAULT 'YES',
    Release_Year VARCHAR(4),
    Check_Out_Date DATE,
    Due_Date DATE,
    Return_Date DATE
    )""")

sql = "INSERT INTO Library (Title, Author, Genre, Release_Year, Check_Out_Date, Due_Date, Return_Date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
Library = [
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', '1960', None, None, None),
    ('1984', 'George Orwell', 'Dystopian', '1949', None, None, None),
    ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', '1951', None, None, None),
    ('Pride and Prejudice', 'Jane Austen', 'Romance', '1813', None, None, None),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', '1925', None, None, None),
    ('Murder on the Orient Express', 'Agatha Christie', 'Mystery', '1934', None, None, None),
    ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', '1937', None, None, None),
    ('Educated', 'Tara Westover', 'Memoir', '2018', None, None, None),
    ('The Silent Patient', 'Alex Michaelides', 'Thriller', '2019', None, None, None),
    ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'Non-Fiction', '2011', None, None, None),
    ('Where the Crawdads Sing', 'Delia Owens', 'Fiction/Mystery', '2018', None, None, None),
    ('Dune', 'Frank Herbert', 'Science Fiction', '1965', None, None, None),
    ('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', '2006', None, None, None),
    ('Little Fires Everywhere', 'Celeste Ng', 'Drama', '2017', None, None, None),
    ('The Name of the Wind', 'Patrick Rothfuss', 'Fantasy', '2007', None, None, None),
    ('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Crime', '2005', None, None, None),
    ('Becoming', 'Michelle Obama', 'Memoir', '2018', None, None, None),
    ('The Leftovers', 'Tom Perrotta', 'Fiction', '2011', None, None, None),
    ('Circe', 'Madeline Miller', 'Fantasy', '2018', None, None, None),
    ('The Martian', 'Andy Weir', 'Science Fiction', '2011', None, None, None),
    ('The Goldfinch', 'Donna Tartt', 'Fiction', '2013', None, None, None),
    ('The Handmaid\'s Tale', 'Margaret Atwood', 'Dystopian', '1985', None, None, None),
    ('The Alchemist', 'Paulo Coelho', 'Fiction/Philosophy', '1988', None, None, None),
    ('Normal People', 'Sally Rooney', 'Contemporary Fiction', '2018', None, None, None),
    ('The Da Vinci Code', 'Dan Brown', 'Thriller/Mystery', '2003', None, None, None),
    ('Gone Girl', 'Gillian Flynn', 'Thriller', '2012', None, None, None),
    ('A Song of Ice and Fire', 'George R.R. Martin', 'Fantasy', '1996', None, None, None),
    ('The Hunger Games', 'Suzanne Collins', 'Dystopian', '2008', None, None, None),
    ('Life of Pi', 'Yann Martel', 'Adventure/Philosophy', '2001', None, None, None),
    ('Big Little Lies', 'Liane Moriarty', 'Drama/Mystery', '2014', None, None, None),
    ('The Shadow of the Wind', 'Carlos Ruiz Zafón', 'Mystery/Thriller', '2001', None, None, None),
    ('The Woman in the Window', 'A.J. Finn', 'Thriller', '2018', None, None, None),
    ('An American Marriage', 'Tayari Jones', 'Fiction', '2018', None, None, None),
    ('Station Eleven', 'Emily St. John Mandel', 'Post-Apocalyptic', '2014', None, None, None),
    ('The Outsiders', 'S.E. Hinton', 'Young Adult', '1967', None, None, None),
    ('Good Omens', 'Neil Gaiman & Terry Pratchett', 'Fantasy/Comedy', '1990', None, None, None),
    ('The Sun Down Motel', 'Simone St. James', 'Thriller/Mystery', '2020', None, None, None),
    ('The Night Circus', 'Erin Morgenstern', 'Fantasy/Romance', '2011', None, None, None),
    ('All the Light We Cannot See', 'Anthony Doerr', 'Historical Fiction', '2014', None, None, None),
    ('Red, White & Royal Blue', 'Casey McQuiston', 'Romance', '2019', None, None, None),
    ('The Giver', 'Lois Lowry', 'Dystopian', '1993', None, None, None)
]

mycursor.executemany(sql, Library)

mydb.commit()

print(mycursor.rowcount, "books were inserted")

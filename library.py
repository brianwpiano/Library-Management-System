import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="brian",
password="apple123",
)

print (mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

mycursor.execute("USE mydatabase")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Library(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    Title VARCHAR(255) NOT NULL, 
    Author VARCHAR(255) NOT NULL, 
    Genre VARCHAR(100), 
    Release_Year VARCHAR(4)
    )""")

sql = "INSERT INTO Library (Title, Author, Genre, Release_Year) VALUES (%s, %s, %s, %s)"
Library = [
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', '1960'),
    ('1984', 'George Orwell', 'Dystopian', '1949'),
    ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', '1951'),
    ('Pride and Prejudice', 'Jane Austen', 'Romance', '1813'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', '1925'),
    ('Murder on the Orient Express', 'Agatha Christie', 'Mystery', '1934'),
    ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', '1937'),
    ('Educated', 'Tara Westover', 'Memoir', '2018'),
    ('The Silent Patient', 'Alex Michaelides', 'Thriller', '2019'),
    ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'Non-Fiction', '2011'),
    ('Where the Crawdads Sing', 'Delia Owens', 'Fiction/Mystery', '2018'),
    ('Dune', 'Frank Herbert', 'Science Fiction', '1965'),
    ('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', '2006'),
    ('Little Fires Everywhere', 'Celeste Ng', 'Drama', '2017'),
    ('The Name of the Wind', 'Patrick Rothfuss', 'Fantasy', '2007'),
    ('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Crime', '2005'),
    ('Becoming', 'Michelle Obama', 'Memoir', '2018'),
    ('The Leftovers', 'Tom Perrotta', 'Fiction', '2011'),
    ('Circe', 'Madeline Miller', 'Fantasy', '2018'),
    ('The Martian', 'Andy Weir', 'Science Fiction', '2011'),
    ('The Goldfinch', 'Donna Tartt', 'Fiction', '2013'),
    ('The Handmaid\'s Tale', 'Margaret Atwood', 'Dystopian', '1985'),
    ('The Alchemist', 'Paulo Coelho', 'Fiction/Philosophy', '1988'),
    ('Normal People', 'Sally Rooney', 'Contemporary Fiction', '2018'),
    ('The Da Vinci Code', 'Dan Brown', 'Thriller/Mystery', '2003'),
    ('Gone Girl', 'Gillian Flynn', 'Thriller', '2012'),
    ('A Song of Ice and Fire', 'George R.R. Martin', 'Fantasy', '1996'),
    ('The Hunger Games', 'Suzanne Collins', 'Dystopian', '2008'),
    ('Life of Pi', 'Yann Martel', 'Adventure/Philosophy', '2001'),
    ('Big Little Lies', 'Liane Moriarty', 'Drama/Mystery', '2014'),
    ('The Shadow of the Wind', 'Carlos Ruiz Zafón', 'Mystery/Thriller', '2001'),
    ('The Woman in the Window', 'A.J. Finn', 'Thriller', '2018'),
    ('An American Marriage', 'Tayari Jones', 'Fiction', '2018'),
    ('Station Eleven', 'Emily St. John Mandel', 'Post-Apocalyptic', '2014'),
    ('The Outsiders', 'S.E. Hinton', 'Young Adult', '1967'),
    ('Good Omens', 'Neil Gaiman & Terry Pratchett', 'Fantasy/Comedy', '1990'),
    ('The Sun Down Motel', 'Simone St. James', 'Thriller/Mystery', '2020'),
    ('The Night Circus', 'Erin Morgenstern', 'Fantasy/Romance', '2011'),
    ('All the Light We Cannot See', 'Anthony Doerr', 'Historical Fiction', '2014'),
    ('Red, White & Royal Blue', 'Casey McQuiston', 'Romance', '2019'),
    ('The Giver', 'Lois Lowry', 'Dystopian', '1993')
]

mycursor.executemany(sql, Library)

mydb.commit()

print(mycursor.rowcount, "books were inserted")

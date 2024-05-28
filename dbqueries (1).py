import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd="password",
    database = "Bookdatabase"
)

my_cursor = mydb.cursor()
# def numOfFavs():
#     my_cursor.execute(  "SELECT Books.title, Count(accounts.favouriteBook) as numberOfFavourites"
#                         "FROM Books"
#                         "CROSS JOIN accounts"
#                         "WHERE Books.title = accounts.favouriteBook"
#                         "ORDER BY Count(accounts.favouriteBook);")
#     result = my_cursor.fetchall()
#     for x in result:
#         print(x)



def changePassword(newpasswrd):
    my_cursor.execute(
	                    "UPDATE accounts"
	                    "SET passwrd = " + "'"+  newpasswrd + "';")

def changeUN(newusername):
    my_cursor.execute(
	                    "UPDATE accounts"
	                    "SET username = " + "'"+  newusername + "';")

# def addBook(title, author, isbn):
#     my_cursor.execute("INSERT INTO Books(title, author, isbn) VALUES (" + "'"+ title +"',"+"'"+  author + "'," +"'"+  isbn+"');")

def addAuthor(authorName):
    my_cursor.execute("INSERT INTO Author(authorName) VALUES("+"'"+ authorName+"');")

# def addAccount(userName, passwrd):
#     my_cursor.execute("INSERT INTO Account(userName, passwrd) VALUES("+ "'"+  userName+ "'"+ ","+ "'"+  passwrd +"') WHERE"+userName+"NOT IN (SELECT userName FROM Accounts);")

# def addFavouriteBook(userName, newfav):
#     my_cursor.execute(  "UPDATE Account" +
#                         "WHERE userName = '" + userName + "'"
#                         "SET favouriteBook =" + "'"+ newfav +"'")

def sortByTitle():
    my_cursor.execute( "SELECT * FROM Books"
                      "Order by title")
    

def AddBio(newbio):
    my_cursor.execute("INSERT INTO Author(biography) VALUES ("+"'"+ newbio+"')")

def sortByAuthor():
    my_cursor.execute("SELECT * FROM Books"
                      "Order by Author")

def sort_by_letter_in_title(inputs):
    my_cursor.execute("SELECT title FROM Books"
                      "WHERE title =" + inputs + "%")
    
def sort_by_letter_in_author(inputs):
    my_cursor.execute("SELECT authorName FROM Author"
                      "WHERE authorName =" + inputs + "%")
    

my_cursor.execute("SHOW DATABASES")


#COME UP WITH A FUNCTION AND A TRIGGER
#Increase number of published books for author when new book is added?

# DELIMITER $$
# CREATE TRIGGER newFavBook
# AFTER UPDATE 
# ON Accounts
# FOR EACH ROW
# BEGIN
# 	IF new.favouriteBook NOT IN (SELECT title FROM Books)
# 		THEN INSERT INTO Books(title, authorName, isbn) VALUES (new.favouriteBook, "Unknown", "Unknown");
# 	END IF;
# END$$
# DELIMITER ;

# DELIMITER $$
# CREATE TRIGGER newAuthor
# AFTER INSERT 
# ON Books
# FOR EACH ROW
# BEGIN
# 	IF new.authorName NOT IN (SELECT authorName FROM Author)
# 		THEN INSERT INTO author(authorName) VALUES (new.authorName);
# 	END IF;
# END$$
# DELIMITER ;

for db in my_cursor:
    print(db)
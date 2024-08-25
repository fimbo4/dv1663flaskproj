import mysql.connector
mydb = mysql.connector.connect(
    host="", 
    user="root",
    passwd="boco_287"
)

my_cursor = mydb.cursor()

my_cursor.execute('USE Bookdatabase;')
#my_cursor.execute("SET SQL_SAFE_UPDATES = 0;")
def addAccount(userName, passwrd):
    out_string = "INSERT INTO accounts(userName, passwrd) SELECT " + "'" + userName + "'" +", " + "'" + passwrd + "'" + " WHERE " + "'" + userName + "' " + "NOT IN (SELECT userName FROM accounts);"
    my_cursor.execute(out_string)
    mydb.commit()
    #return

def check_uname(uname):
    my_cursor.execute("SELECT * FROM accounts;")
    for a in my_cursor:
        if uname == a[1]:
            my_cursor.reset()
            return True
    my_cursor.reset()
    return False
    

def check_passw(uname, passw):
    query = "SELECT passwrd FROM accounts WHERE userName = "  "'" + uname + "'" + ";"
    my_cursor.execute(query)
    ans = my_cursor.fetchall()
    if passw == ans[0][0]:
        my_cursor.reset()
        return True
    else:
        my_cursor.reset()
        return False  

def get_id(uname):
    query = "SELECT id FROM accounts WHERE userName = " + "'" + uname + "'" + ";"
    my_cursor.execute(query)
    for ans in my_cursor:
        out = ans[0]
        my_cursor.reset()
        return out
    
def addBook(title, author, isbn):
    query = "INSERT INTO Books(title, authorName, isbn) VALUES (" + "'"+ title +"',"+"'"+  author + "'," +"'"+  isbn+"');"
    #print(query)
    my_cursor.execute(query)
    mydb.commit()

def get_books(search_input):
    #gets the book information when searching the sites library
    query = """SELECT * FROM books LEFT JOIN (SELECT Books.title, COUNT(favbooks.isbn) as numberOfFavourites
    FROM Books
    CROSS JOIN favbooks
    WHERE Books.isbn = favbooks.isbn
    GROUP BY books.isbn) AS favbooks ON favbooks.title = books.title WHERE books.title LIKE '%""" + search_input + "%' OR books.authorName LIKE '%" + search_input + "%' OR books.isbn LIKE '%" + search_input + "%';" 
    my_cursor.execute(query)
    out_data = []
    for book in my_cursor:
        print(book)
        out_data.append(book)
    return out_data

def add_fav_book(book_name, uid):
    query = "CALL addfavbook('" + book_name + "'" + ', ' + uid + ");"
    my_cursor.execute(query)
    mydb.commit()

def addtofavs(uid, isbn):
    query = "CALL addtofavs('" + uid + "'" + ', ' + '"' + isbn + '"' + ");"
    my_cursor.execute(query)
    mydb.commit()

def get_book_info(isbn):
    query = ""

def get_books_common(session_id, val):
    query = """SELECT * FROM books JOIN (SELECT favbooks.id AS id1, favbooks.isbn AS isbn1 FROM favbooks JOIN favbooks AS booksincommon
    ON favbooks.isbn = booksincommon.isbn WHERE favbooks.id = """ + str(session_id) + " AND booksincommon.id = " + str(val) + ") AS fab WHERE books.isbn = fab.isbn1;"
    print(query)
    temp_cursor = mydb.cursor(buffered=True)
    temp_cursor.execute(query)
    mydb.commit()
    out_data = []
    for book in temp_cursor:
        print(book)
        out_data.append(book)
    return out_data

def get_users_fav_books(uid):
    query = "SELECT * FROM books JOIN favbooks ON books.isbn = favbooks.isbn WHERE favbooks.id = " + uid + ";"
    my_cursor.execute(query)
    out_data = []
    for book in my_cursor:
        print(book)
        out_data.append(book)
    return out_data

def get_user_common(id):
    query = "SELECT userName, id FROM accounts WHERE id = " + str(id) + ";"
    my_cursor.execute(query)
    out_data = []
    for user in my_cursor:
        out_data.append(user)
    return out_data

def book_count(isbn):
    query = "SELECT COUNT(isbn) FROM favbooks WHERE isbn = '" + isbn + "';"
    my_cursor.execute(query)
    out_data = []
    for count in my_cursor:
        out_data.append(count)
    return out_data[0][0]

def my_fav(uid):
    query = "SELECT favouriteBook, books.authorName FROM accounts JOIN books ON accounts.favouriteBook = books.title WHERE id =" + uid + ";"
    my_cursor.execute(query)
    out_data = []
    for fav in my_cursor:
        print(fav)
        out_data.append(fav)
    return out_data
    
def search_authors(auth_info):
    query = "SELECT authorName FROM author WHERE authorName LIKE '%" + auth_info + "%';"
    my_cursor.execute(query)
    out_data = []
    for author in my_cursor:
        out_data.append(author)
    return out_data

def get_auth_info(auth_param):
    query = "SELECT books.title FROM books JOIN author ON books.authorName = author.authorName WHERE author.authorName = '" + auth_param + "';"
    my_cursor.execute(query)
    out_data = []
    for q in my_cursor:
        out_data.append(q)
    return out_data

def search_users(user_info):
    query = "SELECT userName, FavouriteBook FROM accounts WHERE userName LIKE '%" + user_info + "%';"
    my_cursor.execute(query)
    out_data = []
    for user in my_cursor:
        out_data.append(user)
    return out_data

def search_users_common(session_id):
    query = """SELECT DISTINCT fb1.id FROM favbooks as 
    fb1 INNER JOIN favbooks as fb2 ON fb1.isbn = fb2.isbn 
    WHERE fb1.id != fb2.id  AND fb1.id != """ + str(session_id) + ';'
    my_cursor.execute(query)
    print(query)
    out_data = []
    for user in my_cursor:
        out_data.append(user)
    return out_data

def search_user_page(user_info):#new
    query = "SELECT userName, id FROM accounts WHERE userName LIKE '%" + user_info + "%';"
    my_cursor.execute(query)
    out_data = []
    for user in my_cursor:
        out_data.append(user)
    return out_data
  
def get_username(id):
    query = "SELECT userName FROM accounts where id  = " + id + ";"
    my_cursor.execute(query)
    out_data = []
    for uname in my_cursor:
        out_data.append(uname)
    return out_data[0][0]

# def num_of_favs():
#     my_cursor.execute(  """SELECT Books.title, Count(accounts.favouriteBook) as numberOfFavourites
#                         FROM Books
#                         CROSS JOIN accounts
#                         WHERE Books.title = accounts.favouriteBook
#                         ORDER BY Count(accounts.favouriteBook);""")
#     result = my_cursor.fetchall()
#     for x in result:
#         print(x)


#add a procedure or a function and also make a query that uses grouping
#blank username and blank password counts as a valid account lol
from flask import Flask, render_template, url_for, request
#from flask_sqlalchemy import SQLAlchemy
import create_db as db
import search_formatter as sf
from hashlib import sha256
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:boco_287@localhost/books"

app.secret_key = b'akljqw__12'

session_id = -1

prev_page = None
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return render_template("signup.html")

@app.route("/create", methods=['POST'])
def create():
    db.addAccount(request.form['create_uname'], request.form['create_pass'])
    return index()

@app.route("/login", methods=['POST'])
def login():
    uname = request.form['uname']
    passw = request.form['pass']
    if db.check_uname(uname) and db.check_passw(uname, passw):
        global session_id 
        session_id = db.get_id(uname)
    else:#feels unnecesarry but crashes without
        session_id = -1
    #print(session_id)
    profile_rend()
    out = '<a href="">asda</a>'
    #print(db.my_fav(str(session_id)))
    db_books = db.get_users_fav_books(str(session_id))
    if len(db.get_users_fav_books(str(session_id))) != 0:
        table_data = sf.profile_display_favorites(db_books)
        return render_template("home.html", data = out, data2 = session_id, data3 = table_data)
    else:
        return render_template("home.html", data = out, data2 = session_id)

@app.route("/gotoaddbook", methods=['POST', 'GET'])#dont forget GET
def gotoaddbook():
    return render_template("addbook.html")

@app.route("/addbook", methods=['POST'])
def addbook():
    title = request.form['bname']
    author = request.form['author']
    isbn = request.form['ISBN']
    db.addBook(title, author, isbn)
    if session_id == -1:
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/logout", methods=['POST'])
def logout():
    global session_id
    #print(session_id)
    session_id = -1
    return render_template("index.html")

@app.route("/rend", methods=['POST'])
def profile_rend():
    #print(type("""<a href="">asda</a>"""))
    pass

@app.route("/booksearch", methods=['POST', 'GET'])
def booksearch():
    global session_id
    #print(session_id)
    return render_template("booksearch.html")

@app.route("/booklist", methods=['POST', 'GET'])
def booklist():
    #print(session_id)
    book_att = request.form['book_att']
    db_books = db.get_books(book_att)
    table_data = sf.book_list(db_books)
    return render_template("booksearch.html", data = table_data)

@app.route("/param/<val>", methods=['POST', 'GET'])#add books to favs
def param(val):
    #print(val)
    global session_id
    #db.num_of_favs()
    if session_id == -1:
        return '', 204
    else:
        db.addtofavs(str(session_id), val)
        return '', 204
    
@app.route("/auth_param/<val>", methods=['POST', 'GET'])
def auth_param(val):
    #print(val)
    auth_data = db.get_auth_info(val)
    return render_template("authorpage.html", data = val, data2 = sf.get_authors_books(auth_data))

@app.route("/user_profile_param/<val>", methods=['POST', 'GET'])#new
def user_profile_param(val):
    #print(db.get_username(val))
    global session_id
    db_books = db.get_users_fav_books(val)
    table_data = sf.profile_display_favorites(db_books)
    if session_id == -1:
        return render_template("public_profile.html", data = db.get_username(val), data2 = table_data)
    else:
        return render_template("public_profile.html", data = db.get_username(val), data2 = table_data, data3 = '<form method="POST" action="/books_in_common/' + val + '"><button type="submit">Find books in common</button></form>')
    
@app.route("/books_in_common/<val>", methods=['POST'])
def books_in_common(val):
    global session_id
    db_books = db.get_books_common(session_id, val)
    table_data = sf.display_books_common(db_books)
    if len(db_books) > 0:
        return render_template("books_in_common.html", data = table_data)
    else:
        return render_template("books_in_common.html")


@app.route("/goback", methods=['POST', 'GET'])
def goback():
    global session_id
    #print(session_id)
    if session_id == -1:
        print(session_id)
        return render_template("index.html")
    elif session_id != -1:
        #print("true")
        out = '<a href="">asda</a>'
        db_books = db.get_users_fav_books(str(session_id))
        if len(db.get_users_fav_books(str(session_id))) != 0:
            table_data = sf.profile_display_favorites(db_books)
            return render_template("home.html", data = out, data2 = session_id, data3 = table_data)
        else:
            return render_template("home.html", data = out, data2 = session_id)

@app.route('/searchauthor', methods=['POST', 'GET'])
def searchauthor():
    return render_template('searchauthors.html')

@app.route('/searchuser', methods=['POST', 'GET'])
def searchuser():
    return render_template('searchusers.html')

@app.route('/authlist', methods=['POST', 'GET'])
def authlist():
    auth_att = request.form['auth_att']
    db_auths = db.search_authors(auth_att)
    table_data = sf.auth_list(db_auths)
    return render_template('searchauthors.html', data = table_data)

@app.route('/userlist', methods=['POST', 'GET'])
def userlist():
    user_att = request.form['user_att']
    db_users = db.search_user_page(user_att)
    table_data = sf.user_list(db_users)
    return render_template('searchusers.html', data = table_data)

if __name__ == "__main__":
    app.run(debug=True)
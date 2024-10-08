import create_db as db
def book_list(db_books):#add a label to each <tr> and button within so that they can be matched, probably just index them in order by what sql returns, then they can be grabbed easier
    #add function call to button with index as parameter
    book_list = """<table>
    <tr>
      <th>Title</th>
      <th>Author</th>
      <th>ISBN</th>
      <th></th>
      <th>No. People who have this as their favorite</th>
    </tr>
  """
    for book in db_books:
        book_list += "<tr> <td>" + book[0] + "</td>" + "<td>" + book[2] + "</td>"+ "<td>" + book[3] + "</td>" + "<td>" + """<form method="POST" action="/param/""" + book[3] + """">""" + """<button type="submit">Add this to your favorites</button> </form> """ + "<td>" + str(book[5]) + "</td>" + "</tr>"
        #print(book)
        #print()
    book_list += """</table>"""

    return book_list

def display_books_common(db_books):
    book_list = """<table>
    <tr>
      <th>Title</th>
      <th>Author</th>
      <th>ISBN</th>
    </tr>
  """
    for book in db_books:
        book_list += "<tr> <td>" + book[0] + "</td>" + "<td>" + book[2] + "</td>"+ "<td>" + book[3] + "</td>" + "</tr>"
    book_list += """</table>"""

    return book_list

def profile_display_favorites(db_books):
    book_list = """<table>
    <tr>
      <th>Title</th>
      <th>Author</th>
      <th>ISBN</th>
    </tr>
  """
    for book in db_books:
        book_list += "<tr> <td>" + book[0] + "</td>" + "<td>" + book[2] + "</td>"+ "<td>" + book[3] + "</td>" + "</tr>"
        #print(book)
        #print()
    book_list += """</table>"""

    return book_list

def auth_list(db_auths):
    auth_list = """<table>
    <tr>
      <th>Author</th>
      <th>Author page</th>
    </tr>
  """
    for auth in db_auths:
        auth_list += """<tr><td>""" + str(auth[0]) + """</td><td><form method="POST" action="/auth_param/""" + str(auth[0]) + """">""" + """<button type="submit">Go to author page</button></form></td></tr>"""
    return auth_list

def get_authors_books(auth_info):
    auth_list = """<table>
    <tr>
      <th>Title</th>
    </tr>"""
    for book in auth_info:
        #print(str(book[0]))
        auth_list += """<tr><td>""" + str(book[0]) + """</td></tr>"""
    auth_list += "</table>"
    return auth_list

def user_list(db_users):
    user_list = """<table>
    <tr>
      <th>Username</th>
      <th>Profile link</th>
    </tr>
  """

    for user in db_users:
        user_list += """<tr><td>""" + str(user[0]) + """</td><td><form method="POST" action="/user_profile_param/""" + str(user[1]) + """">""" + """<button type="submit">Go to user page</button></form></td></tr>"""
    return user_list

#"""<form method="POST" action="/auth_param/""" + str(auth[0]) + ">"
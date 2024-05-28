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
        book_list += "<tr> <td>" + book[0] + "</td>" + "<td>" + book[2] + "</td>"+ "<td>" + book[3] + "</td>" + "<td>" + """<form method="POST" action="/param/""" + book[0] + """">""" + """<button type="submit">Make this your favorite</button> </form> """ + "<td>" + str(book[5]) + "</td>" + "</tr>"
        print(book)
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

def user_list():
    pass

def get_authors_books(auth_info):
    auth_list = """<table>
    <tr>
      <th>Title</th>
    </tr>"""
    for book in auth_info:
        print(str(book[0]))
        auth_list += """<tr><td>""" + str(book[0]) + """</td></tr>"""
    auth_list += "</table>"
    return auth_list

#"""<form method="POST" action="/auth_param/""" + str(auth[0]) + ">"
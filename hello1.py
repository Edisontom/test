import cgi

form = cgi.FieldStorage()
username = form.getfirst("username")
print("Content-type: text/html\n")
print("<p>Hello, {}</p>".format(username))
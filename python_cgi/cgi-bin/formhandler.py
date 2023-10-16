import cgi
import html
import http.cookies
import os

def delete_cookies(cookie):
    for key in cookie.keys():
        cookie[key]['expires'] = 0
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))


if "counter" in cookie.keys():
    counter = int(cookie["counter"].value)
else:
    counter = 0

form = cgi.FieldStorage()    
counter += 1


if "delete_cookies" in form:
    delete_cookies(cookie)
    counter = 0
username = form.getfirst("username", "Anonymous")
password = form.getfirst("password", "")
lang = form.getvalue("lang", "en")
toppings = ["tomato", "salami", "pineapple", "olives"]
toppings_checkbox = {}
for topping in toppings:
    value_choice = form.getvalue(topping, "off")
    toppings_checkbox[topping] = value_choice

username = html.escape(username)
password = html.escape(password)
lang = html.escape(lang)
print(f"Set-cookie: counter={counter}")
print(f"Set-cookie: name={username};")
print(f"Set-cookie: password={password};")
print("Content-type:text/html\r\n\r\n")
escaped_cookie = html.escape(os.environ["HTTP_COOKIE"])
template_html = f"""
<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Processing</title>
</head>
<body>
    <h1>Welcome, {username}!</h1>
    <h2>Order number (form number) {counter}</h2>
    <h3>Groups Selected: {toppings_checkbox}</h3>
    <h3>Escaped cookie: {escaped_cookie}</h3>
    <br><br>
    You can try again:
    <form action="formhandler.py" method="post">
        Enter credentials to order 4-dimensional pizza<br>
        Username: <input type="text" name="username">
        Password: <input type="password" name="password">
        <br>
        <input type="radio" name="lang" value="en"> English
        <input type="radio" name="lang" value="ua"> Українська
        <br>
        <input type="checkbox" name="tomato" value="on"> Tomato
        <input type="checkbox" name="salami" value="on"> Salami
        <input type="checkbox" name="pineapple" value="on"> Pineapple
        <input type="checkbox" name="olives" value="on"> Olives
        <br>
        <input type="submit" value="Order">
        <input type="submit" name="delete_cookies" value="Delete Cookies">
    </form>
</body>
</html>
"""
print(template_html)
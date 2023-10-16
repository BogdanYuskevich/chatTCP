from wsgiref.simple_server import make_server
def app(enviroment, responce):
    status = "200 OK"
    headers = [("Content-type", "text/html; charset=utf-8")]
    responce(status,headers)

    return [b'<h1> my first WSGI</h1>']

with make_server("", 8000, app) as server:
    print("Server start on port 8000")
    server.serve_forever
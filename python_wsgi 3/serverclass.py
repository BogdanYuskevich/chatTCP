from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = b'Get response'
        self.wfile.write(message)

    def do_POST(self):
        .
with HTTPServer(("", 8000), Handler) as server:
    print("Server start on port 8000")
    server.serve_forever()
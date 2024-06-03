from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        # Determine the size of the data
        content_length = int(self.headers['Content-Length'])
        # Read the data (the request body)
        post_data = self.rfile.read(content_length)

        # Convert bytes to string if necessary and print it to the console
        print("Received POST data:", post_data.decode('utf-8'))

        # Respond to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()
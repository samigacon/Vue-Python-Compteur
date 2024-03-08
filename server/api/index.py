import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if data:
            compteur = int(data['compteur'])
            compteur += 1

            response = {
                "compteur": compteur,
                "echo": ["Le compteur a été incrémenté avec succès en Python"]
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(400, 'Le contenu de la requête n\'est pas au format JSON valide.')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello World')

def run_server():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Serveur démarré sur le port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

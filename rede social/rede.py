from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import json

# Listas para armazenar usuários e postagens
users = []
posts = []

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/register":
            # Processa o cadastro de usuários
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urlparse.parse_qs(post_data.decode('utf-8'))

            # Captura os dados do formulário
            name = data.get('name', [''])[0]
            email = data.get('email', [''])[0]

            # Adiciona o usuário à lista
            users.append({'id': len(users) + 1, 'name': name, 'email': email})

            # Redireciona para a página principal
            self.send_response(303)
            self.send_header('Location', '/social-network')
            self.end_headers()

        elif self.path == "/post":
            # Processa a criação de postagens
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urlparse.parse_qs(post_data.decode('utf-8'))

            user_id = data.get('user_id', [''])[0]
            content = data.get('content', [''])[0]

            if user_id.isdigit():
                posts.append({'user_id': int(user_id), 'content': content})

            self.send_response(303)
            self.send_header('Location', '/social-network')
            self.end_headers()

    def do_GET(self):
        if self.path == "/social-network":
            # Página principal da rede social
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("social_network.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))

        elif self.path == "/users":
            # Lista os usuários
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(users).encode("utf-8"))

        elif self.path == "/posts":
            # Lista as postagens
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(posts).encode("utf-8"))

PORT = 8082
httpd = HTTPServer(("", PORT), RequestHandler)
print(f"Server running on port {PORT}")
httpd.serve_forever()

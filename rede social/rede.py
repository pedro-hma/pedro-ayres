import http.server
import socketserver
import json

PORT = 8081

# Base de dados simulada
data = {
    "users": [],
    "posts": []
}

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            html_content = """
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <title>Rede Social</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        padding: 20px;
                        background-color: #f4f4f9;
                    }
                    h1, h2 {
                        color: #333;
                    }
                    form {
                        margin-bottom: 20px;
                    }
                    input, textarea {
                        width: 100%;
                        padding: 10px;
                        margin: 10px 0;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    button {
                        background-color: #007bff;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #0056b3;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #f2f2f2;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <h1>Bem-vindo à Social Network!</h1>
                <h2>Cadastrar Usuário</h2>
                <form action="/register_user" method="post">
                    <label>Nome:</label>
                    <input type="text" name="username" placeholder="Nome de usuário" required />
                    <label>Email:</label>
                    <input type="email" name="email" placeholder="Email do usuário" required />
                    <button type="submit">Cadastrar Usuário</button>
                </form>
                <h2>Cadastrar Postagem</h2>
                <form action="/register_post" method="post">
                    <label>ID do Usuário:</label>
                    <input type="text" name="author" placeholder="ID do usuário" required />
                    <label>Conteúdo:</label>
                    <textarea name="content" placeholder="Conteúdo da postagem" required></textarea>
                    <button type="submit">Criar Postagem</button>
                </form>
                <h2>Usuários Cadastrados</h2>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Email</th>
                        </tr>
                    </thead>
                    <tbody id="user-table"></tbody>
                </table>
                <h2>Postagens</h2>
                <table>
                    <thead>
                        <tr>
                            <th>ID do Usuário</th>
                            <th>Conteúdo</th>
                        </tr>
                    </thead>
                    <tbody id="post-table"></tbody>
                </table>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_data = json.loads(post_data.decode("utf-8"))

        if self.path == "/register_user":
            username = post_data.get("username")
            email = post_data.get("email")
            if username and email:
                user_id = len(data["users"]) + 1
                data["users"].append({"id": user_id, "username": username, "email": email})
                self.send_response(201)
                self.end_headers()
                self.wfile.write(json.dumps({"message": f"Usuário '{username}' cadastrado com sucesso!"}).encode("utf-8"))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Dados inválidos para o cadastro do usuário."}).encode("utf-8"))

        elif self.path == "/register_post":
            author = post_data.get("author")
            content = post_data.get("content")
            if author and content:
                data["posts"].append({"author": author, "content": content})
                self.send_response(201)
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Postagem cadastrada com sucesso!"}).encode("utf-8"))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Dados inválidos para o cadastro da postagem."}).encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode("utf-8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://127.0.0.1:{PORT}")
    httpd.serve_forever()

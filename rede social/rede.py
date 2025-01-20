from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Dados em memória para usuários e postagens
users = []
posts = []

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
    
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            html_content = f"""
            <html>
            <head>
                <title>Social Network</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f9f9f9;
                        color: #333;
                    }}
                    .container {{
                        width: 90%;
                        max-width: 1200px;
                        margin: 20px auto;
                        padding: 20px;
                        background: #fff;
                        border-radius: 8px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    }}
                    h1, h2 {{
                        color: #444;
                    }}
                    form {{
                        margin-bottom: 30px;
                    }}
                    form label {{
                        font-weight: bold;
                    }}
                    form input, form textarea, form button {{
                        display: block;
                        width: 100%;
                        margin-top: 5px;
                        margin-bottom: 15px;
                        padding: 10px;
                        font-size: 14px;
                        border: 1px solid #ddd;
                        border-radius: 4px;
                    }}
                    form button {{
                        background-color: #007BFF;
                        color: white;
                        cursor: pointer;
                        border: none;
                        transition: background 0.3s;
                    }}
                    form button:hover {{
                        background-color: #0056b3;
                    }}
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }}
                    th, td {{
                        border: 1px solid #ddd;
                        padding: 10px;
                        text-align: left;
                    }}
                    th {{
                        background-color: #f4f4f4;
                    }}
                    .section {{
                        margin-bottom: 40px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Bem-vindo à Social Network!</h1>

                    <div class="section">
                        <h2>Cadastrar Usuário</h2>
                        <form method="POST" action="/users">
                            <label for="name">Nome:</label>
                            <input type="text" id="name" name="name" required>
                            
                            <label for="email">Email:</label>
                            <input type="email" id="email" name="email" required>
                            
                            <button type="submit">Cadastrar Usuário</button>
                        </form>
                    </div>

                    <div class="section">
                        <h2>Cadastrar Postagem</h2>
                        <form method="POST" action="/posts">
                            <label for="user_id">ID do Usuário:</label>
                            <input type="number" id="user_id" name="user_id" required>
                            
                            <label for="content">Conteúdo:</label>
                            <textarea id="content" name="content" rows="4" required></textarea>
                            
                            <button type="submit">Criar Postagem</button>
                        </form>
                    </div>

                    <div class="section">
                        <h2>Usuários Cadastrados</h2>
                        <table>
                            <tr>
                                <th>ID</th>
                                <th>Nome</th>
                                <th>Email</th>
                            </tr>
                            {"".join(f"<tr><td>{i}</td><td>{u['name']}</td><td>{u['email']}</td></tr>" for i, u in enumerate(users, start=1))}
                        </table>
                    </div>

                    <div class="section">
                        <h2>Postagens</h2>
                        <table>
                            <tr>
                                <th>ID do Usuário</th>
                                <th>Conteúdo</th>
                            </tr>
                            {"".join(f"<tr><td>{p['user_id']}</td><td>{p['content']}</td></tr>" for p in posts)}
                        </table>
                    </div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode("utf-8"))
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)
    
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")
        data = {key: value for key, value in [item.split("=") for item in post_data.split("&")]}
        
        if self.path == "/users":
            user = {"name": data["name"], "email": data["email"]}
            users.append(user)
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
        elif self.path == "/posts":
            post = {"user_id": int(data["user_id"]), "content": data["content"]}
            posts.append(post)
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

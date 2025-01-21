import http.server
import socketserver
import requests

PORT = 8080

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Rede Social Simples</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 0; }
                    header { background: #4CAF50; color: white; padding: 1rem; text-align: center; }
                    ul { list-style: none; padding: 0; }
                    li { margin: 0.5rem 0; }
                    a { text-decoration: none; color: #4CAF50; }
                    a:hover { text-decoration: underline; }
                    form { margin-top: 1rem; }
                    input, button { padding: 0.5rem; margin: 0.5rem 0; }
                </style>
            </head>
            <body>
                <header>
                    <h1>Bem-vindo à Rede Social Simples</h1>
                </header>
                <main style="padding: 1rem;">
                    <ul>
                        <li><a href="/users">Listar Usuários</a></li>
                        <li><a href="/posts">Listar Postagens</a></li>
                        <li>
                            Buscar Tweets de um Usuário:
                            <form action="/tweets" method="get">
                                <input type="text" name="username" placeholder="Digite o username" />
                                <button type="submit">Buscar Tweets</button>
                            </form>
                        </li>
                    </ul>
                </main>
            </body>
            </html>
            """
            self.wfile.write(bytes(html, "utf8"))
        elif self.path == "/users":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<h1>Usuários cadastrados</h1>", "utf8"))
        elif self.path.startswith("/tweets"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            username = self.path.split("?username=")[-1]
            tweets = f"<h1>Tweets de {username}</h1>"
            self.wfile.write(bytes(tweets, "utf8"))
        else:
            self.send_response(404)
            self.end_headers()

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()

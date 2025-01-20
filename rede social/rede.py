import http.server
import urllib.parse
import requests

class SimpleSocialNetworkHandler(http.server.BaseHTTPRequestHandler):
    users = []
    posts = []

    def do_GET(self):
        if self.path == "/":
            html = """
            <html>
            <head><title>Rede Social Simples</title></head>
            <body>
                <h1>Bem-vindo à Rede Social Simples</h1>
                <ul>
                    <li><a href="/users">Listar Usuários</a></li>
                    <li><a href="/posts">Listar Postagens</a></li>
                    <li>Buscar Tweets de um Usuário:
                        <form action="/tweets" method="get">
                            <input type="text" name="username" placeholder="Digite o username" />
                            <button type="submit">Buscar Tweets</button>
                        </form>
                    </li>
                </ul>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        elif self.path == "/users":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(self.users).encode("utf-8"))
        elif self.path == "/posts":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(self.posts).encode("utf-8"))
        elif self.path.startswith("/tweets"):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            username = params.get("username", [None])[0]

            if username:
                tweets = self.fetch_tweets(username)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(str(tweets).encode("utf-8"))
            else:
                self.send_error(400, "Bad Request: Missing 'username' parameter")
        else:
            self.send_error(404, "Endpoint not found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        parsed_data = urllib.parse.parse_qs(post_data)

        if self.path == "/users":
            new_user = {
                "name": parsed_data.get("name", [None])[0],
                "email": parsed_data.get("email", [None])[0]
            }
            if new_user["name"] and new_user["email"]:
                self.users.append(new_user)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(str(new_user).encode("utf-8"))
            else:
                self.send_error(400, "Bad Request: Missing 'name' or 'email'")
        elif self.path == "/posts":
            new_post = {
                "title": parsed_data.get("title", [None])[0],
                "content": parsed_data.get("content", [None])[0]
            }
            if new_post["title"] and new_post["content"]:
                self.posts.append(new_post)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(str(new_post).encode("utf-8"))
            else:
                self.send_error(400, "Bad Request: Missing 'title' or 'content'")
        else:
            self.send_error(404, "Endpoint not found")

    def fetch_tweets(self, username):
        # Replace 'your_bearer_token' with your actual Twitter API Bearer Token
        bearer_token = "your_bearer_token"
        url = f"https://api.twitter.com/2/tweets/search/recent?query=from:{username}"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch tweets: {response.status_code}"}

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, SimpleSocialNetworkHandler)
    print("Servidor rodando na porta 8080...")
    httpd.serve_forever()
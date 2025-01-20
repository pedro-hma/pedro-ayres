from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
users = {}
posts = []
post_id_counter = 1

# Endpoint to register users
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    if username in users:
        return jsonify({'error': 'Username already exists'}), 400
    users[username] = {'username': username, 'posts': []}
    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint to create a post
@app.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.json
    username = data.get('username')
    content = data.get('content')
    image_url = data.get('image_url')

    if not username or username not in users:
        return jsonify({'error': 'Invalid username'}), 400
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    post = {
        'id': post_id_counter,
        'username': username,
        'content': content,
        'image_url': image_url,
        'likes': 0,
        'comments': []
    }
    posts.append(post)
    users[username]['posts'].append(post_id_counter)
    post_id_counter += 1

    return jsonify({'message': 'Post created successfully', 'post': post}), 201

# Endpoint to like a post
@app.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    post['likes'] += 1
    return jsonify({'message': 'Post liked successfully', 'likes': post['likes']}), 200

# Endpoint to comment on a post
@app.route('/posts/<int:post_id>/comment', methods=['POST'])
def comment_post(post_id):
    data = request.json
    comment = data.get('comment')

    if not comment:
        return jsonify({'error': 'Comment is required'}), 400

    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404

    post['comments'].append(comment)
    return jsonify({'message': 'Comment added successfully', 'comments': post['comments']}), 201

# Endpoint to list all posts
@app.route('/posts', methods=['GET'])
def list_posts():
    return jsonify({'posts': posts}), 200

# Root endpoint
@app.route('/')
def home():
    return jsonify({'message': 'Bem-vindo à mini-rede social! Use os endpoints adequados para interagir com a API.'})

if __name__ == '__main__':
    app.run(debug=True)

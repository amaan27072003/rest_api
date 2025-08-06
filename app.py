from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    1: {"username": "alice", "email": "alice@example.com"},
    2: {"username": "bob", "email": "bob@example.com"},
    3: {"username": "Mia", "email": "Mia@example.com"}
}
next_user_id = 3

@app.route('/')
def home():
    return "Welcome to the User Management API!"

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    global next_user_id
    new_user_data = request.get_json()
    if not new_user_data or 'username' not in new_user_data or 'email' not in new_user_data:
        return jsonify({"error": "Missing username or email"}), 400

    new_user = {
        "username": new_user_data['username'],
        "email": new_user_data['email']
    }
    users[next_user_id] = new_user
    new_user_id += 1

    return jsonify({"message": "User created successfully", "user_id": next_user_id - 1}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    update_data = request.get_json()
    if 'username' in update_data:
        user['username'] = update_data['username']
    if 'email' in update_data:
        user['email'] = update_data['email']
    
    return jsonify({"message": "User updated successfully", "user": user})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
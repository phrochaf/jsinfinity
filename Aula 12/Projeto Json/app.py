from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/books/*": {"origins": "*"}})
DATA_FILE = 'data.json'

def check_file_permissions(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return False
    if not os.access(file_path, os.R_OK):
        print(f"File {file_path} is not readable.")
        return False
    if not os.access(file_path, os.W_OK):
        print(f"File {file_path} is not writable.")
        return False
    return True

def read_books():
    if not check_file_permissions(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_books(books):
    if not check_file_permissions(DATA_FILE):
        return
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=2)

def validate_books(books):
    if not isinstance(books, list):
        return False
    for book in books:
        if 'nome' not in book:
            return False
    return True

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        books = read_books()
        return jsonify(books), 200
    elif request.method == 'POST':
        new_books = request.json
        if not validate_books(new_books):
            return jsonify({"error": "Invalid book data"}), 400
        write_books(new_books) 
        return jsonify(new_books), 201

if __name__ == '__main__':
    if check_file_permissions(DATA_FILE):
        print(f"File {DATA_FILE} exists and has the correct permissions.")
    else:
        print(f"File {DATA_FILE} does not have the correct permissions.")
    app.run(debug=True, port=5000)
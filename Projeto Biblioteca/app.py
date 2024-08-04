from Flask import Flask, request, jsonify
import json
import os


app = Flask(__name__)
DATA_FILE = 'data.json'

def read_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
        return []
    
def write_books(books):
    with open(DATA_FILE, 'w') as file:
        json.dump(books, file, indent=2)

@app.rout('/addBook', methods=['POST'])

def add_book():
    new_book = reques.json
    book = read_books()
    books.append(new_book)
    write_book(books)
    return jsonify({'message':'Livro adicionado com sucesso'}), 200

@app.route('/books', methods=['GET'])
def get_books():
    books = read_books()
    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/simulate')
def hello_world():
    try:
        return 'Hello, World!'
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro interno do servidor", 500

if __name__ == '__main__':
    app.run(debug=True)

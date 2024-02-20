from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  try:
    # Seu código aqui
    return 'Hello, World!'
  except Exception as e:
    print(f"Erro: {e}")
    return "Erro interno do servidor", 500

if __name__ == '__main__':
  app.run(debug=True)

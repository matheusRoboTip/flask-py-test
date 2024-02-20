from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    try:
        # Seu código aqui
        return "Hello Vercel"
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro interno do servidor", 500

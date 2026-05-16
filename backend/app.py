from flask import Flask

app = Flask(__name__)

@app.route('/') #criar rota pelo URL q eu vou colocar
def home():
    return {
        "mensagem": "ATLASEDU API ta funcionando"
    }

if __name__ == "__main__":
    app.run(debug=True)
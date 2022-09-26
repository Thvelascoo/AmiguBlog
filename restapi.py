from flask import Flask
from dogs import get_dogs
from cats import get_cats

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def homepage():
    return "Bem Vindo a API de amigurumis! Use as rotas /cats ou /dogs dependendo do link que você queira ver!"

@app.route("/cats")
def cats():
    cat = get_cats()
    return cat

@app.route("/dogs")
def dogs():
    dog = get_dogs()
    return dog

if __name__ == "__main__":
    app.run(debug=True)
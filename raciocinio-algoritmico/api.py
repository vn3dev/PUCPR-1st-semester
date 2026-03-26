from flask import Flask
from routes.doadores import doadores_bp
from routes.bolsas import bolsas_bp

app = Flask(__name__)

# mantem a ordem dos atributos na hora de exibir o json pq sou fresco
app.json.sort_keys = False

# registra os blueprints
app.register_blueprint(doadores_bp)
app.register_blueprint(bolsas_bp)

app.run(debug = True)

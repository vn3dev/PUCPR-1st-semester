from flask import Flask
from doadores import doadores_bp
from sangue import sangue_bp

app = Flask(__name__)

# mantem a ordem dos atributos na hora de exibir o json pq sou fresco
app.json.sort_keys = False

# registra os blueprints
app.register_blueprint(doadores_bp)
app.register_blueprint(sangue_bp)

app.run(debug = True)
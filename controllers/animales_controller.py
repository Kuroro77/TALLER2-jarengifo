from flask import Blueprint, render_template, jsonify
from models.huron import Huron
from models.boa import Boa

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    return jsonify({
        "mensaje": 'Prueba Api',
        "code": 200
    })

@home_blueprint.route("/api/huron")
def api_huron():
    data_huron = Huron('Hugo', 56.2, 2, 'Peru', 0.67)
    sonido_huron = data_huron.hacer_sonido()

    return jsonify({
        "mensaje": f'El huron hace {sonido_huron}',
        "code": 200
    })

@home_blueprint.route("/huron")
def huron():
    data_huron = Huron('Hugo', 56.2, 2, 'Peru', 0.67)
    sonido_huron = data_huron.hacer_sonido()
    mensaje = f'El huron hace {sonido_huron}'

    return render_template("index.html", sonido=mensaje)

@home_blueprint.route("/api/boa")
def api_boa():
    data_boa = Boa('Pedro', 128.0, 5, 'Colombia', 1.25, 0)
    sonido_boa = data_boa.hacer_sonido()

    return jsonify({
        "mensaje": f'La boa hace {sonido_boa}',
        "code": 200
    })

@home_blueprint.route("/boa")
def boa():
    data_boa = Boa('Pedro', 128.0, 5, 'Colombia', 1.25, 0)
    sonido_boa = data_boa.hacer_sonido()
    mensaje = f'La boa hace {sonido_boa}'

    return render_template("index.html", sonido=mensaje)
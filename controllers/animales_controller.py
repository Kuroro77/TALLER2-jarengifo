from flask import Blueprint, render_template, jsonify
from models.huron import Huron

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
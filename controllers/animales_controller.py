from flask import Blueprint, render_template, jsonify

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    return jsonify({
        "mensaje": 'Prueba Api',
        "code": 200
    })
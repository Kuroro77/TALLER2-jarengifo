from flask import Flask
from config.routes import register_routes

app = Flask(__name__, template_folder="views")

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
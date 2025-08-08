# __init__.py
from flask import Flask
from app.routes.analyze import analyze_bp
from app.routes.health import health_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(health_bp)
    return app

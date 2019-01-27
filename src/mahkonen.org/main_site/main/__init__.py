from flask import Flask

def create_app():
    app = Flask(__name__)

    from main.home.routes import home
    from main.admin.routes import admin
    app.register_blueprint(home)
    app.register_blueprint(admin)

    return app

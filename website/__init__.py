import os

from flask import Flask, render_template
# from flask_scss import Scss
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    Bootstrap(app)
    # Scss(app)
    CSRFProtect(app)

    @app.route('/')
    def index():
        return render_template('about.html')

    @app.route('/ping')
    def success():
        return "Success!"

    return app

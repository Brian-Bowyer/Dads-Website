import os

from flask import Flask, render_template
# from flask_scss import Scss
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
    app = Flask(__name__)

    Bootstrap(app)
    # Scss(app)

    @app.route('/')
    def index():
        return render_template('about.html')

    @app.route('/ping')
    def success():
        return "Success!"

    return app

from flask import Flask
from midi_generator.api.view import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')
from flask import Blueprint
from flask import request
from flask import abort

from midi_generator.midi_extender.generator import generate

api = Blueprint('api', __name__)


@api.route('/', methods=['POST'])
def get_midi_string():
    raw_data = request.stream.read()

    if raw_data is None:
        abort(400)
    print(raw_data)
    buffer = raw_data
    raw_data = generate(buffer, 2500)
    return raw_data

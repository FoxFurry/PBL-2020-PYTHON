from flask import Blueprint
from flask import request

import json
from midi_generator.midi_extender.jsonUtil import intArrayToString
from midi_generator.midi_extender.generator import generate

api = Blueprint('api', __name__)


@api.route('/', methods=['POST'])
def get_midi_string():
    raw_data = request.get_data(as_text=True)
    json_data = json.loads(raw_data)
    print(json_data)

    gen_len = json_data["generateLen"]
    text_source = intArrayToString(json_data)

    print(gen_len)
    print(text_source)

    temp = generate(text_source, int(gen_len))
    return temp

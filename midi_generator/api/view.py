from flask import Blueprint
from flask import request
from flask import abort

import json

from midi_generator.midi_extender.generator import generate

api = Blueprint('api', __name__)


@api.route('/', methods=['POST'])
def get_midi_string():
    raw_data = request.get_data(as_text=True)
    #dict = json.loads(raw_data, strict=False)
    dict = eval(raw_data)
    if "source" not in dict or "generateLen" not in dict:
        abort(400)

    text_source = dict["source"]
    gen_len = dict["generateLen"]
    temp = generate(text_source, int(gen_len))
    return temp

import json
from typing import Optional


CONFIG_FILE = 'test.json'


def get_id(conf_name: str=CONFIG_FILE) -> Optional[int]:
    """Return the user id from conf_fname, or None
    if it hasn't been set yet.

    Precondition:
        Valid JSON-encoded dictionary at conf_name
    """
    with open(conf_name, 'r') as fobj:
        data = json.load(fobj)

    uid = data.get('id')

    assert uid is None or isinstance(uid, int), \
        'The user id must be an integer if it exists'

    return uid

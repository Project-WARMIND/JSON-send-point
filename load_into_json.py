import json
import string
import random

from test_dicts import (
    OS_DETECTION,
    EXPLOIT
)


def send_to_api():
    # have to wait for a way to access the API first
    pass


def random_filename(length=7):
    retval = []
    file_path = "/tmp"
    acceptable = string.ascii_letters
    for _ in range(length):
        retval.append(random.choice(acceptable))
    return "{}/{}.json".format(file_path, ''.join(retval))


def parse_sent_items(*args):
    retval = {}
    for i, item in enumerate(args):
        retval[i] = item
    return retval


print parse_sent_items(OS_DETECTION, EXPLOIT)
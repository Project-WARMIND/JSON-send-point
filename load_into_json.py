import os
import json
import string
import random

from test_dicts import (
    OS_DETECTION,
    SUCCESSFUL_EXPLOIT,
    UNSUCCCESSFUL_EXPLOIT,
    EXPECTED_FAILED_OUTPUT,
    EXPECTED_SUCCESSFUL_OUTPUT
)


JSON_DATA_FILE_PATH = "{}/etc".format(os.getcwd())


def clean_files(files, main_dir):
    try:
        for f in files:
            os.remove(f)
        os.remove(main_dir)
        return True
    except Exception:
        return False


def send_to_api():
    # have to wait for a way to access the API first
    pass


def random_filename(filepath, length=7):
    retval = []
    acceptable = string.ascii_letters
    for _ in range(length):
        retval.append(random.choice(acceptable))
    return "{}/{}.json".format(filepath, ''.join(retval))


def jsonize(data, filepath, key):
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    json_filename = random_filename(filepath)
    with open(json_filename, "a+") as temp_json_file:
        jsonized_data = json.dumps({key: data})
        temp_json_file.write(jsonized_data)
    return json_filename


def merge_json_data(filenames, dest_dir):
    out_filename = random_filename(dest_dir)
    results = []
    for f in filenames:
        with open(f, "rb") as data:
            results.append(json.load(data))
    with open(out_filename, "a+") as merged:
        merged.write(json.dumps(results, sort_keys=True, indent=4))
    return out_filename


files = [
    jsonize(OS_DETECTION, JSON_DATA_FILE_PATH, "detected system"),
    jsonize(SUCCESSFUL_EXPLOIT, JSON_DATA_FILE_PATH, "exploit status")
]
out_file = merge_json_data(files, JSON_DATA_FILE_PATH)

"""
This file is apart of project WARMIND (https://github.com/Project-WARMIND)
it will be used in conjunction with the project and is licensed under GPUv3.

You can see the license here https://github.com/Project-WARMIND/AISploit-Whitepaper/blob/master/LICENSE

This file will be used as a send point between the API, OS detection, and exploit statuses
"""

import os
import sys
import json
import string
import random
import shutil

from test_dicts import (
    OS_DETECTION,
    SUCCESSFUL_EXPLOIT,
    UNSUCCCESSFUL_EXPLOIT,
    EXPECTED_FAILED_OUTPUT,
    EXPECTED_SUCCESSFUL_OUTPUT
)


# the path that will be used to store the temporary JSON data
JSON_DATA_FILE_PATH = "{}/.tmp".format(os.getcwd())


def clean_files(path):
    """
    clean a tree of folders, mimics the `rm -rf` command
    """
    return shutil.rmtree(path)


def random_filename(filepath, length=7):
    """
    create a random filename, this shouldn't cause any problems because
    they files will be deleted after used
    """
    retval = []
    acceptable = string.ascii_letters
    for _ in range(length):
        retval.append(random.choice(acceptable))
    return "{}/{}.json".format(filepath, ''.join(retval))


def jsonize(data, filepath, key):
    """
    jsonize data by pulling a dict and adding it to a temp JSON file
    """
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    json_filename = random_filename(filepath)
    with open(json_filename, "a+") as temp_json_file:
        jsonized_data = json.dumps({key: data})
        temp_json_file.write(jsonized_data)
    return json_filename


def merge_json_data(filenames, dest_dir):
    """
    merge multiple JSON files into a single file
    """
    out_filename = random_filename(dest_dir)
    results = []
    for f in filenames:
        with open(f, "rb") as data:
            results.append(json.load(data))
    with open(out_filename, "a+") as merged:
        merged.write(json.dumps(results, sort_keys=True, indent=4))
    return out_filename


def send_to_api(url, data):
    # have to wait for a way to access the API first
    pass


def main(exploit_status, os_detection, test=False):
    """
    main function
    """
    files_to_merge = []
    keys = {"exploit status": exploit_status, "detected system": os_detection}
    for key in keys.keys():
        files_to_merge.append(jsonize(keys[key], JSON_DATA_FILE_PATH, key))
    # merge all the files into a singular file
    out_file = merge_json_data(files_to_merge, JSON_DATA_FILE_PATH)
    with open(out_file, 'rb') as _data:
        # this is the data we will send to the API in a POST?
        send_data = json.loads(_data.read())
    # cleans the temp JSON files so they don't exist anymore
    clean_files(JSON_DATA_FILE_PATH)
    if test:
        print(send_data)
    send_to_api("", send_data)


if __name__ == "__main__":
    # to see the test data you will need to add `test` into the argv
    # python2/3 load_into_json.py test it will then print out the send data
    if "test" in sys.argv:
        main(SUCCESSFUL_EXPLOIT, OS_DETECTION, test=True)
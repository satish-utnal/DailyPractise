"""

Read given metadata contain file and convert it to json file

"""

import csv
import json


def convert_csv_to_json(input_file, output_file):
    """
    :param input_file:  receive input file name
    :param output_file: filename to create
    :return: nothing
    """
    tags = []
    with open(input_file, 'r') as file:
        key_val_pair = csv.DictReader(file)
        for row in key_val_pair:
            tags.append(row)

    with open(output_file, 'w') as file:
        json.dump(tags, file, indent=4)


FILE_TO_PROCESS = "../data/metadata.csv"
FINAL_FILE = "../data/metadata.json"
convert_csv_to_json(FILE_TO_PROCESS, FINAL_FILE)

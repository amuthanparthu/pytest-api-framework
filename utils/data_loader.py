import csv
import json

def load_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def load_json(path):
    with open(path) as f:
        return json.load(f)

import json


def load_careers_data():
    with open("data/careers.json", "r", encoding="utf-8") as file:
        return json.load(file)
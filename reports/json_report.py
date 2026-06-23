import json

def export_json(bugs, filename="output/report.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(bugs, file, indent=4)
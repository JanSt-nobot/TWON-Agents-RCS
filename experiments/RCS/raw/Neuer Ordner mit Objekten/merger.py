import json
import glob

python_objects = []

for json_file in glob.glob("*.json"):
    with open(json_file, "r") as f:
        python_objects.append(json.load(f))

with open("combined.json", "w") as f:
    json.dump(python_objects, f, indent=4)

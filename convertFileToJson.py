import json
import sys
str_data = "jsonFormat.txt"
dict1 = {}
try:
    with open(str_data) as fh:
        for line in fh:
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip()
    output = open("JsonConverted.json", "w")
    json.dump(dict1, output, indent=4, sort_keys=False)
    output.close()
except:
    print(sys.exc_info())
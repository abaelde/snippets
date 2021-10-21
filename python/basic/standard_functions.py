
# Deal with json files
https://docs.python.org/fr/3/library/json.html

import json

with open(file_path, 'w') as json_file:
    json.dump(data_dict, json_file)
        
with open(file_path) as json_file:
    saved_data = json.load(json_file)    




# Deal with json files
https://docs.python.org/fr/3/library/json.html

import json
from traceback import format_exc

with open(file_path, 'w') as json_file:
    json.dump(data_dict, json_file)
    
# Paramètres à connaitre
- indent=
- default= 
- sort_keys= 
    
Cas de json.dumps() : Utilisé pour imprimer une string mais pas pour export sous forme 
de fichiers.   
https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python
        
with open(file_path) as json_file:
    saved_data = json.load(json_file)    



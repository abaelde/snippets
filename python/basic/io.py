


import json
import joblib
from traceback import format_exc


#-----------JOBLIB-----------
# TODO test with context manager
# https://joblib.readthedocs.io/en/latest/generated/joblib.dump.html

#---
joblib.dump(value,
            filename, 
            compress=0,
            protocol=None,
            cache_size=None)
#---
joblib.load(filename,
            mmap_mode=None)



#-----------JSON-------------
# Deal with json files
# https://docs.python.org/fr/3/library/json.html

#---
with open(file_path, 'w') as json_file:
    json.dump(data_dict,
              json_file,
              skipkeys=False,
              ensure_ascii=True,
              check_circular=True,
              allow_nan=True,
              cls=None,
              indent=None,
              separators=None,
              default=None,
              sort_keys=False,)
    
    
Cas de json.dumps() : Utilisé pour imprimer une string mais pas pour export sous forme 
de fichiers.   
https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python

#---
with open(file_path) as json_file:
    saved_data = json.load(json_file,
                           cls=None, 
                           object_hook=None,
                           parse_float=None,
                           parse_int=None,
                           parse_constant=None,
                           object_pairs_hook=None)    



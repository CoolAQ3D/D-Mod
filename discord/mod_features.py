
import os, json

#Saves Sesison
def save_session_id(new_session_id):
  settings = read_json("config.json")
  settings["Session ID"] = new_session_id

  write_json("config", settings)
  


#Save Files

def write_json(file_path, data):
  file_path = file_path_finder('config', '.json')
  with open(file_path, 'w') as outfile:
      json.dump(data, outfile, indent=2)

def read_json(file_path):
  file_path = file_path_finder('config', '.json')
  f = open(file_path)
  data = json.load(f)
    
  return data


def file_path_finder(file_name, extension):
  file_location = os.path.join(os.path.dirname(__file__), f'{file_name}') + f'{extension}'

  return file_location

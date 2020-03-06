import os
import sys
import xml.etree.ElementTree as ET

# Singleton Config
config = None

def get(key):
    if key == None or config == None or config.get(str(key)) == None:
        print("Invalid config get request: " + str(key))
        sys.exit(1)
    
    return config.get(str(key))

# Generalized config generator. parser_func is responsible with returnning a valid config object
def generate_config(config_path, parser_func):
    global config

    if config_path != None and os.path.isfile(config_path):
        tree = ET.parse(config_path)
        if tree == None:
            return False
        root = tree.getroot()
        if root == None:
            return False

        # Read config xml
        try:
            config = parser_func(root)
        except Exception as e:
            print("Config exception: {0}".format(e))
            return False

        return True
        
    return False
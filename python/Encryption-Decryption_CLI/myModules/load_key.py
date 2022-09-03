import json;

def enc_load(key, *args):
    filename = args[1]
    if key and key['file'] == filename:
        print('The key already loaded')
    else:
        try:
            with open(filename, 'r') as f:
                key = json.load(f)
        except FileNotFoundError:
            print("No such key")
        except:
            print("Something went wrong while opening the file")
    return key




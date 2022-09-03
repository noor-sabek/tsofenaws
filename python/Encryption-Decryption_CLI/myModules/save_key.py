#saving the new key 
import json


def enc_save(key, *args):
    filename = args[1]
    if key:
        try:
            key['file'] = filename
            with open(filename, "w") as fp:
                json.dump(key,fp)
            print('Enc/Dec keys saved in '+filename+' file')
        except:
            key['file'] = False
            print("Something went wrong while saving the file")
    else:
        print('No such Key')
    return key

    
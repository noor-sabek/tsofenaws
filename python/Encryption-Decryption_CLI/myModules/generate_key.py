import random
import string

def enc_newkey(key, *args):
    if key and key['file'] is False:
        print('Are you sure you want to override the current UNSAVED key named ('+key['keyname']+') ?!')
        cmd_str = input('subs (y,n)>')
        cmd = cmd_str.split()
        if cmd[0] == 'n':
            return key
    keyname = args[1];

    letters = string.ascii_lowercase;
    letters_list = list(letters);
    random.shuffle(letters_list);
    shuffled = ''.join(letters_list);



    enckey = {letters[i]:shuffled[i] for i in range(len(letters))};
    deckey = {list(enckey.values())[i]:list(enckey.keys())[i] for i in range(len(enckey))};
    print(enckey)
    print('')
    sorted_deckey = dict(sorted(deckey.items()));
    print(deckey);
    
    print('A new key : '+keyname+' was created.')
    return {'keyname': keyname, 'keyvalue': shuffled,'file': False , 'enckey': enckey, 'deckey': sorted_deckey}


def enc_info(key, *args):
    if key:
        print('Current key: ', key['keyname'])
        print('key value: ',key['keyvalue'])
        print('State: saved in ' + key['file'] if key['file'] else 'State: not saved')
        print('Encryption:')
        print( ''.join(key['enckey'].keys()) )
        print( ''.join(key['enckey'].values()) )
        print('Decryption:')
        print( ''.join(key['enckey'].keys()) )
        print( ''.join(key['deckey'].values()) )
    else:
        print('No key')
    return key



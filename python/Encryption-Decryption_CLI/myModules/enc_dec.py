#enc to dec 
#OR
#dec to enc 
def enc_dec_file(key, *args):
    method = args[0]
    txtfile = args[1]
    encfile = args[2]
    
    if key:
        try:
            with open(txtfile, 'r') as fr:
                lines = [ line.strip() for line in fr.readlines()]
                with open(encfile, 'w') as fw:
                    for line in lines:
                        for ch in line:
                                if ch in key[method+'key'].keys():
                                    fw.write(key[method+'key'][ch])
                                else:
                                    fw.write(ch)
                        fw.write("\n")
        except FileNotFoundError:
            print('File not found.')
        except:
            print('Please try again.')
    else:
        print('Encryption Key not found, Kindly add a key first to encrypt the file .')

    return key
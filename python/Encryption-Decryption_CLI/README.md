
We'll create a program that can:

    create encryption keys, convert them to decryption keys
    save and load keys to files (ex:  my-key.key)
    accept a clear-text file and encrypt it using an encryption key
    Accept an encrypted file, and decrypt.

There is always the "current key"  (the created, or loaded key)
You should write a CLI (command line interface) that a user can use to support all of these actions (see example file).
Programming instructions:

    Create a directory called "enc" under python
    Write a modular program, with different modules for specific tasks; For example:
    - an subs module to handle the cli
    - enckey file to handle the creation of keys
    Your main file should be called subs.pi
    All code should be placed inside functions, except ONE line that should call the entry function
    Small functions, each function should do just ONE thing, good and meaningful names....
    You cannot submit files, your code should be in your git repository,



subs>
subs>
subs>newkey my-key
A new key called my-key was created
subs>
subs>save key1
Enc/Dec keys saved in key1 file
subs>
subs>load other
No such key
subs>
subs>load other1
Key my-other from file other1 loaded
subs>
subs>enc text1.txt enc.txt
File text1.txt was encrypted into enc.txt
subs>
subs>dec enc.txt clear.txt
File enc.txt was decrypted into clear.txt
subs>
subs>info
Current key: my-other
state: saved in other1
Encryption:
  abcdefghijklmnopqrstuvwxyz
  rzat.....
Decryption:
  abcdefghijklmnopqrstuvwxyz
  c ...            a d     b
subs>
subs>newkey key3
A new key called key3 was created
subs>info
Current key: key3
state: not saved
Encryption:
  abcdefghijklmnopqrstuvwxyz
  rzat.....
Decryption:
  abcdefghijklmnopqrstuvwxyz
  c ...            a d     b
subs>
subs>
subs>done
osboxes$
osboxes$
osboxes$








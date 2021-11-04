import pyperclip as pc
import sys

passwords = {
    "github": 'yourPass',
    "email": 'yourPass',
    "gmail": 'yourPass'
            }

def findpass(name):
    try:
        pc.copy(passwords[name])
        print(f'Password of "{name}" copied to clipboard.')
    except KeyError:
        print('Key Not Found!')

findpass(sys.argv[1])

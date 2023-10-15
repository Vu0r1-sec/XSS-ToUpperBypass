#!/bin/python

import sys

def encode_string(string_to_encode, config):
    oldLen = 0
    encoding = string_to_encode
    while len(encoding) != oldLen :
        oldLen = len(encoding)
        for key, value in config.items():
            encoding = encoding.replace(key, value)

    return encoding

def main(string):
    dictionary = {
        "a": '(![]+{})[1]',
        "b": '([]+{})[2]',
        "c": '([]+{})[5]',
        "d": '([][1]+[])[2]',
        "e": '([]+{})[4]',
        "f": '([][1]+[])[4]',
        "g": '([0]+[""][0][c+o+n+s+t+r+u+c+t+o+r])[15]',
        "h": '(17)[t+o+"S"+t+r+i+n+g](36)',
        "i": '([][1]+[])[5]',
        "j": '([]+{})[3]',
        "k": '(20)[t+o+"S"+t+r+i+n+g](36)',
        "l": '(![]+[])[2]',
        "m": '(22)[t+o+"S"+t+r+i+n+g](36)',
        "n": '([][1]+[])[1]',
        "o": '([]+{})[1]',
        "p": '(25)[t+o+"S"+t+r+i+n+g](36)',
        "q": '(26)[t+o+"S"+t+r+i+n+g](36)',
        "r": '(!![]+[])[1]',
        "s": '(![]+[])[3]',
        "t": '([]+{})[6]',
        "u": '([][1]+[])[0]',
        "v": '(31)[t+o+"S"+t+r+i+n+g](36)',
        "w": '(32)[t+o+"S"+t+r+i+n+g](36)',
        "x": '(33)[t+o+"S"+t+r+i+n+g](36)',
        "y": '(34)[t+o+"S"+t+r+i+n+g](36)',
        "z": '(35)[t+o+"S"+t+r+i+n+g](36)'
    }

    print("Result :")
    print(encode_string(string, dictionary))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} '<string to encode>'")
        sys.exit(1)

    main(sys.argv[1])

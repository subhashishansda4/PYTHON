# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:28:12 2022

@author: VAGUE
"""

from morse_codes import codes

# using dictionary comprehension
# found it on stackoverflow - https://stackoverflow.com/a/32094652
CODE_REVERSED = {value:key for key,value in codes.items()}

def to_morse(s):
    return ' '.join(codes.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

# extracting each character from a word and matching it with its corresponding morse code
# adding 1 space between every character and '/' between every word
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += codes[letter] + ' '
        else:
            cipher += '/ '
    return cipher

# extracting characters from the given string till a space
# adding corresponding english alphabets to a variable that will store the result
# after getting two spaces, we will add space to our variable containing the decoded string
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(codes.keys())[list(codes.values()).index(citext)]
                citext = ''
                
    return decipher

# temporary message for encryption and decryption
def main():
    to_morse('hello')
    from_morse('.... . .-.. .-.. ---')
    
    message = "Decision defines Destiny"
    result = encrypt(message.upper())
    print(result)
    
    message = "-.. . -.-. .. ... .. --- -. / -.. . ..-. .. -. . ... / -.. . ... - .. -. -.-- "
    result = decrypt(message)
    print(result)
    
if __name__ == "__main__":
    main()
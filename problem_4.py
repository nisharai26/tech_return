# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:57:37 2020

@author: nisharai
"""

import string
def pig_it(text):
    pig_latin = ''
    length = len(text)
    cursor = 0

    if length < 1:
        return text

    for i in range(length):
        if text[i] in string.punctuation or text[i].isspace():
            if i != cursor:
                pig_latin = pig_latin + text[cursor + 1:i] + text[cursor] + 'ay' + text[i]
            # don't pig latin symbols
            else:
                pig_latin = pig_latin + text[i]
            cursor = i + 1

        # consider last word
        elif i == length - 1:
            pig_latin = pig_latin + text[cursor + 1:i + 1] + text[cursor] + 'ay'

    return pig_latin + '\n'

print(pig_it('Hello World !'))



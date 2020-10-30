# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:53:48 2020

@author: nisharai
"""

def wave(people):
    wave_arr=[]
    for i in range(len(people)):
        people=people.lower()
        each_word=list(people)
        if each_word[i].isalpha():
            each_word[i]=people[i].upper()
            people =''.join(each_word)
            wave_arr.append(people)
            
    return wave_arr

print(wave("hello"))
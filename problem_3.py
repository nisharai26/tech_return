# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:24:11 2020

@author: nisharai
"""

def row_weights(array):
    l=len(array)
    arr1=[];arr2=[]
    s1=0;s2=0
    for i in range(l):
        if i%2==0:
           arr1.append(array[i]) 
           s1=s1+array[i]
        else:
            arr2.append(array[i])
            s2=s2+array[i]
    print("Team 1 :", arr1,"\nTeam 2 :",arr2)
    print("The total weight of team 1:",s1)
    print("The total weight of team 2:",s2)
    

row_weights([50,60,70,80])
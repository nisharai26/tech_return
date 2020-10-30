# tech_return


import numpy as np
def repeats(arr):
    ar1=[]
    a1=0;a2=0;a3=0
    arr1=np.sort(arr)
    l= len(arr)
    print(arr1)
    if arr1[0] != arr1[1]:
        a1=arr1[0]      
    if arr1[l - 2] != arr1[l - 1]:
       a3=arr1[l-1]  
    for i in range(1, l - 1):
        if (arr1[i] != arr1[i + 1] and arr1[i] != arr1[i - 1]):
            a2=a2+arr1[i]
            ar1.append(arr1[i])
           
    s=a1+a2+a3
    print("Sum of non repated number is :", s)
    print("Non repeated numbers :",[ a1, *ar1, a3])
   
 
arr=[4,5,7,5,4,8]
repeats(arr) 

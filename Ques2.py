# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:00:29 2023

@author: donac
"""
import math
def cal_weight(num):
    weight = 0
    if (math.sqrt(num)).is_integer():
        weight=5
    elif (num%4==0 and num%6==0):
        weight=4
    elif (num%2==0):
        weight=3
    return weight
        
def weight_sort(nums):
    weighted_num=[]
    for num in nums:
        weight=cal_weight(num)
        weighted_num.append((num,weight))
    weighted_num.sort(key=lambda x:x[1])
    return weighted_num
        
nums=[10,36,54,89,12]
weighted_num=weight_sort(nums)

result_str=" "
for num,weight in weighted_num:
    result_str=result_str+f"<{num},{weight}>"
print(result_str)
    
    
    
    
    
    
    
    
 



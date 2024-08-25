#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:41:37 2024

@author: trongg
"""

#đếm nút biển số xe 5 số
def dem_nut_bien_so(num):
    a,b,c,d,e =map(int , num.split(":"))
    sum=((a+b+c+d+e)%10)
    return sum
num= input("nhập số ở hàng cuối cùng theo định dạng x:x:x:x:x nhé ")
sum = dem_nut_bien_so(num)
print(f"Biển số {num} có số nút là {sum} nút.")
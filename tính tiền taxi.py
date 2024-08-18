#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:53:09 2024

@author: trongg
"""

#tính tiền taxi
km=float(input("KM đã đi là :"))
m=float=0
if km<=1:
    m=km *20
if 1<km<=3:
    m=km*13
if 3<km<8:
    m=km*12
if 8<km:
    m=km*10
print("Tiền phải trả là :" ,m) 

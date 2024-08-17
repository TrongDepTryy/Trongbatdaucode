#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:14:28 2024

@author: trongg
"""

a = float(input( "Hãy nhập số thứ 1 vào nhé : "))
b = float(input("Hãy nhập số thứ 2 vào nhé :"))
c = float(input("Hãy nhập số thứ 3 vào nhé :"))
d = float(input("Hãy nhập số thứ 4 vào nhé :"))
f=a
if a>b :
    f=b
if b>c:
    f=c
if c>d:
    f=d
print(f"số lớn nhất trong đám này là :{f}")
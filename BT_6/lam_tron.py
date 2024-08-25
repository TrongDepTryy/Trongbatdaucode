#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:01:14 2024

@author: trongg
"""

a = float(input( "Hãy nhập số thứ 1 vào nhé : "))
b = float(input("Hãy nhập số thứ 2 vào nhé :"))

tong= a+b
hieu= a-b
tich=a*b
thuong=a/b
lamtron = thuong
lamtron2 = round(lamtron, 2)
lamtron3 = round(lamtron, 3)
print("Tổng , hiệu ,tích sẽ lần lượt là : ",[tong],[hieu],[tich])
print("Thương được làm tròn lần lượt 2 và 3 chữ số là : ",lamtron2)
print("và",lamtron3)
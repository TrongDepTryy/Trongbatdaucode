#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:54:35 2024

@author: trongg
"""
print("Tìm một loại tam giác cho banj")
a=float(input("Hãy nhập điểm A của bạn vào :"))
b=float(input("Hãy nhập điểm b của bạn vào :"))
c=float(input("Hãy nhập điểm của bạn vào :"))
if a+b>c and a+c>b and c+b>a:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b :
        print("Đây là tam giác zuôngggggg")
    if a==b or b==c :
         print("Đây là tam giác đều")
    if a==b or b==c or c==a:
        print("Đây là tam giác c")
    if a*a>b*b+c*c or b*b>a*a+c*c or c*c >a*a+b*b:
        print("Đây là tam giác tù")
else:
    print("đây là tm giác thường")
     
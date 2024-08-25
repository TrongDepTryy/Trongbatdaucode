#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:18:32 2024

@author: trongg
"""
a = float(input( "Hãy nhập số a vào nhé : "))
b = float(input("Hãy nhập số b  vào nhé :"))
c = float(input("Hãy nhập số c  vào nhé :"))
d=(b*b)- 4*a*c
if d==0:
    k= -b/2*a
    print("PT kép là :",k)
elif d >0 :
    n1=(-b + d**0.5) / (2*a)
    n2=(-b - d**0.5) / (2*a)
    print(f"PT có 2 nghiệm {n1} và {n2}.")
if d <0 :
    print("PT vô nghiệm")
    
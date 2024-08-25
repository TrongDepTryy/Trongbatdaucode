#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:25:59 2024

@author: trongg
"""
import math

a=float(input("Nhập số thứ nhất vào nhé : "))
b=float(input("Nhập số thứ hai vào nữa là xong  : "))
s = ((a+b) / (((math.pow(a,1/3)) + (math.pow(b,1/3)) - (math.pow((a*b),1/3))) / ((math.pow(a,1/2)) * (math.pow(2,(math.pow(a,1/2)))))))
print(s)
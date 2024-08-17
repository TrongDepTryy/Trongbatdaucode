#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:25:59 2024

@author: trongg
"""

a=float(input("Nhập số thứ nhất vào nhé : "))
b=float(input("Nhập số thứ hai vào nữa là xong  : "))
s = ((a+b) / (((a**(1/3)) + (b**(1/3)) - ((a*b)**(1/3))) / ((a**(1/2)) * (b**(1/2)))**2))
print(s)
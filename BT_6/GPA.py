#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:40:14 2024

@author: trongg
"""
a=float(input("Hãy nhập điểm GPA của bạn vào :"))
if a<3.5:
    print("Bạn loại Kém")
if 3.5<a<5:
    print("Bạn loại Yếu")
if 5<a<7:
    print("Bạn loại TB")
if 7<a<8:
    print("Bạn loại Khá")
if 8<a<9:
    print("Bạn loại Giỏi")
if 9<a<=10:
    print("Bạn loại Xuất sắc")
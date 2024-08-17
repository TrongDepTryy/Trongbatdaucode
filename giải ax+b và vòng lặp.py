#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:54:40 2024

@author: trongg
"""
while True:
    a = float(input( "Hãy nhập số thứ 1 vào nhé : "))
    b = float(input("Hãy nhập số thứ 2 vào nhé :"))
    if -0.9999999<a>0.0000000001:
        print("phương trình  có nghiệm duy nhất x = -b/a" )
        x=-b/a 
        print( x)
    if a==0 :
        if b ==0:
            print ("đi khắp thể gian, không ai tìm được x (vì nó không tồn tại)")
        elif -0.9999999<b>0.0000001:
            print("phương trình có vô số nghiệm")
    user_input = input("bấm phím bất kì để tiếp tục tính hoặc nhập trongdeptrai để thoát: ")
    if user_input == 'trongdeptrai':
        break
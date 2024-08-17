#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:57:04 2024

@author: trongg
"""
h=float(input("Hãy nhập chiều cao của bạn  nhé, đơn vị là mét nhé: "))
w=float(input("Hãy nhập cân nặng của bạn  nhé, đơn vị là kg nha: "))
bmi= float=(w/(h*h))
print(f"Chỉ số BMI của bạn là : {bmi}")
if bmi < 18.5 :
    print("bạn đang ốm")
elif 18.5<bmi< 24.9:
        print("Your're ok, keep it")
elif 25<bmi<29.9:
        print("bạn đang có nguy cơ thừa cân, hãy cẩn thận!")
else:
    print("bạn đang ở mức báo động, hãy tham khảo ý kiến của bác sĩ !!!")

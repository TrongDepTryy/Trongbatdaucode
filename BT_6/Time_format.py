#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 11:07:23 2024

@author: trongg
"""
#đổi ngày tháng , thàng ngày
from datetime import datetime
def born_format(y, m, d):
    d_m_y =datetime(y, m, d)
    ft= d_m_y.strftime("%d/%m/%y")
    return ft
def born_format2(y, m, d):
    d_m_y =datetime(y, m, d)
    ft2= d_m_y.strftime("%d/%m/%Y")
    return ft2
def born_format3(y, m, d):
    d_m_y =datetime(y, m, d)
    ft3= d_m_y.strftime("%Y/%m/%d/")
    return ft3
d= int(input("Nhập ngày: "))
m= int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
fted=born_format(y, m, d)
fted2=born_format2(y, m, d)
fted3=born_format3(y, m, d)
print("Ngày/tháng/năm đã định dạng DD/MM/YY:", fted)
print("Ngày/tháng/năm đã định dạng DD/MM/YYYY:", fted2)
print("Ngày/tháng/năm đã định dạng YYYY/MM/DD:", fted3)
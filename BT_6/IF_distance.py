#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:34:43 2024

@author: trongg
"""

h=float(input("Hãy nhập khoảng cách đường đi đến trường của bạn nhé của bạn  nhé, đơn vị là mét nhé: "))
if h<300:
    print("Đường không xa, đi bộ cùng mình nhé")
if 300<h<1200:
    print("Đường hơi xa, đi xe đạp được nè")
elif h>1200:
        print("Đường quá xa, đi xe máy nhó")

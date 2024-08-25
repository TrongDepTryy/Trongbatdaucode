#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:44:46 2024

@author: trongg
"""

text='Đại học Quốc gia, Khu phố 6, P. Linh Trung, T. Thủ Đức, Tp. HCM'
text=text.replace("P. ","").replace("T. ", "").replace("Tp. ", "")
sub_tring=text.split(", ")
for sub in sub_tring:
    print (sub)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:56:19 2024

@author: trongg
"""

def time(doi_time):
    h, m, s = map(int, doi_time.split(":"))
    tg = h * 3600 + m * 60 + s
    return tg
doi_time = input("Nhập thời gian theo định dạng hh:mm:ss: ")
tg=time(doi_time)
print("tương đương với số giây là :", [tg])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:08:14 2024

@author: trongg
"""

def time(doi_time):
    h, m, s = map(int, doi_time.split(":"))
    tg = h * 3600 + m * 60 + s
    return tg
def timev2(doi_timev2):
    h, m, s = map(int, doi_timev2.split(":"))
    tg2 = h * 3600 + m * 60 + s
    return tg2
doi_time = input("Nhập thời gian thứ 1 theo định dạng hh:mm:ss: ")
doi_timev2 = input("Nhập thời gian thứ 2  theo định dạng hh:mm:ss: ")
tg=time(doi_time)+timev2(doi_timev2)
print("tương đương với số giây là :", [tg])
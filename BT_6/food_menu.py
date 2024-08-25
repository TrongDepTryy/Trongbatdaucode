#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:18:24 2024

@author: trongg
"""

#thực đơn
print("============ MENU ============")
print('1. Mỳ cay')
print('2. Lẩu Thái')
print('3. Cơm tấm Xì Gòn')
print('4. Bò nhúng giấm') 
print('5. Bún đậu mắm tôm')
print("==============================")
buy=float(input("nhập món mà bạn muốn ăn nèooo: "))
if buy == 1:
    print("chúc mừng bạn là đứa đạo mì")
elif buy == 2:
    print("bạn có biết lẩu Thái không đến từ Thái?")
elif buy == 3:
    print("Xích nây chờ của sanh ziên ")
elif buy == 4:
    print("Dev chưa ăn nên chê =))")
elif buy ==5:
    print("Thích bún đậu nhưng ăn nước mắm =]]]")
else :
    print("bạn nhịn đói à =))")

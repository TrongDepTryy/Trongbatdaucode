#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:33:01 2024

@author: trongg
"""

def kiem_tra_ngay_thang_nam(ngay_thang_nam):
    """Kiểm tra tính hợp lệ của ngày tháng năm nhập vào.

    Args:
        ngay_thang_nam (str): Ngày tháng năm dưới dạng dd/mm/yyyy hoặc ddmm-yyyy.

    Returns:
        bool: True nếu hợp lệ, False nếu không hợp lệ.
    """

    try:
        # Loại bỏ dấu gạch nếu có
        ngay_thang_nam = ngay_thang_nam.replace("-", "")

        # Tách ngày, tháng, năm
        ngay, thang, nam = int(ngay_thang_nam[:2]), int(ngay_thang_nam[2:4]), int(ngay_thang_nam[4:])

        # Kiểm tra điều kiện
        if 1 <= thang <= 12 and 1 <= ngay <= 31 and nam > 0:
            # Kiểm tra số ngày trong tháng
            so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if thang == 2:
                # Kiểm tra năm nhuận
                if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
                    so_ngay_trong_thang[1] = 29
            if ngay <= so_ngay_trong_thang[thang - 1]:
                return True
    except ValueError:
        # Xử lý trường hợp nhập liệu không hợp lệ (ví dụ: không phải số)
        pass
    return False

# Nhập dữ liệu từ người dùng
ngay_thang_nam = input("Nhập ngày tháng năm (dd/mm/yyyy hoặc ddmm-yyyy): ")

# Kiểm tra và in kết quả
if kiem_tra_ngay_thang_nam(ngay_thang_nam):
    print("Ngày tháng năm hợp lệ.")
else:
    print("Ngày tháng năm không hợp lệ.")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:33:50 2024

@author: trongg
"""

import random

def keo_bua_bao():
  """Mô phỏng trò chơi kéo búa bao giữa người và máy.

  Returns:
    None
  """

  while True:
    # Máy tính chọn ngẫu nhiên một trong ba lựa chọn
    may_chon = random.choice(['keo', 'bua', 'bao'])

    # Người chơi nhập lựa chọn
    nguoi_chon = input("Bạn chọn gì? (kéo/búa/bao): ").lower()

    # Kiểm tra tính hợp lệ của lựa chọn
    if nguoi_chon not in ['keo', 'bua', 'bao']:
      print("Lựa chọn không hợp lệ. Vui lòng chọn kéo, búa hoặc bao.")
      continue

    # So sánh lựa chọn và đưa ra kết quả
    if nguoi_chon == may_chon:
      print("Hòa!")
    elif (nguoi_chon == 'keo' and may_chon == 'bua') or \
         (nguoi_chon == 'bua' and may_chon == 'bao') or \
         (nguoi_chon == 'bao' and may_chon == 'keo'):
      print("Bạn thua rồi!")
    else:
      print("Bạn thắng rồi!")

    # Hỏi người chơi có muốn chơi tiếp không
    chon = input("Bạn có muốn chơi tiếp không? (có/không): ").lower()
    if chon != 'có':
      break

# Chạy trò chơi
keo_bua_bao()
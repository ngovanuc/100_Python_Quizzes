"""
Tính chu vi và diện tích hình tam giác khi biết độ dài ba cạnh bất kỳ.
"""
import math
from math import sqrt

def kiem_tra_tam_giac_hop_le(a, b, c):
    """
    Kiểm tra xem ba cạnh a, b, c có tạo thành một tam giác hợp lệ hay không.
    """
    return a + b > c and a + c > b and b + c > a


while True:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if kiem_tra_tam_giac_hop_le(a, b, c):
        # Tính chu vi
        P = a + b + c
        print("Chu vi hình tam giác là:", P)

        # Tính diện tích
        s = (a + b + c) / 2
        S = sqrt(s * (s - a) * (s - b) * (s - c))
        print("Diện tích hình tam giác là:", S)
        break
    else:
        print("Ba cạnh a, b, c không tạo thành một tam giác hợp lệ. Vui lòng nhập lại.")
        continue
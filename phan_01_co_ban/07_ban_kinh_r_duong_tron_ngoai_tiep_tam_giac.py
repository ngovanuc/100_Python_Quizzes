"""
Tính bán kính r của đường tròn ngoại tiếp tam giác khi biết độ dài 3 cạnh a, b, c.
"""

import math


def tam_gic_hop_le(a, b, c):
    """
    Kiểm tra xem 3 cạnh a, b, c có tạo thành tam giác hay không.
    """
    return a + b > c and a + c > b and b + c > a


while True:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if tam_gic_hop_le(a, b, c):
        # Nua chu vi
        p = (a + b + c) / 2

        # Dien tich (theo cong thuc Heron)
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))

        # Banh kinh duong tron ngoai tiep tam giac rr
        R = (a * b * c) / (4 * s)

        print(f"Bán kính R của đường tròn ngoại tiếp tam giác là: {R:.2f}")
        break
    else:
        print("3 cạnh a, b, c không tạo thành tam giác. Vui lòng nhập lại.")
        continue
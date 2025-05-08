"""
Tính chu vi và diện tích hình tròn
"""

import math

r = float(input("Nhập bán kính hình tròn: "))

c = 2 * math.pi * r  # Chu vi hình tròn
s = math.pi * r ** 2  # Diện tích hình tròn

print("Chu vi = ", c)
print("Diện tích = ", s)
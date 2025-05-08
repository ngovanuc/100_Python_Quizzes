"""
Chia táo cho số người
"""

while True:
    tao = int(input("Nhập số táo: "))
    nguoi = int(input("Nhập số người: "))
    if tao < 0 or nguoi <= 0:
        print("Số táo và số người phải là số nguyên dương.")
        continue
    else:
        ket_qua = tao // nguoi
        du = tao % nguoi
        print(f"Mỗi người được {ket_qua} táo, còn lại {du} táo.")
        break

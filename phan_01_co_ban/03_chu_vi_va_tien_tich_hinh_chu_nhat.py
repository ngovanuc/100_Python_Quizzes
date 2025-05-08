"""
Tính chu vi và diện tích hình chữ nhật
"""

def hinh_chu_nhat_hop_le(a, b):
    """
    Kiểm tra xem a và b có phải là chiều dài và chiều rộng hợp lệ của hình chữ nhật hay không.
    """
    return a > 0 and b > 0


while True:
    a = float(input("Nhập chiều dài hình chữ nhật: "))
    b = float(input("Nhập chiều rộng hình chữ nhật: "))

    if hinh_chu_nhat_hop_le(a, b):
        C = 2 * (a + b)  # Chu vi hình chữ nhật
        S = a * b  # Diện tích hình chữ nhật
        print("Chu vi hình chữ nhật là: ", C)
        print("Diện tích hình chữ nhật là: ", S)
        break
    else:
        print("Chiều dài và chiều rộng phải lớn hơn 0. Vui lòng nhập lại.")
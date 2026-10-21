ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: ")) 
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# LỖI SỐ 1 (SyntaxError): Thiếu dấu đóng ngoặc tròn ở câu lệnh print cuối cùng.
# LỖI SỐ 2 (TypeError): Chưa ép kiểu float cho biến cong_suat_w lấy từ input().
# LỖI SỐ 3 (NameError): Đặt tên biến là dien_nang_kwh nhưng f-string gọi nhầm là dien_nang.

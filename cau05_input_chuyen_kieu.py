ma_may = input("Nhập mã máy: ")
print("Kiểu dữ liệu mã máy vừa nhập:", type(ma_may))

cong_suat_raw = input("Nhập công suất W: ")
print("Kiểu dữ liệu công suất vừa nhập:", type(cong_suat_raw))

so_phut_raw = input("Nhập số phút sử dụng: ")
print("Kiểu dữ liệu số phút vừa nhập:", type(so_phut_raw))

don_gia_raw = input("Nhập đơn giá điện/kWh: ")
print("Kiểu dữ liệu đơn giá vừa nhập:", type(don_gia_raw))

cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả sau khi chuyển kiểu ---")
print(f"Mã máy: {ma_may}")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh")
print(f"Chi phí điện: {chi_phi} VND")

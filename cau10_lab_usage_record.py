from datetime import datetime

# Nhập các thông tin đầu vào phục vụ quản lý phòng Lab
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VND/kWh): "))

# Các phép tính toán kỹ thuật dựa trên dữ liệu nhập (Không sử dụng câu lệnh IF)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi_goc = dien_nang_kwh * don_gia_kwh
thue_vat = chi_phi_goc * 0.10  # Bổ sung tính 10% thuế VAT để nâng cấp lên Phiên bản 2
tong_chi_phi = chi_phi_goc + thue_vat

tren_60_phut = so_phut > 60  # Trả về True/False nhờ toán tử so sánh

# Lấy thời điểm hiện tại và định dạng chuỗi văn bản
thoi_diem_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# In kết quả định dạng đầu ra chuẩn hoá nâng cấp v2
print("\n" + "="*35)
print(f"Mã phiên    : {ma_phien}")
print(f"Máy         : {ma_may}")
print(f"Công suất   : {cong_suat_w:.2f} W")
print(f"Thời lượng  : {so_phut} phút")
print(f"Điện năng   : {dien_nang_kwh:.3f} kWh")
print(f"Chi phí gốc : {chi_phi_goc:.2f} VND")
print(f"Thuế VAT(10%): {thue_vat:.2f} VND")
print(f"TỔNG CHI PHÍ: {tong_chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_hien_tai}")
print("="*35)

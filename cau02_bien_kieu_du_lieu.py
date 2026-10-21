ma_phien = "LAB026"          # Kiểu str
ma_may = "PC12"              # Kiểu str
cong_suat_w = 250.0          # Kiểu float
thoi_gian_phut = 90          # Kiểu int
trang_thai_hoat_dong = True  # Kiểu bool
ghi_chu = None               # Kiểu NoneType

print("Mã phiên:", ma_phien, "-", type(ma_phien))
print("Mã máy:", ma_may, "-", type(ma_may))
print("Công suất (W):", cong_suat_w, "-", type(cong_suat_w))
print("Thời gian (phút):", thoi_gian_phut, "-", type(thoi_gian_phut))
print("Trạng thái:", trang_thai_hoat_dong, "-", type(trang_thai_hoat_dong))
print("Ghi chú:", ghi_chu, "-", type(ghi_chu))

thoi_gian_phut = 120
print("Thời gian mới sau khi gán lại (phút):", thoi_gian_phut)

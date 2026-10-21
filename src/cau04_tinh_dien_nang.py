cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("--- Lần 1 (90 phút) ---")
print("Điện năng tiêu thụ:", dien_nang_kwh, "-", type(dien_nang_kwh))
print("Chi phí điện:", chi_phi, "-", type(chi_phi))

so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("--- Lần 2 (60 phút) ---")
print("Điện năng tiêu thụ mới:", dien_nang_kwh, "-", type(dien_nang_kwh))
print("Chi phí điện mới:", chi_phi, "-", type(chi_phi))

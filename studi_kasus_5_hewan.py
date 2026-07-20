"""
Studi Kasus 5 — Hewan Peliharaan di Klinik Hewan
Fokus: Class & Attribute (belum pakai constructor)
"""

class Hewan:
    pass


# Instansiasi object hewan
hewan1 = Hewan()
hewan2 = Hewan()
hewan3 = Hewan()

# Mengisi attribute
hewan1.nama = "Milo"
hewan1.jenis = "Kucing"
hewan1.umur = 2
hewan1.berat_kg = 3.5

hewan2.nama = "Bruno"
hewan2.jenis = "Anjing"
hewan2.umur = 4
hewan2.berat_kg = 12.0

hewan3.nama = "Kiki"
hewan3.jenis = "Kelinci"
hewan3.umur = 1
hewan3.berat_kg = 1.8

# Menampilkan data pasien klinik
print("=== DATA PASIEN KLINIK HEWAN ===")
for hewan in [hewan1, hewan2, hewan3]:
    print(f"{hewan.nama} ({hewan.jenis}), umur {hewan.umur} tahun, berat {hewan.berat_kg} kg")

print()

# Simulasi: Milo kontrol rutin, berat badan naik
print(f"Berat {hewan1.nama} sebelum kontrol: {hewan1.berat_kg} kg")
hewan1.berat_kg = 3.8
print(f"Berat {hewan1.nama} setelah kontrol: {hewan1.berat_kg} kg")

# Hewan lain tidak ikut berubah
print(f"Berat {hewan2.nama} tetap: {hewan2.berat_kg} kg")
print(f"Berat {hewan3.nama} tetap: {hewan3.berat_kg} kg")

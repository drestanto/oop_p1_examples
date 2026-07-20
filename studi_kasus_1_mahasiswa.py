"""
Studi Kasus 1 — Data Mahasiswa
Fokus: Class & Attribute (belum pakai constructor)
"""

class Mahasiswa:
    pass


# Instansiasi 3 object dari class yang sama
mhs1 = Mahasiswa()
mhs2 = Mahasiswa()
mhs3 = Mahasiswa()

# Mengisi attribute tiap object
mhs1.nama = "Andi"
mhs1.nim = "2023001"
mhs1.jurusan = "Informatika"

mhs2.nama = "Budi"
mhs2.nim = "2023002"
mhs2.jurusan = "Sistem Informasi"

mhs3.nama = "Citra"
mhs3.nim = "2023003"
mhs3.jurusan = "Informatika"

# Menampilkan data
print("=== DATA MAHASISWA ===")
for mhs in [mhs1, mhs2, mhs3]:
    print(f"{mhs.nama} ({mhs.nim}) - {mhs.jurusan}")

print()

# Bukti tiap object independen
mhs1.jurusan = "Teknik Komputer"  # pindah jurusan, cuma mhs1 yang berubah
print("Setelah mhs1 pindah jurusan:")
for mhs in [mhs1, mhs2, mhs3]:
    print(f"{mhs.nama} ({mhs.nim}) - {mhs.jurusan}")

"""
Studi Kasus 2 — Data Mobil di Showroom
Fokus: Class & Attribute (belum pakai constructor)
"""

class Mobil:
    pass


# Instansiasi object mobil
mobil1 = Mobil()
mobil2 = Mobil()
mobil3 = Mobil()

# Mengisi attribute
mobil1.merek = "Toyota"
mobil1.model = "Avanza"
mobil1.warna = "Hitam"
mobil1.harga = 250_000_000

mobil2.merek = "Honda"
mobil2.model = "Brio"
mobil2.warna = "Putih"
mobil2.harga = 180_000_000

mobil3.merek = "Suzuki"
mobil3.model = "Ertiga"
mobil3.warna = "Silver"
mobil3.harga = 230_000_000

# Menampilkan daftar mobil di showroom
print("=== DAFTAR MOBIL SHOWROOM ===")
for mobil in [mobil1, mobil2, mobil3]:
    print(f"{mobil.merek} {mobil.model} ({mobil.warna}) - Rp{mobil.harga:,}")

print()

# Simulasi diskon: harga mobil2 diturunkan
mobil2.harga = 170_000_000
print("Setelah mobil2 kena diskon:")
for mobil in [mobil1, mobil2, mobil3]:
    print(f"{mobil.merek} {mobil.model} ({mobil.warna}) - Rp{mobil.harga:,}")

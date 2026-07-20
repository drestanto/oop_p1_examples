"""
Studi Kasus 4 — Produk di Toko Online
Fokus: Class & Attribute (belum pakai constructor)
"""

class Produk:
    pass


# Instansiasi object produk
produk1 = Produk()
produk2 = Produk()
produk3 = Produk()

# Mengisi attribute
produk1.nama = "Sepatu Lari"
produk1.harga = 350_000
produk1.stok = 12

produk2.nama = "Tas Ransel"
produk2.harga = 220_000
produk2.stok = 8

produk3.nama = "Botol Minum"
produk3.harga = 45_000
produk3.stok = 30

# Menampilkan daftar produk
print("=== DAFTAR PRODUK TOKO ===")
for produk in [produk1, produk2, produk3]:
    print(f"{produk.nama} - Rp{produk.harga:,} (stok: {produk.stok})")

print()

# Simulasi: ada pembeli checkout 3 Sepatu Lari
jumlah_beli = 3
produk1.stok = produk1.stok - jumlah_beli

print(f"Setelah ada pembelian {jumlah_beli} '{produk1.nama}':")
print(f"Stok tersisa: {produk1.stok}")

# Produk lain tidak terpengaruh sama sekali
print(f"Stok '{produk2.nama}' tetap: {produk2.stok}")
print(f"Stok '{produk3.nama}' tetap: {produk3.stok}")

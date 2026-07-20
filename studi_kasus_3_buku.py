"""
Studi Kasus 3 — Buku di Perpustakaan
Fokus: Class & Attribute (belum pakai constructor)
"""

class Buku:
    pass


# Instansiasi object buku
buku1 = Buku()
buku2 = Buku()
buku3 = Buku()

# Mengisi attribute
buku1.judul = "Belajar Python Dasar"
buku1.penulis = "Rina Kartika"
buku1.stok = 5
buku1.tersedia = True

buku2.judul = "Struktur Data & Algoritma"
buku2.penulis = "Doni Saputra"
buku2.stok = 0
buku2.tersedia = False

buku3.judul = "Konsep OOP"
buku3.penulis = "Rina Kartika"
buku3.stok = 3
buku3.tersedia = True

# Menampilkan katalog
print("=== KATALOG PERPUSTAKAAN ===")
for buku in [buku1, buku2, buku3]:
    status = "Tersedia" if buku.tersedia else "Dipinjam semua"
    print(f"{buku.judul} - {buku.penulis} (stok: {buku.stok}) [{status}]")

print()

# Simulasi: buku1 dipinjam, stok berkurang
buku1.stok = buku1.stok - 1
if buku1.stok == 0:
    buku1.tersedia = False

print(f"Setelah dipinjam, stok '{buku1.judul}': {buku1.stok}, tersedia: {buku1.tersedia}")

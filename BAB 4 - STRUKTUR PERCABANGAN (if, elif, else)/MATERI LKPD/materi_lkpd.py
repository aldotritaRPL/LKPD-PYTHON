#Struktur if — Satu Kondisi
nilai = int(input("Masukkan nilai : "))

if nilai >= 75:
    print ("Selamat! Kamu LULUS.")
    print ("Nilai kamu :", nilai)

print ("Terima kasih sudah mengikuti ujian.")

#Struktur if-else — Dua Pilihan
#Contoh : Angka Genap atau Ganjil

angka = int(input("Masukkan angka : "))

if angka % 2 == 0:
    print (angka, "adalah bilangan GENAP")
else:
    print (angka, "adalah bilangan GANJIL")

#Struktur if-elif-else — Banyak Pilihan
#Contoh : Kategori Nilai

nilai = int(input("Masukkan nilai {0-100} : "))

if nilai >= 90:
    kategori = "A (Sangat Baik)"
elif nilai >= 80:
    kategori = "B (Baik)"
elif nilai >= 70:
    kategori = "C (Cukup)"
elif nilai >= 60:
    kategori = "D (Kurang)"
else:
    kategori = "E (Sangat Kurang)"

print ("Nilai : ", nilai)
print ("Kategori :", kategori)

#Nested if — Percabangan Bersarang
#Contoh : Syarat Kelulusan dengan 2 kondisi

nilai = int(input("Nilai ujian : "))
absen = int(input("Jumlah absen : "))

if nilai >= 75:
    if absen <= 5:
        print ("LULUS — Selamat!")
    else:
        print ("TIDAK LULUS — Terlalu banyak absen")

#Ekspresi Kondisional (Ternary Operator)
#Contoh biasa 3 baris :
x = 10
if x > 0:
    status = "Positif"
else:
    status = "Negatif/nol"

#Versi ternary (1 baris) :
status = "Positif" if x > 0 else "Negatif/nol"
print ("Status:", status)
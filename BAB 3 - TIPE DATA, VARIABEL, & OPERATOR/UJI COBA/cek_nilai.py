# Program Cek Kondisi Nilai

nama    = input("Nama Siswa :")
nilai   = int(input("Nilai Ujian : "))
hadir   = input("hadir 80%? (iya/tidak) : ")

# Operator Perbandingan

print ()
print ("=== HASIL CEK ===")
print ("Nilai >= 75             :", nilai >= 75)
print ("Nilai >= 90             :", nilai >= 90)
print ("Nilai antara 75 - 89    :", nilai >= 75 and nilai <= 89)

# Operator Logika

hadir_ok = hadir == "iya"
lulus = nilai >= 75 and hadir_ok
remidial = nilai <= 75 or not hadir_ok

print ("lulus                   :", lulus)
print ("Perlu remidial          :", remidial)
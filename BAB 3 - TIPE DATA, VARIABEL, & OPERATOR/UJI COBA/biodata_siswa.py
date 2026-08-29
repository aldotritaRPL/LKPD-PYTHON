# Program Biodata Siswa

print ("=" * 35)
print ("    FORM BIODATA SISWA")
print ("=" * 35)

nama    = input("Nama lengkap           : ")
kelas   = input("Kelas                  : ")
umur    = int(input("Umur (tahun)       : "))
tinggi  = float(input("Tinggi (cm)      : "))

print ()
print ("=" * 35)
print ("    DATA TERSIMPAN")
print ("=" * 35)
print ("Nama            :", nama)
print ("Kelas           :", kelas)
print ("Umur            :", umur, "tahun")
print ("Tinggi          :", tinggi, "cm")
print ("Sudah dewasa    :", umur >= 17)
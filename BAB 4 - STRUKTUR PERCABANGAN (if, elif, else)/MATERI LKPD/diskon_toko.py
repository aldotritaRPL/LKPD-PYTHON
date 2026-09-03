Total = int(input("Masukkan total belanja : "))

if (Total >= 500000):
    diskon = 0.2
else :
    if (Total >= 200000):
        diskon = 0.1
    else :
        diskon = 0

bayar = Total - (Total * diskon)
print ("Total : Rp", Total)
print ("Diskon :", diskon * 100, "%")
print ("Bayar : Rp", bayar)
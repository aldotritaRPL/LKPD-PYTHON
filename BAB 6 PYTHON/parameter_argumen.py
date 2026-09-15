# Parameter biasa
def luas_persegi_panjang(panjang, lebar):
    print("Luas:", panjang * lebar)

luas_persegi_panjang(8, 5)         # argumen posisional
luas_persegi_panjang(lebar=18, panjang=10)    # Keyword argument

# Nilai default
def sapa (nama, salam='Halo'):
    print(salam + ", " + nama + "!")

sapa('Budi')                   # Output: Halo, Budi!
sapa('Ani', 'Selamat pagi')    # Output: Selamat pagi , Ani!
# Contoh: Tabel Perkalian 1-3
for i in range(1, 4):  # Loopn luar: baris
    for j in range(1, 11):  # Loop dalam: kolom
        print(i, "x", j, "=", i * j,)  
    print()  # baris kosong antr tabel
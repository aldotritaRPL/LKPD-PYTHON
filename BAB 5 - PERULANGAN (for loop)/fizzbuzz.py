# Fizzbuzz 1 sampai n menggunakan while
n = int(input("Masukkan batas atas: "))
i = 1
while i <= n:
    if i % 15 == 0:        # habis dibagi 3 DAN 5
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
    i += 1                  # jangan lupa update i
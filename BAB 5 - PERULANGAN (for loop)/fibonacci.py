# Deret Fibonacci
n = int(input("Tampilkan berapa suku Fibonacci? "))
a, b = 0, 1
for i in range(n):
    print (a, end=" ")
    a, b = b, a + b         # geser a jadi b,  jadi a+b
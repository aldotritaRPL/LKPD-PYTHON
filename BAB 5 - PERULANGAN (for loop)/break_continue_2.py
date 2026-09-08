# Demonstrasi break
print ("=== BREAK ===")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")
print()

# Demonstrasi continue
print ("=== CONTINUE ===")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
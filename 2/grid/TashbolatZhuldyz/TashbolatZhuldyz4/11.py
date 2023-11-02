zh = int(input())
for q in range(1, zh + 1):
    for w in range(zh - q):
        print(" ", end=" ")
    for w in range(1, q + 1):
        print(w, end=" ")
    print()

       



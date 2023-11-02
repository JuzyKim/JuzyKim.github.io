for a in range(20):
    for b in range(20):
        for c in range(20):
            for d in range(20):
                if a != b and a != c and b != c and a != d and b != d and c != d:
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        print(a ** 3 + b ** 3)

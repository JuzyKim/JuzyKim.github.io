
N, T = map(int, input().split())
w = list(map(int, input().split()))
w.sort(reverse=True)
cost = (w[0] + w[1]) * T
print(cost)


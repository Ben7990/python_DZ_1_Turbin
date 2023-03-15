n, m, k = map(int, input().split())
print(((k % n == 0) or (k % m == 0)) and (k < n**m))

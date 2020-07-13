N = int(input())
L = []

for i in range(N):
    k = int(input())
    L.append(k)

for j in sorted(L):
    print(j)

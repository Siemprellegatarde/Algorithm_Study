L = list(range(1,31))
N = 28

while N != 0:
    N = N - 1
    num = int(input())
    L.remove(num)

print(L[0])
print(L[1])

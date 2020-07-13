T = int(input())

while T != 0:
    T = T - 1
    N,M = map(int, input().split())

    x = 1
    for i in range(1, M-N+1):
        x = x * i

    y = 1
    for j in range(1, M+1):
        y = y * j

    z = 1
    for k in range(1, N+1):
        z = z * k

    print(int(y/(x*z)))

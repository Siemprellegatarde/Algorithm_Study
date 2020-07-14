N = int(input())
S = 0

for i in list(range(1,N+1)):
    S = S + len(str(i))

print(S)

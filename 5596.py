L_1 = list(map(int,input().split()))
L_2 = list(map(int,input().split()))

S = 0
T = 0

for i in range(len(L_1)):
    S = S + L_1[i]

for i in range(len(L_2)):
    T = T + L_2[i]

if S >= T:
    print(S)
else:
    print(T)

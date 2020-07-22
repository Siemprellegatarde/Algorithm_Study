A,B = map(int, input().split())

L_A = list(str(A))
L_B = list(str(B))

A = int("".join(reversed(L_A)))
B = int("".join(reversed(L_B)))

if A > B:
    print(A)
else:
    print(B)

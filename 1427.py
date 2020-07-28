A = input()
B = ""
L = list(A)

for i in reversed(sorted(L)):
    B = B+i

print(B)

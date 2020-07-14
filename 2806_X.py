N = int(input())
S = input()

a = 0
b = 0
K = 0

for i in range(len(S)):
    if S[i] == 'A':
        a = a + 1
    elif S[i] == 'B':
        b = b + 1

if a>=b:
    K = b
else :
    K = 1 + a

print(K)

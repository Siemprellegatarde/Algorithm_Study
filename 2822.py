a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())

L = [a,b,c,d,e,f,g,h]

K = sorted(L)

print(K[7]+K[6]+K[5]+K[4]+K[3])

R = []

for i in range(3,8):
    R.append(L.index(K[i])+1)

R = sorted(R)

for j in R:
    print(j, end = ' ')

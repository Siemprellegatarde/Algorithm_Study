N = int(input())
L = []
X = 0

for i in range(N+1,2*N+1):
    L.clear()
    for j in range(1,i+1):
        if i%j==0:
            L.append(j)
    
    if L==[1,i]:
        X = X+1
    
print(X)

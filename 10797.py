N = int(input())
L = list(map(int,input().split()))
X = 0

for i in range(len(L)):
    if str(L[i]) == str(N):
        X = X + 1
        
print(X)

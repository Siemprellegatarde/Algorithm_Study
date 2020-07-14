N = int(input())

X_for_cute = 0
X_for_not_cute = 0

while N != 0:
    N = N - 1
    K = int(input())
    
    if K == 1:
        X_for_cute = X_for_cute + 1
    elif K == 0:
        X_for_not_cute = X_for_not_cute + 1

if X_for_cute < X_for_not_cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

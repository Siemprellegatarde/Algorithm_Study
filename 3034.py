N,W,H = map(int,input().split())

while N != 0:
    N = N-1
    x = int(input())
    if x**2 <= W**2+H**2 :
        print("DA")
    else:
        print("NE")

T = int(input())

while T != 0:
    T = T - 1
    a,b = map(int, input().split())

    num = (a**b)%10
    
    if num != 0:
        print(num)
    else:
        print(10)
    

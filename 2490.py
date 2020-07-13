first_time = input()
second_time = input()
third_time = input()

L = [first_time, second_time, third_time]


for i in range(len(L)):
    k = 0
    for j in range(len(L[i])):
        if L[i][j] == '0':
            k = k + 1

    if k == 0:
        print('E')
    elif k == 1:
        print('A')
    elif k == 2:
        print('B')
    elif k == 3:
        print('C')
    else :
        print('D')

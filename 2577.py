A = int(input())
B = int(input())
C = int(input())

X = str(A * B * C)

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eieght = 0
nine = 0

for i in range(len(X)):
    if X[i] == '0':
        zero = zero + 1
    elif X[i] == '1':
        one = one + 1
    elif X[i] == '2':
        two = two + 1
    elif X[i] == '3':
        three = three + 1
    elif X[i] == '4':
        four = four + 1
    elif X[i] == '5':
        five = five + 1
    elif X[i] == '6':
        six = six + 1
    elif X[i] == '7':
        seven = seven + 1
    elif X[i] == '8':
        eieght = eieght + 1
    elif X[i] == '9':
        nine = nine + 1

print(zero)
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eieght)
print(nine)

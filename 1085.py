x,y,w,h = map(int,input().split())

a = h-y
b = w-x

L = [a,b,x,y]

print(sorted(L)[0])

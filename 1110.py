N = input()

if int(N) < 10:
    N = "0"+N

k = int(N[0]) + int(N[1])

if len(str(k)) == 1:
    x = int(N[1]+str(k)[0])
else:
    x = int(N[1]+str(k)[1])

count = 1

while int(N) != x:  
    count += 1
    
    if x < 10:
        x = "0"+str(x)
        
    k = int(str(x)[0])+int(str(x)[1])
    
    if len(str(k)) == 1:
        x = int(str(x)[1]+str(k)[0])
    else:
        x = int(str(x)[1]+str(k)[1])
        
        
print(count)

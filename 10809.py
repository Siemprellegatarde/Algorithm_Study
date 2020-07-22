S = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z']
index = {}


for i in range(len(alphabet)):
    for j in range(len(S)):
        if alphabet[i] == S[j]:
            index[alphabet[i]] = j
            break

for k in alphabet:
    if k in index.keys():
        print(index[k], end=' ')
    else:
        print(-1, end=' ')
            

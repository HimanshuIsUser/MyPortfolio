a = '1,2,3,4,5,6,7,8,9'
k = 5
b = []
for i in a:
    if i.isnumeric():
        b.append(int(i))
c = []
for i in b:
    for y in b:
        if sum(c) == k:
            print(c , 'got it')
        else:
            
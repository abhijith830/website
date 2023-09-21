a=int(input('enter any number'))
print('*')
for i in range (1,a+1):
    for j in range (1,i):
        print (j,end='')
    for k in range (i,0,-1):
        print (k,end='')
        print('*')
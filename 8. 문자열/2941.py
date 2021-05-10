a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
b = input()
for x in a:
    b = b.replace(x,'a')
print(len(b))
a = 1
b = 2
c = 3
d = 4
print('  |',a,'|',b,'|',c,'|',d)
for i in range(9):
    print(a,'|', a*1,'|',a*b,'|',a*c,'|',a*d)
    a = a + 1
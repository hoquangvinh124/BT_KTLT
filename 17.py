lst = []
def convert(n):
    hexchar='0123456789ABCDEF'
    lst.insert(0, hexchar[n%16])
    n = n//16
    if n == 0:
        return 0
    else:
        return convert(n)

inp = int(input("Nhap he co so 10: "))
convert(inp)
for i in lst:
    print(i,end='')
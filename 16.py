lst = []
def convert(n):
    lst.insert(0, n%2)
    n = n//2
    if n == 0:
        return 0
    else:
        return convert(n)

inp = int(input("Nhap he co so 10: "))
convert(inp)
for i in lst:
    print(i,end='')
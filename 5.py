def funX(m, n1=2,n2=4):
 sum=n1+n2
 for i in range(1, m):
    sum=sum+i
 return sum
s1 = funX(5)
print(f"s1 = {s1}")
s2 = funX(5,3)
print(f"s2 = {s2}")
s3 = funX(5,3,2)
print(f"s3 = {s3}")


'''
a) s1 = funX(5)
Uses m=5, n1=2 (default), n2=4 (default)
Initial sum = 2 + 4 = 6
Loop adds: 1 + 2 + 3 + 4 = 10
Final sum = 16
Output: "s1 = 16"

b) s2 = funX(5, 3)
Uses m=5, n1=3, n2=4 (default)
Initial sum = 3 + 4 = 7
Loop adds: 1 + 2 + 3 + 4 = 10
Final sum = 17
Output: "s2 = 17"

c) s3 = funX(5, 3, 2)
Uses m=5, n1=3, n2=2
Initial sum = 3 + 2 = 5
Loop adds: 1 + 2 + 3 + 4 = 10
Final sum = 15
Output: "s3 = 15
'''
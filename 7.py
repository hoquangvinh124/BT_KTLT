def handle(f,x,y):
 if x % 2==0:
    return f(x+2*y,x-y)
 else:
    return f(x-y,x+2*y)
def fn(x,y):
 return x+y
z=handle(lambda x,y:fn(x,y),3,5)
print(f"z={z}")
t=handle(lambda x,y:fn(x,y),2,5)
print(f"t={t}")
k=handle(fn,6,8)
print(f"k={k}")

'''
a) First call: z=handle(lambda x,y:fn(x,y), 3, 5)
x=3 (odd), y=5
Since 3 is odd, it uses else branch: f(x-y, x+2*y)
Parameters passed to lambda will be: (3-5, 3+2*5)
So: f(-2, 13)
The lambda calls fn(-2, 13)
Result: -2 + 13 = 11
Output: "z=11"

b) Second call: t=handle(lambda x,y:fn(x,y), 2, 5)
x=2 (even), y=5
Since 2 is even, it uses if branch: f(x+2*y, x-y)
Parameters passed to lambda will be: (2+2*5, 2-5)
So: f(12, -3)
The lambda calls fn(12, -3)
Result: 12 + (-3) = 9
Output: "t=9"

c) Third call: k=handle(fn, 6, 8)
x=6 (even), y=8
Since 6 is even, it uses if branch: f(x+2*y, x-y)
Parameters passed directly to fn: (6+2*8, 6-8)
So: fn(22, -2)
Result: 22 + (-2) = 20
Output: "k=20
'''
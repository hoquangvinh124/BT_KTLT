x=5
def fnX():
 global x
 x=9
 x+=2
 print(f"x={x}")
fnX()
print(f"x={x}")

'''
The global variable x is initially defined as 5.
Inside the function fnX, the statement global x declares that the function will use and modify the global x.
The global x is set to 9 in the function.
The global x is then incremented by 2, making its value 11.
The value of x (11) is printed inside the function.
After the function completes, the global x retains the modified value 11.
Finally, the updated value of x (11) is printed outside the function
'''
x=5
def fnX():
 x=9
 x+=2
 print(f"x={x}")
fnX()
print(f"x={x}")

'''
Scope of Variables:
The x inside fnX is a local variable and only exists within the function. (x=11)
The global x (defined outside the function) remains unaffected by changes to the local x. (x=5)
'''
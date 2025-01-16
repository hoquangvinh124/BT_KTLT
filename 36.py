lst = [3, 0, 1, 5, 2]
x = 2

'''
a) lst[0]
Result: 3
Explanation: The element at index 0 in lst is 3.

(b) lst[3]
Result: 5
Explanation: The element at index 3 in lst is 5.

(c) lst[x]
Result: 1
Explanation: x = 2, so this accesses the element at index 2 in lst, which is 1.

(d) lst[-x]
Result: 5
Explanation: -x = -2, so this accesses the second-to-last element in lst, which is 5.

(e) lst[x + 1]
Result: 5
Explanation: x + 1 = 3, so this accesses the element at index 3 in lst, which is 5.

(f) lst[x] + 1
Result: 2
Explanation: lst[x] = 1, so 1 + 1 = 2.

(g) lst[lst[x]]
Result: 0
Explanation:
lst[x] = 1, so this becomes lst[1].
lst[1] = 0.
So, the result is 0.

(h) lst[lst[lst[x]]]
Result: 3
Explanation:
lst[x] = 1, so this becomes lst[lst[1]].
lst[1] = 0, so this becomes lst[0].
lst[0] = 3.
So, the result is 3.
'''
lst = [20, 1, -34, 40, -8, 60, 1, 3]

'''
a) lst
Result: [20, 1, -34, 40, -8, 60, 1, 3]

(b) lst[0:3]
Result: [20, 1, -34]
Explanation: This slices the list from index 0 (inclusive) to index 3 (exclusive).

(c) lst[4:8]
Result: [-8, 60, 1, 3]
Explanation: This slices the list from index 4 (inclusive) to index 8 (exclusive).

(d) lst[4:33]
Result: [-8, 60, 1, 3]
Explanation: The slice goes from index 4 to the end of the list because index 33 exceeds the length of the list.

(e) lst[-5:-3]
Result: [40, -8]
Explanation: This slices the list from index -5 (inclusive) to index -3 (exclusive).

(f) lst[-22:3]
Result: [20, 1, -34]
Explanation: Since -22 is out of range, the slice starts from index 0 and goes to index 3 (exclusive).

(g) lst[4:]
Result: [-8, 60, 1, 3]
Explanation: This slices the list from index 4 (inclusive) to the end.

(h) lst[:]
Result: [20, 1, -34, 40, -8, 60, 1, 3]
Explanation: This creates a copy of the entire list.

(i) lst[:4]
Result: [20, 1, -34, 40]
Explanation: This slices the list from the beginning to index 4 (exclusive).

(j) lst[1:5]
Result: [1, -34, 40, -8]
Explanation: This slices the list from index 1 (inclusive) to index 5 (exclusive).

(k) -34 in lst
Result: True
Explanation: The value -34 exists in the list.

(l) -34 not in lst
Result: False
Explanation: The value -34 exists in the list, so the statement is false.

(m) len(lst)
Result: 8
Explanation: The list contains 8 elements.
'''
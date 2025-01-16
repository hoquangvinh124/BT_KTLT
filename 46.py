main_set = {1, 2, 3, 4}
subsets = [{2, 3}, {1, 2}, {5, 6}, {3, 4}]

def largest_subset(m_set, s_set):
    max = set()
    for t in s_set:
        flag = False
        for d in t:
            if d in m_set:
                flag = True
                break
        if not flag and len(t) > len(max):
            max = t
    return max

print(largest_subset(main_set, subsets))
set_of_tuples = {(1, 2), (2, 1), (3, 4), (4, 3), (5, 6)}

def solution(inp):
    set_for_checking = set()
    for t in inp:
        if t in set_for_checking:
            return True
        set_for_checking.add(t)
        set_for_checking.add(t[::-1])
    return False

print(solution(set_of_tuples))
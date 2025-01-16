def tower_of_Hanoi(Nod, start, end, mid):
    if Nod == 0:
        return 
    tower_of_Hanoi(Nod - 1, start, mid, end)
    print(f"Di chuyển đĩa {Nod} từ {start} sang {end}")
    tower_of_Hanoi(Nod - 1, mid, end, start)

tower_of_Hanoi(4, 'A', 'C', 'B')


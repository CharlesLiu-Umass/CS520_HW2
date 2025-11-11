def minimum_traps(m, x):
    visited = set()
    current_room = 0
    cycle_length = 0
    
    while current_room not in visited:
        visited.add(current_room)
        current_room = (current_room * x) % m
        cycle_length += 1
    
    return cycle_length

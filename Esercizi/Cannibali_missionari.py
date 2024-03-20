from collections import deque

def is_valid(state):
    m, c, b = state
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if (m > 0 and m < c) or (3 - m > 0 and 3 - m < 3 - c):
        return False
    return True

def successors(state):
    m, c, b = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for move in moves:
        delta_m, delta_c = move
        new_state = (m - delta_m * b, c - delta_c * b, 1 - b)
        if is_valid(new_state):
            yield new_state

def solve():
    start_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)
        for successor_state in successors(state):
            queue.append((successor_state, path + [successor_state]))

solution = solve()
print(solution)

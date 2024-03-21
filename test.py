from collections import deque

def connect_dots(start, end, matrix):
    # Define function to check if coordinates are within bounds of the matrix
    def is_valid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != -1

    # Define function to get adjacent coordinates
    def get_adjacent(x, y):
        adjacent = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # Up, Down, Left, Right
        return [(i, j) for i, j in adjacent if is_valid(i, j)]

    # BFS to find the shortest path
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        x, y = current
        if current == end:
            return path + [current]
        if current not in visited:
            visited.add(current)
            for next_pos in get_adjacent(x, y):
                queue.append((next_pos, path + [current]))

    return None

# Given dots
dots = [(0, 1), (10, 2), (8, 3)]

# Create matrix
matrix = [[0] * 11 for _ in range(4)]
print(matrix)

# Mark dots as obstacles (-1) in the matrix
for x, y in dots:
    print(x,y)
    matrix[x][y] = -1

# Connect the dots and print the pathway
for i in range(len(dots) - 1):
    start = dots[i]
    end = dots[i + 1]
    path = connect_dots(start, end, matrix)
    if path:
        print("Pathway from", start, "to", end, ":", path)
    else:
        print("No pathway found from", start, "to", end)

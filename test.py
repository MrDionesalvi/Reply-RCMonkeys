import itertools

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    W, H, GN, SM, TL = map(int, lines[0].split())
    
    golden_points = [tuple(map(int, line.split())) for line in lines[1:GN+1]]
    silver_points = [tuple(map(int, line.split())) for line in lines[GN+1:GN+SM+1]]
    
    tiles = {}
    for line in lines[GN+SM+1:]:
        tile_id, cost, count = line.split()
        tiles[tile_id] = {'cost': int(cost), 'count': int(count)}
    
    return W, H, golden_points, silver_points, tiles

def calculate_score(path, silver_points):
    total_score = sum(silver_point[2] for silver_point in silver_points)
    for point in path:
        if point in silver_points:
            total_score -= silver_points[point][2]  # deducting score if revisiting silver point
    return max(0, total_score)  # ensuring non-negative score

def solve(W, H, golden_points, silver_points, tiles):
    directions = {
        '3': [(0, 1)],
        '5': [(1, 0)],
        '6': [(0, 1), (1, 0)],
        '7': [(0, 1), (1, 0), (1, 1)],
        '9': [(1, -1)],
        '96': [(0, 1), (1, -1)],
        'A': [(-1, 0)],
        'A5': [(-1, 0), (1, 0)],
        'B': [(0, 1), (-1, 0), (1, -1)],
        'C': [(1, 0)],
        'C3': [(0, 1), (1, 0)],
        'D': [(1, 0), (1, -1), (1, 1)],
        'E': [(-1, 0), (1, 0), (0, 1)],
        'F': [(0, 1), (1, 0), (1, -1), (0, 1), (1, 1), (1, -1)]
    }

    def is_valid(x, y):
        return 0 <= x < W and 0 <= y < H

    def neighbors(x, y):
        for dx, dy in directions[tile_id]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                yield nx, ny

    def backtrack(x, y, visited, path, score):
        if (x, y) in visited:
            return float('inf'), []

        if len(path) == len(golden_points):
            return calculate_score(path, silver_points), path

        min_cost, min_path = float('inf'), []
        for tile_id, tile_info in tiles.items():
            if tile_info['count'] > 0:
                for nx, ny in neighbors(x, y):
                    cost = tile_info['cost']
                    if (nx, ny) in silver_points:
                        cost *= 2  # doubling cost if visiting silver point
                    tiles[tile_id]['count'] -= 1
                    new_score, new_path = backtrack(nx, ny, visited | {(x, y)}, path + [(nx, ny)], score + cost)
                    tiles[tile_id]['count'] += 1
                    if new_score < min_cost:
                        min_cost = new_score
                        min_path = new_path

        return min_cost, min_path

    min_cost, min_path = float('inf'), []
    for gx, gy in golden_points:
        for tile_id, _ in tiles.items():
            for nx, ny in neighbors(gx, gy):
                cost = tiles[tile_id]['cost']
                if (nx, ny) in silver_points:
                    cost *= 2  # doubling cost if visiting silver point
                tiles[tile_id]['count'] -= 1
                score, path = backtrack(nx, ny, {(gx, gy)}, [(nx, ny)], cost)
                tiles[tile_id]['count'] += 1
                if score < min_cost:
                    min_cost = score
                    min_path = path

    return min_path

def format_output(path):
    return '\n'.join(['{} {} {}'.format(tile_id, x, y) for tile_id, x, y in path])

# Esempio di utilizzo
input_string = """10 7 3 4 11
2 4
7 2
6 6
4 4 100
4 2 100
6 0 150
7 5 150
3 6 4
5 2 6
6 2 6
7 8 5
9 2 7
A 2 7
B 8 5
C 6 5
D 8 5
E 8 5
F 15 3"""

W, H, golden_points, silver_points, tiles = parse_input(input_string)
path = solve(W, H, golden_points, silver_points, tiles)
output_string = format_output(path)
print(output_string)

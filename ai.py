class Tile:
    def __init__(self, id, cost, count):
        self.id = id
        self.cost = cost
        self.count = count

class Point:
    def __init__(self, x, y, score=0):
        self.x = x
        self.y = y
        self.score = score

def find_path(W, H, golden_points, silver_points, tiles):
    # Initialize grid
    grid = [[None for _ in range(W)] for _ in range(H)]

    # Place golden points
    for point in golden_points:
        grid[point.y][point.x] = 'G'

    # Place silver points
    for point in silver_points:
        grid[point.y][point.x] = 'S'

    # TODO: Implement path finding and scoring logic here

    # Return list of chosen tiles with their coordinates
    for i in grid:
        print(i)
    return []
    
# Define your input here
W = 10
H = 10
golden_points = [Point(1, 1), Point(8, 8)]
silver_points = [Point(5, 5, 10), Point(2, 2, 20)]
tiles = [Tile(1, 5, 10), Tile(2, 10, 5)]

# Call the function
chosen_tiles = find_path(W, H, golden_points, silver_points, tiles)

# Print the output
for tile in chosen_tiles:
    print(f"Tile ID: {tile.id}, Coordinates: ({tile.x}, {tile.y})")

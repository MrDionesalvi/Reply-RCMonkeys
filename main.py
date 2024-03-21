file_path = "input/00-trailer.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    line = file.readline()

    # Extracting values from the first line
    values = line.split()
    W = int(values[0])
    H = int(values[1])
    GN = int(values[2])
    SM = int(values[3])
    TL = int(values[4])

    matrix = [[0 for _ in range(W)] for _ in range(H)]


    for _ in range(GN):
        line = file.readline().split(" ")
        i, j = int(line[0])-1, int(line[1])-1
        matrix[i][j] = "G"


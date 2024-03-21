file_path = "input/01-comedy.txt"


tile_rules = {
    1: [(0, -1)],  # From up to down
    2: [(1, 0)],   # From left to right
    3: [(0, 1)],   # From down to up
    4: [(0, -1), (1, 0), (0, 1)],   # From up to down, From left to right, From down to up
    5: [(-1, 1)],  # From down-left to up-right
    6: [(1, 1), (-1, 0)],   # From down-right to up-left, From left to right
    7: [(-1, 0)],  # From right to left
    8: [(-1, 0), (1, 1)],   # From right to left, From down-left to up-right
    9: [(1, -1)],  # From up-left to down-right
    10: [(0, 1), (0, -1)],   # From down to up, From up to down
    11: [(1, 0), (0, 1)],   # From left to right, From down to up
    12: [(0, 1), (1, -1), (1, 1)],   # From down to up, From up-left to down-right, From down-right to up-left
    13: [(-1, 0), (0, -1), (0, 1)],   # From right to left, From up to down, From down to up
    14: [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1)]   # From left to right, From down to up, From right to left, From up to down, From down-right to up-left, From down-left to up-right
}



def distanza_gp(lista_gp, diz):  #return = [gp_diverso, row_d, col_d, dista]
    for i in range(len(lista_gp)-1):
        for j in range(i+1, len(lista_gp)):
            row_distance = abs(lista_gp[i][1] - lista_gp[j][1])
            col_distance = abs(lista_gp[i][0] - lista_gp[j][0])
            distance = row_distance + col_distance
            diz[f"{lista_gp[i][0]}_{lista_gp[i][1]}"].append([f"{lista_gp[j][0]}_{lista_gp[j][1]}", row_distance, col_distance, distance])
    
            diz[f"{lista_gp[j][0]}_{lista_gp[j][1]}"].append([f"{lista_gp[i][0]}_{lista_gp[i][1]}", -row_distance, -col_distance, distance])

def distanza_sp(lista_sp, diz):
    for i in range(len(lista_sp)-1):
        for j in range(i+1, len(lista_sp)):
            row_distance = lista_sp[i][1] - lista_sp[j][1]
            col_distance = lista_sp[i][0] - lista_sp[j][0]
            distance = row_distance + col_distance
            diz[f"{lista_sp[i][0]}_{lista_sp[i][1]}"].append([f"{lista_sp[j][0]}_{lista_sp[j][1]}", row_distance, col_distance, distance])
            diz[f"{lista_sp[j][0]}_{lista_sp[j][1]}"].append([f"{lista_sp[i][0]}_{lista_sp[i][1]}", -row_distance, -col_distance, distance])

def distanza_gp_to_sp(GPLIST, SPLIST, diz):
    for gp in range(len(GPLIST)):
        for sp in range(len(SPLIST)):
            row_distance = abs(GPLIST[gp][1] - SPLIST[sp][1])
            col_distance = abs(GPLIST[gp][0] - SPLIST[sp][0])
            distance = row_distance + col_distance
            diz[f"{GPLIST[gp][0]}_{GPLIST[gp][1]}"].append([f"{SPLIST[sp][0]}_{SPLIST[sp][1]}", row_distance, col_distance, distance])


with open(file_path, "r", encoding='utf-8-sig') as file:
    line = file.readline()
    gp_to_sp = {}

    # Extracting values from the first line
    values = line.split()
    W = int(values[0])
    H = int(values[1])
    GN = int(values[2])
    SM = int(values[3])
    TL = int(values[4])

    matrix = [[" " for _ in range(H+1)] for _ in range(W+1)]
    print(len(matrix), " || ", len(matrix[0]))

    lista_gp = []
    distanze_gp = {}
    for _ in range(GN):
        line = file.readline().split(" ")
        i, j = int(line[0]), int(line[1])
        lista_gp.append([i, j])
        distanze_gp[f"{i}_{j}"] = []
        gp_to_sp[f"{i}_{j}"] = []

    distanza_gp(lista_gp, distanze_gp)

    silver_points = {}
    distanze_sp = {}
    lista_sp = []
    for _ in range(SM):
        line = file.readline().split(" ")
        i, j, points = int(line[0]), int(line[1]), int(line[2]) 
        silver_points[f"{i}_{j}"] = points
        lista_sp.append([i, j])
        distanze_sp[f"{i}_{j}"] = []

    distanza_sp(lista_sp, distanze_sp)

    som = 0

    for key in silver_points:
        som += silver_points[key]

    print(som)

    costo_blocchi = {}
    disponibilita_blocchi = {}

    for _ in range(TL):
        line = file.readline().split(" ")
        i = line[0]
        costo = int(line[1])
        disponibile = int(line[2])
        costo_blocchi[i] = costo
        disponibilita_blocchi[i] = disponibile

    distanza_gp_to_sp(lista_gp, lista_sp, gp_to_sp)



start = lista_gp[0]
return_list = []

PLIST = lista_gp + lista_sp

PLIST = sorted(PLIST, key=lambda coord: (coord[0], coord[1]))


def get_path(start, end):
    path = []
    x1, y1 = start
    x2, y2 = end
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1
    x, y = x1, y1
    while x != x2:
        path.append([x, y])
        x += dx
    while y != y2:
        path.append([x, y])
        y += dy
    path.append([x2, y2])
    return path

for i in range(len(PLIST) - 1):
    path = get_path(PLIST[i], PLIST[i+1])
    return_list.extend(path)

bau = set()
realRET = []
for element in return_list:
    miao = f"{element[0]}_{element[1]}"
    if not miao in bau:
        bau.add(miao)
        realRET.append(element)
    else:
        continue


for element in realRET:
    if element in lista_gp: 
        matrix[element[0]][element[1]] = "X"
    elif element in lista_sp:
        matrix[element[0]][element[1]] = "Y"
    else:
        matrix[element[0]][element[1]] = "-"
print(matrix)

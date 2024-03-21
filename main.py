file_path = "input/00-trailer.txt"


def distanza_gp(lista_gp, diz):  #return = [gp_diverso, row_d, col_d, dista]
    for i in range(len(lista_gp)-1):
        for j in range(i+1, len(lista_gp)):
            row_distance = abs(lista_gp[i][1] - lista_gp[j][1])
            col_distance = abs(lista_gp[i][0] - lista_gp[j][0])
            distance = row_distance + col_distance
            diz[f"{lista_gp[i][0]}_{lista_gp[i][1]}"].append([f"{lista_gp[j][0]}_{lista_gp[j][1]}", row_distance, col_distance, distance])
    
            diz[f"{lista_gp[j][0]}_{lista_gp[j][1]}"].append([f"{lista_gp[i][0]}_{lista_gp[i][1]}", row_distance, col_distance, distance])

def distanza_sp(lista_sp, diz):
    for i in range(len(lista_sp)-1):
        for j in range(i+1, len(lista_sp)):
            row_distance = abs(lista_sp[i][1] - lista_sp[j][1])
            col_distance = abs(lista_sp[i][0] - lista_sp[j][0])
            distance = row_distance + col_distance
            diz[f"{lista_sp[i][0]}_{lista_sp[i][1]}"].append([f"{lista_sp[j][0]}_{lista_sp[j][1]}", row_distance, col_distance, distance])
    
            diz[f"{lista_sp[j][0]}_{lista_sp[j][1]}"].append([f"{lista_sp[i][0]}_{lista_sp[i][1]}", row_distance, col_distance, distance])

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

    lista_gp = []
    distanze_gp = {}
    for _ in range(GN):
        line = file.readline().split(" ")
        i, j = int(line[0])-1, int(line[1])-1
        matrix[i][j] = "G"
        lista_gp.append([i, j])
        distanze_gp[f"{i}_{j}"] = []

    distanza_gp(lista_gp, distanze_gp)
    print(distanze_gp)

    silver_points = {}
    distanze_sp = {}

    for _ in range(SM):
        line = file.readline().split(" ")
        i, j, points = int(line[0])-1, int(line[1])-1, int(line[2]) 
        silver_points[f"{i}_{j}"] = points
        matrix[i][j] = "S"

    costo_blocchi = {}
    disponibilita_blocchi = {}

    for _ in range(TL):
        line = file.readline().split(" ")
        i = line[0]
        costo = int(line[1])
        disponibile = int(line[2])
        costo_blocchi[i] = costo
        disponibilita_blocchi[i] = disponibile


print(costo_blocchi, disponibilita_blocchi)
        
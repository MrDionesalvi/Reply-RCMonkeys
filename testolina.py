def connetti_punti(punti):
    # Trova i massimi valori di x e y
    max_x = max(punti, key=lambda punto: punto[0])[0]
    max_y = max(punti, key=lambda punto: punto[1])[1]

    # Crea una matrice con i punti
    matrice = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Disegna i punti nella matrice
    for punto in punti:
        x, y = punto
        matrice[y][x] = '*'

    m = len(matrice)
    n = len(matrice[0])

    # Creazione di una nuova matrice per i punti collegati
    matrice_collegata = [[' ' for _ in range(2*n + 1)] for _ in range(2*m + 1)]

    # Copia dei punti originali nella nuova matrice
    for i in range(m):
        for j in range(n):
            matrice_collegata[2*i + 1][2*j + 1] = matrice[i][j]

    # Collegamento orizzontale
    for i in range(m):
        for j in range(n - 1):
            if matrice[i][j] == matrice[i][j + 1] == '*':
                matrice_collegata[2*i + 1][2*j + 2] = '-'

    # Collegamento verticale
    for i in range(m - 1):
        for j in range(n):
            if matrice[i][j] == matrice[i + 1][j] == '*':
                matrice_collegata[2*i + 2][2*j + 1] = '|'

    # Costruzione della rappresentazione in stringa della matrice collegata
    matrice_collegata_str = '\n'.join([''.join(row) for row in matrice_collegata])

    return matrice_collegata_str

# Esempio di utilizzo
def main():
    punti_input = [(60, 22), (17, 22), (70, 17), (76, 11 ), (37, 24 ), (76, 3 ), (77, 26 ), (64, 32 ), (4, 27 ), (72, 26 ), (8, 8 ), (24, 37 ), (59 ,3 ), (28 ,36 ), (56 ,6 ), (70 ,30 )]

    matrice_collegata = connetti_punti(punti_input)
    print(matrice_collegata)

if __name__ == "__main__":
    main()
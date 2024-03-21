with open('output/output.txt', 'w') as file:
    for i in range(80):
        for j in range(40):
            file.write(f"F {i} {j}\n")
file_path = "/home/dione/Documenti/Università/Reply/main.py"

with open(file_path, "r") as file:
    lines = file.readlines()

# Extracting values from the first line
values = lines[0].split()
W = int(values[0])
H = int(values[1])
GN = int(values[2])
SM = int(values[3])
TL = int(values[4])

print(f"W: {W}")
print(f"H: {H}")
print(f"GN: {GN}")
print(f"SM: {SM}")
print(f"TL: {TL}")
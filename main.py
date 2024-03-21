file_path = "input/00-trailer.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    lines = file.readlines()

# Extracting values from the first line
values = lines[0].split()
print(values)
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
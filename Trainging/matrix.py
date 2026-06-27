matrix = []

for i in range(4):      # 4 rows
    row = []
    for j in range(3):  # 3 columns
        pair = list(map(int, input(f"Enter 2 numbers for element [{i}][{j}] (e.g. 0 1): ").split()))
        row.append(pair)
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(row)
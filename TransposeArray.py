rows = int(input("rows"))
cols = int(input("cols"))
matrix = []

for row in range(rows):
    row_data = []
    for col in range(cols):
        row_data.append(int(input()))
    matrix.append(row_data)
print(matrix)
res = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    res.append(row)

print(res)
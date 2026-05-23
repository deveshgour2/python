a = [10,30], [20,40]
b = [5,15], [25, 35]
result = [[0,0], [0,0]]
for i in range(2):
    for j in range(2):
        result[i][j] = a[i][j] * b[i][j]

print(f"Result= {result}")
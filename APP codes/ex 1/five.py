rows = int(input())
cols = int(input())
arr = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(i*j)
    arr.append(col)
print(arr)

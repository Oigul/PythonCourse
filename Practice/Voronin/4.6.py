a = [
    [2, 5, 7, 3, 5],
    [3, 11, 43, 2, 9],
    [5, 8, 32, 13, 6],
    [4, 2, 1, 4, 8]
]

for i in a:
    for j in i:
        if j == 5:
            a.pop(i)


print(a)
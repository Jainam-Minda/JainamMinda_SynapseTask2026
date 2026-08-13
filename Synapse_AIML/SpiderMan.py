n = int(input("Enter the size of grid: "))
grid = []

for i in range(n):
    row = []
    for j in range(n):
        while True:
            val = int(input("Enter the value for cell ({}, {}) [0 or 1 only]: ".format(i, j)))
            if val == 0 or val == 1:
                row.append(val)
                break
            else:
                print("Invalid input. Please enter 0 or 1.")
    grid.append(row)

print("\nYour Grid:")
for row in grid:
    print(*row)

best_count = -1
best_m = -1
best_i = -1
best_j = -1

for m in range(1, n + 1, 2):
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            center_row = i + m // 2
            center_col = j + m // 2

            if grid[center_row][center_col] == 0:
                continue

            count = 0
            for r in range(i, i + m):
                for c in range(j, j + m):
                    if grid[r][c] == 1:
                        count += 1

            if count > best_count:
                best_count = count
                best_m = m
                best_i = i
                best_j = j

if best_count == -1:
    print("\nNo valid launch position.")
else:
    center_row = best_i + best_m // 2
    center_col = best_j + best_m // 2
    launch_x = center_col
    launch_y = n - 1 - center_row

    print("\nBest value of m:", best_m)
    print("Best launch coordinate:", (launch_x, launch_y))
    print("Maximum criminals captured:", best_count)
    print("Captured criminals:")

    for r in range(best_i, best_i + best_m):
        for c in range(best_j, best_j + best_m):
            if grid[r][c] == 1:
                x = c
                y = n - 1 - r
                print((x,y))

maximum = 0
idx_row, idx_col = 0, 0

for i in range(9):
    row = list(map(int, input().split()))
    
    if max(row) >= maximum:
        maximum = max(row)
        idx_col = row.index(max(row)) + 1
        idx_row = i + 1
        
print(maximum)
print(idx_row, idx_col)
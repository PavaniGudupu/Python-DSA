arr = [0, 1, 0, 3, 12]

pos = 0  # position for next non-zero
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

# Fill remaining positions with zeros
for i in range(pos, len(arr)):
    arr[i] = 0

print(arr)

## Worst Case ##

# arr = [1, 2, 3, 4, 5]
# k = 2

# for _ in range(k):
#     first = arr[0]
#     for i in range(1, len(arr)):
#         arr[i - 1] = arr[i]
#     arr[-1] = first
# print(arr)


## BEST CASE - using reverse method ##

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

pos1 = []
pos2 = []

for i in range(k, len(arr)):
    pos1.append(arr[i])

for i in range(k):
    pos2.append(arr[i])

arr = pos1 + pos2

print(arr)

## BEST CASE - without using reverse method ##


arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)

# Reverse first k elements
left = 0
right = k - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Reverse remaining elements
left = k
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Reverse entire array
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
#1. Worst Case: Rotate One Position at a Time
for _ in range(k):
    last = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last

"""
 Time Complexity: O(k × n)
 Space Complexity: O(1)
 Worst case when k ≈ n: O(n²)
"""

#2. Better: Using Extra Arrays

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

pos1 = []
pos2 = []

for i in range(len(arr) - k, len(arr)):
    pos1.append(arr[i])

for i in range(len(arr) - k):
    pos2.append(arr[i])

arr = pos1 + pos2

print(arr)


#3. Best: Reversal Algorithm (Right Rotation)

"""For right rotation, the order is:
Reverse entire array
Reverse first k elements
Reverse remaining elements"""

arr = [1, 2, 3, 4, 5]
k = 2

k %= len(arr)

# Reverse entire array
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Reverse first k elements
left, right = 0, k - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Reverse remaining elements
left, right = k, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)


"""Time Complexity: O(n)
 Space Complexity: O(1) ✅"""


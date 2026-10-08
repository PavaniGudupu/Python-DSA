# My approach ->  Time  = O(n), Space = O(n)

arr = [1, 1, 2, 2, 3, 4, 4]

seen = set()
duplicate = set()
result = []

for i in arr:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
        result.append(i)
        
print(f"Without Duplicate: {result}")
print(f"Duplicate list: {list(duplicate)}")


# Slow Fast Approach -> Time  = O(n), Space = O(1)

slow = 0
for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]
print(arr[:slow + 1])
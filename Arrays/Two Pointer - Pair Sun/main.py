'''
Q3 — Pair Sum 🔥

'''
arr = [1, 2, 3, 4, 6]
left = 0
right = len(arr) - 1
target = 7
total = 0
while left < right:
    total = arr[left] + arr[right]
    if total == target:
        print(arr[left], " + " , arr[right], " = ", total)
        break
    elif total < target:
        left += 1
    else: 
        right -= 1
        
    
    
    
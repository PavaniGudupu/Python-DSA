arr = [1, 2, 3, 2, 1]
left = 0
right = len(arr) - 1
is_palindrom = True
while left < right:
    if arr[left] != arr[right]:
        is_palindrom = False
        break
    
    left += 1
    right -= 1
    
if is_palindrom:
    print("Palindrom number")
else:
    print("Not an Palindrom number")
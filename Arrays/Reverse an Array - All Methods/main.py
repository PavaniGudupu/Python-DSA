# Method 1 - Create new arr, rev loop, append - TM: O(n) SM: O(n)

arr = [10, 20, 30, 40, 50]
new_arr = []
for i in range(len(arr) - 1, -1, -1):
    new_arr.append(arr[i])
    
print(new_arr)




# Method 2 - Using Slicing Method - TM: O(n) SM: O(n) 

arr = [10, 20, 30, 40, 50]
new_arr = []
for i in arr[::-1]:
    new_arr.append(i)
    
print(new_arr)




# Method 3 - Using built in Method - TM: O(1) SM: O(1) 

arr = [10, 20, 30, 40, 50]
arr.reverse()
print(arr)





# Method 4 - 🔥 Two Pointer Technique - Swap 
#Approximately: n / 2 But: n / 2 is still: O(n)

#Therefore: Time = O(n)TM: O(n) SM: O(1)

'''
10  20  30  40  50
↑                   ↑
L  = 0      lst idx R  Continue until: left < right
'''


arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    # in Java, c = a, a = b, b = c works but not in python
            #''' int temp = arr[left];
            #    arr[left] = arr[right];
            #    arr[right] = temp; '''
    
    left += 1
    right -= 1
    
print(arr)






# Method 5 - 🔥 Recursion
'''/*----

Define a function reverse(arr, left, right).
Base case: if left >= right, stop recursion.
Recursive step: swap arr[left] and arr[right], then call reverse(arr, left+1, right-1).


-----*/'''


def reverse(arr, left, right):
    if left >= right:
        return
    
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)
    
arr = [10, 20, 30, 40, 50]
reverse(arr, 0, len(arr) - 1)
print(f"Recursion Reverse Array: ", arr)






























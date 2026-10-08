# -------------  Q8 — Coding Challenge 🏆 
#Write a Python program to find the second largest element without using: max(), sort(), sorted()
#---------------- 


############### CASE 1 ##################

arr = [10, 25, 7, 45, 40, 40, 12]
second = -1
first = arr[0]
for i in arr:
    if i > first:
        first = i
    
for i in arr:    
    if i > second and i < first:
        second = i

print("Second largest num: ", second)


############### CASE 2: Robust One-Pass Approach ##################


def secondLargest(arr):
    first = second = float('-inf')  #//-ve infinite
    for i in arr:
        if i > first:
            second = first
            first = i
            
        elif i>second and i!=first:
            second = i
            
    return second

arr = [10, 25, 7, 45, 50, 12]
result = secondLargest(arr)
print("Second largest element is:", result)
        
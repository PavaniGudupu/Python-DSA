# Finding the Largest Element TM-O(n) SM-O(1)

arr = [10, 25, 7, 45, 12]
largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print(largest)


# Finding the Smallest Element TM-O(n) SM-O(1)

arr = [10, 25, 7, 45, 12]
smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print(smallest)


# Searching an Element - Linear Search by default TM-O(n)

arr = [10, 25, 7, 45, 12]
target = 45

for i in arr:
    if target == i:
        print("Found")
        break



# Inserting into an Array - TM O(n)

arr = [10, 20, 30, 40]
value = 15

arr.insert(1, value) #index, value
print(arr)


# Appending to a Python List - TM O(1) SM-O(1)


arr = [10, 20, 30, 40]
value = 50

arr.append(value) # instantly add at end
print(arr)


# Deleting from the End - TM O(1) SM-O(1)

arr = [10, 20, 30, 40]

arr.pop() # instantly delete at end
print(arr)


# Deleting from the Beginning - TM O(1) SM-O(1)

arr = [10, 20, 30, 40]

arr.pop(0) # instantly delete at beginning
print(arr)





















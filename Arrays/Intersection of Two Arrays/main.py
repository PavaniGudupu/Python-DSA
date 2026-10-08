# --— Intersection of Two Arrays 🔥

#My Approach

# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 4, 6]
# result = []
# for i in arr2:
#     if i in arr1 and i not in result:
#         result.append(i)
# print(result)


# Using set

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]
s1 = set(arr1)
s2 = set(arr2)

result = []

for i in s1:
    if i in s2:
        result.append(i)

print(result)
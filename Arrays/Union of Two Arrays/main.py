arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 4, 5, 6]

s1 = set(arr1)
s2 = set(arr2)

# using built in method
print(s1.union(s2))

# without using built in method
""" Time  : O(n + m), Space : O(n + m) """

result = set()

for x in s1:
    result.add(x)

for x in s2:
    result.add(x)

print(result)
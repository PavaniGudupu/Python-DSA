#arr = [1, 2, 4, 5]

# --------- My Approach ---------
# result = []
# last = arr[-1]
# for i in range(1, last + 1):
#     if i not in arr:
#         result.append(i)
        
# print(f"The missing number: {result}")

# result = [i for i in range(1, arr[-1] + 1) if i not in arr]
# print(f"The missing number: {result}")


# --------- Best Approach for given array without duplicate only single missing numbers ---------
# Time Complexity = O(n), Space Complexity = O(1)
arr = [1, 2, 4, 5]
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
missing = expected_sum - sum(arr)
print(missing)




#---- Best Approach - for any array with duplicates and list of missing numbers
# Time Complexity = O(n), Space Complexity = O(n)
arr = [1, 1, 4, 5]
n = 5

hash_arr = [0] * (n + 1)

for num in arr:
    hash_arr[num] = 1

for i in range(1, n + 1):
    if hash_arr[i] == 0:
        print(i)
        
        
        
        
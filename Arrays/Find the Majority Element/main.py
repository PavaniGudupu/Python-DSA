## --- Better Approach ----
""" Time Complexitiy: O(n), Space Complexitiy: O(n) """

arr = [3, 3, 4, 2, 3, 3, 5, 3]
n = len(arr)
majority_len = n // 2
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1                                    
print(freq)
print(majority_len)
        
for k,v in freq.items():
    if v > majority_len:
        print(k, end=", ")



# ----- Boyer-Moore Voting Algorithm. 🎉 Optimal Approach -----
""" Time Complexitiy: O(n), Space Complexitiy: O(1) """


arr = [2, 2, 1, 1, 1, 2, 2]

candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

print("Majority Element:", candidate)
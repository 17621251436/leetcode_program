xa = []
b = []
if not nums:
    return []
for i in range(len(nums)):
    if nums[i] % 2 == 1:
        a.append(nums[i])
    else:
        b.append(nums[i])
return a + b
def twosum(nums, target):
    kq = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                kq.extend([i])
                kq.extend([j])
    return kq


so = [3, 2, 4]
kqua = 6
print(twosum(so, kqua))

#Initial approach: brute force by iterating through the array twice and adding the elements together
#time complexity is O(n^2) 
def twoSum(nums: list[int], target: int) -> list[int]:
    for i_index, i in enumerate(nums):
        for j_index, j in enumerate(nums):
            #Since we need two different indexes, we have to make sure i*2==target doesn't return [i_index, i_index]
            if i + j == target and i_index != j_index:
                return [i_index, j_index]
    return []

print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
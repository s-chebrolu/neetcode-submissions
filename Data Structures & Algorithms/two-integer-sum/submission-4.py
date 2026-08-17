class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for idx, key in enumerate(hashmap.keys()):
            if target - key in hashmap.keys() and idx != hashmap[target - key]:
                return [idx, hashmap[target - key]]
        return []

        

        

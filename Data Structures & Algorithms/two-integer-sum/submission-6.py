class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return []
        arr = defaultdict(int)

        for ind, i in enumerate(nums):
            if target - i in arr.keys() and arr[target - i] != ind:
                return [arr[target - i], ind]
            arr[i] = ind
        return []

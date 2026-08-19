class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        
        count = self.k
        curr = self.nums[-self.k]
        # for i in range(len(self.nums) - 1, -1, -1):
        #     if self.nums[i] == curr:
        #         continue
        #     else:
        #         curr = self.nums[i]
        #         count -= 1
        #         if count == 0:
        #             return curr
        return curr

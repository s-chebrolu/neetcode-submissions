class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mane = [[] for i in range(len(nums) + 1)]
        temp = {}

        for i in nums:
            temp[i] = 1 + temp.get(i, 0)

        for x, y in temp.items():
            mane[y].append(x)
        
        res = []
        for i in range(len(mane) - 1, 0, -1):
            for num in mane[i]:
                res.append(num)
                if len(res) == k:
                    return res



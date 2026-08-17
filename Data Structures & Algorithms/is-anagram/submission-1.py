class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr1 = defaultdict(int)
        arr2 = defaultdict(int)

        for i in s:
            arr1[i] += 1
        
        for i in t:
            arr2[i] += 1
        
        if arr1 == arr2:
            return True
        else:
            return False
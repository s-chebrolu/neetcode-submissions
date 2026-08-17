from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = {}
            for i in word:
                count[i] = count.get(i, 0) + 1

            key = tuple(sorted(count.items()))
            res[key].append(word)
        return list(res.values())

        # words -> word -> dictionary of letter and occurances


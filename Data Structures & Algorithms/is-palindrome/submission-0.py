class Solution:
    def isPalindrome(self, s: str) -> bool:
        # temp = s.replace(" ", "").lower()

        start = 0
        end = len(s) - 1

        while start < end:
            if not (s[start].isalpha() or s[start].isnumeric()):
                start += 1
            elif not (s[end].isalpha() or s[end].isnumeric()):
                end -= 1
            else:
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                else:
                    return False
        return True


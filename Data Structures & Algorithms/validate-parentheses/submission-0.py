class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for n in s:
            if n == "(" or n == "[" or n == "{":
                arr.append(n)
            else:
                if len(arr) == 0:
                    return False
                letter = arr.pop()
                if letter == "(" and n != ")":
                    return False
                if letter == "[" and n != "]":
                    return False
                if letter == "{" and n != "}":
                    return False

        if len(arr) == 0:
            return True    
        else:
            return False
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        res = []
        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                res.append(s[i])
            else:
                mappedChar = mapping[s[i]]
                if len(res) > 0 and res.pop() == mappedChar:
                    continue
                else:
                    return False
        
        return len(res) == 0
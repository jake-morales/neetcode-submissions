class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        # Count the number of each character in s
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1

        # Iterate through t
        for c in t:
            temp = counts.get(c)
            if temp is None:
                return False
            elif temp == 0:
                return False
            else:
                counts[c] = temp - 1
        
        return True

                

        
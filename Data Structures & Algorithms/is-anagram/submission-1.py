class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        # Count the number of each character in s
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        # Iterate through t
        for char in t:
            freq = counts.get(char)
            if freq is None:
                return False
            elif freq == 0:
                return False
            else:
                counts[char] = freq - 1
        
        # If reached, then isAnagram
        return True

                

        
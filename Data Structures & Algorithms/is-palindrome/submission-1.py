class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize string
        normalized = ""
        for char in s:
            if char.isalnum():
                normalized += char.lower()

        # Iterate through half the array, checking both sides at the same time
        length = len(normalized)
        for i in range(length // 2):
            if normalized[i] != normalized[length-1-i]:
                return False

        return True
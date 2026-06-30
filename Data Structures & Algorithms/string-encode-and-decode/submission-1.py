class Solution:
    # 3 numbers denoting the length of the string, then the string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += f"{length:03d}{s}"

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while(i < len(s)):
            prefix = s[i:i+3]
            length = int(prefix)
            elem = s[i+3:i+3+length] # 005ABCDE
            res.append(elem)
            i += 3 + length

        return res


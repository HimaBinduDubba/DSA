class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res=""
        for i in range(len(s)):
            res=res+s[(i+k)%len(s)]
        return res    

        
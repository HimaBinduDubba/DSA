class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine=list(magazine)
        count=0
        for ch in ransomNote:
            if ch in magazine:
                magazine.remove(ch)
                count=count+1
        return count==len(ransomNote) 
        
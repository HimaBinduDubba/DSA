class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
          s=0
          while num:
            s=s+num%10
            num=num//10
          num=s  
        return num    

        
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        res=""
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) :
                res=res+i
        return res==res[::-1]            


       
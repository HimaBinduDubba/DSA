class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lis = []
        for i in s:
            if i != '-':
                lis.append(i.upper()) 

        first_group = len(lis) % k or k
        result = ''.join(lis[:first_group]) 

        for i in range(first_group, len(lis), k):
            result += '-' + ''.join(lis[i:i + k])  

        return result

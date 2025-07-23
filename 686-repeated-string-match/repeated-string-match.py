class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated=a
        count=1
        while len(repeated)<len(b):
            
            
           
           
            repeated=repeated+a
            count=count+1
        if b in repeated:
                return count   
        repeated=repeated+a
        if b in repeated:
            return count+1        
                 
        return -1   


                


        
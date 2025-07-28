class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=[]
        res=[]
        i=0;j=0
        while i<len(names) and j<len(heights):
            people.append((names[i],heights[i]))
            i=i+1
            j=j+1
        people.sort(key=lambda item: item[1], reverse=True)
        for key,value in people:
            res.append(key)
        return res    


        
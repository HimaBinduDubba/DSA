class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        units=0;size=0
        for box in boxTypes:
            if box[0]+size<truckSize:
                units=units+box[0]*box[1]
                size=size+box[0]
            else:
                unit=truckSize-size
                units=units+unit*box[1]  
                break  

        return units


        
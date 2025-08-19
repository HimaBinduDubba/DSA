class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,date=map(int,date.split("-"))
        total=0
        dates=[31,28,31,30,31,30,31,31,30,31,30,31]
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            dates[1]=29
        return total+sum(dates[:month-1])+date    

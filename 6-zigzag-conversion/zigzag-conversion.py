class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s
        current_row=0
        rows=["" for _ in range(numRows)]
        down=False
        for i in s:
            rows[current_row]=rows[current_row]+i
            if current_row==0 or current_row==numRows-1:
                down=not down
            if down:
                current_row=current_row+1
            else:
                current_row=current_row-1    
        return "".join(rows)            

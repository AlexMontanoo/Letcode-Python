class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        cols=len(grid[0])


        for row in grid:
            inicio, final=0, cols-1
            while inicio<=final:
                mid=(inicio+final)//2
                
                if row[mid]<0:
                    final=mid-1
                else:
                    inicio=mid+1
            
            count+= cols-inicio   
        return count
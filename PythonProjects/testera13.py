# Python program to count all possible paths  
# from top left to bottom right 
  
# Returns count of possible paths to reach cell  
# at row number m and column number n from the  
# topmost leftmost cell (cell at 1, 1) 
def numberOfPaths(m, n): 
    # Create a 2D table to store 
    # currentNums of subproblems 
    count = [[0 for x in range(m)] for y in range(n)] 

    # Count of paths to reach any  
    # cell in first column is 1 
    for i in range(m): 
        count[i][0] = 1; 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for j in range(n): 
        count[0][j] = 1;
    
    
    # Calculate count of paths for other 
    # cells in bottom-up  
    # manner using the recursive solution 
    for i in range(1, m): 
        for j in range(n):              
            count[i][j] = count[i-1][j] + count[i][j-1]
            printG(count)
    return count[m-1][n-1]  
def printG(lst):
    for i in range(len(lst)):
        print(lst[i])
    print("------")
n = 4
def MaximumPath(grid): 
    currentNum = 0
    storeValues = [[0 for i in range(n+2)] for j in range(n)] 
    for i in range(n): 
        for j in range(1, n+1): 
            storeValues[i][j] = max(storeValues[i-1][j-1],max(storeValues[i-1][j],storeValues[i-1][j+1])) + grid[i][j-1] 
  
    # Find maximum path sum that end ups 
    # at any column of last row 'N-1' 
    for i in range(n+1): 
        currentNum = max(currentNum, storeValues[n-1][i]) 
  
    # return maximum sum path 
    return currentNum 
  
# driver program to test above function 
def main():
    Mat = [[4, 2, 3, 4], [2, 9, 1, 10], [15, 1, 3, 0],[16, 92, 41, 44]] 
    print(MaximumPath(Mat))
main()

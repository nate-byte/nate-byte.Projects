#  File: Spiral.py

#  Description: A program that shows numbers around a spiral

#  Nate Eastwick


#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged
#          in a spiral
def create_spiral (dim):
    spiral = [[1 for i in range(dim)] for i in range(dim)] # Initialize List with 1's to account for the center
    # Finds Center
    vert = dim // 2
    horiz = dim // 2
    count = 2 # Begin at 2 because 1 has already been added
    # This loop will begin at 2 and count by two because the spiral is in square, the first constraint is 2, and it gets bigger by 2
    for i in range(2, dim, 2):
        # This will adjust the position to start one before where it will begin counting
        horiz += 1
        vert -= 1
        # This loop adds however many times in range according to dim
        for x in range(i): # Down right 
            vert += 1
            spiral[vert][horiz] = count
            count += 1
        for x in range(i): # Left bottom
            horiz -= 1
            spiral[vert][horiz] = count
            count += 1
        for x in range(i): # Up left
            vert -= 1
            spiral[vert][horiz] = count
            count += 1
        for x in range(i): # Right top
            horiz += 1
            spiral[vert][horiz] = count
            count += 1
    return spiral


#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid (grid, val):
    constraint = int(len(grid))
    horiz = 0
    verti = 0
    # Creat 3x3 grid of 0's
    newGrid = [[0 for i in range(3)] for i in range(3)]
    centerH = 1
    centerV = 1
    # Get Index
    for i in range(constraint):
        if val in grid[i]:
            horiz = grid[i].index(val)
            verti = i
    # Add center value
    newGrid[centerH][centerV] = grid[verti][horiz]
    # Add value to the left
    if check(horiz - 1,constraint):
        newGrid[centerH][centerV - 1] = grid[verti][horiz - 1]
    # Add value to the right
    if check(horiz + 1,constraint):
        newGrid[centerH][centerV + 1] = grid[verti][horiz + 1]
    # Add value above
    if check(verti - 1,constraint):
        newGrid[centerH - 1][centerV] = grid[verti - 1][horiz]
    # Add value above left
    if check(verti - 1,constraint) and check(horiz - 1,constraint):
        newGrid[centerH - 1][centerV - 1] = grid[verti - 1][horiz - 1]
    # Add value above right
    if check(verti - 1,constraint) and check(horiz + 1,constraint):
        newGrid[centerH - 1][centerV + 1] = grid[verti - 1][horiz + 1]
    # Add value below
    if check(verti + 1,constraint):
        newGrid[centerH + 1][centerV] = grid[verti + 1][horiz]
    # Add value below left
    if check(verti + 1,constraint) and check(horiz - 1,constraint):
        newGrid[centerH + 1][centerV - 1] = grid[verti + 1][horiz - 1]
    # Add value below right
    if check(verti + 1,constraint) and check(horiz + 1,constraint):
        newGrid[centerH + 1][centerV + 1] = grid[verti + 1][horiz + 1] 
    return newGrid
        

# This function checks to see if the value is acceptable 
def check(value,constraint):
    if value < 0:
        return False
    elif value > constraint - 1:
        return False
    else:
        return True

            
# This prints the grid
def printGrid(grid):
    for i in range(len(grid)):
        line = ""
        for x in range(len(grid[i])):
            if grid[i][x] == 0:
                None
            else:
                line += str(grid[i][x])
                line += " "
        if line != "":
            print(line)

            
def main():
    # prompt user to enter dimension of grid
    num = int(input("Enter dimension: "))
    # Check if it is odd
    if (num + 1) % 2 != 0:
        num += 1
    bigList = create_spiral(num)
    # prompt user to enter value in grid
    value = int(input("Enter number in spiral: "))
    # Check if it is in range
    if value < 1 or value > (num**2):
        print("Number not in range")
    else:
    # print subgrid surrounding the value
        print("")
        printGrid(sub_grid(bigList,value))
        print("")
if __name__ == "__main__":
      main()

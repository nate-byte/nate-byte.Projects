#  File: Queens.py

#  Description: Finds all possible solutions on a board for queens

#  Nate Eastwick


class Queens (object):
  # initialize the board
  def __init__ (self, n):
    self.board = []
    self.n = n
    self.numSolutions = 0
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()


  # checks if no queen captures another, I did this by using a list instead of the board
  def is_valid (self, qPlacements, row, col):
    for i in range(row):
      if qPlacements[i] == col:
        return False
      elif qPlacements[i] - i == col - row:
        return False
      elif qPlacements[i] + i == col + row:
        return False
    return True


  # do a recursive backtracking solution
  def recursive_solve (self, qPlacements, row):
    print(row)
    if row == self.n:
      self.placeTheQ(qPlacements)
      self.print_board()
      self.removeTheQ()
      print()
      self.numSolutions += 1
    else:
      for col in range(self.n):
        if self.is_valid(qPlacements,row,col):
          qPlacements[row] = col
          print(qPlacements)
          self.recursive_solve(qPlacements, row + 1)


  # if the problem has a solution print the board
  def solve (self, dim):
    qPlacements = [-1]*self.n
    print(qPlacements)
    self.recursive_solve(qPlacements,0)
    print("There are",self.numSolutions, "solutions for a",dim,"x",dim,"board.")
    

  # This takes in the location of the Queens and places them on the board
  def placeTheQ(self, qPlacements):
    for i in range(self.n):
      for x in range(self.n):
        if x == qPlacements[i]:
          self.board[i][x] = 'Q'

          
  # This removed the queens from the board
  def removeTheQ(self):
    for i in range(self.n):
      for x in range(self.n):
        if self.board[i][x] == 'Q':
          self.board[i][x] = '*'

    
def main():
  userIn = int(input("Enter the size of board: "))
  print()
  game = Queens (userIn)
  game.solve(userIn)
if __name__ == "__main__":
  main()


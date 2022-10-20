#  File: Pancake.py

#  Description: Program that sorts pancakes by flipping sections of a stack
 
#  Nate Eastwick and Caleb Campbell


# input list of pancakes - return list of ordered maxes for use in indexing
def find_max(stack):
  pancakeSize = stack
  maxLst = []
  while len(pancakeSize) != 0:
    currentMax = max(pancakeSize)
    maxLst.append(currentMax)
    pancakeSize.remove(currentMax)
  return maxLst


#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula 
#          this is a list of lists
#          the last item in this list is the sorted stack
def sort_pancakes ( pancakes ):
  every_flip = []
  currentList = []
  passLst = pancakes
  currentList += pancakes
  maxIndexes = find_max(passLst)
  for i in range(len(currentList)):
    # use maxIndexes[i] to index current largest pancake to flip
    largestPancake = maxIndexes[i]
    positionToFlip = currentList.index(largestPancake)
    if positionToFlip != 0:
      # get max pancake on top of stack
      stackToFlip = currentList[:positionToFlip + 1]
      stackUnflipped = currentList[positionToFlip + 1:]
      stackToFlip.reverse()
      currentList = stackToFlip + stackUnflipped
    # flip portion of stack that is currently unorganized
    flipperStack = currentList[:len(currentList)-i]
    flipperStack.reverse()
    # prevents unnecessary flip if largest pancake is at top
    if i == 0:
      organizedStack = []
    else:
      organizedStack = currentList[len(currentList)-i:]
    currentList = flipperStack + organizedStack
    every_flip.append(currentList)
  return every_flip


def main():
  # open the file pancakes.txt for reading
  in_file = open ("./pancakes.txt", "r")

  line = in_file.readline()
  line = line.strip()
  line = line.split()
  print (line)
  pancakes = []
  for item in line:
    pancakes.append (int(item))

  # print content of list before flipping
  print ("Initial Order of Pancakes = ", pancakes)

  # call the function to sort the pancakes
  every_flip = sort_pancakes ( pancakes )

  # print the contents of the pancake stack after
  # every flip
  for i in range (len(every_flip)):
    print (every_flip[i])

  # print content of list after all the flipping
  # print ("Final Order of Pancakes = ", every_flip[-1])

if __name__ == "__main__":
  main()


#  File: Work.py

#  Description: A program that displays how many lines of code is effective

# Nate Eastwick   

import time


# This is my helper function calculates how many lines can be coded
# using k productivity and v starting lines
def coffee(v,k):
  total = v
  value = None
  p = 1
  while value != 0:
    value = v // (k**p)
    p += 1
    total += value
  return total
    

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  for num in range(n):
    if coffee(num,k) >= n:
      return num
  

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  mid = n // 2
  # While loop here to keep it going
  check = True
  while check:
    if coffee(mid,k) >= n:
      return mid
      check = False
    elif coffee(mid,k) > n:
      mid -= 1
      if coffee(mid,k) >= n:
        return mid
        check = False
    else:
      mid += 1
      if coffee(mid,k) >= n:
        return mid
        check = False


# main has been completed for you
# do NOT change anything below this line
def main():
  in_file = open("work.txt", "r")
  num_cases = int((in_file.readline()).strip())

  for i in range(num_cases):
    inp = (in_file.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

    

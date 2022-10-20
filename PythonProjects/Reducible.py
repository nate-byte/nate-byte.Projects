#  File: Reducible.py 

#  Description: A program that reduces words.

#  Nate Eastwick


# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True


# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
  index = 0
  for j in range (len(s)):
    letter = ord(s[j]) - 96
    index = (index * 26 + letter) % size
  return index


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const):
  num = 0
  for i in range(len(s)):
    letter = ord(s[i]) - 96
    num = (num * 26 + letter) % const
  return (const - num)
                  

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
  size = len(hash_table)
  index = hash_word(s, size)
  if (hash_table[index] != ""):
    const = 13
    step = step_size(s, const)
    newIndex = index + step
    while (hash_table[newIndex] != ""):
      newIndex = newIndex + step
      newIndex = newIndex % size
    hash_table[newIndex] = s
  else:
    hash_table[index] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
  size = len (hash_table)
  index = hash_word (s, size)
  if (hash_table[index] == s):
    return True
  if (hash_table[index] == ""):
    return False
  const = 13
  step = step_size (s,const)
  newIndex = (index + step) % size
  while(True):
    if (hash_table[newIndex] == s):
      return True
    if (hash_table[newIndex] == ""):
      return False
    newIndex = (newIndex + step) % size


# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):
  # This is the break here
  if (len(s) == 1):
    if (containsVowel(s)):
      return True
    else:
      return False
  else:
    # This will check to see if it can even be fully reducable 
    if (not containsVowel(s) or not find_word(s, hash_table)):
      return False
    if (find_word(s, hash_memo)):
      return True
    # Passes all possible words within words
    for i in range(len(s)):
      sub = s[0:i] + s[i + 1:]
      if (is_reducible(sub, hash_table, hash_memo)):
        insert_word(sub, hash_memo)
        return True
    return False
  

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
  maximum = 0
  lst = []
  for i in string_list:
    if (len(i) > maximum):
      maximum = len(i)
      lst.clear()
      lst.append(i)
    elif (len(i) == maximum):
      lst.append(i)
  return lst


# this will return the correct prime number
def determinePrime (num):
  num = num * 2
  while is_prime(num) == False:
    num += 1
  return num


# retruns true if it contains a vowels a, i or o
def containsVowel (s):
  for l in s:
    if (l== 'a') or (l == 'i') or (l == 'o'):
      return True
  return False


def main():
  # create an empty word_list
  word_list = []
  # open the file words.txt
  file = open("words.txt","r")
  # read words from words.txt and append to word_list
  for line in file:
    line = line.strip()
    word_list.append(line)
  # close file words.txt
  file.close()
  # find length of word_list
  listLen = len(word_list)
  # determine prime number N that is greater than twice
  # the length of the word_list
  n = determinePrime(listLen)      
  # create an empty hash_list
  hash_list = []
  # populate the hash_list with N blank strings
  for i in range(n):
    hash_list.append("")
  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
    insert_word (word, hash_list)
  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  # populate the hash_memo with M blank strings
  m = 27000
  while (not is_prime(m)):
    m = m + 1
  for i in range(m):
    hash_memo.append("")
  # create an empty list reducible_words
  reducible_words = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    if (containsVowel(word) and is_reducible(word, hash_list, hash_memo)):
      reducible_words.append(word)
  # find words of the maximum length in reducible_words
  longestWords = get_longest_words(reducible_words)
  # print the words of maximum length in alphabetical order
  # one word per line
  for word in longestWords:
    print (word)
# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

#  File: TestCipher.py
 
#  Description: A program that encrypts/decrypts a string 
#  using either the rail fence encode or vigenere encode
 
#  Nate Eastwick and Caleb Campbell
 
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    # Create empty 2D list with as many inner list ("rails") as keys
    lst = [[] for i in range(key)]
    while 0 < len(strng):
        # Inserts all letters into each rail going diagonally down
        for railNumber in range(key):
            if len(strng) != 0:
                lst[railNumber].append(strng[0])
                # Splices string to remove letters inserted into lists
                strng = strng[1:]
        # Inserts all letters into each rail going diagonally up
        for railNumber in range(key - 2, 0, -1):
            if len(strng) != 0:
                lst[railNumber].append(strng[0])
                # Splices string to remove letters inserted into lists
                strng = strng[1:]
    # Joins letters in all rails into a encrypted string
    encryptedStrng = ''.join([i for sub in lst for i in sub])
    return encryptedStrng
 
 
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    # This creats a 2D lists based on keys
    encryptedNumberList = [[] for i in range(key)]
    stringList = []
    numberList = []
    # Creates a list of numbers and list of letters for comparison later
    for i in range(len(strng)):
        numberList.append(i)
        stringList.append(strng[i])
    # This will be a counter
    counter = 0
    # This loops will return a encrypted 2D list in the form of numbers
    while counter < len(strng):
        # These for loops count up and down the range of key
        for i in range(key):
            if counter < len(strng):
                encryptedNumberList[i].append(numberList[counter])
            counter += 1
        for j in range(key - 2, 0, -1):
            if counter < len(strng):
                encryptedNumberList[j].append(numberList[counter])
            counter += 1
    # This creates the new list of encrypted numbers
    encryptedList = []
    for i in range(key):
        for x in range(len(encryptedNumberList[i])):
            encryptedList.append(encryptedNumberList[i][x])
    # Combines encrypted numbers with the encrypted string chars from zip to dictionary
    compareZip = zip(encryptedList, stringList)
    dictOfEncryption = dict(compareZip)
    finalString = ""
    # Orders numbers into correct letter postions as decrypted string
    # by counting from 0 - length of strng
    for i in range(len(strng)):
        finalString += dictOfEncryption[i]
    return finalString
 
 
#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    return ''.join(i for i in strng if i.isalpha()).lower()
 
 
# Creates dictionary with key assignments as letters of the alphabet (a-z) and
# value assignments as numbers (0-25) that correspond to each letter ('a': 0)
def create_alphaDict():
    alphabetString = "abcdefghijklmnopqrstuvwxyz"
    alphaList = []
    numList = []
    # Appends each character of string in alphaList
    # Appends index of each character of string in numList 
    for i in range(len(alphabetString)):
        alphaList.append(alphabetString[i])
        numList.append(i)
    # Combines alphaList and numList into a dictionary (aplhaDict)
    alphaZip = zip(alphaList, numList)
    alphaDict = dict(alphaZip)
    return alphaDict
    
 
#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm.
def encode_character (p, s):
    alphabet = create_alphaDict()
    output = ''
    # Assigns number to each letter passed through (a=0, b=1, etc.) for s and p
    charNum = alphabet[s]
    passNum = alphabet[p]
    # Get encoded number that will correspond to encrypted number
    encodeNum = charNum + passNum
    # Performs math to ensure encodeNum value corresponds to correct letter
    if encodeNum > 25:
        encodeNum = encodeNum % 26
    # Assigns encodeNum to correct encrypted letter
    for key, value in alphabet.items():
        if value == encodeNum:
            output += key
    return output
 
 
#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    alphabet = create_alphaDict()
    output = ''
    # Assigns number to each letter passed through (a=0, b=1, etc.) for s and p
    charNum = alphabet[s]
    passNum = alphabet[p]
    # Get encoded number that will correspond to decrypted number
    encodeNum = charNum - passNum
    # Performs math to ensure encodeNum value corresponds to correct letter
    if encodeNum < 0:
        encodeNum += 26
    # Assigns encodeNum to correct encrypted letter
    for key, value in alphabet.items():
        if value == encodeNum:
            output += key
    return output
 
 
#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    # Filters string to lowercase and strips punctuation
    strng = filter_string(strng)
    newString = ""
    count = 0
    # Call on encode_character function for every character in string
    for i in range(len(strng)):
        newString += encode_character(phrase[count],strng[i])
        # Ensures passcode repeats itself for length of string
        if count == int(len(phrase)-1):
            count = 0
        else:
            count += 1
    return newString
 
 
#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    strng = filter_string(strng)
    newString = ""
    count = 0
    # Call on decode_character function for every character in string
    for i in range(len(strng)):
        newString += decode_character(phrase[count],strng[i])
        # Vnsures passcode repeats itself for length of string
        if count == int(len(phrase)-1):
            count = 0
        else:
            count += 1
    return newString
 
 
 
def main():
    # encrypt and print the plain text using rail fence cipher
    print("Rail Fence Cipher")
    print("")
    userTextRail = input("Enter Plain Text to be Encoded: ")
    while True:
        try:
            userKeyRail =  int(input("Enter Key: "))
            if userKeyRail < 2:
                userKeyRail = 2
                print("Key has been set to default minimum of 2.")
            print("Encoded Text:",rail_fence_encode(userTextRail, userKeyRail))
            print("")
            break
        except ValueError:
            print("Wrong type of value. Please enter a numeric digit.")
    # decrypt and print the encoded text using rail fence cipher
    userEncodedTextRail = input("Enter Encoded Text to be Decoded: ")
    while True:
        try:
            userEncodedKeyRail = int(input("Enter Key: "))
            if userKeyRail < 2:
                userKeyRail = 2
                print("Key has been set to default minimum of 2.")
            print("Decoded Plain Text:",rail_fence_decode(userEncodedTextRail, userEncodedKeyRail))
            print("")
            break
        except ValueError:
            print("Wrong type of value. Please enter a numeric digit.")
    # encrypt and print the plain text using Vigenere cipher
    print("Vigenere Cipher")
    print("")
    userTextVig = input("Enter Plain Text to be Encoded: ")
    while True:
        userPassVig = input("Enter Pass Phrase (no spaces allowed): ")
        if len(userPassVig) < len(userTextVig):
            break
        else:
            print("Pass code must be shorter in length than text to be encoded.")
    print("Encoded Text:",vigenere_encode(userTextVig,userPassVig))
    print("")
    # decrypt and print the encoded text using Vigenere cipher
    userEncodedTextVig = input("Enter Encoded Text to be Decoded: ")
    while True:
        userEncodedPassVig = input("Enter Pass Phrase (no spaces allowed): ")
        if len(userEncodedPassVig) < len(userEncodedTextVig):
            break
        else:
            print("Pass code must be shorter in length than text to be decoded.")
    print("Decoded Plain Text:",vigenere_decode(userEncodedTextVig,userEncodedPassVig))


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
 


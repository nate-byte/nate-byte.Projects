
#  File: BabyNames.py 

#  Description: A program that ranks baby names

#  Nate Eastwick   


class BabyNames(object):
    """Class to store all the baby names"""
    
    # Initializes the dictionary that will hold all the baby names
    def __init__(self):
        # key: name
        # value: list of ranks
        self.names = {}


    # Reads in the file and adds to the dictionary
    def fill_data(self, file_name):
            file = open(file_name,"r")
            for i in file:
                line = i.split()
                if len(line[0]) > 1:
                    self.names[line[0]] = line[1:]
                    

    # True if a name exists in the dictionary and False otherwise.
    def contains_name (self, name):
            if name in self.names:
                return True
            else:
                return False

            
    # Returns all the rankings for a given name. Assume the name exists
    def find_ranking(self, name):
        lst = self.names.get(name)
        intLst = []
        # Here I had to change the values to ints to compare value
        for i in range(len(lst)):
            intLst.append(int(lst[i]))
        return intLst
    

    # Returns a list of names that have a rank in all the decades in sorted order by name.
    def ranks_of_all_decades(self):
        newLst = []
        # This sorts through the dictionary based on names, then will add to list if there are no 0's present
        for name in self.names:
            if 0 not in self.find_ranking(name):
                newLst.append(name)
        return newLst

    
    #  Returns a list of all the names that have a rank in a given decade in order of rank.
    def ranks_of_a_decade(self, decade):
        nameList = []
        rankList = []
        finalList = []
        # Here I came up with this formula to get index, and I use that to determine rank
        indexPosition = getIndex(decade)
        for name in self.names:
            rank = self.find_ranking(name)[indexPosition]
            if rank != 0:
                nameList.append(name)
                rankList.append(rank)
        # I put both lists into a dictionary so I could resort
        zipThem = zip(nameList,rankList)
        tempDict = dict(zipThem)
        sortedDict = sorted((value, key) for (key,value) in tempDict.items())
        for key in sortedDict:
            finalList.append(key[1])
        return finalList


    # Return all names that are getting more popular in every decade. The list must be sorted by name.
    def getting_popular(self):
        newLst = []
        for name in self.names:
            ranks = self.find_ranking(name)
            counter = 0
            # Compared each value to the next, and if it has enough counts then it is increasing
            for i in range(len(ranks) - 1):
                if ranks[i] > ranks[i + 1]:
                    counter += 1
            if counter == len(ranks) - 1:
                newLst.append(name)
        return newLst

    
    # Return all names that are getting less popular in every decade. The list must be sorted by name.
    def less_popular(self):
        newLst = []
        for name in self.names:
            ranks = self.find_ranking(name)
            counter = 0
            # This is the reverse of the popular function
            for i in range(len(ranks) - 1):
                if ranks[i] < ranks[i + 1]:
                    counter += 1
            # Made an exception below so that names that are no longer ranked in the end still get counted
            if ranks[len(ranks)-1] == 0:
                counter += 1
            if counter == len(ranks) - 1:
                newLst.append(name)
        return newLst
                

# This is useful to get the correct year
def getDecade(lst):
        value = lst.index(min(lst))
        year = 0
        if 1900 + value*10 > 2000:
            year = 2000
        else:
            year = 1900 + value*10
        return year


# Made a function that return index based on year
def getIndex(year):
    return (int(year) % 1900) // 10


def main():
    babyNames = BabyNames()
    babyNames.fill_data("names.txt")
    exitLoop = True
    print("")
    # Main Loop 
    while exitLoop:
        print("Options:")
        print("Enter 1 to search for names.")
        print("Enter 2 to display data for one name.")
        print("Enter 3 to display all names that appear in only one decade.")
        print("Enter 4 to display all names that appear in all decades.")
        print("Enter 5 to display all names that are more popular in every decade.")
        print("Enter 6 to display all names that are less popular in every decade.")
        print("Enter 7 to quit.")
        print("")
        userInput = input("Enter choice: ")
        if userInput == '7':
            print("")
            print("Goodbye.")
            print("")
            exitLoop = False
        if userInput ==  '1':
            userInputName = input("Enter a name: ")
            value = babyNames.contains_name(userInputName)
            if value:
                rank = getDecade(babyNames.find_ranking(userInputName))
                print("The matches with their highest ranking decade are:")
                print(userInputName,rank)
                print("")
            else:
                print(userInputName,"does not appear in any decade.")
                print("")
        if userInput == '2':
            userInputName = input("Enter a Name: ")
            string = userInputName + ": "
            rankList = babyNames.find_ranking(userInputName)
            print("")
            for i in range(len(rankList)):
                string += str(rankList[i])
                string += " "
            print(string)
            year = 1900
            for i in range(len(rankList)):
                line = str(year) + ": " + str(rankList[i])
                print(line)
                year += 10
            print("")
        if userInput == '3':
            userInputYear = input("Enter decade: ")
            decadeNameList = babyNames.ranks_of_a_decade(userInputYear)
            print("The names are in order of rank:")
            for i in decadeNameList:
                rank = babyNames.find_ranking(i)[getIndex(userInputYear)]
                line = str(i) + ": " + str(rank)
                print(line)
        if userInput == '4':
            count = 0
            for i in babyNames.ranks_of_all_decades():
                count += 1
            print(count,"names appear in every decade. The names are:")
            for i in babyNames.ranks_of_all_decades():
                print(i)
            print("")
        if userInput == '5':
            count = 0
            for i in babyNames.getting_popular():
                count += 1
            print(count,"names are more popular in every decade. ")
            for i in babyNames.getting_popular():
                print(i)
            print("")
        if userInput == '6':
            count = 0
            for i in babyNames.less_popular():
                count += 1
            print(count,"names are less popular in every decade. ")
            for i in babyNames.less_popular():
                print(i)
            print("")

            
if __name__ == '__main__':
        main()



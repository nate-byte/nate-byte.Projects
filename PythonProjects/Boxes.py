
#  File: Boxes.py

#  Description: Find largest subset of boxes that fit within each other.

#  Nate Eastwick




# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  hi = len(box_list)
  if idx == hi:
    all_box_subsets.append(sub_set)
    return
  else:
    temp_subs = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, temp_subs, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
  for sub_set in all_box_subsets:
    current_nest = []
    for i in range(len(sub_set)):
      # checks that i is within appropriate range of sub_set
      if i < len(sub_set) - 1:
        # append first box in subset to temporary list
        if i == 0 and does_fit(sub_set[0], sub_set[0 + 1]):
          current_nest.append(sub_set[0])
        # append following boxe if it fits previous box
        if does_fit(sub_set[i], sub_set[i + 1]):
          current_nest.append(sub_set[i + 1])
        else:
          break
      # append temp list to all_nesting_boxes if size greater than current
      if len(current_nest) > largest_size:
        all_nesting_boxes *= 0
        all_nesting_boxes.append(current_nest)
        largest_size = len(current_nest)
        current_nest = []
      # append temp list to all_nesting_boxes if size = current and not already added
      elif len(current_nest) == largest_size and current_nest not in all_nesting_boxes:
        all_nesting_boxes.append(current_nest)
        current_nest = []
  return


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def main():
  # open the file for reading
  in_file = open ("./boxes.txt", "r")

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # print (box_list)
  # print()

  # sort the box list
  box_list.sort()
  # print (box_list)
  # print()

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # initialize the size of the largest sub-set of nesting boxes
  largest_size = 0

  # create a list to hold the largest subsets of nesting boxes
  all_nesting_boxes = []

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes)

  # print all the largest subset of boxes
  if len(all_nesting_boxes) < 2:
    print("No Nesting Boxes")
  else:
    print("Largest Subset of Nesting Boxes")
    for case in all_nesting_boxes:
      for box in case:
        print(box)
      print()
    

if __name__ == "__main__":
  main()


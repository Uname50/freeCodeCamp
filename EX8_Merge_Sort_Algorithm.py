# This exercise is aimed at practicing data structures by building the merge sort algorithm.

# This is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data. That is, it 'divides' a collection into smaller sub-parts, and 'conquers' the sub-parts by sorting them independently, then merges the sorted sub-parts.

# The merge sort algorithm mainly performs three actions:
# - Divide an unsorted sequence of items into sub-parts
# - Sort the items in the sub-parts
# - Merge the sorted sub-parts
# The above happens recursively until the sub-parts are merged into the complete sorted sequence. 

# create a function that will perform the sort on a data structure (DS)
def merge_sort(array):
    # find the middle point of the DS
    middle_point = len(array) // 2
    
    # initialize the left part
    left_part = array[:middle_point]
    
    # initialize the right part
    right_part = array[middle_point:]
    
    # use recursion to divide the DS until every element stands alone in its own list. A list with a single number is always sorted 
    merge_sort(left_part)
    merge_sort(right_part)

    # merge the parts into the original DS by comparing elements on both lists, and merging the smaller element to the main list. Repeat that for all the indexes in left_part and right_part
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # create a while loop that compares an element in left_part to an element in right_part, and merges the smaller element to the main array list. 
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        
        # check if the index of left_part is less than the index of right_part
        if left_part[left_array_index] < right_part[right_array_index]:
            
            # if True, it means that the element in the left_part list is smaller that the element it's being compared to in the right_part list. So, assign the left_part indes to the sorted array 
            
            array[sorted_index] = left_part[left_array_index]
            # increment the left_array_index index by 1
            left_array_index += 1 

        # create the instruction if the right_part is smaller
        else: 
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1

    # an element from the if-else loop will take an index in the sorted list array. move to the next free space for the next loop iteration 
    sorted_index += 1
        

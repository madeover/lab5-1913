# Lab 5, list partners here!
# CSCI 1913
# Izra Bereket
# Mohammed Dek Hussein



# LAB5 has a substantial written Q&A component as well. You answer these questions by updating the
# multi-line strings below to indicate your answer. It's a bit hokey, but it works.

# Question 1: Which image file you submitted covers which analysis case?
Answer1 = '''
backwards.csv = backwards.png
near_sorted.csv = near_sorted.png
random.csv = random.png
sorted_list = sorted.png
'''

# Question 2: For each algorithm, explain how you see it behaving in your images.
# If the algorithm's behavior differed case-by-case say this and explain how it behaved in each case.

Answer2_insertion = '''
In sorted_list the insertion line is a linear straight line
In near_sorted the insertion line isn't linear but it's following that pattern not constant
in random for insertion the line is growing but it still looks sort of random but still constant
backwards it's growing exponentially 
'''

Answer2_selection = '''
In sortedlist its growing positevly exponentially
in near sorted its growing positevly exponentially
in random its growing positively exponentially 
in backwards its growing positively exponentially 
'''

Answer2_merge = '''
in sorted list its growing linearally but no constant 
in near sorted its growing constant linearally 
in random It is a line growing constant linearally
in backwards It is a line growing constant linerally
'''


# Question 3: For each algorithm, What is the theoretical expectation. I.E. what is the expected big-O runtime behavior.
# If the algorithm's expected behavior differs case-by-case say this and explain how it is
# expected to behave case-by-case. (You should be able to find this information in the textbook.
# If not we will discuss this in class)

Answer3_insertion = '''
O(N) Would be the best case scenario if it is already sorted 
However if the list is flipped it would take even longer if its O(N^2)
'''

Answer3_selection = '''
O(N^2) It doesn't avoid any loops but in the worst case if the things are still similar
'''

Answer3_merge = '''
O(nlog(n)) Breaks the list in half and in half again repeating the process then rebuilds it by comparing
past elements used. It is still its own worst and best case scenario
'''


# Question 4: For each algorithm, How did the observed behavior match the theoretical behavior? Again, if your answer
# differs case by case, say that here and explain your findings for each case.

Answer4_insertion = '''
sorted list since it is already sorted this grows linear and in a straight path throoughout the graph
near sorted second closest to sorted list but since its close it can look as its 0(N) runtime
but it isnt since there are some elements that dont follow
random It follows mostly as if it was O(N) but there are cases where it isnt 
constant and has dips and cuts in the graph
backwards since its a curve its a O(N^2)
'''

Answer4_selection = '''
sorted list Since its an exponential curve it matched with the O(N^2) 
near sorted Since its an exponential curve it matched with the O(N^2)
random Since its an exponential curve it matched with the O(N^2)
backwards Since its an exponential curve it matched with the O(N^2)
'''

Answer4_merge = '''
sorted list Matched with a small curved up almost exponentially with the O(nlog(n))
near sorted Matched with a small curved up almost exponentially with the O(nlog(n))
random Matched with a small curved up almost exponentially with the O(nlog(n))
backwards Matched with a small curved up almost exponentially with the O(nlog(n))
'''


# Question 5: Merge sort is theoretically the fastest algorithm, are there
# cases where another algorithm might be faster?

Answer5 = '''
If the list is sorted then insertion sort would be the best case scenario for this specific use case 
'''


# Question 6: If you didn't know the order of data you might want to sort,
# what algorithm might you use to sort it, and why?

Answer6 = '''
Merge because as for most scenarios its runtime is the same and if we are flipping a coin
we won't know which we will need but most of the time this is the best option
'''






# Selection, Insertion, and Merge sorts -- taken from ZyBooks.
# Not too different, its still the same algorithm, they just did it using less memory than I did
# (Which leads to a slightly harder to understand piece of code)

def selection_sort(numbers):
    """Sort the list numbers in-place. (Note, this doesn't have to be numbers)"""
    count = 0
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            count += 1
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
     
    

        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
    return count
def insertion_sort(numbers):
    """Sort the list numbers in-place. (Note, this doesn't have to be numbers)"""
    count = 0
    for i in range(1, len(numbers)):
        count += 1
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] in correct position
        # KLUVER NOTE - PLEASE READ - so this line is a bit tricky. Technically, if j > 0 then numbers would not be compared
        #               to make things easier you can assume that every time the list condition is checked one array element
        #               comparison occurs. That is -- you can ignore the short-circuit evaluatio of the logical and in this
        #               counting problem.
        while j > 0 and numbers[j] < numbers[j - 1]:
            count += 1
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j = j - 1
    return count
def merge(numbers, i, j, k):
    """ Given two sorted sub-lists create one sorted list. This is done in-place, meaning we are given one list
    and expected to modify the list to be sorted. Furthermore, this operates on "sub-lists" (a specific range of the list)
    The list named numbers may contain other types of data than just numbers
    the variables i, j, and k are all indices into the numbers list
    So so the part of the list to be sorted is from position i to k (inclusive) with i to j being one sorted list, and j+1 to k being another."""
    merged_size = k - i + 1   #  Size of merged partition
    merged_numbers = []        #  Temporary list for merged numbers
    count = 0
    for l in range(merged_size):
        merged_numbers.append(0)

    merge_pos = 0      #  Position to insert merged number

    left_pos = i       #  Initialize left partition position
    right_pos = j + 1  #  Initialize right partition position

    #  Add smallest element from left or right partition to merged numbers
    while left_pos <= j and right_pos <= k:
        count += 1
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    #  If left partition is not empty, add remaining elements to merged numbers
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1
    #  If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    #  Copy merge number back to numbers
    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1
    return count
def merge_sort_recursive(numbers, i, k):
    """ Sort the sub-list in numbers from position i to k (inclusive)"""
    count = 0
    if i < k:
        j = (i + k) // 2  #  Find the midpoint in the partition

        #  Recursively sort left and right partitions
        # KLUVER NOTE - PLEASE READ - you should think about these two function calls as returning a count of
        #     comparisons. Naturally the comparisons done by those function-calls will count against this function-call.
        #     make sure you're not ignoring the return values on the following two lines.
        
        count += merge_sort_recursive(numbers, i, j)
        count += merge_sort_recursive(numbers, j + 1, k)

        #  Merge left and right partition in sorted order
        count += merge(numbers, i, j, k)
    return count 
def merge_sort(numbers):
    """ Sort a list of numbers

    This function is added on-top of the textbook's code to simply start the recursive process with the
    appropriate parameters. This also gives us a consistent sorting interface over the three sorts."""
   
    return merge_sort_recursive(numbers, 0, len(numbers)-1)


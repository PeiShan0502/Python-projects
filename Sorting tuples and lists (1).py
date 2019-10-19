###########
# Task 1a #
###########

def search(x, seq): 
    """Takes in a value x and a sorted sequence seq, and returns the position
       that x should go to such that the sequence remains sorted."""
    if not seq: 
        return 0
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i  # x should go to position i if x <= seq[i]
        return i+1        # if x is larger than all elements in the sequence,
                          # x should go to the back of the sequence
                          # so that the sequence remains sorted.


# The enumerate function takes in a sequence (either a list or a tuple)
# and returns an iteration of pairs, each of which contains the index of
# the element and the element itself.


print("## Q1a ##")
print(search(-5, (1, 5, 10)))
# => 0
print(search(3, (1, 5, 10)))
# => 1
print(search(7, [1, 5, 10]))
# => 2
print(search(5, (1, 5, 10)))
# => 1
print(search(42, [1, 5, 10]))
# => 3
print(search(42, (-5, 1, 3, 5, 7, 10)))
# => 6



###########
# Task 1b #
###########

def binary_search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
        position that x should go to such that the sequence remains sorted.
        Uses O(lg n) time complexity algorithm."""
    def helper(low, high):
        if low > high:
            return low
        elif x <= seq[0] or not seq:  # if x is less than or equal to first element of the sequence, or if sequence is empty,
            return 0                  # x should be in the front of the sequence (position indexed 0) 
        mid = (low+high)//2           # find middle point
        if x == seq[mid]:
            return mid
        elif x < seq[mid]:            # if x is smaller than the middle element of the sorted sequence, 
            return helper(low, mid-1) # look at left side of sorted sequence
        else:
            return helper(mid+1, high)# if x is larger, look at right side of sorted sequence
    return helper(0, len(seq)-1)  


print("## Q1b ##")
print(binary_search(-5, (1, 5, 10)))
# => 0
print(binary_search(3, (1, 5, 10)))
# => 1
print(binary_search(7, [1, 5, 10]))
# => 2
print(binary_search(5, (1, 5, 10)))
# => 1
print(binary_search(42, [1, 5, 10]))
# => 3
print(binary_search(42, (-5, 1, 3, 5, 7, 10)))
# => 6



###########
# Task 2a #
###########

def insert_list(x, lst):
    """ Inserts element x into list lst such that x is less than or equal
        to the next element, and returns the resulting list."""
    lst.insert(search(x, lst), x)  # lst.insert(<pos>,<element>)inserts element into position pos
    return lst                     # Use search function in Task 1a to get the position that x should be inserted into
                                   # such that the sequence remains sorted.

                                   
print("## Q2a ##")
print(insert_list(2, [1, 5, 9]))
#=> [1, 2, 5, 9]
print(insert_list(10, [1, 5, 9]))
#=> [1, 5, 9, 10]
print(insert_list(5, [2, 6, 8]))
#=> [2, 5, 6, 8]



###########
# Task 2b #
###########

def insert_tup(x, tup):
    """ Inserts element x into tuple tup such that x is less than or equal
        to the next element, and returns the resulting tuple."""
    i = search(x, tup)              # i is the position that element x should be inserted into
    return tup[:i] + (x,) + tup[i:] # tuple concatenation to insert x as tuples are immutable. 


print("## Q2b ##")
print(insert_tup(2, (1, 5, 9)))
#=> (1, 2, 5, 9)
print(insert_tup(10, (1, 5, 9)))
#=> (1, 5, 9, 10)
print(insert_tup(5, (2, 6, 8)))
#=> (2, 5, 6, 8)



###########
# Task 2c #
###########

tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)

print("## Q2c ##")
print(tup is output_tup)
#=> Output: False
print(tup == output_tup)
#=> Output: False

# Reason: Tuples are immutable.

print(lst is output_lst)
#=> Output: True
print(lst == output_lst)
#=> Output: True

# Reason: Lists are mutable. 



###########
# Task 3a #
###########

def sort_list(lst):
    """ Sorts list lst in an ascending order."""
    l = []                       # start with empty list
    for elem in lst:
        l = insert_list(elem, l) # insert elements in ascending order in l 
    return l
        

print("## Q3a ##")
print(sort_list([9, 6, 2, 4, 5]))
#=> [2, 4, 5, 6, 9]
print(sort_list([42, 7, 6, -42, 0]))
#=> [-42, 0, 6, 7, 42]
print(sort_list(["soda", "cola", "sprite", "root beer", "apple cider"]))
#=> ['apple cider', 'cola', 'root beer', 'soda', 'sprite']
print(sort_list(["turtle", "penguin", "dog", "cat", "ant eater", "butterfly"]))
#=> ['ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle']



###########
# Task 3b #
###########

def sort_tup(tup):
    """ Sorts tuple tup in an ascending order."""
    t = ()                      # start with empty tuple
    for elem in tup:
        t = insert_tup(elem, t) # insert elements in ascending order in t 
    return t
        

print("## Q3b ##")
print(sort_tup((9, 6, 2, 4, 5)))
#=> (2, 4, 5, 6, 9)
print(sort_tup((42, 7, 6, -42, 0)))
#=> (-42, 0, 6, 7, 42)
print(sort_tup(("soda", "cola", "sprite", "root beer", "apple cider")))
#=> ('apple cider', 'cola', 'root beer', 'soda', 'sprite')
print(sort_tup(("turtle", "penguin", "dog", "cat", "ant eater", "butterfly")))
#=> ('ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle')


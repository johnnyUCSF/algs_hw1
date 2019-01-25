######################################################
###########################bubblesort#################
######################################################
def swapsort(test):
    edited = False
    for i in range((len(test)-1)):
        if test[i] > test[i+1]:
            tmp = test[i]
            test[i] = test[i+1]
            test[i+1] = tmp
            edited = True
    return test, edited
 
def bubblesort(array):
    edited = True
    while edited == True:
        array, edited = swapsort(array)
    return array

######################################################
###########################quicksort##################
######################################################
def swappity(array,left,right):
    ####used for easy swapping by element
    #print(array)
    tmp = array[left]
    array[left] = array[right]
    array[right] = tmp
    #print(array)
    
def recurse(array,first,last):
    ####first and last just to keep things from getting screwy
    if last > first:
        ####find the new separator for the two new lists
        sep = split_compare(first,last,array)
        ####continue processing two sides after you know which element to split on
        right_start = 1+sep
        left_end = -1+sep
        ####recurse
        recurse(array,right_start,last)
        recurse(array,first,left_end)

def split_compare(first,last,array):
    ###define values; remember first has changed by this point
    #print(array)
    left = 1+first
    right = last
    pivot = array[first]
    while True:
        #print(array)
        ### find indices to swap by testing coming into the middle element from both sides
        while left <= right and array[left] <= pivot:
            #print(left,pivot)
            left +=1
        while array[right] >= pivot and right >= left:
            #print(pivot)
            right -= 1
        ###test if right and left pointers have crossed
        if left > right:
            break
        swappity(array,left,right)
    swappity(array,first,right)
    ####return the right pointer because it points to last element of leftside new list
    return right

def quicksort(array):
    ##this is the main function
    ####need to recurse!!
    ####since python everything will be modified in reference, no need to create two new lists
    last = len(array)-1
    ###
    recurse(array,0,last)
    return(array)
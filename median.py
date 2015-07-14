##Script Name: median.py
##Author: Ameet Bora
##Description: This script will take a list of numbers from a text file
##             called input.txt. It will parse through the list and add the
##             number into a growing list variable and calculate the median.
##             This will continue until there are no numbers to parse.
"""This part will first sort the list and then calculate the median of the list"""
def median(list):
    lst = sorted(list)
    """Print the Sorted List"""
    print "Sorted List"
    print lst,"\n"
    index = len(lst)//2
    """Calculate the median of the input list"""
    if len(lst)<1:
        return None
    if len(lst)%2 == 1:
        return lst[index]
    else:
        return (lst[index-1]+lst[index])/2.0

"""Two Empty list to hold down numbers"""
list1 = []    
list2 = []
input_file = open("input.txt","r")
list_input = input_file.read().split(',')
#print list_input
for i in list_input:
    if i == '':
        break
    list1.append(int(i))
for i in list1:
    list2.append(i)
    """Print the Number List"""
    print "Numbers read"
    print list2
    res = median(list2)
    """Print the median"""
    print "Median :", res
    print "\n"



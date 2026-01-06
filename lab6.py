# # 1.	Take a sample list [2, 1, 3, 5, 4, 3, 8]
# # 1.	Apply del(), remove(), sort(), insert(), pop(), extend()…)


# s_list = [2, 1, 3, 5, 4, 3, 8]
# del s_list[2]
# print("The list after deleting 2nd index element become :",s_list)
#
# #remove
# s_list = [2, 1, 3, 5, 4, 3, 8]
# s_list.remove(4)
# print("The list after removing 4 becomes:",s_list)
#
# #sort():
# s_list = [2, 1, 3, 5, 4, 3, 8]
# s_list.sort()
# print("The list after sorting becomes:",s_list)
#
# # insert:
# s_list = [2, 1, 3, 5, 4, 3, 8]
# s_list.insert(2,4)
# print("The list after inserting 4 on index 2 is:",s_list)
#
#  #pop()
# s_list = [2, 1, 3, 5, 4, 3, 8]
# s_list.pop()
# print("The list after poping becomes",s_list)
#
# #extend:
# s_list = [2, 1, 3, 5, 4, 3, 8]
# s_list2 = [34,56,88,99,100]
# s_list.extend(s_list2)
# print("The list after exding the list with s_list2 becomes",s_list)


# import math
# #given data:
# #part a:
# length_1 = 16  #length in feet
# angle_a_deg = 75  #angle in degree
# angle_a_rad = math.radians(angle_a_deg)  # angle in radians
#
# #part b:
# length_2 = 20         # length in feet
# angle_b_deg = 0           # angle in degree
# angle_b_rad = math.radians(angle_b_deg)       #angle in radians
#
# #part c:
# length_3 = 24       # length in feet
# angle_c_deg = 45          # angle in degree
# angle_c_rad = math.radians(angle_c_deg)       # angle in radians
#
# # part d:
# length_4 = 24       # length in feet
# angle_d_deg = 80         # angle in degree
# angle_d_rad = math.radians(angle_d_deg)     # angle in radians
#
# #solution
# # for height:
#
# #height = length * math.sin(angle)
#
# height_1 = length_1 * math.sin(angle_a_rad)
# height_2 = length_2 * math.sin(angle_b_rad)
# height_3 = length_3 * math.sin(angle_c_rad)
# height_4 = length_4 * math.sin(angle_d_rad)
#
# # printing the results:
# print("The height of part a is :",height_1,"feet")
# print("The height of part b is :",height_2,"feet")
# print("The height of part c is :",height_3,"feet")
# print("The height of part d  is :",height_4,"feet")





# #Write the relevant Python expression or statement, involving a list of numbers lst and using
# # list operators and methods for these speciﬁcations:
# # (a)An expression that evaluates to the index of the middle element of lst
# # (b)An expression that evaluates to the middle element of lst
# # (c)A statement that sorts the list lst in descending order
# # (d)A statement that removes the ﬁrst number of list lst and puts it at the end
# # Note: If a list has even length, then the middle element is deﬁned to be the rightmost of
# # the two elements in the middle of the list.
#
#
#
# lst = [1,2,3,4,5,6,7,73,7,3,6]
# y = lst.index(len(lst)//2)
# print(y)
# z = len(lst)//2
# print(z)
# lst.sort(reverse=True)
# print(lst)
# lst.append(lst.pop(0))
# print(lst)

#
# #4.   Start by assigning to variables monthsL and monthsT a list and a tuple, respectively,
# # both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order.
# # Then attempt the following with both containers:
# # (a)Insert string 'Apr' between 'Mar' and 'May'. (b)Append string 'Jun'.
# # (c)Pop the container.
# # (d)Remove the second item in the container. (e)Reverse the order of items in the container.
#
# monthL = ['Jan', 'Feb', 'Mar','May']
# monthT = ('Jan', 'Feb', 'Mar','May')
#
# #insering apr b/w mar and may in list
# monthL.insert(3,'Apr')
# print("Inserting 'Apr' between Mar and May in list :",monthL)
#
# #inserting apr b/w mar and may in tuple
# monthL_2 = list(monthT)
# monthL_2.insert(3,'Apr')
# monthT = tuple(monthL_2)
# print("Inserting 'Apr' between Mar and May in tuple :",monthT)
#
#
# #appending Jun in list
# monthL.append('Jun')
# print("List after appending Jun",monthL)
#
# #appending Jun in tuple:
# monthL_2 = list(monthT)
# monthL_2.append('Jun')
# monthT = tuple(monthL_2)
# print("Tuple after appending Jun",monthT)
#
# #poping list:
# monthL.pop()
# print("List after using pop method:",monthL)
#
# #poping tuple:
# monthL_2 = list(monthT)
# monthL_2.pop()
# monthT = tuple(monthL_2)
# print("Tuple after using pop method :",monthT)
#
#
# # removing 2nd item in list
# monthL.remove(monthL[1])
# print("List after removing 2nd item :",monthL)
#
# #removing 2nd item in tuple
# monthL_2 = list(monthT)
# monthL_2.remove(monthL_2[1])
# monthT = tuple(monthL_2)
# print("Tuple after removing 2nd item :",monthT)
#
# #sorting list in reverse order
# monthL.sort(reverse=True)
# print("List after sorting in reverseorder:",monthL)
#
# #sorting tuple in reverse order:
# monthL_2 = list(monthT)
# monthL_2.sort(reverse=True)
# monthT = tuple(monthL_2)
# print("Tuple after sorting in reverse order: ",monthT)
#
# #sorting list
# monthL.sort()
# print("list after sorting becomes: ",monthL)
#
# #sorting tuple
# monthL_2 = list(monthT)
# monthL_2.sort()
# monthT = tuple(monthL_2)
# print("Tuple after sorting becomes: ",monthT)
#
# # 6.   Write the corresponding Python assignment statements:
# # (a)Assign 6 to variable a and 7 to variable b.
# # (b)Assign to variable c the average of variables a and b.
# # (c)Assign to variable inventory the list containing strings 'paper', 'staples', and 'pencils'.
# # (d)Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy'.
# # (e)Assign to variable fullname the concatenation of string variables first, middle, and last.
# # Make sure you incorporate blank spaces appropriately.
#
a = 6
b = 7
c = (a + b)/2
inventory = ['paper', 'staples','pencils']
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
fullname = first + " " + middle + " " + last
#
#
#
#

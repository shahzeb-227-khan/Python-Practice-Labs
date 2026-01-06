# printing odd numbers using while loop:
# starting_limit = 0
# ending_limit = 100
# i = 0
# while starting_limit <= i < ending_limit:
#     i = i + 1
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# Q.2 Write down a Python Program using While loop to generate the following outputs
#
#
# a)	             **************
#              **************
#              **************
#              **************
#                                                 **************
#              			**************
#             		             **************
#              			**************

# r1 = 4
# r2 = 9
# i = 1
# while i <= r2:
#     while i <= r1:
#         print("**************")
#         i = i + 1
#     i = i + 1
#     while i >= 4 and i <= r2:
#         print("                                   **************")
#         i = i + 1
#     i = i + 1


# b)	 *
#      **
#      ***
#      ****
#      *****
#      ******
#      *******
#      ********

#
# row = 8
# i = 0
# while i <= row:
#     j = i + 1
#     while j >0 :
#         print("*",end="")
#         j = j -  1
#     i = i + 1
#     print()
#

# rows = 7
# i = 0
# while (i < rows):
#     stars = rows - i
#     while (stars >=1 ):
#         print("*",end="")
#         stars = stars - 1
#     i = i + 1
#     print()


#3)Write down a python program having one
# function for calculating factorial of a no And call that function within a While loop to
# generate factorial of numbers from 0 to 10

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

i = -1
n = 10
while (i < n) :
    i = i + 1
    print(f"The factorial of {i} is :",fact(i))








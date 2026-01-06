# try:
#   print(x)
# except:
#   print("An exception occurred")
# list = [1,2,234,4,5,6]
# print(list)
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except ValueError:
#   print("Something else went wrong")
# else:
#     print("everything went wrong")
# finally:
#     print("try and except completed")
#The try block will raise an error when trying to write to a read-only file:

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
#
# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


#quest 1
list1 = [10, 20, 30,45]
list2 = [5, 0, 10, 2]
try:
    result = []
    for i in range(len(list1)):
        division = list1[i] / list2[i]
        result.append(division)
except IndexError:
    print("Sorry the index is out of range.")
except ZeroDivisionError:
    print("You cannot divide any number by zero.")

#ques 2
try:
    fact = 1
    n = int(input("Enter a number to calculate factorial"))
    for i in range(1,n + 1):
        fact = fact * i
        print(fact)
except EOFError:
    print("End of line error occured")


#ques 3
try:
    import kim.py
except IndentationError as e:
    print("Please correct the identation mistake")


#ques 4
# Design a python program to demonstrate IOError by using Try-Except Block.
try:
    with open("inputouput.py",'r') as f:
        f.read()
except IOError:
    print("Sorry the file you are accessing does not exist!")
















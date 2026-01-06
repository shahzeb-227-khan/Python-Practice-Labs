#question4
provinces_tuple = ()
list1 = list(provinces_tuple)
for i in range(4):
    provinces = input("Enter name of provinces: ")
    list1.append(provinces)
list1 = tuple(list1)
print(list1)

#question5:
monthL = ['Jan', 'Feb', 'Mar','May']
monthT = ('Jan', 'Feb', 'Mar','May')

#insering apr b/w mar and may in list
monthL.insert(3,'Apr')
print("Inserting 'Apr' between Mar and May in list :",monthL)

#inserting apr b/w mar and may in tuple
monthL_2 = list(monthT)
monthL_2.insert(3,'Apr')
monthT = tuple(monthL_2)
print("Inserting 'Apr' between Mar and May in tuple :",monthT)

#appending Jun in list
monthL.append('Jun')
print("List after appending Jun",monthL)

#appending Jun in tuple:
monthL_2 = list(monthT)
monthL_2.append('Jun')
monthT = tuple(monthL_2)
print("List after appending Jun",monthT)

#poping list:
monthL.pop()
print("List after using pop method:",monthL)

#poping tuple:
monthL_2 = list(monthT)
monthL_2.pop()
monthT = tuple(monthL_2)
print("Tuple after using pop method :",monthT)


# removing 2nd item in list
monthL.remove(monthL[1])
print("List after removing 2nd item :",monthL)

#removing 2nd item in tuple
monthL_2 = list(monthT)
monthL_2.remove(monthL_2[1])
monthT = tuple(monthL_2)
print("Tuple after removing 2nd item :",monthT)

#sorting list in descending order
monthL.sort(reverse=True)
print("List after sorting in descending order:",monthL)

#sorting tuple in descending order:
monthL_2 = list(monthT)
monthL_2.sort(reverse=True)
monthT = tuple(monthL_2)
print("Tuple after sorting in descending order: ",monthT)

#sorting list
monthL.sort()
print("list after sorting becomes: ",monthL)

#sorting tuple
monthL_2 = list(monthT)
monthL_2.sort()
monthT = tuple(monthL_2)
print("Tuple after sorting becomes: ",monthT)


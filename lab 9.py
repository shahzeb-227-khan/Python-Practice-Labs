# family = {
# 'Father':{
#     'Name':'Muneer alam',
#     'Occupation':'Business',
#     'Age':50,
#     'height':5.7
#     },
# 'Mother':{
#     'name':'Saima muneer',
#     'Occupation':'House wife',
#     'Age':48,
#     'Height':5.5
#     },
# 'Brother':{
#     'name':'Shahameer alam',
#     'occupation':'Student',
#     'Age':21,
#     'Height':5.7
#     },
# 'Sister':0
# }
# family['Grand parents'] = {'Maternal':{'Grand father':'Jan e alam','Grand mother':'Razia begum'},
#                                           'Paternal':{'Grand father':'Tauseeq ahmed','Grand mother':'Tahseen bano'}}
# # family['Uncles'] = {'Maternal':['Sohail','Yasir','raheel'],
# #                              'Paternal':['Junaid','owias','zaheer','saleem']}
# # family['Aunties'] = {'Maternal':['Ifrah','Sana','Asma'],
# #                                 'Paternal':['Tasneem']}
# # print(family)
#
#
# # Write a function to design a personal phone directory of your parents and friends. You
# # must add 12 members. Then make a function to delete a member from a
# # telephone directory. Print total number of members in your personal phone directory.
#
# contact_diary = {}
# def add_num():
#     for i in range(12):
#         name = input("Enter the person's name :")
#         number = int(input(f"Enter  {name} phone number: "))
#         contact_diary[name] = number
# def del_num():
#     item = input("enter a name to delete")
#     if item in contact_diary:
#         contact_diary.pop(item, None)
#         print(f"{item} has been deleted from contact diary")
#     else:
#         print(f"{item} is not in the contact diary")
#     return contact_diary
# add_num()
# print(del_num())
# print("The total number of members in your contact diary is:",len(contact_diary))
#
#

# Write a function hexASCII() that prints the correspondence between the lowercase
# characters in the alphabet and the hexadecimal representation of their ASCII code. Note:
# [A format string and the format string method can be used to represent a number value
# in hex notation.]
# def hexASCII():
#     alphabets = "abcdefghijklmnopqrstuvwxyz"
#     for i in alphabets:
#         print(i,"=",hex(ord(i)),end="\t|\t")
# hexASCII()


# Create double dictionaries one of which is your choice of dishes. Other one is dishes
# cooked
# in a week. Compare them and find how many dishes you will get of your choice to be
# cooked in next week. Print the name of those dishes as well.

fav_dishes = {'choosen_dishes': ['Biryani', 'Korma', 'nihari', 'pizza', 'chinese', 'aloo gosht', 'Paye', 'Burger', 'Palak']}
cooked_dishes = {'cooked': ['chinese', 'Palak', 'nihari', 'Korma']}
next_week_dishes = []
for dish in fav_dishes['choosen_dishes']:
    if dish in cooked_dishes['cooked']:
        continue
    else:
        next_week_dishes.append(dish)
print("The dishes of your choice to be made next week are:", next_week_dishes)
print("The number of your choice dishes to be made next week are:", len(next_week_dishes))


# Design a list of guests with family members on your sister wedding. Each family members
# must be counted. Your parents have made a list of guests and you have made another list.
# At the end compare both the list and find the common guests which both of you have
# invited and count them once. The program will return the number of guest with members
# and total number of guest. Use functions to perform the required actions.
def count_family(guest_list):
    count = 0
    for family_members in guest_list.values():
        count += len(family_members)
    print("Total family members are:", count)

def common_guest(parents_list, my_list):
    common = set(parents_list['parents guest']) & set(my_list['my guest'])
    return list(common)

def total_guests(parents_list, my_list):
    return len(set(parents_list['parents guest'] + my_list['my guest']))

family = {'family members': ['mama', 'baba', 'khala', 'sajid bhai', 'bhai']}
my_list = {'my guest': ['mama', 'baba', 'bhai', 'khala', 'munni baji', 'shammi baji', 'basheer bhai', 'sajid bhai', 'abdul karim', 'saad bhai']}
parents_list = {'parents guest': ['shakeela baji', 'sharma uncle', 'rukhsana aunty', 'kashmala baji', 'sajid bhai', 'basheer bhai', 'munni baji']}

count_family(family)
common_guest_list = common_guest(parents_list, my_list)
print("Common guests:", common_guest_list)
print("Total number of guests:", total_guests(parents_list, my_list))

























# for x,y in family.items():
#     print(x,':',y)
#
# family.update()
#
# print(family['Father'])
# print(family['Mother'])
# print(family['Brother'])
# print(family['Sister'])
#
# for x in family:
#     print(family[x])
#
# if 'Father' in family.keys():
#     print("Yes father is in family")
#
# family['Brother'] = 'aliyan'
# family['Sister'] = 'bilal'
# print(family)
#
# family['aunties'] = 'ifrah'
# family['uncles'] = 'owais'
# print(family)
#
# y = family.pop('Brother')
# z = family.pop('Sister')
# print(y,z)
#
# try:
#     del family['Brother']
#     print(family)
# except:
#     print("there is no brother")
#
# family.popitem()
# print(family)
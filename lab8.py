# # Write a program which will add your best five students name in a set. You will use a loop
# # to insert names in set.
#
# best_friends = set()
# for i in range(5):
#     friends = input("enter your best friends names")
#     best_friends.add(friends)
# print(best_friends)
#
#
# friends = {'furqan','abdul wahab','murtaza','danial','shaheer','umar'}
# friends_left_ned = {'danial','shaheer','umar'}
# friends = friends.difference(friends_left_ned)
# print(friends)
#

# items = {"rice", "spices", "milk", "chocolate", "juice"}
# prices = []
# for i in range(len(items)):
#     z = items.pop()
#     price = int(input(f"Enter price for {z}: "))
#     prices.append(price)
#
# print(f"-------------------------------------TOTAL BILL : {sum(prices)}   --------------------------------")
# print("The maximum amount of item sold is:",max(prices))
# print("The minimum amount of item sold is:",min(prices))


# Write a program which will add your best dishes and then pop one by one until the set is
# empty.
# #
# best_dishes = set()
# n = int(input("Enter your number of favourite dishes: "))
# for i in range(n):
#     dish = input("enter your best dish:")
#     best_dishes.add(dish)
# print(f"Your best dishes are: {best_dishes}")
# while best_dishes:
#     popped_dishes = best_dishes.pop()
#     print(f"Popped dish is: {popped_dishes}")
# print(f"Now Your best dishes are: {best_dishes}")



# Write a program which will compare two sets, Set A and Set B. Both the sets have some students
# who love to play one is hockey and other one is cricket. 10 of them play both. Now using sets find
# how many of them are playing cricket only, if universal set is 40, students who play hockey are
# 21.
universal = set(range(1,41))
hockey_players = set(range(1,22))
both = set(range(1,11))

cricket_player = universal.difference(hockey_players)

print("Total players are",len(universal))
print("Player who play both cricket and hockey",len(both))
print("Players who play only cricket are:",len(cricket_player))
print("Players who play only hockey are:",len(hockey_players.difference(both)))


#program 5:
# Define sets for purchases
dog = set(range(1, 84))
cat = set(range(47, 148))
fish = set(range(72, 78)) | set(range(138, 154)) | set(range(1, 9))
other = set(range(155, 189))

# Calculate sets for exclusive purchases
only_dog = dog - (cat | fish | other)
only_cat = cat - (dog | fish | other)
only_fish = fish - (dog | cat | other)
dog_or_fish = dog | fish - (cat | other)
total_purchases = dog | cat | fish | other

# Display the results
print("People who purchased only dog products:", len(only_dog))
print("People who purchased only cat products:", len(only_cat))
print("People who purchased a dog or a fish product:", len(dog_or_fish))
print("Total purchases:", len(total_purchases))


# Q7
totalStudents=110
englishSpeakers=75
frenchSpeakers=50
spanishSpeakers=52
english_french_Speakers=30
english_spanish_Speakers=33
french_spanish_Speakers=22
english_french_spanish_Speakers=13

englishOnly=englishSpeakers-english_french_Speakers-english_spanish_Speakers+english_french_spanish_Speakers
frenchOnly=frenchSpeakers-english_french_Speakers-french_spanish_Speakers+english_french_spanish_Speakers
spanishOnly=spanishSpeakers-english_spanish_Speakers-french_spanish_Speakers+english_french_spanish_Speakers

english_spanishOnly=englishOnly+spanishOnly+english_spanish_Speakers-english_french_spanish_Speakers
noLang=totalStudents-frenchSpeakers-english_spanishOnly
anyTwolangSpeakers=english_french_Speakers+english_spanish_Speakers+french_spanish_Speakers-(english_french_spanish_Speakers)*3
print("The no of students who can speak English and Spanish but not French are:",english_spanishOnly)
print("The students who speak Neither English, Spanish, nor French are:",noLang)
print("The students who can speak French, but neither English nor Spanish are:",frenchOnly)
print("The students who can speak Only one of the three languages are:",frenchOnly+spanishOnly+englishOnly)
print("The students who can speak Exactly two of the three languages are:",anyTwolangSpeakers)



























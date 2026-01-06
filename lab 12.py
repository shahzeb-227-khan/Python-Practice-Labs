# import random
# print(random())
#
# print(random.randint(1,1000))
# print(random.uniform(1,1000))
#
# items = [1,2,3,4,5,6]
# random.shuffle(items)
# print(items)
#
# # items = [1,2,3,4,5,6,7,8,9]
# # x = random.sample(items,1)
# # print(x[0])
# # x += random.sample(items,4)
# # print(x)
# # print(random.randrange(1,100,1))
# # #start,stop,step (1-99)
# # names=['ali','mushtaq','marine','munddi']
# # random.choice(names)

#ques 1
import random

cities = ['karachi','hyderabad','lahore','peshawar','faislabad','pindi']
random.shuffle(cities)
print(cities)

#ques 2
list_of_students = ['shahzeb','abdul karim','abdul wahab','furqan','abdullah','tooba','batool']
list_of_students.pop()
list_of_new_Students = list_of_students.copy()
scholarship_winner1=random.choice(list_of_new_Students)
scholarship_winner2=random.choice(list_of_new_Students)
print(f"Congratulations {scholarship_winner1} on getting scholarship")
print(f"Congratulations {scholarship_winner2} on getting scholarship")

#ques 3

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
inputs = int(input("How many times you want to roll the dice?"))
for i in range(inputs):
    player1_turn1 = random.choice(dice1)
    player1_turn2 = random.choice(dice1)
    player1_score = player1_turn1 + player1_turn2
    player2_turn1 = random.choice(dice2)
    player2_turn2 = random.choice(dice2)
    player2_score = player2_turn1 + player2_turn2
    print(f"PLayer 1 You rolled the dice and got {player1_turn1} and {player1_turn2}")
    print(f"PLayer 2 You rolled the dice and got {player2_turn1} and {player2_turn2}")
    if player1_score > player2_score:
        print("Congratulation player 1 ! You won the match")
    elif player2_score > player1_score:
        print("Congratulation player 2! You won the match")
    elif player1_score == player2_score:
        print("Draw")


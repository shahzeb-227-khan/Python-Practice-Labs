# def file_open(file):
#     try:
#         with open(file,"r") as f:
#             data = f.read()
#             lines = data.split("\n")
#             words = data.split()
#             count_l = 0
#             for word in words:
#                 count_l += len(word)
#             print("Total lines are",len(lines))
#             print("Total words are",len(words))
#             print("Total letter are",count_l)
#     except FileNotFoundError:
#         print("You entered an invalid file name")
# file = input("Please enter a valid file name: ")
# file_open(file)


#ques 2
def distribution(filename):
    with open(filename, "r") as file:
        content = file.read()

    grade_list = content.split()
    grade_counts = {}
    grades = ["A", "A-", "B+", "B", "B-", "C", "C-", "F"]

    for grade in grades:
        count = grade_list.count(grade)
        grade_counts[grade] = count

    for grade, count in grade_counts.items():
        print("Students who got", grade, "=", count)

# Example usage
distribution("worker.txt")


#ques 3:
def duplicate(filename):
    f=open(filename,"r")
    content=f.read()
    f.close()
    word_list=content.split()
    for i in range(len(word_list)):
        if word_list[i] in word_list[i+1:]:
            print(True)
            break
    else:
        print(False)
duplicate("worker.txt")


#ques 4
def abc(filename):
    f = open(filename, "r+")
    content = f.read()
    f.close()
    f1 = open('workonword', "a")
    word_list = content.split()
    for i in range(len(word_list)):
        if len(word_list[i]) == 4:
            word_list[i] = 'XXXX'
    f1.write(" ".join(word_list))
    f1.close()
abc("workonword")

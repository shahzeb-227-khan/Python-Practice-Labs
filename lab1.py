# for i in  range(9):
#     for j in range(9):
#         if i == j:
#             print("2",end="")
#         elif j == 0:
#             print("1",end="")
#         elif j == 8:
#             print("3",end="")
#         else:
#             print("  ",end="")
#     print()

#tuples: tuples are immutable,indexed and allows dublicates
# t1 = ('aisha','fatima','nabeel','apple',(1,2,3,4),'banana',[2,4,6,8])
# # for i in t1:
# #     print(i)
#
# # for i in t1:
# #     if i[0] == 'a' and i[-1] == 'a':
# #         print(i)
#
# # l1 = list(t1)
# # l1.append('azeem')
# # l1.insert(3,'ahmed')
# # l1.append([1,3,5,7,9])
# # t1 = tuple(l1)
# # for i in t1:
# #     print(i)
#
#
# # for i in t1:
# #     if i[0] == 'a' and i[-2] == 'a':
# #         print(i)
#
# t1 = ('aisha','fatima','nabeel','apple',(1,2,3,4),'banana',[2,4,6,8])
# # print(t1[:-3])
# # print(t1[:3])
# # print(t1[-2:-1])
# # print(t1[-5:-1])
# # print(t1[1][3])
# # print(t1[-3][3])
# #
# # t2 = ('a','b','c','d')
# # print('c' in t2)
# # print('f' in t2)
# # print('k' not in t2)
# #
# # t1 = ("shahzeb")
# # print(type(t1))
# # t1 = ("shahzeb",)
# # print(type(t1))
# # t1 = "shahzeb",
# # print(type(t1))
#
#
# t3 = 1,2,3
# x,y,z = t3
# # print(x)
# # print(y)
# # print(z)
#
#
# t2 = 'appa','aksa','aara','anaa'
# for i in t2:
#     if i[0] =='a' and i[-1] == 'a':
#         # print(i.replace(i[0] and i[-1],'x'))
#
#
# #dictionaries:
# my_family = {
# 'mother':'saima muneer',
# 'father':{'name':'muneer',
# 'designation':'business',
# 'salary': '30000',
# 'residence': 'fb area',
# 'hobbies': 'mobile',},
# 'brother':'shahmeer'
# }
# for x,y in my_family.items():
#     print("{:^10}:{:^10}".format(x,str(y)))

# grand_family = {
# 'maternal':{
#     'grand father':'jan e alam',
#     'grand mother':'razia begum',
#     'uncles':['shakeel','basheer','haneef','rafeeq'],
#     'aunties':['shabana','rukhsana','kashmala','rehana']},
# 'paternal':{
#     'grand father':'tauseeq',
#     'grand mother':'tasneem',
#     'uncles':0,
#     'aunties':['ifrah','sana','asma']}
# }
#
# for familyside,familydetails in grand_family.items():
#     print(f"{familyside.capitalize()} Family")
#     for role,name in familydetails.items():
#         if isinstance(name,list):
#             print(f"  {role.capitalize()} : {',  '.join(name)}")
#         elif name == 0:
#             print(f"{role.capitalize()} : No {role}")
#         else:
#             print(f"{role.capitalize()} : {name}")


# s1 = {'spices','chocholate','milk','orange','fruits'}
# d1 = {}
# for i in range(len(s1)):
#     s2 = s1.pop()
#     print(f"price for {s2} ")
#     d1[s2] = int(input("price: "))
# print(d1)
# totalprice = sum(d1.values())
# print(f"Your total bill is : {totalprice}")

# def is_leap(year):
#     while year>=1900 and year<= 10**5:
#         if year%4 == 0 and (year%100 != 0 or year%400 == 0):
#             return True
#         else:
#             return False
# year = int(input("Enter your choice of year: "))
# print("Th year is leap:",is_leap(year))

import argparse

import pygame

from consts import GRIDPADDING
from consts import BLOCK_SIZE

parser = argparse.ArgumentParser()
parser.add_argument("-x", type=int, default=16)
parser.add_argument("-y", type=int, default=16)
parser.add_argument("-m", "--mines", type=int, default=40)

args = parser.parse_args()


BACKGROUND_COLOUR = (204, 204, 204)
FLAG_COUNT = 20

dx = (GRIDPADDING * 2) + (args.x * BLOCK_SIZE)
dy = (GRIDPADDING * 2) + (args.y * BLOCK_SIZE) + FLAG_COUNT

GUESS_TEXT_LENGTH = 40

fx = (dx / 2) - GUESS_TEXT_LENGTH
fy = dy - FLAG_COUNT

pygame.init()
win = pygame.display.set_mode((dx, dy))

import sprites
from board import Board


pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont("monospace", 15)


def _render_flg_count(mines: int, flags: int):
    return font.render(
        f"Mines: {mines - flags}", 1, (0, 0, 0)
    )


board = Board(args.x, args.y, mines=args.mines)
flag_count = _render_flg_count(board.n_mines, len(board.flags))


def render():
    win.fill(BACKGROUND_COLOUR)
    board.render(win)
    win.blit(flag_count, (fx, fy))

    pygame.display.update()


safe = True
playing = True
while playing:

    pos = None
    event = pygame.event.wait()

    if not safe:
        board.show_mines()

    if event.type == pygame.MOUSEBUTTONDOWN:
        leftclick, _, rightclick = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if rightclick and safe:
            board.rightclick(pos)
            flag_count = _render_flg_count(
                board.n_mines, len(board.flags)
            )

        elif leftclick and safe:
            safe = board.leftclick(pos)

        elif leftclick:
            playing = False

    if board.check_win():
        board.display_win()
        flag_count = _render_flg_count(
            board.n_mines, len(board.flags)
        )
        safe = False

    if event.type == pygame.QUIT:
        playing = False

    render()


pygame.quit()





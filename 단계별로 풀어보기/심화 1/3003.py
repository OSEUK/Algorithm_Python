lst = input()
chess = lst.split()
king = 1
queen = 1
look = 2
vishop = 2
knight = 2
pone = 8
origin = [king, queen, look, vishop, knight, pone]
result = [king-int(chess[0]), queen-int(chess[1]), look-int(chess[2]), vishop-int(chess[3]), knight-int(chess[4]), pone-int(chess[5]) ]
for i in result:
    print(i, end = " ")
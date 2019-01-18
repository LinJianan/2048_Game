import random
import time



# 全局变量
Board = [[0 for j in range(4)] for i in range(4)]
MaxScore = 0
Choices = [2, 2, 2, 4]
Target = 2048



# 如果是 0 就啥也不输出了，相当于空白
def Vision(value):
    if value == 0:
        return ""
    else:
        return value



# 输出棋盘
def printBoard():
    for i in range(4):
        print("+---------+---------+---------+---------+")
        for j in range(4):
            print("|         ", end="")
        print("|")
        for j in range(4):
            print("|", str(Vision(Board[i][j])).center(8), end="")
        print("|")
        for j in range(4):
            print("|         ", end="")
        print("|")
    print("+---------+---------+---------+---------+")



# 初始化
def Init_Board():
    global Board
    temp, known = 0, -1
    while temp < 2:
        i, j = random.randrange(0, 4), random.randrange(0, 4)
        if 4 * i + j != known:
            known = 4 * i + j
            temp += 1
            Board[i][j] = random.choice(Choices)
    printBoard()
    print("\nw--↑  a--←  s--↓  d--→\n")



# 这游戏还能不能玩了
def canContinue():
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if Board[i][j] == 0 or Board[i][j + 1] == 0 or Board[i + 1][j] == 0 or Board[i + 1][j + 1] == 0:
                return True
            elif Board[i][j] == Board[i][j + 1] or Board[i][j] == Board[i + 1][j]:
                return True
            elif Board[i][j + 1] == Board[i + 1][j + 1] or Board[i + 1][j] == Board[i + 1][j + 1]:
                return True
            else:
                return False



# 选出一个空格加入数字 2 或者 4
def addNumber():
    global Board
    blank = []
    for i in range(4):
        for j in range(4):
            if Board[i][j] == 0:
                blank.append(4 * i + j)
    index = random.choice(blank)
    if len(blank) != 0:
        Board[index // 4][index % 4] = random.choice(Choices)
    printBoard()



# 上移
def moveUp():
    global Board
    global MaxScore
    for i in range(4):
        for j in range(3):
            for k in range(j + 1, 4):
                if Board[k][i] > 0:
                    if Board[j][i] == 0:
                        Board[j][i] = Board[k][i]
                        Board[k][i] = 0
                    elif Board[k][i] == Board[j][i]:
                        Board[j][i] *= 2
                        MaxScore += Board[j][i]
                        Board[k][i] = 0                   
    addNumber()



# 下移
def moveDown():
    global Board
    global MaxScore
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if Board[k][i] > 0:
                    if Board[j][i] == 0:
                        Board[j][i] = Board[k][i]
                        Board[k][i] = 0
                    elif Board[j][i] == Board[k][i]:
                        Board[j][i] *= 2
                        MaxScore += Board[j][i]
                        Board[k][i] = 0
    addNumber()



# 左移
def moveLeft():
    global Board
    global MaxScore
    for i in range(4):
        for j in range(3):
            for k in range(j + 1, 4):
                if Board[i][k] > 0:
                    if Board[i][j] == 0:
                        Board[i][j] = Board[i][k]
                        Board[i][k] = 0
                    elif Board[i][j] == Board[i][k]:
                        Board[i][j] *= 2
                        MaxScore += Board[i][j]
                        Board[i][k] = 0
    addNumber()



# 右移
def moveRight():
    global Board
    global MaxScore
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if Board[i][k] > 0:
                    if Board[i][j] == 0:
                        Board[i][j] = Board[i][k]
                        Board[i][k] = 0
                    elif Board[i][j] == Board[i][k]:
                        Board[i][j] *= 2
                        MaxScore += Board[i][j]
                        Board[i][k] = 0
    addNumber()




# 主函数
def main():
    global Board
    global MaxScore
    global Target
    print ("欢迎来到 2048 游戏，操作说明见下方标志！\n")
    # printBoard()
    Init_Board()
    judge = True
    while judge:
        print("当前分数 ", MaxScore, "，请输入移动方向")
        Input = input() 
        if Input == "w" or Input == "W":
            moveUp()
            if canContinue() == False:
                print("无法继续走，游戏结束")
                break
        elif Input == "a" or Input == "A":
            moveLeft()
            if canContinue() == False:
                print("无法继续走，游戏结束")
                break
        elif Input == "s" or Input == "S":
            moveDown()
            if canContinue() == False:
                print("无法继续走，游戏结束")
                break
        elif Input == "d" or Input == "D":
            moveRight()
            if canContinue() == False:
                print("无法继续走，游戏结束")
                break
        else:
            continue
        for i in range(4):
            for j in range(4):
                if Board[i][j] == Target:
                    print("成功获得 2048 ！ 恭喜你获得胜利！")
                    judge = False
        # printBoard()



# 运行
if __name__ == "__main__":
    main()
    print("本局分数为 ", MaxScore, "\n", "30秒后关闭窗口")
    time.sleep(30)
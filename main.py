#初始化参数
import random
import time
import os
#奖品列表
prise = ["五年高考三年模拟", "阿拉伯炸弹", "锂电池优惠券", "硫酸铅饮料", "三角符文第五章demo", "“大人物”交易神器", "深海冰激凌"] 

#生成欢迎语
print("""
-----井字棋游戏-----
这是一传统井字棋游戏
请输入x,y坐标放置棋子
在横竖斜方向内成线胜利
      """)

#生成棋子列表
qz = [["Q"]*3 for i in range(3)]
#print(qz)

#生成棋盘
def mkqp():
    os.system("cls" if os.name == "nt" else "clear")
    print("  1 2 3")
    for i in range(3):
        for j in range(3):
            if j == 0:
                print(f"{i+1} {qz[i][j]}", end=" ")
            else:
                print(f"{qz[i][j]}", end = " ")
        print()

#玩家下棋交互
def the_player_hh():    
    while True:
        try:
            x, y = map(int, input("请输入坐标（x,y）：").split(","))
            if qz[x-1][y-1] == "Q":
                qz[x-1][y-1] = "X"
                #print(f"玩家下棋位置：{x},{y}")
                break
            else:
                print("该位置已被占用，请重新输入")
        except (ValueError, IndexError):
            print("输入有误，请输入正确的坐标")

#机器人下棋交互
def the_robot_hh():
    # 检查机器人是否有机会获胜
    for i in range(3):
        for j in range(3):
            if qz[i][j] == "Q":
                qz[i][j] = "W"
                # 判断是否胜利
                if check_win("W"):
                    #print([str(i+1), str(j+1)])
                    return
                qz[i][j] = "Q"
    # 检查玩家是否有机会获胜，进行阻挡
    for i in range(3):
        for j in range(3):
            if qz[i][j] == "Q":
                qz[i][j] = "X"
                if check_win("X"):
                    qz[i][j] = "W"
                    #print([str(i+1), str(j+1)])
                    return
                qz[i][j] = "Q"
    # 否则随机落子
    empty = [(i, j) for i in range(3) for j in range(3) if qz[i][j] == "Q"]
    if empty:
        i, j = random.choice(empty)
        qz[i][j] = "W"
        #print([str(i+1), str(j+1)])

# 辅助函数：判断某方是否胜利
def check_win(chess):
    # 行
    for row in qz:
        if row.count(chess) == 3:
            return True
    # 列
    for col in range(3):
        if [qz[row][col] for row in range(3)].count(chess) == 3:
            return True
    # 对角线
    if [qz[i][i] for i in range(3)].count(chess) == 3:
        return True
    if [qz[i][2-i] for i in range(3)].count(chess) == 3:
        return True
    return False

#游戏结束
def gameover(winner):
    print(f"""
-----游戏结束-----
获胜方是：{winner}
恭喜获得奖品：{random.choice(prise)}
欢迎下次游玩
          """)
    exit()

#胜负条件判断
def win_or_over():
    #检查横向
    for row in qz:
        if row.count("X") == 3:
            gameover("玩家")
        if row.count("W") == 3:
            gameover("机器人")
    #检查纵向
    for col in range(3):
        if all(qz[row][col] == "X" for row in range(3)):
            gameover("玩家")
        if all(qz[row][col] == "W" for row in range(3)):
            gameover("机器人")
    #检查斜向
    if all(qz[i][i] == "X" for i in range(3)):
        gameover("玩家")
    if all(qz[i][i] == "W" for i in range(3)):
        gameover("机器人")
    if all(qz[i][2-i] == "X" for i in range(3)):
        gameover("玩家")
    if all(qz[i][2-i] == "W" for i in range(3)):
        gameover("机器人")  
    #检查平局
    if all(cell != "Q" for row in qz for cell in row):
        print("""
-----游戏结束-----
游戏结果是：平局
没有获胜方
欢迎下次游玩""")
        exit()

    
    
#回合制循环
mkqp()
while True:
    the_player_hh()
    mkqp()
    win_or_over()
    print("机器人正在思考中。。。")
    time.sleep(2)
    the_robot_hh()
    mkqp()
    win_or_over()
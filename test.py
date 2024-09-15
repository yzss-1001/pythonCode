#two_d_list = [
#    [1,2,3],
  # [4,5,6],
 #   [7,8,9]
#]
#print(two_d_list[1][2])
#two_d_list[2][2]=10
#print(two_d_list)
#two_d_list.append([10,11,12])
#print(two_d_list)
#x = 0
#while x<3:
  #  two_d_list[x].append(4)
 #   x=x+1


#print(two_d_list)
#/////////////////////////////五子棋/////////////////////////////////////


checkerboard=[]
flagNum=1
finish = False
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append('-')
def show():
    print('-------------------简易五子棋游戏-------------------')
    print('\033[1;30;46m-------------------------------------------------')
    print('   1  2  3  4  5  6  7  8  9  10')
    for i in range(len(checkerboard)):
        print(chr(65+i),end='')
        print('  ',end='')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j],end='')
            print('  ',end='')
        print()
    print('-------------------------------------------------\033[0m')

while not finish:

    show()
    if flagNum == 1:
        flagCh = '*'
        print("请*输入棋子坐标如A1:",end='')
    else:
        flagCh = 'o'
        print("请0输入棋子坐标A2:",end='')

    str = input()
    ch = str[0]
    num = str[1:]
    print(ch)
    print(num)
    x =ord( str[0])-65
    y =int (str[1:])-1
    if x>9 or x<0 or y>9 or y<0:
        print("超出棋盘范围,请重新输入：")
        continue
    if checkerboard[x][y]=='*' or checkerboard[x][y]=='o':
        print("重复下棋，请重新输入：")
        continue
    checkerboard[x][y]=flagCh
    num =1#横向
    i=1
    while y-i>=0 and checkerboard[x][y-i]==flagCh:
        i=i+1
        num=num+1
    i=1
    while  y+i<=9 and checkerboard[x][y+i]==flagCh:
        i=i+1
        num=num+1
    num1=1#纵向·
    i=1

    while x-i>=0 and checkerboard[x-i][y]==flagCh:

        i=i+1
        num1=num1+1
    i=1
    while x+i<=9 and checkerboard[x+i][y]==flagCh:
        i=i+1
        num1=num1+1

    num2=1#第一个斜向
    i=1
    while x+i<=9 and y+i<=9 and checkerboard[x+i][y+i]==flagCh:
        i=i+1
        num2=num2+1
    i=1
    while x-i>=0 and y-i>=0 and checkerboard[x-i][y-i]==flagCh:
        i=i+1
        num2=num2+1
    num3=1#第二个斜向
    i=1
    while x+i<=9 and y-i>=0 and checkerboard[x+i][y-i]==flagCh:
        i=i+1
        num3=num3+1
    i=1
    while x-i>=0 and  y+i<=9 and checkerboard[x-i][y+i]==flagCh:
        i=i+1
        num3=num3+1
    if num>=5 or num1>=5 or num2>=5 or num3>=5:

        finish = True
        show()
        print(f"恭喜{flagCh} 棋子获得胜利！")

    flagNum = -flagNum
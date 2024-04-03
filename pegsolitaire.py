def printdot(x):#print the dots to indicate pegs and holes.
    if x == 0:
        print(bg_cyan+fg_white+' ● '+reset,end='')
    if x == 2:
        print(bg_cyan+fg_magenta+' ● '+reset,end='')
    if x == 1:
        print(bold+bg_cyan+fg_white+' ○ '+reset,end='')
    if x == -1:
        print(bg_red+'   '+reset,end='')

def printboard(x):#print out the board(including the axes).
    print(space+'  ',end='')
    for i in range(len(x[0])):
        print(bold+'\033[47m'+' '+str(i)+' '+'\033[0m',end='')
        if i == len(x[0])-1:
            print(bold+'\033[95m'+' destination:('+str(row)+','+str(col)+')'+reset)
    for i in range(len(x)):
        print(space+bold+'\033[47m'+str(i)+' '+'\033[0m',end='')
        for j in range(len(x[0])):
                       
            printdot(x[i][j])
            if j == len(x[0])-1:
                print()
    print()

def findmove(x,y):#for the peg locates in row x col y, find all its possaible moves.
    l = []
    if checkboard[x+2][y+1]==0 and checkboard[x+2][y]==1:
        l.append('a')
    if checkboard[x+2][y+3]==0 and checkboard[x+2][y+4]==1:
        l.append('d')
    if checkboard[x+1][y+2]==0 and checkboard[x][y+2]==1:
        l.append('w')
    if checkboard[x+3][y+2]==0 and checkboard[x+4][y+2]==1:
        l.append('s')
    return l

def makemove():#player enters his/her move
    m = input(space+bold+fg_blue+'Enter your move(wasd):'+reset)
    return m
 
def choosepeg():#player choose a peg to move. And return board after movement
    x = input(space+bold+fg_blue+"Choose a Peg(which row?):"+reset)
    y = input(space+bold+fg_blue+"Choose a Peg(which col?):"+reset)
    if (x not in [str(i) for i in range(len(board))]) or (y not in [str(i) for i in range(len(board))]):
        #when the input of the peg's location is invalid, call the function again.
        print(space+bold+fg_red+'INVALID INPUT'+reset)
        choosepeg()
    else:
        x,y = int(x),int(y)
        mlist = findmove(x,y)
        #find possible moves for the peg selected
        if board[x][y] != 0 :
            #this is the case when the input location is not a peg
            #thus call the function again until a peg is selected
            print(space+bold+fg_red+'NO PEG HERE'+reset)
            print(space+bold+fg_red+'TRY AGAIN'+reset)
            choosepeg()
        elif len(mlist)==0:
            ##this is the case when the peg selected has no possible move
            #thus call the function again until a 'good' peg is selected
            print(space+bold+fg_red+'THIS PEG HAS NO POSSIBLE MOVE'+reset)
            print(space+bold+fg_red+'CHOOSE ANOTHER PEG'+reset)
            choosepeg()
        else:
            board[x][y]=2
            printboard(board)
            #highlight the peg selected
            m = makemove()
            #make a move
            while m not in mlist:#if the move made is invalid, make another move until a valid pne appears
                print(space+bold+fg_red+'INVALID MOVE'+reset)
                board[x][y]=0
                m = makemove()
            if m =='w':
                board[x][y],board[x-1][y],board[x-2][y]=1,1,0
                checkboard[x+2][y+2],checkboard[x+1][y+2],checkboard[x][y+2]=1,1,0
            if m =='s':
                board[x][y],board[x+1][y],board[x+2][y]=1,1,0
                checkboard[x+2][y+2],checkboard[x+3][y+2],checkboard[x+4][y+2]=1,1,0
            if m =='d':
                board[x][y],board[x][y+1],board[x][y+2]=1,1,0
                checkboard[x+2][y+2],checkboard[x+2][y+3],checkboard[x+2][y+4]=1,1,0
            if m =='a':
                board[x][y],board[x][y-1],board[x][y-2]=1,1,0
                checkboard[x+2][y+2],checkboard[x+2][y+1],checkboard[x+2][y]=1,1,0
            # four directions, change the board and checkboard
            return 

def countpeg(board):#count the number of peg on the board to check the win-condition #return the coordinates of pegs
                    
    l=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                l.append([i, j]) 
    return l

def checkWin(board):# to check if the player wins
    pegCoordinates = countpeg(board)
    indicator = 0
    for coor in pegCoordinates:
        indicator += len(findmove(coor[0], coor[1]))
    # the value of indicator is the total number of possible moves of pegs on the board.
    if indicator == 0 and len(pegCoordinates)>1:
        # if there are at least 2 pegs and none of them has possible moves, then the player loses
        return 0
    elif len(pegCoordinates)==1:
        # if there is only 1 peg left
        if  board[row][col]==0:
            # if the peg locates in the destination, then the player wins
            return 1
        else:# if the peg locates somewhere else, then the player loses
            return 0

def playorquit():# check if player wants to play this map
    n = input(space+bold+fg_blue+'Play or Quit This Map(p/q):'+reset)
    if n == 'p':
        return 'play'
    elif n == 'q':
        return 'quit'
    else:
        return 'invalidinput'

def choosemap():# call the maps module and select the map
    print(space+bold+fg_magenta+'Map 3~8 are difficult, try to look it up in README.txt first')
    x = input(space+bold+fg_blue+'Choose A Map(1-8):'+reset)
    if x == '1':
        board = maps.map1()
    elif x == '2':
        board = maps.map2()
    elif x == '3':
        board = maps.map3()
    elif x == '4':
        board = maps.map4()
    elif x == '5':
        board = maps.map5()
    elif x == '6':
        board = maps.map6()
    elif x == '7':
        board = maps.map7()
    elif x == '8':
        board = maps.map8()
    else:
        print(space+bold+fg_red+'INVALID INPUT'+reset)
        board = choosemap()
    return board

def mapmain():# the main part for a map the player choose to play
    while True:#when win, lose or quit, break this while loop
        printboard(board)
        play = playorquit()
        while play =='invalidinput':
            print(space+bold+fg_red+'INVALID INPUT'+reset)
            play = playorquit()
        if play=='quit':
            print(space+fg_magenta+bold+'Thank You For Playing!')
            print(space+fg_magenta+bold+'        BYE~~')
            break
        elif play =='play':
            choosepeg()
        if checkWin(board)==0:
            printboard(board)
            printfunc.p('lose')#call printfunc module
            break
        elif checkWin(board)==1:
            printboard(board)
            printfunc.p('win')#call printfunc module                                                 
            break

fg_white = "\033[97m"
fg_magenta = '\033[95m'
fg_red = '\033[91m'
fg_blue = '\033[94m'
bg_black = "\033[101m"
bg_yellow = "\033[43m"
bg_cyan = "\033[43m"
bg_red = "\033[41m"
reset = '\033[0m'
bold = '\033[1m'
space = '                                                       '
import intro
import maps
import printfunc

intro.intro()# call the intro module for the intro part
while True:# the main part for the game
    choice = input(space+bold+fg_blue+'PLAY OR QUIT GAME (p/q):'+reset)
    if choice =='p':

        board = choosemap() #choose the game board
        for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==1:
                        row, col = i, j 
        checkboard = [[-1]*(len(board[0])+4),[-1]*(len(board[0])+4)]+[([-1,-1]+i+[-1,-1]) for i in board]+[[-1]*(len(board[0])+4),[-1]*(len(board[0])+4)]
        # generate the checkboard for the chosen board
        mapmain()
        # start the playing part
    elif choice == 'q':
        print(space+bold+fg_magenta+'     '+'   BYE~~')
        break
    else:# if input is invalid, call for input again
        print(space+fg_red+bold+'INVALID INPUT')

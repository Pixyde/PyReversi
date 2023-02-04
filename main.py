import pygame
pygame.font.init()
pygame.display.init()

game = False
bot = True
changed = False

player1Score = 0
player2Score = 0

textFont = pygame.font.SysFont('Calibri', 30)
scoreFont = pygame.font.SysFont('Calibri', 50)
player1Text = textFont.render('Player 1 Turn', False, (0, 0, 0))
player2Text = textFont.render('Player 2 Turn', False, (255, 255, 255))
player1WinText = textFont.render('Player 1 Win!', False, (255, 255, 255))
player2WinText = textFont.render('Player 2 Win!', False, (255, 255, 255))

Button1img = pygame.image.load('1pModeButton.png')
Button2img = pygame.image.load('2pModeButton.png')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
darkGreen = (12, 160, 35)
blue = (20, 228, 241)

WIDTH = 26
HEIGHT = 26
MARGIN = 5
grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)
possibleMoveGrid = []
for row in range(8):
    possibleMoveGrid.append([])
    for column in range(8):
        possibleMoveGrid[row].append(0)
pygame.init()
window_size = [255, 300]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Reversi")
done = False
clock = pygame.time.Clock()
playerTurn = 1
grid[3][3] = 1
grid[4][4] = 1
grid[3][4] = 2
grid[4][3] = 2

p1ValidMove = 0
p2ValidMove = 0
valideRow = []
valideColum = []


def p1Verif():
    global playerTurn
    global grid
    global row
    global column
    global valideRow
    global valideColum
    global p1ValidMove
    global counter

    counter = 0
    p1ValidMove = 0
    valideRow.clear()
    valideColum.clear()

    if playerTurn == 1:
        for row in range(8):
            for column in range(8):

                if grid[row][column] == 0:
                    p1VerifRight()
                    p1VerifLeft()
                    p1VerifUP()
                    p1VerifDOWN()
                    p1VerifRightUP()
                    p1VerifRightDOWN()
                    p1VerifLeftUP()
                    p1VerifLeftDOWN()


def p1VerifRight():
    counter = 0
    global p1ValidMove
    firstfound =False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column + i <= 7:
                    if grid[row][column + i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row][column + i] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifLeft():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0:
                    if grid[row][column - i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row][column - i] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifUP():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0:
                    if grid[row - i][column] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row - i][column] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifDOWN():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:

                if row + i <= 7:
                    if grid[row + i][column] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row + i][column] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifRightUP():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column + i <= 7 and row - 1 >= 0:
                    if grid[row - i][column + i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row - i][column + i] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifLeftUP():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0 and row - i >= 0:
                    if grid[row - i][column - i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row - i][column - i] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifLeftDOWN():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0 and row + i <= 7:
                    if grid[row + i][column - i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row + i][column - i] == 1 and firstfound == True:
                        for i in range(counter):
                            p1ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p1VerifRightDOWN():
    counter = 0
    global p1ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        elif searchCompleted == False:
            if row + i <= 7 and column + i <= 7:
                if grid[row + i][column + i] == 2:
                    if i == 1:
                        firstfound = True
                    if firstfound:
                        counter += 1
                elif grid[row + i][column + i] == 1 and firstfound == True:
                    for i in range(counter):
                        p1ValidMove += 1
                        valideRow.append(row)
                        valideColum.append(column)
                        firstfound = False
                        searchCompleted = True
                else:
                    firstfound = False
                    searchCompleted = True



def p2Verif():
    global playerTurn
    global grid
    global row
    global column
    global valideRow
    global valideColum
    global p2ValidMove
    global counter

    counter = 0
    p2ValidMove = 0
    valideRow.clear()
    valideColum.clear()

    for row in range(8):
        for column in range(8):
            possibleMoveGrid[row][column] = 0

    if playerTurn == 2:
        for row in range(8):
            for column in range(8):
                global firstfound

                if grid[row][column] == 0:
                    p2VerifRight()
                    p2VerifLeft()
                    p2VerifUP()
                    p2VerifDOWN()
                    p2VerifRightUP()
                    p2VerifRightDOWN()
                    p2VerifLeftUP()
                    p2VerifLeftDOWN()


def p2VerifRight():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column + i <= 7:
                    if grid[row][column + i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row][column + i] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifLeft():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0:
                    if grid[row][column - i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row][column - i] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifUP():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0:
                    if grid[row - i][column] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row - i][column] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifDOWN():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:

                if row + i <= 7:
                    if grid[row + i][column] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row + i][column] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifRightUP():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column + i <= 7 and row - 1 >= 0:
                    if grid[row - i][column + i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row - i][column + i] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifLeftUP():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0 and row - i >= 0:
                    if grid[row - i][column - i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row - i][column - i] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifLeftDOWN():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0 and row + i <= 7:
                    if grid[row + i][column - i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                    elif grid[row + i][column - i] == 2 and firstfound == True:
                        for i in range(counter):
                            p2ValidMove += 1
                            valideRow.append(row)
                            valideColum.append(column)
                            possibleMoveGrid[row][column] += 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2VerifRightDOWN():
    counter = 0
    global p2ValidMove
    firstfound = False
    searchCompleted = False
    for i in range(8):
        if i == 0:
            i = i
        elif searchCompleted == False:
            if row + i <= 7 and column + i <= 7:
                if grid[row + i][column + i] == 1:
                    if i == 1:
                        firstfound = True
                    if firstfound:
                        counter += 1
                elif grid[row + i][column + i] == 2 and firstfound == True:
                    for i in range(counter):
                        p2ValidMove += 1
                        valideRow.append(row)
                        valideColum.append(column)
                        possibleMoveGrid[row][column] += 1
                        firstfound = False
                else:
                    firstfound = False
                    searchCompleted = True


def p1ChangeGrid():
    global changesrow
    global changescolum
    global counter
    global firstfound
    counter = 0
    changesrow = []
    changesrow.clear()
    changescolum = []
    changescolum.clear()
    firstfound = False

    if playerTurn == 1:
        p1ChangeGridLeft()
        p1ChangeGridRight()
        p1ChangeGrideUP()
        p1ChangeGrideDOWN()
        p1ChangeGridRighUP()
        p1ChangeGridRighDOWN()
        p1ChangeGridLeftUP()
        p1ChangeGridLeftDown()


def p1ChangeGridLeft():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column + i <= 7:
                    if grid[row][column + i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row)
                            changescolum.append(column + i)
                    elif grid[row][column + i] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGridRight():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0:
                    if grid[row][column - i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row)
                            changescolum.append(column - i)
                    elif grid[row][column - i] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGrideUP():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0:
                    if grid[row - i][column] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row - i)
                            changescolum.append(column)
                    elif grid[row - i][column] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGrideDOWN():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row + i <= 7:
                    if grid[row + i][column] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row + i)
                            changescolum.append(column)
                    elif grid[row + i][column] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGridRighUP():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0 and column - i >= 0:
                    if grid[row - i][column - i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row - i)
                            changescolum.append(column - i)
                    elif grid[row - i][column - i] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGridRighDOWN():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row + i <= 7 and column - i >= 0:
                    if grid[row + i][column - i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row + i)
                            changescolum.append(column - i)
                    elif grid[row + i][column - i] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGridLeftUP():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0 and column + i <= 7:
                    if grid[row - i][column + i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row - i)
                            changescolum.append(column + i)
                    elif grid[row - i][column + i] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p1ChangeGridLeftDown():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row + i <= 7 and column + i <= 7:
                    if grid[row + i][column + i] == 2:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row + i)
                            changescolum.append(column + i)
                    elif grid[row + i][column + i] == 1 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 1
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGrid():

    p2ChangeGridLeft()
    p2ChangeGridRight()
    p2ChangeGrideUp()
    p2ChangeGrideDown()
    p2ChangeGridRighUP()
    p2ChangeGridRighDOWN()
    p2ChangeGridLeftUP()
    p2ChangeGridLeftDown()


def p2ChangeGridLeft():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column + i <= 7:
                    if grid[row][column + i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row)
                            changescolum.append(column + i)
                    elif grid[row][column + i] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGridRight():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if column - i >= 0:
                    if grid[row][column - i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row)
                            changescolum.append(column - i)
                    elif grid[row][column - i] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGrideUp():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0:
                    if grid[row - i][column] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row - i)
                            changescolum.append(column)
                    elif grid[row - i][column] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                            searchCompleted = True
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGrideDown():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row + i <= 7:
                    if grid[row + i][column] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row + i)
                            changescolum.append(column)
                    elif grid[row + i][column] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGridRighUP():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0 and column - i >= 0:
                    if grid[row - i][column - i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row - i)
                            changescolum.append(column - i)
                    elif grid[row - i][column - i] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGridRighDOWN():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row + i <= 7 and column - i >= 0:
                    if grid[row + i][column - i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row + i)
                            changescolum.append(column - i)
                    elif grid[row + i][column - i] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGridLeftUP():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(8):
        if i == 0:
            i = i
        else:
            if searchCompleted == False:
                if row - i >= 0 and column + i <= 7:
                    if grid[row - i][column + i] == 1:
                        if i == 1:
                            firstfound = True
                        if firstfound:
                            counter += 1
                            changesrow.append(row - i)
                            changescolum.append(column + i)
                    elif grid[row - i][column + i] == 2 and firstfound == True:
                        for i in range(counter):
                            grid[changesrow[i]][changescolum[i]] = 2
                            firstfound = False
                    else:
                        firstfound = False
                        searchCompleted = True


def p2ChangeGridLeftDown():
    changesrow = []
    changescolum = []
    counter = 0
    firstfound = False
    searchCompleted = False

    for i in range(1, 8):
        if searchCompleted == False:
            if row + i <= 7 and column + i <= 7:
                if grid[row + i][column + i] == 1:
                    if i == 1:
                        firstfound = True
                    if firstfound:
                        counter += 1
                        changesrow.append(row + i)
                        changescolum.append(column + i)
                elif grid[row + i][column + i] == 2 and firstfound == True:
                    for i in range(counter):
                        grid[changesrow[i]][changescolum[i]] = 2
                        firstfound = False
                else:
                    firstfound = False
                    searchCompleted = True



def countScore():
    global player1Score
    global player2Score

    player1Score = 0
    player2Score = 0

    for row in range(8):
        for column in range(8):
            if grid[row][column] == 1:
                player1Score += 1
            elif grid[row][column] == 2:
                player2Score += 1


p1Verif()
countScore()
while not done:

    if game == False:
        for event in pygame.event.get():
            scr.blit(Button1img, (100, 200))
            scr.blit(Button2img, (100, 250))
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if playerTurn == 1:
                    if p1ValidMove > 0:
                        for i in range(len(valideRow)):
                            if i + 1 <= len(valideColum):
                                if row == valideRow[i - 1] and column == valideColum[i - 1]:
                                        grid[row][column] = 1
                                        p1ChangeGrid()
                                        playerTurn = 2
                                        valideRow.clear()
                                        valideColum.clear()
                                        valideMove = 0
                                        p1Verif()
                                        p2Verif()
                                        countScore()
                    else:
                        playerTurn = 2
                        valideMove = 0
                        p1Verif()
                        p2Verif()
                elif playerTurn == 2:
                    if p2ValidMove > 0:
                        if bot == False:
                            for i in range(len(valideRow)):
                                if i + 1 <= len(valideColum):
                                    if row == valideRow[i] and column == valideColum[i]:
                                        grid[row][column] = 2
                                        playerTurn = 1
                                        valideRow.clear()
                                        valideColum.clear()
                                        valideMove = 0
                                        p2Verif()
                                        p1Verif()
                                        countScore()
                        elif bot == True:
                            bestmovecolumn = 0
                            bestmoverow = 0
                            bestmovepoints = 0
                            for y in range(8):
                                for x in range(8):
                                    if possibleMoveGrid[y][x] > bestmovepoints:
                                        bestmovepoints = possibleMoveGrid[y][x]
                                        bestmovecolumn = x
                                        bestmoverow = y
                            grid[bestmoverow][bestmovecolumn] = 2
                            row=bestmoverow
                            column=bestmovecolumn
                            p2ChangeGrid()
                            playerTurn = 1
                            valideRow.clear()
                            valideColum.clear()
                            valideMove = 0
                            p2Verif()
                            p1Verif()
                            countScore()

                    else:
                        playerTurn = 1
                        valideMove = 0
                        p2Verif()
                        p1Verif()
                print("Click ", pos, "Grid coordinates: ", row, column)
        scr.fill(darkGreen)
        scr.fill(blue, ((0, 255), (255, 300)))
        player1ScoreText = scoreFont.render(str(player1Score), False, (0, 0, 0))
        player2ScoreText = scoreFont.render(str(player2Score), False, (255, 255, 255))
        scr.blit(player1ScoreText, (10, 260))
        scr.blit(player2ScoreText, (220, 260))
        if playerTurn == 1:
            scr.blit(player1Text, (47, 275))
        elif playerTurn == 2:
            scr.blit(player2Text, (47, 275))
        for row in range(8):
            for column in range(8):
                color = green
                if grid[row][column] == 1:
                    color = black
                elif grid[row][column] == 2:
                    color = white
                pygame.draw.rect(scr,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        if p1ValidMove == 0 and p2ValidMove == 0:
            if player1Score > player2Score:
                scr.fill(black)
                scr.blit(player1WinText, (0, 0))
            elif player1Score < player2Score:
                scr.fill(black)
                scr.blit(player2WinText, (0, 0))
        clock.tick(50)
        pygame.display.flip()
    elif game == True:
        scr.blit(Button1img, (0, 0))

pygame.quit()

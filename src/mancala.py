'''
Created on 01.04.2019

@author: Robin Fluss
'''
import sys
from lib2to3.fixer_util import Number

class Field():
    stones = 0
    
    def increment(self):
        self.stones += 1
    
    def getNumberOfStones(self):
        return self.stones
    
    def setNumberOfStones(self, number):
        self.stones = number
    
    def emptyField(self):
        numberOfStones = self.getNumberOfStones()
        self.setNumberOfStones(0)
        return numberOfStones
    


class Board():
    
    numStonesGamestart = 4

    #initialize placeholder list
    fieldList = [Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field()]
    
    def resetFields(self):
        for i in range(0, 14):
            self.fieldList[i].setNumberOfStones(self.numStonesGamestart)
        self.fieldList[1].setNumberOfStones(self.numStonesGamestart)

        self.fieldList[0].setNumberOfStones(0)
        self.fieldList[7].setNumberOfStones(0)

    def toString(self):
        string = "     "
        for i in range(13, 8, -1):
            string = string + str(self.fieldList[i].getNumberOfStones()) + " - "
        
        string = string + str(self.fieldList[8].getNumberOfStones())
        
        string = string + "\n  " \
        + str(self.fieldList[0].getNumberOfStones()) \
        + "                         " \
        + str(self.fieldList[7].getNumberOfStones()) \
        + "\n     "

        for i in range(1, 6):
            string = string + str(self.fieldList[i].getNumberOfStones()) + " - "
        
        string = string + str(self.fieldList[6].getNumberOfStones())

        return(string)
        
        
    def checkGameEnd(self):
        gameEnd1 = True
        gameEnd2 = True
        for i in range(1, 7):
            if (self.fieldList[i].getNumberOfStones()!=0):
                gameEnd1= False
        for i in range(8, 14):
            if (self.fieldList[i].getNumberOfStones()!=0):
                gameEnd2= False
        if (gameEnd1 == True or gameEnd2 == True):
            return True
        else:
            return False

board = Board()
def gameStartText():
    print()
    
def printHelp():
    print()
    print ("Commands:")
    print ("-e: Exit game")
    print ("-n: Start a new game")
    print ("-r: Show game rules")
    print ("-h: Show this help")
    print ("[fieldIndex]: Make a turn")
    print()
    print ("    [13]-[12]-[11]-[10]-[09]-[08]")
    print ("  X                               X")
    print ("    [01]-[02]-[03]-[04]-[05]-[06]")
    
    print ()


def printRules():
    print("RULES:")

def checkForStandardInputs(str):
    if str == "-e":
        print ("The program has terminated. Bless the universe and see you soon.")
        sys.exit()
    elif str == "-n":
        print ("You forced the game end. Restart Mancala by pressing Enter.")
        return True
    elif str == "-r":
        printRules()
    elif str == "-h":
        printHelp()
    
    return False

def makeMove(fieldIndex, player):
    numberOfStones = board.fieldList[fieldIndex].emptyField()
    i = numberOfStones
    while (i>0):
        if fieldIndex+i>13:
            smartIndex = fieldIndex+i-14
        else:
            smartIndex=fieldIndex+i
        if(player==1 and smartIndex==0):
            smartIndex=smartIndex+1
        if(player==2 and smartIndex==7):
            smartIndex=smartIndex+1
        board.fieldList[smartIndex].increment()
        i = i - 1
    lastFieldIndex = (fieldIndex+numberOfStones)%14
    if(player==1 and lastFieldIndex==7):
        print("--> One more turn!")
        return 1
    elif (player==1):
        return 2
    if(player==2 and lastFieldIndex==0):
        print("--> One more turn!")
        return 2
    elif (player==2):
        return 1
        
def checkForPlayerMoveInput(uI, player):
    numberInRange1 = False
    numberInRange2 = False

    if ((uI == "1") | (uI == "2") | (uI == "3") | (uI == "4") | (uI == "5") | (uI == "6")):
        numberInRange1 = True
    if ((uI == "8") | (uI == "9") | (uI == "10") | (uI == "11") | (uI == "12") | (uI == "13")): 
        numberInRange2 = True
    if (player==1 and numberInRange1==True or player==2 and numberInRange2==True):
        
        uI = int(uI)

        if (board.fieldList[uI].getNumberOfStones()!=0):
            return True
        else:
            print("You cannot select an empty field.")
            return False
    else:
        print("You cannot chose opponents fields.")
        return False
    
def printBoard():
    print (board.toString())

def gameLoop():
    gameFinnished = False
    board.resetFields()
    player = 1

    while(gameFinnished == False):
        printBoard()
        validInput = False
        userInput = ""
        while(validInput==False):
            userInput = input("Player " + str(player) + ": ")
            gameFinnished = checkForStandardInputs(userInput)
            if (gameFinnished): break
            validInput = checkForPlayerMoveInput(userInput, player)
            if (validInput==False):
                print("To make a move please enter a valid number.")
        if (gameFinnished):
            break
        print()
        userInput = int(userInput)
        player = makeMove(userInput, player)       
        gameFinnished = board.checkGameEnd()
        if (gameFinnished):
            print("Player " + str(player) + " has won!")

if __name__ == '__main__':
    print("Welcome to Mancala.")
    printHelp()
    print("Start Mancala by pressing Enter.")
    while(True):
        userInput = input()
        checkForStandardInputs(userInput)
        gameLoop()
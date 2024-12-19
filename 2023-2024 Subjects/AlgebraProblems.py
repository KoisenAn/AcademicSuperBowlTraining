import pygame
import Elements
import random
import math

#Problem template
'''
class AlgebraProblem1: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []
        
        self.generateProblem()
        self.generateQuestionAndAnswer()

        pass
    
    def generateProblem(self):
        pass

    def generateQuestionAndAnswer(self):
    
        self.answers = []
        self.question = []
        self.inputTexts = []

        pass

    def checkCorrect(self):
        pass
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass
'''

#Two linear equations with Integer Solutions
class AlgebraProblem1: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.problemDisplayType = "lines"

        self.create()

        pass

    def create(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.generateProblem()
        self.generateQuestionAndAnswer()

    def equationBuilder(self, coefficient1, coefficient2, LHS):
        equationString = ""
        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        if (abs(coefficient2) == 1):
            equationString += "x + "
        elif (coefficient2 == -1):
            equationString += "x - "
        elif(coefficient2 < 0):
            equationString += "x - " + str(abs(coefficient2))
        else:
            equationString += "x + " + str(coefficient2)
        equationString += "y = " + str(LHS)

        return equationString
    
    def generateProblem(self):
        
        choice = random.randint(1,100)
        if (choice <= 50):
            rangeAnswer = 10
            rangeCoefficient = 20
        elif (choice <= 90):
            rangeAnswer = 20
            rangeCoefficient = 50
        else:
            rangeAnswer = 50
            rangeCoefficient = 100

        self.answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerX == 0):
            self.answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerY == 0):
            self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)

        #First equation coefficients
        coefficient1x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1x == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient1y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1y == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)        
        coefficient2x = random.randint(-1*rangeCoefficient, rangeCoefficient)

        #Second equation coefficients
        while (coefficient2x == 0):
            coefficient2x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2y == 0):
            coefficient2y = random.randint(-1 * rangeAnswer , rangeAnswer)
        
        LHS1 = self.answerX * coefficient1x + self.answerY * coefficient1y
        LHS2 = self.answerX * coefficient2x + self.answerY * coefficient2y

        self.question.append(self.equationBuilder(coefficient1x, coefficient1y, LHS1))
        self.question.append(self.equationBuilder(coefficient2x, coefficient2y, LHS2))

    def generateQuestionAndAnswer(self):

        self.answers = []
        self.inputTexts = []

        choice = random.randint(1,100)
        if (choice <= 25):
            self.question.append("Find x,y")
            self.answerReceiver = ("textBox",2)
            self.answers.append(self.answerX)
            self.answers.append(self.answerY)
            self.inputTexts.append("x:")
            self.inputTexts.append("y:")
        elif (choice <= 50):
            self.question.append("Find x+y")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX+self.answerY)
            self.inputTexts.append("x+y:")
        elif (choice <= 75):
            self.question.append("Find x-y")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX-self.answerY)
            self.inputTexts.append("x-y:")
        else:
            self.question.append("Find xy")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX*self.answerY)
            self.inputTexts.append("xy:")

        return self.question
    
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                #print(abs(float(self.answers[i]) - float(answer[i])))
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.001):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList

#Three linear equatons wtih integer solution 
class AlgebraProblem2: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.problemDisplayType = "lines"

        self.create()

        pass

    def create(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.generateProblem()
        self.generateQuestionAndAnswer()

    def equationBuilder(self, coefficient1, coefficient2, coefficient3, LHS):
        equationString = ""
        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        if (abs(coefficient2) == 1):
            equationString += "x + "
        elif (coefficient2 == -1):
            equationString += "x - "
        elif(coefficient2 < 0):
            equationString += "x - " + str(abs(coefficient2))
        else:
            equationString += "x + " + str(coefficient2)

        if (abs(coefficient3) == 1):
            equationString += "y + "
        elif (coefficient3 == -1):
            equationString += "y - "
        elif(coefficient3 < 0):
            equationString += "y - " + str(abs(coefficient3))
        else:
            equationString += "y + " + str(coefficient3)

        equationString += "z = " + str(LHS)
        return equationString
    
    def generateProblem(self):
        
        multiplier = False

        choice = random.randint(1,100)
        if (choice <= 90):
            rangeAnswer = 10
            rangeCoefficient = 15
        else:
            rangeAnswer = 15
            rangeCoefficient = 30

        self.answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerX == 0):
            self.answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerY == 0):
            self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        self.answerZ = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerZ == 0):
            self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)

        #First equation coefficients
        coefficient1x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1x == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient1y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1y == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)   
        coefficient1z = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1z == 0):
            coefficient1z = random.randint(-1 * rangeAnswer , rangeAnswer)  

        #Second equation coefficients
        coefficient2x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2x == 0):
            coefficient2x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2y == 0):
            coefficient2y = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2z = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2z == 0):
            coefficient2z = random.randint(-1 * rangeAnswer , rangeAnswer)   

        #Third equation coefficients
        coefficient3x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient3x == 0):
            coefficient3x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient3y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient3y == 0):
            coefficient3y = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient3z = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient3z == 0):
            coefficient3z = random.randint(-1 * rangeAnswer , rangeAnswer)   
        
        LHS1 = self.answerX * coefficient1x + self.answerY * coefficient1y + self.answerZ * coefficient1z
        LHS2 = self.answerX * coefficient2x + self.answerY * coefficient2y + self.answerZ * coefficient2z
        LHS3 = self.answerX * coefficient3x + self.answerY * coefficient3y + self.answerZ * coefficient3z

        self.question.append(self.equationBuilder(coefficient1x, coefficient1y, coefficient1z, LHS1))
        self.question.append(self.equationBuilder(coefficient2x, coefficient2y, coefficient2z, LHS2))
        self.question.append(self.equationBuilder(coefficient3x, coefficient3y, coefficient3z, LHS3))
    
    def generateQuestionAndAnswer(self):

        self.answers = []
        self.inputTexts = []

        choice = random.randint(1,100)
        if (choice <= 24):
            self.question.append("Find x,y,z")
            self.answerReceiver = ("textBox",3)
            self.answers.append(self.answerX)
            self.answers.append(self.answerY)
            self.answers.append(self.answerZ)
            self.inputTexts.append("x:")
            self.inputTexts.append("y:")
            self.inputTexts.append("z:")
        elif (choice <= 40):
            self.question.append("Find x+y+z")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX+self.answerY+self.answerZ)
            self.inputTexts.append("x+y+z:")
        elif (choice <= 56):
            self.question.append("Find x-y+z")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX-self.answerY+self.answerZ)
            self.inputTexts.append("x-y+z:")
        elif (choice <= 72):
            self.question.append("Find x+y-z")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX+self.answerY-self.answerZ) 
            self.inputTexts.append("x+y-z:")
        elif (choice <= 88):
            self.question.append("Find -x+y+z")
            self.answerReceiver = ("textBox",1)      
            self.answers.append(-1 * self.answerX+self.answerY+self.answerZ)
            self.inputTexts.append("-x+y+z:")
        else:
            self.question.append("Find xyz")
            self.answerReceiver = ("textBox",1)
            self.answers.append(self.answerX*self.answerY*self.answerZ)
            self.inputTexts.append("xyz:")

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                #print(abs(float(self.answers[i]) - float(answer[i])))
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.001):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList

    def display(self):
        pass
    
# 2 variable, 
class AlgebraProblem3:

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.problemDisplayType = "lines"

        self.create()

        pass

    def create(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.generateProblem()
        self.generateQuestionAndAnswer()

    def equationBuilder1(self, coefficient1, coefficient2, LHS):
        equationString = ""
        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        if (abs(coefficient2) == 1):
            equationString += "x + "
        elif (coefficient2 == -1):
            equationString += "x - "
        elif(coefficient2 < 0):
            equationString += "x - " + str(abs(coefficient2))
        else:
            equationString += "x + " + str(coefficient2)

        equationString += "y = " + str(LHS)

        return equationString

    def equationBuilder2(self, coefficient1, LHS):
        equationString = ""
        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        equationString += "xy"

        equationString += " = " + str(LHS)

        return equationString
    
    '''
    def equationBuilder3(self, coefficient1, coefficient2, variable, LHS):
        equationString = ""

        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        equationString += "xy"

        equationString += " = " + str(LHS)

        return equationString
    '''
    
    def generateProblem(self):
        
        multiplier = False

        choice = random.randint(1,100)
        if (choice <= 90):
            rangeAnswer = 10
            rangeCoefficient = 15
        else:
            rangeAnswer = 15
            rangeCoefficient = 30

        self.answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerX == 0):
            self.answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (self.answerY == 0):
            self.answerY = random.randint(-1 * rangeAnswer , rangeAnswer)

        #First equation coefficients
        coefficient1 = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1 == 0):
            coefficient11 = random.randint(-1 * rangeAnswer , rangeAnswer)

        #Second equation coefficients
        coefficient2x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2x == 0):
            coefficient2x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2y == 0):
            coefficient2y = random.randint(-1 * rangeAnswer , rangeAnswer)
        
        LHS1 = self.answerX * coefficient1 * self.answerY
        LHS2 = self.answerX * coefficient2x + self.answerY * coefficient2y

        self.question.append(self.equationBuilder2(coefficient1, LHS1))
        self.question.append(self.equationBuilder1(coefficient2x, coefficient2y, LHS2))
    
    def generateQuestionAndAnswer(self):

        self.answers = []
        self.inputTexts = []

        choice = random.randint(1,100)
        if (choice <= 100):
            self.question.append("Find x,y")
            self.answerReceiver = ("textBox",2)
            self.answers.append(self.answerX)
            self.answers.append(self.answerY)
            self.inputTexts.append("x:")
            self.inputTexts.append("y:")

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.001):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

problemList = [AlgebraProblem1(), AlgebraProblem2(), AlgebraProblem3()]

#print(pygame.font.get_fonts())
#problem = print(AlgebraProblem1().getQuestion())
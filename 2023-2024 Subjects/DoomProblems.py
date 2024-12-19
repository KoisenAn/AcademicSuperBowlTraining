import pygame
import Elements
import random
import math
import DoomProblems

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

sundayInputs = ["sunday","sun","su"]

mondayInputs = ["monday","mon","m","mu"]

tuesdayInputs = ["tuesday","tues","t","tu","tus","tue"]

wednesdayInputs = ["wednesday","wed","w","we","wednes"]

thursdayInputs = ["thursday","thr","thu","th","thur","thurs"]

fridayInputs = ["friday","fri","fr","f"]

saturdayInputs = ["saturday","sat","sa"]

dayInputs = [sundayInputs, mondayInputs, tuesdayInputs, wednesdayInputs, thursdayInputs, fridayInputs, saturdayInputs]

numberOfDaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

#Note January and February changes doomsdays on leap years
doomsDays = [3,7,7,4,2,6,4,1,5,3,7,5]

monthNames = ["January","February","March","April","May","June","July","August","September","October","November","December"]

#Problem template
'''
class ModProblem1: 

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
    
    def generateProblem(self):
        pass

    def generateQuestionAndAnswer(self):
    
        self.answers = []
        self.question = []

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

#Find the anchor day for a given year in the Gregorian calcender
class DoomProblem1: 

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
    
    def generateProblem(self):
        
        choice = random.randint(1,100)
        if (choice <= 65):
            self.year = random.randint(1582,10000)
        elif (choice <= 85):
            self.year = 4 * random.randint(396,2500)
        elif (choice <= 95):
            self.year = 100 * random.randint(16,100)
        elif (choice <= 100):
            self.year = 400 * random.randint(4,25)

        self.anchorDay = (2 + self.year + math.floor(self.year/4) - math.floor(self.year/100) + math.floor(self.year/400))%7

        pass

    def testAlgorithm(self,test):

        return (2 + test + math.floor(test/4) - math.floor(test/100) + math.floor(test/400))%7


    def generateQuestionAndAnswer(self):
    
        self.answers = DoomProblems.dayInputs[self.anchorDay]

        self.answerReceiver = ("textBox",1)

        self.inputTexts.append("Day of the week:")

        self.question = []

        question = "Find the anchor day of the year " + str(self.year) + " in the Gregorian Calender"

        self.question.append(question)

        pass

    def checkCorrect(self, answer):

        reformatedAnswer = (answer[0].upper()).lower()

        if (reformatedAnswer in self.answers):
            return True

        return False
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return [DoomProblems.days[self.anchorDay]]
        
    def display(self):
        pass

#Find the actual day of the week in the Gregorian Calender
class DoomProblem2: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []
        #print("---------")

        self.problemDisplayType = "lines"

        self.create()

        pass

    def create(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.generateProblem("null")
        self.generateQuestionAndAnswer()
    
    def generateProblem(self, test):
        
        try:
            self.month = int(test.split("/")[0])-1
            self.day = int(test.split("/")[1])
            self.year = int(test.split("/")[2])

            #Check for leap year
            self.isLeapYear = False
            if (self.year % 400 == 0 or self.year % 4 == 0 and self.year % 100 != 0):
                self.isLeapYear = True

        except:

            #Generate year
            choice = random.randint(1,100)
            if (choice <= 65):
                self.year = random.randint(1582,10000)
            elif (choice <= 85):
                self.year = 4 * random.randint(396,2500)
            elif (choice <= 95):
                self.year = 100 * random.randint(16,100)
            elif (choice <= 100):
                self.year = 400 * random.randint(4,25)

            #Check for leap year
            self.isLeapYear = False
            if (self.year % 400 == 0 or self.year % 4 == 0 and self.year % 100 != 0):
                self.isLeapYear = True

            #Generate the month
            self.month = random.randint(0,11)
            #print("Month: " + str(DoomProblems.monthNames[self.month]))

            #Generate Day
            if (self.isLeapYear and self.month == 1):
                self.day = random.randint(1,DoomProblems.numberOfDaysInMonth[1]+1)
            else:
                self.day = random.randint(1,DoomProblems.numberOfDaysInMonth[self.month])


        #Find the anchor day
        self.anchorDay = (2 + self.year + math.floor(self.year/4) - math.floor(self.year/100) + math.floor(self.year/400))%7
        #print("Anchor day: " + str(DoomProblems.days[self.anchorDay]))

        #Find the day of the week the day is on
        if (self.isLeapYear and (self.month == 0 or self.month == 1)):
            #print("Doomsday of month: " + str(DoomProblems.doomsDays[self.month]+1))
            self.daysAway = (self.day-(DoomProblems.doomsDays[self.month]+1))%7
        else:
            #print("Doomsday of month: " + str(DoomProblems.doomsDays[self.month]))
            self.daysAway = (self.day-(DoomProblems.doomsDays[self.month]))%7

        #print("Days away: " + str(self.daysAway))

        self.answer = (self.anchorDay + self.daysAway)%7

        #print("Gregorian Day: " + str(DoomProblems.days[self.answer]))

        pass

    def generateQuestionAndAnswer(self):
    
        self.answers = DoomProblems.dayInputs[self.answer]

        self.answerReceiver = ("textBox",1)

        self.inputTexts.append("Day of the week:")

        self.question = []

        question = "What day is " + str(self.month+1) + "/" + str(self.day) + "/" + str(self.year) + " in the Gregorian Calender"

        self.question.append(question)

        pass

    def checkCorrect(self, answer):

        reformatedAnswer = (answer[0].upper()).lower()

        if (reformatedAnswer in self.answers):
            return True

        return False

    def testAlgorithm(self, test):

        month = int(test.split("/")[0])
        day = int(test.split("/")[1])
        year = int(test.split("/")[2])

        isLeapYear = False
        if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
            isLeapYear = True

        anchorDay = (2 + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400))%7

        doomsDay = DoomProblems.doomsDays[month]

        daysUntil = (day-doomsDay)%7

        day = (anchorDay + daysUntil)%7

        return day

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return [DoomProblems.days[self.answer]]
        
    def display(self):
        pass


#Find the anchor day for a given year in the Julian calcender
class DoomProblem3: 

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
    
    def generateProblem(self):
        
        choice = random.randint(1,100)
        if (choice <= 75):
            self.year = random.randint(1,4000)
        elif (choice <= 100):
            self.year = 4 * random.randint(1,500)

        self.anchorDay = (self.year + math.floor(self.year/4))%7
        pass

    def testAlgorithm(self,test):

        return (test + math.floor(test/4))%7


    def generateQuestionAndAnswer(self):
    
        self.answers = DoomProblems.dayInputs[self.anchorDay]

        self.answerReceiver = ("textBox",1)

        self.inputTexts.append("Day of the week:")

        self.question = []

        question = "Find the anchor day of the year " + str(self.year) + " in the Julian Calender"

        self.question.append(question)

        pass

    def checkCorrect(self, answer):

        reformatedAnswer = (answer[0].upper()).lower()

        if (reformatedAnswer in self.answers):
            return True

        return False
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return [DoomProblems.days[self.anchorDay]]

# Find the day of the week in the Julian Calender
class DoomProblem4: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []
        #print("---------")

        self.problemDisplayType = "lines"

        self.create()

        pass

    def create(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.generateProblem("null")
        self.generateQuestionAndAnswer()
    
    def generateProblem(self, test):
        
        try:
            self.month = int(test.split("/")[0])-1
            self.day = int(test.split("/")[1])
            self.year = int(test.split("/")[2])

            #Check for leap year
            self.isLeapYear = False
            if (self.year % 4 == 0):
                self.isLeapYear = True

        except:

            #Generate year
            choice = random.randint(1,100)
            if (choice <= 85):
                self.year = random.randint(1,10000)
            else:
                self.year = 4 * random.randint(1,2500)

            #Check for leap year
            self.isLeapYear = False
            if (self.year % 4 == 0):
                self.isLeapYear = True

            #Generate the month
            self.month = random.randint(0,11)
            #print("Month: " + str(DoomProblems.monthNames[self.month]))

            #Generate Day
            if (self.isLeapYear and self.month == 1):
                self.day = random.randint(1,DoomProblems.numberOfDaysInMonth[1]+1)
            else:
                self.day = random.randint(1,DoomProblems.numberOfDaysInMonth[self.month])


        #Find the anchor day
        self.anchorDay = (self.year + math.floor(self.year/4))%7
        #print("Anchor day: " + str(DoomProblems.days[self.anchorDay]))

        #Find the day of the week the day is on
        if (self.isLeapYear and (self.month == 0 or self.month == 1)):
            #print("Doomsday of month: " + str(DoomProblems.doomsDays[self.month]+1))
            self.daysAway = (self.day-(DoomProblems.doomsDays[self.month]+1))%7
        else:
            #print("Doomsday of month: " + str(DoomProblems.doomsDays[self.month]))
            self.daysAway = (self.day-(DoomProblems.doomsDays[self.month]))%7

        #print("Days away: " + str(self.daysAway))

        self.answer = (self.anchorDay + self.daysAway)%7

        #print("Julian Day: " + str(DoomProblems.days[self.answer]))

        pass

    def generateQuestionAndAnswer(self):
    
        self.answers = DoomProblems.dayInputs[self.answer]

        self.answerReceiver = ("textBox",1)

        self.inputTexts.append("Day of the week:")

        self.question = []

        question = "What day is " + str(self.month+1) + "/" + str(self.day) + "/" + str(self.year) + " in the Julian Calender"

        self.question.append(question)

        pass

    def checkCorrect(self, answer):

        reformatedAnswer = (answer[0].upper()).lower()

        if (reformatedAnswer in self.answers):
            return True

        return False

    def testAlgorithm(self, test):

        month = int(test.split("/")[0])
        day = int(test.split("/")[1])
        year = int(test.split("/")[2])

        isLeapYear = False
        if (year % 4 == 0):
            isLeapYear = True

        anchorDay = (self.year + math.floor(self.year/4))%7

        doomsDay = DoomProblems.doomsDays[month]

        daysUntil = (day-doomsDay)%7

        day = (anchorDay + daysUntil)%7

        return day

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return [DoomProblems.days[self.answer]]
        
    def display(self):
        pass

problemList = [DoomProblem1(),DoomProblem2(),DoomProblem3(),DoomProblem4()]

#Jtest = DoomProblem4()
#Gtest = DoomProblem2()
#print("Test: " + str(DoomProblems.days[test.testAlgorithm("2/5/1923")]))
#print("GTest: " + str(DoomProblems.days[Gtest.testAlgorithm(1737)]))
#print("JTest: " + str(DoomProblems.days[Jtest.testAlgorithm(1737)]))
#print(test.getQuestion())
#print(test.getAnswer())
import pygame
import Elements
import random
import math

primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

#Problem template
'''
class ModProblem1: 

    def __init__(self):

        self.question = []
        self.answers = []
        
        self.generateProblem()
        self.generateQuestionAndAnswer()

        pass
    
    def generateProblem(self):
        pass

    def generateQuestionAndAnswer(self):
        pass

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass
'''

# Chinese Remainder Problem
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

        self.mod1 = random.randint(2,100)
        self.mod2 = random.randint(2,100)

        while (math.gcd(self.mod1, self.mod2) != 1):
            self.mod2 = random.randint(1,100)
        
        self.remainder1 = random.randint(1, self.mod1-1)
        self.remainder2 = random.randint(1, self.mod2-1)

        for i in range(self.mod1 * self.mod2):
            if (i%self.mod1 == self.remainder1 and i%self.mod2 == self.remainder2):
                self.answer = i
        pass

    def generateQuestionAndAnswer(self):
        
        self.question.append(str(self.remainder1)+" (mod "+str(self.mod1)+")")
        self.question.append(str(self.remainder2)+" (mod "+str(self.mod2)+")")
        self.question.append("Find the smallest positive integer that is")

        self.answerReceiver = ("textBox",1)
        self.answers.append(self.answer)
        self.inputTexts.append("Smallest Integer:")

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

# 2 gcd problem
class ModProblem2: 

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

        self.factor = random.randint(1,300)
        self.extra1 = random.randint(1,300)
        self.extra2 = random.randint(1,300)

        while (math.gcd(self.extra1, self.extra2) != 1):
            self.extra2 = random.randint(1,300)

        self.answer = self.factor
        pass

    def generateQuestionAndAnswer(self):
        
        self.question.append("Find the gcd of " + str(self.factor*self.extra1) + " and " + str(self.factor*self.extra2))

        self.answerReceiver = ("textBox",1)
        self.answers.append(self.answer)
        self.inputTexts.append("GCD:")

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

# 3 gcd problem
class ModProblem3: 

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

        self.factor = random.randint(1,300)
        self.extra1 = random.randint(1,300)
        self.extra2 = random.randint(1,300)
        self.extra3 = random.randint(1,300)

        while (math.gcd(self.extra1, self.extra2) != 1):
            self.extra2 = random.randint(1,300)

        while (math.gcd(self.extra2, self.extra3) != 1 and math.gcd(self.extra1, self.extra3) != 1):
            self.extra3 = random.randint(1,300)

        self.answer = self.factor
        pass

    def generateQuestionAndAnswer(self):
        
        self.question.append("Find the gcd of " + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", and " + str(self.factor*self.extra3))

        self.answerReceiver = ("textBox",1)
        self.answers.append(self.answer)
        self.inputTexts.append("GCD:")

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

class ModProblem4: 

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

        self.factor = random.randint(1,300)
        self.extra1 = random.randint(1,300)
        self.extra2 = random.randint(1,300)

        while (math.gcd(self.extra1, self.extra2) != 1):
            self.extra2 = random.randint(1,300)

        self.answer = self.factor * self.extra1 * self.extra2
        pass

    def generateQuestionAndAnswer(self):
        
        self.question.append("Find the lcm of " + str(self.factor*self.extra1) + " and " + str(self.factor*self.extra2))

        self.answerReceiver = ("textBox",1)
        self.answers.append(self.answer)
        self.inputTexts.append("LCM:")

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

# 3 lcm problem
class ModProblem5: 

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

        self.factor = random.randint(1,300)
        self.extra1 = random.randint(1,300)
        self.extra2 = random.randint(1,300)
        self.extra3 = random.randint(1,300)

        while (math.gcd(self.extra1, self.extra2) != 1):
            self.extra2 = random.randint(1,300)

        while (math.gcd(self.extra2, self.extra3) != 1 and math.gcd(self.extra1, self.extra3) != 1):
            self.extra3 = random.randint(1,300)

        self.answer = self.factor * self.extra1 * self.extra2 * self.extra3
        pass

    def generateQuestionAndAnswer(self):
        
        choice = random.randint(1,3)
        if (choice == 1):
            self.question.append("Find the lcm of " + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", and " + str(self.factor*self.extra3))
        elif (choice == 2):
            self.question.append("Find the least common multiple of " + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", and " + str(self.factor*self.extra3))
        else:
            self.question.append("Compute lcm(" + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", " + str(self.factor*self.extra3)+ ")")

        self.answerReceiver = ("textBox",1)
        self.answers.append(self.answer)
        self.inputTexts.append("LCM:")

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

# Diophantine Equations Problems
class ModProblem6: 

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

        self.factor = random.randint(1,300)
        self.extra1 = random.randint(1,300)
        self.extra2 = random.randint(1,300)
        self.extra3 = random.randint(1,300)

        while (math.gcd(self.extra1, self.extra2) != 1):
            self.extra2 = random.randint(1,300)

        while (math.gcd(self.extra2, self.extra3) != 1 and math.gcd(self.extra1, self.extra3) != 1):
            self.extra3 = random.randint(1,300)

        self.answer = self.factor * self.extra1 * self.extra2 * self.extra3
        pass

    def generateQuestionAndAnswer(self):
        
        choice = random.randint(1,3)
        if (choice == 1):
            self.question.append("Find the lcm of " + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", and " + str(self.factor*self.extra3))
        elif (choice == 2):
            self.question.append("Find the least common multiple of " + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", and " + str(self.factor*self.extra3))
        else:
            self.question.append("Compute lcm(" + str(self.factor*self.extra1) + ", " + str(self.factor*self.extra2) + ", " + str(self.factor*self.extra3)+ ")")

        self.answerReceiver = ("textBox",2)
        self.answers.append(self.answer)
        self.inputTexts.append("Answer:")

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
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

problemList = [ModProblem1(), ModProblem2(), ModProblem3(), ModProblem4(), ModProblem5()]

#print(problemList[4].getQuestion())
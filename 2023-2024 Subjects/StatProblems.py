import pygame
import Elements
import random
import math

def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0)))/2

def normalcdf(mean, stanDev, lower, upper):
    zScoreLower = float(lower-mean)/stanDev
    zScoreUpper = float(upper-mean)/stanDev
    return phi(zScoreUpper)-phi(zScoreLower)

def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier


#Normal Distribution Problem, standard normal distribution (mean = 0, stanDev = 1)
class StatsProblem1: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.type = None

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

        self.zscore1 = None
        self.zscore2 = None

        self.type = random.randint(1,6)
        if (self.type == 1):
            self.zscore1 = random.randint(0,350)/100
            self.answers.append(normalcdf(0,1,-1*self.zscore1,self.zscore1))
        elif (self.type == 2):
            self.zscore1 = random.randint(0,350)/100
            self.answers.append(1-normalcdf(0,1,-1*self.zscore1,self.zscore1))
        elif (self.type == 3):
            self.zscore1 = random.randint(-350,350)/100
            self.answers.append(1-phi(self.zscore1))
        elif (self.type == 4):
            self.zscore1 = random.randint(-350,350)/100
            self.answers.append(phi(self.zscore1))
        elif (self.type == 5):
            self.zscore1 = random.randint(-350,350)/100
            self.zscore2 = random.randint(-350,350)/100
            if (self.zscore1 > self.zscore2):
                self.answers.append(phi(self.zscore1)-phi(self.zscore2))
            else:
                self.answers.append(phi(self.zscore1)-phi(self.zscore2))
        else:
            self.zscore1 = random.randint(-350,350)/100
            self.zscore2 = random.randint(-350,350)/100
            if (self.zscore1 > self.zscore2):
                self.answers.append(1-(phi(self.zscore1)-phi(self.zscore2)))
            else:
                self.answers.append(1-(phi(self.zscore2)-phi(self.zscore1)))


    def generateQuestionAndAnswer(self):

        self.answerReceiver = ("textBox",1)
        self.inputTexts = []
        self.inputTexts.append("Probability: ")

        
        if (self.type == 1):
            self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is within " + str(self.zscore1) + " standard deviations of the mean?")
        elif (self.type == 2):
            self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is farther than " + str(self.zscore1) + " standard deviations of the mean?")
        elif (self.type == 3):
            self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is greater than " + str(self.zscore1) + "?")
        elif (self.type == 4):
            self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is less than " + str(self.zscore1) + " standard deviations of the mean?")
        elif (self.type == 5):
            if (self.zscore1 > self.zscore2):
                self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is in between " + str(self.zscore2) + " and " + str(self.zscore1) + "?")
            else:
                self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is in between " + str(self.zscore1) + " and " + str(self.zscore2) + "?")
        else:
            if (self.zscore1 > self.zscore2):
                self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is not in between " + str(self.zscore2) + " and " + str(self.zscore1) + "?")
            else:
                self.question.append("If x is a random continuous variable that follows the \n standard normal distribution, what is the probability that \n x is not in between " + str(self.zscore1) + " and " + str(self.zscore2) + "?")
        
        return self.question
    
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.01):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList
    
#Normal distribution problem but not standard distribution
class StatsProblem2: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.type = None

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

        self.zscore1 = None
        self.zscore2 = None

        self.type = random.randint(1,6)
        if (self.type == 1):
            self.zscore1 = random.randint(0,350)/100
            self.answers.append(normalcdf(0,1,-1*self.zscore1,self.zscore1))
        elif (self.type == 2):
            self.zscore1 = random.randint(0,350)/100
            self.answers.append(1-normalcdf(0,1,-1*self.zscore1,self.zscore1))
        elif (self.type == 3):
            self.zscore1 = random.randint(-350,350)/100
            self.answers.append(1-phi(self.zscore1))
        elif (self.type == 4):
            self.zscore1 = random.randint(-350,350)/100
            self.answers.append(phi(self.zscore1))
        elif (self.type == 5):
            self.zscore1 = random.randint(-350,350)/100
            self.zscore2 = random.randint(-350,350)/100
            if (self.zscore1 > self.zscore2):
                self.answers.append(phi(self.zscore1)-phi(self.zscore2))
            else:
                self.answers.append(phi(self.zscore1)-phi(self.zscore2))
        else:
            self.zscore1 = random.randint(-350,350)/100
            self.zscore2 = random.randint(-350,350)/100
            if (self.zscore1 > self.zscore2):
                self.answers.append(1-(phi(self.zscore1)-phi(self.zscore2)))
            else:
                self.answers.append(1-(phi(self.zscore2)-phi(self.zscore1)))


    def generateQuestionAndAnswer(self):

        self.answerReceiver = ("textBox",1)
        self.inputTexts = []
        self.inputTexts.append("Probability: ")

        mean = random.randint(-10000, 10000)
        stanDev = random.randint(0,abs(int(mean/2)))
        if (self.type == 1):
            self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is within " + str(truncate_float(self.zscore1*stanDev, 2)) + " units of the mean?")
        elif (self.type == 2):
            self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is farther than " + str(truncate_float(self.zscore1*stanDev, 2)) + " units of the mean?")
        elif (self.type == 3):
            self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is greater than " + str(truncate_float(self.zscore1*stanDev+mean, 2)) + "?")
        elif (self.type == 4):
            self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is less than " + str(truncate_float(self.zscore1*stanDev+mean, 2)) + "?")
        elif (self.type == 5):
            if (self.zscore1 > self.zscore2):
                self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is between " + str(truncate_float(self.zscore2*stanDev+mean, 2)) + " and " + str(truncate_float(self.zscore1*stanDev+mean, 2)) + "?")
            else:
                self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is between " + str(truncate_float(self.zscore1*stanDev+mean, 2)) + " and " + str(truncate_float(self.zscore2*stanDev+mean, 2)) + "?")
        else:
            if (self.zscore1 > self.zscore2):
                self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is not between " + str(truncate_float(self.zscore2*stanDev+mean, 2)) + " and " + str(truncate_float(self.zscore1*stanDev+mean, 2)) + "?")
            else:
                self.question.append("If x is a random continuous variable that follows a \n normal distribution with mean " + str(mean) + " and \n standard deviation " + str(stanDev) + ", what is the probability that \n x is not between " + str(truncate_float(self.zscore1*stanDev+mean, 2)) + " and " + str(truncate_float(self.zscore2*stanDev+mean, 2)) + "?")
        
        return self.question
    
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.01):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList

#Estimating the binomial distribution with the normal distribution
class StatsProblem3: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.type = None

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

        self.trials = random.randint(30, 10000)
        self.success = random.randint(1,100)/100
        mean = truncate_float(self.trials * self.success, 2)
        stanDev = math.sqrt(self.trials*self.success*(1-self.success))

        self.bound1 = mean + random.randint(int(stanDev*-3.5), int(stanDev*3.5))
        zscore1 = (self.bound1-mean)/stanDev

        self.bound2 = mean + random.randint(int(stanDev*-3.5), int(stanDev*3.5))
        zscore2 = (self.bound2-mean)/stanDev

        self.type = random.randint(1,4)
        if (self.type == 1):
            self.answers.append(phi(zscore1))
        elif (self.type == 2):
            self.answers.append(1-phi(zscore1))
        elif (self.type == 3):
            if (self.bound1 < self.bound2):
                self.answers.append(phi(zscore2)-phi(zscore1))
            else:
                self.answers.append(phi(zscore2)-phi(zscore1))
        elif (self.type == 4):
            if (self.bound1 < self.bound2):
                self.answers.append(1-(phi(zscore2)-phi(zscore1)))
            else:
                self.answers.append(1-(phi(zscore2)-phi(zscore1)))

    def generateQuestionAndAnswer(self):

        self.answerReceiver = ("textBox",1)
        self.inputTexts = []
        self.inputTexts.append("Probability: ")

        if (self.type == 1):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is less than " + str(self.bound1) + "?")
        elif (self.type == 2):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is greater than " + str(self.bound1) + "?")
        elif (self.type == 3):
            if (self.bound1 < self.bound2):
                self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is in between " + str(self.bound1) + " and "  + str(self.bound2) + "?")
            else:
                self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is in between " + str(self.bound2) + " and "  + str(self.bound1) + "?")
        elif (self.type == 4):
            if (self.bound1 < self.bound2):
                self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is not in between " + str(self.bound1) + " and "  + str(self.bound2) + "?")
            else:
                self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is not in between " + str(self.bound2) + " and "  + str(self.bound1) + "?")            
            
        return self.question
    
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.01):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList

#Finding the probability of a fixed number of trials given a small binomial distribution
class StatsProblem4: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.type = None

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

        self.trials = random.randint(6,20)
        self.probabilityList = [0.01,0.05,0.1,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
        self.success = self.probabilityList[random.randint(0,len(self.probabilityList)-1)]
        self.bound = random.randint(0,self.trials)

        answer = 0

        self.type = random.randint(1,5)
        if (self.type == 1): 
            for i in range(self.bound):
                answer += (self.success ** i) * ((1-self.success) ** (self.trials-i)) * (math.comb(self.trials, i))
            self.answers.append(answer)
        elif (self.type == 2):
            for i in range(self.bound):
                answer += (self.success ** i) * ((1-self.success) ** (self.trials-i)) * (math.comb(self.trials, i))
            self.answers.append(1-answer)
        elif (self.type == 3): 
            for i in range(self.bound+1):
                answer += (self.success ** i) * ((1-self.success) ** (self.trials-i)) * (math.comb(self.trials, i))
            self.answers.append(answer)
        elif (self.type == 4): 
            for i in range(self.bound+1):
                answer += (self.success ** i) * ((1-self.success) ** (self.trials-i)) * (math.comb(self.trials, i))
            self.answers.append(1-answer)
        elif (self.type == 5): 
            answer += (self.success ** self.bound) * ((1-self.success) ** (self.trials-self.bound)) * (math.comb(self.trials, self.bound))
            self.answers.append(answer)

    def generateQuestionAndAnswer(self):

        self.answerReceiver = ("textBox",1)
        self.inputTexts = []
        self.inputTexts.append("Probability: ")

        if (self.type == 1):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is less than " + str(self.bound) + "?")
        elif (self.type == 2):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is greater than or equal to " + str(self.bound) + "?")
        elif (self.type == 3):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is less than or equal to " + str(self.bound) + "?")
        elif (self.type == 4):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is greater than " + str(self.bound) + "?")
        elif (self.type == 5):
            self.question.append("If x is a binomial random variable that with n = \n" + str(self.trials) + " and p = " + str(self.success) + ", what is the probability \n that x is equals " + str(self.bound) + "?")

        return self.question
    
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.01):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList

#Finding the mean, median and mode of a set of numbers
class StatsProblem5: 

    def __init__(self):

        self.question = []
        self.answers = []
        self.inputTexts = []

        self.type = None

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

        self.maxNumberOfElement = random.randint(3,6)
        self.numberOfDifferentElement = int(16/(self.maxNumberOfElement/2))
        self.listOfNumbers = []

        self.mode = random.randint(1, 100)
        for i in range(self.maxNumberOfElement):
            self.listOfNumbers.append(self.mode)
        for i in range(self.numberOfDifferentElement):

            number = random.randint(1,100)
            while (number == self.mode):
                number = random.randint(1,100)

            for j in range(random.randint(1, self.maxNumberOfElement)):
                self.listOfNumbers.append(number)

        totalSum = sum(self.listOfNumbers)
        self.mean = truncate_float(totalSum/len(self.listOfNumbers), 4)

        self.listOfNumbers.sort() 
        middle = len(self.listOfNumbers) // 2
        self.median = (self.listOfNumbers[middle] + self.listOfNumbers[~middle]) / 2

        random.shuffle(self.listOfNumbers)

        self.type = random.randint(1,11)
        if (self.type == 1):
            self.answers.append(self.median)
        elif (self.type == 2):
            self.answers.append(self.mean)
        elif (self.type == 3):
            self.answers.append(self.mode)
        elif (self.type == 4):
            self.answers.append(self.mean + self.median)
        elif (self.type == 5):
            self.answers.append(self.mean + self.mode)
        elif (self.type == 6):
            self.answers.append(self.mode + self.median)
        elif (self.type == 7):
            self.answers.append(self.mean * self.median)
        elif (self.type == 8):
            self.answers.append(self.mean * self.mode)
        elif (self.type == 9):
            self.answers.append(self.mode * self.median)
        elif (self.type == 10):
            self.answers.append(self.mode + self.median + self.mean)
        elif (self.type == 11):
            self.answers.append(self.mode * self.median * self.mean)

    def generateQuestionAndAnswer(self):

        self.answerReceiver = ("textBox",1)
        self.inputTexts = []
        self.inputTexts.append("Probability: ")

        listString = ""

        for i in range(16):
            listString += str(self.listOfNumbers[i]) + ", "
        
        if (len(self.listOfNumbers) > 16):
            listString += "\n"
            for i in range(16, len(self.listOfNumbers)-1):
                listString += str(self.listOfNumbers[i]) + ", "
            listString += str(self.listOfNumbers[len(self.listOfNumbers)-1])

        self.question.append(listString)
        if (self.type == 1):
            self.question.append("Find the median of the following list")
        elif (self.type == 2):
            self.question.append("Find the mean of the following list")
        elif (self.type == 3):
            self.question.append("Find the mode of the following list")
        elif (self.type == 4):
            self.question.append("Find the sum of the mean and median")
        elif (self.type == 5):
            self.question.append("Find the sum of the mean and mode")
        elif (self.type == 6):
            self.question.append("Find the sum of the mode and median")
        elif (self.type == 7):
            self.question.append("Find the product of the mean and median")
        elif (self.type == 8):
            self.question.append("Find the product of the mean and mode")
        elif (self.type == 9):
            self.question.append("Find the product of the mode and median")
        elif (self.type == 10):
            self.question.append("Find the sum of the mean, median, and mode")
        elif (self.type == 11):
            self.question.append("Find the product of the mean, median, and mode")

        return self.question

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers

    def checkCorrect(self, answer):
        correctList = []
        for i in range(len(answer)):
            try:
                if (abs(float(self.answers[i]) - float(answer[i])) > 0.01):
                    correctList.append(False)
                else:
                    correctList.append(True)
            except:
                correctList.append(False)

        return correctList
    
problemList = [StatsProblem1(), StatsProblem2(), StatsProblem3(), StatsProblem4(), StatsProblem5()]
import pygame
import random
import math

import os
import sys

current_dir = os.path.dirname(__file__)
current_dir = os.path.dirname(current_dir)
folder_dir = os.path.join(current_dir, 'Util')
print(folder_dir)
sys.path.insert(0, folder_dir)

import Elements


problemList = []

#Problem template
'''
class ExampleProblem1: 

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


class HistoryProblem1: 

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
        self.inputTexts = ["hi"]

        self.generateProblem()
        self.generateQuestionAndAnswer()
    
    def generateProblem(self):
        self.answerReceiver = ("mcq",2)
        pass

    def generateQuestionAndAnswer(self):
    
        self.answerReceiver = ("mcq",2)
        self.answers = ["super amazing"]
        self.question = ["How amazing is An"]

        pass

    def checkCorrect(self):
        pass
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answers
        
    def display(self):
        pass

problemList = [HistoryProblem1()]
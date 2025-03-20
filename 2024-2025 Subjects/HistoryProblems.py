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
import Enums

problemList = []

'''
historyProblem1 = Elements.Problem(questionType = Enums.QuestionType.Generate(),
                                   question = Elements.Question(),
                                   answer = Elements.Answer(),
                                   problemDisplayType = Enums.ProblemDisplayType.Text(),
                                   problemInputType = Enums.ProblemInputType.MCQ())
'''

problemList = []
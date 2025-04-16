import pygame
import random
import math

import os
import sys

current_dir = os.path.dirname(__file__)
current_dir = os.path.dirname(current_dir)
folder_dir = os.path.join(current_dir, 'Util')
sys.path.insert(0, folder_dir)

import Elements
import Enums

historyProblem1 = Elements.Problem(question="Who is the cutest?",
                                   answer="Ollie",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(answerChoices=["An", "Ollie", "Chuckie", "Lillian"],
                                                                               numMCQs=4,
                                                                               numAnswers=1))

historyProblem2 = Elements.Problem(question="Who is the toughest?",
                                   answer="Ollie",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(answerChoices=["An", "Ollie", "Jenny", "Ansel"],
                                                                               numMCQs=4,
                                                                               numAnswers=1))

problemList = [historyProblem1, historyProblem2]
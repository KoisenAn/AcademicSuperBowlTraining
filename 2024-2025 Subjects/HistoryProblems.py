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

testProblem1 = Elements.Problem(question="Who is the cutest?",
                                   answer="Ollie",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["An", "Chuckie", "Lillian"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

testProblem2 = Elements.Problem(question="Who is the toughest?",
                                   answer="Ollie",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["An", "Jenny", "Ansel"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

testProblem3 = Elements.Problem(question="How much Aura does Ollie have?",
                                   answer="10000",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.TextBox(numTextBoxes=1,
                                                                                   firstInputBoxText="Answer: "))

problemList = [testProblem1,
               testProblem2,
               testProblem3]
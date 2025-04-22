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
                                answer=["10000","1000","100"],
                                problemDisplayType=Enums.ProblemDisplayType.Text(),
                                problemInputType=Enums.ProblemInputType.TextBox(numTextBoxes=3,
                                                                                inputBoxText1="Answer 1: ",
                                                                                inputBoxText2="Answer 2: ",
                                                                                inputBoxText3="Answer 3: "))


#
# William Hamilton Problems
#

historyProblem101 = Elements.Problem(question="What mathematical system did William Hamilton invent in 1843?",
                                   answer="Quaternions",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Calculus", "Vector Alegbra", "Tensor Analysis", "Differential Geometry"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem102 = Elements.Problem(question="Where did William Hamilton carve the famous quaternion equation?",
                                   answer="Into Bloom Bridge",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["On a blackboard in Trinity College", "Into his study desk", "Into the wall of his observatory"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem103 = Elements.Problem(question="What was the title of William Hamilton's first published work on quaternions?",
                                   answer="Lectures on Quaternions",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Elements of Quaternions", "Quaternion Mechanics", "Principles of Quaternion Calculus"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem104 = Elements.Problem(question="Which famous poet was a lifelong friend of William Hamilton's?",
                                   answer="William Wordsworth",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Robert Burns", "William Blake", "Percy Shelley"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem105 = Elements.Problem(question="What was William Hamilton's unique physical condition related to his vision?",
                                   answer="He saw different images with each eye",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Extreme sensitivity to light", "Total blindness in one eye", "Colorblindness"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem106 = Elements.Problem(question="What college did William Hamilton attend?",
                                   answer="Trinity College",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Oxford", "Cambridge", "King's College", "St John's College"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem107 = Elements.Problem(question="What was the title of William Hamilton's early paper, originally presented in 1824 and later renamed as it developed?",
                                   answer="The Theory of Systems of Rays",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Elements of Quaternions", "The Principia Mathematica", "Lectures on Optics and Dynamics"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem108 = Elements.Problem(question="What event led to William Hamilton’s student career being cut short?",
                                   answer="He was appointed to the Andrews Professorship of Astronomy at the University of Dublin",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["He was offered a position at the Royal Irish Academy", "He moved to Cambridge", "He was invited to assist with astronomical research at Dunsink Observatory"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem109 = Elements.Problem(question="What significant optical phenomenon did William Hamilton predict in the third portion of \"Systems of Rays\" (1832)?",
                                   answer="Conical refraction",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Total internal reflection", "Polarization of light", "Diffraction patterns in single-slit experiments"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem110 = Elements.Problem(question="Which of the following Irish mathematicians published \"On a General Method in Dynamics\"?",
                                   answer="William Hamilton",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "George Salmon", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem111 = Elements.Problem(question="Which of the following Irish mathematicians was elected President of the Royal Irish Academy?",
                                   answer="William Hamilton",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "George Salmon", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem112 = Elements.Problem(question="In Hamilton's formulation of classical mechanics, what does the Hamiltonian function allow scientists to do?",
                                   answer="Predict the motion of a body or system under idealized conditions",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Identify conserved quantities in isolated mechanical systems", "Calculate the gravitational pull between two bodies", "Determine the temperature of a dynamic system"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem113 = Elements.Problem(question="Who did William Hamilton summon and confide in when he believed his death was near?",
                                   answer="Charles Graves",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["John Brinkley", "James Clerk Maxwell", "Humphrey Lloyd"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem114 = Elements.Problem(question="Which of the following statements is true about Hamilton’s book Elements of Quaternions?",
                                   answer="It contained 800 pages and was nearly finished at the time of his death",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["It was co-authored with Charles Graves", "It was completed and published during his lifetime", "It focused primarily on applications in celestial mechanics."],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem115 = Elements.Problem(question="Which of the following Irish mathematicians was admitted into the National Academy of Science?",
                                   answer="William Hamilton",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "George Salmon", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem116 = Elements.Problem(question="What year did Hamilton publish Lectures on Quaternions",
                                   answer="1852",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=[str(x) for x in range(1845, 1851)] + [str(x) for x in range(1852, 1860)],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem117 = Elements.Problem(question="Which of the following Irish mathematicians invented the hodograph?",
                                   answer="William Hamilton",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "George Salmon", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem118 = Elements.Problem(question="What year was William Hamilton born?",
                                   answer="1805",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=[str(x) for x in range(1700, 1805)] + [str(x) for x in range(1806, 1900)],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem119 = Elements.Problem(question="What year did William Hamilton die?",
                                   answer="1865",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=[str(x) for x in range(1800, 1865)] + [str(x) for x in range(1866, 1900)],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem120 = Elements.Problem(question="Where was William Hamilton born?",
                                   answer="Dublin",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Cork", "Galway", "Limerick", "Waterford", "Kilenny", "Sligo", "Drogheda", "Bray"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem121 = Elements.Problem(question="Who was the math prodigy William Hamilton encountered that led him to pursue mathematics?",
                                   answer="Zerah Colburn",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Carl Friedrich Gauss", "Blaise Pascal", "John von Neumann"], 
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem122 = Elements.Problem(question="Who was the math prodigy William Hamilton encountered that led him to pursue mathematics?",
                                   answer="Zerah Colburn",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Carl Friedrich Gauss", "Blaise Pascal", "John von Neumann"], 
                                                                               numChoices=4,
                                                                               numAnswers=1))

#
# George Salmon Problems
#

historyProblem201 = Elements.Problem(question="What year was George Salmon born?",
                                   answer="1819",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=[str(x) for x in range(1700, 1819)] + [str(x) for x in range(1806, 1900)],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem202 = Elements.Problem(question="What year did George Salmon die?",
                                   answer="1904",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=[str(x) for x in range(1800, 1904)] + [str(x) for x in range(1905, 1950)],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem203 = Elements.Problem(question="Which of the following Irish mathematicians was the 32nd Provost of Trinity College?",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem204 = Elements.Problem(question="Where did George Salmon attend before he attended Trinity College?",
                                   answer="Hamblin and Porter's School",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Eton College", "King’s School", "Harrow School"],
                                                                               numChoices=4,
                                                                               numAnswers=1))


historyProblem205 = Elements.Problem(question="Which of the following Irish mathematicians was an Anglican theologian?",
                                     answer="George Salmon",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem206 = Elements.Problem(question="During the late 1840s and 1850s, with which two prominent mathematicians was George Salmon in regular and frequent communication?",
                                     answer="Arthur Cayley and J. J. Sylvester",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Carl Gauss and Augustin-Louis Cauchy", "William Hamilton and Charles Babbage", "Bernhard Riemann and Henri Poincaré"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem207 = Elements.Problem(question="During the late 1940s and 1950s, what subject did George Salmon primarily focus on?",
                                     answer="Arthur Cayley and J. J. Sylvester",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Carl Gauss and Augustin-Louis Cauchy", "William Hamilton and Charles Babbage", "Bernhard Riemann and Henri Poincaré"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

problemList = [testProblem1, testProblem2, testProblem3]

'''
problemList = [historyProblem101,
               historyProblem102,
               historyProblem103]
'''
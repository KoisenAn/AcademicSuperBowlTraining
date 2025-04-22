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

'''
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
                                answer=["10000", "1000", "100"],
                                problemDisplayType=Enums.ProblemDisplayType.Text(),
                                problemInputType=Enums.ProblemInputType.TextBox(numTextBoxes=3,
                                                                                inputBoxText1="Your Answer 1: ",
                                                                                inputBoxText2="Your Answer 2: ",
                                                                                inputBoxText3="Your Answer 3: "))
'''

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
                                     answer="n-dimensional algebra and geometry",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Probability theory and statistics", "Number theory and cryptography", "Topology and functional analysis"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem208 = Elements.Problem(question="How many papers did George Salmon publish during the late 1940s and early 1950s?",
                                     answer="36",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=[str(x) for x in range(1, 36)] + [str(x) for x in range(37, 50)],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem209 = Elements.Problem(question="What significant mathematical work did George Salmon publish in 1859?",
                                     answer="Lessons Introductory to the Modern Higher Algebra",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Principles of Calculus", "Foundations of Number Theory", "An Introduction to Euclidean Geometry"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem210 = Elements.Problem(question="Who was the Donegall Lecturer in Mathematics at Trinity from 1858 to 1867?",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem211 = Elements.Problem(question="Who published A Treatise on Conic Sections (1848)?",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem212 = Elements.Problem(question="Who published A Treatise on Higher Plane Curves (1852)",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem213 = Elements.Problem(question="A Treatise on the Analytic Geometry of Three Dimensions (1862)?",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem214 = Elements.Problem(question="Who was awarded the Cunningham Medal of the Royal Irish Academy in 1858?",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem215 = Elements.Problem(question="Who was elected a Fellow of the Royal Society in 1868 and given the award of Royal Medal for \"For his researches in analytical geometry and the theory of surfaces\"?",
                                   answer="George Salmon",
                                   problemDisplayType=Enums.ProblemDisplayType.Text(),
                                   problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                               numChoices=4,
                                                                               numAnswers=1))

historyProblem216 = Elements.Problem(question="Who was awarded the Copley Medal in 1889?",
                                     answer="George Salmon",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["George Stokes", "William Hamilton", "Sarah Flannery"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

#
# George Stokes Problems
#

historyProblem301 = Elements.Problem(question="What school did George Stokes spend all his career?",
                                     answer="University of Cambridge",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["University of Oxford", "University of Edinburgh", "Trinity College"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1)) 

historyProblem302 = Elements.Problem(question="Who was awarded the Copley Medal in 1889?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem303 = Elements.Problem(question="Who was the Lucasian Professor of Mathematics at Cambridge?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem304 = Elements.Problem(question="Who was the Lucasian Professor of Mathematics at Cambridge?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem305 = Elements.Problem(question="Who made many important contributions to fluid dynamics and optics?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem305 = Elements.Problem(question="What was George Stokes first paper?",
                                     answer= "On some cases of fluid motion",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["On light and optics", "On the aberration of light", "On the motion of fluids in pipes"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem306 = Elements.Problem(question="Who was associated with James Clerk Maxwell and Lord Kelvin?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem307 = Elements.Problem(question="Where did George Stokes first go to school?",
                                     answer= "Bristol College",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Pembroke College", "Trinity College", "Cambridge Univeristy"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem308 = Elements.Problem(question="How did Stokes\'s Theorem get its name?",
                                     answer= "Stokes posed the theorem as an exam question based on Kelvin's extension of George Green’s work",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Stokes discovered the theorem during his research on fluid dynamics", "Lord Kelvin named it in honor of Stokes after a collaborative proof", "Stokes published the theorem in his first academic paper"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem309 = Elements.Problem(question="What does Stoke\'s Law describe?",
                                     answer= "The drag force experienced by a small spherical object moving through a viscous fluid.",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["The relationship between the pressure and volume of a gas at constant temperature.", "The gravitational force acting on an object near the Earth's surface.", "The rate at which heat is transferred between two bodies"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem310 = Elements.Problem(question="Who lectured at Cambridge about hydrostatics and optics?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem311 = Elements.Problem(question="Who published a paper on the internal friction of air and the motion of a pendulum?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem312 = Elements.Problem(question="Who won the Rumford Medal for thier work on the refrangibility of light?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

#
# Sarah Flannery Problems
#

historyProblem401 = Elements.Problem(question="What school did Sarah Flannery recieve her primary education from?",
                                     answer= "George Stokes",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "Sarah Flannery", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem402 = Elements.Problem(question="Who published the paper Cryptography - The Science of Secrey?",
                                     answer= "Sarah Flannery",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "George Stokes", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem403 = Elements.Problem(question="What place did Sarah Flannery win in the East Telecom Young Scientist and Technology Exhibition?",
                                     answer= "1st",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["2nd", "3rd", "4th", "5th"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem404 = Elements.Problem(question="Who represented Ireland at the Intel International Science and Engineering Fair?",
                                     answer= "Sarah Flannery",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "George Stokes", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem405 = Elements.Problem(question="Who developed the Cayley-Purser algorithm?",
                                     answer= "Sarah Flannery",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["William Hamilton", "George Stokes", "George Salmon"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem406 = Elements.Problem(question="How much faster was Sarah Flannery's algorithm compared to the popular RSA public key encryption algorithm?",
                                     answer= "20x",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["5x", "10x", "30x", "40x", "50x", "100x"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem407 = Elements.Problem(question="What novel did Sarah Flannery publish?",
                                     answer= "In Code: A Mathematical Journey",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["The Code Book", "Beautiful Numbers", "The Cryptographer’s Secret"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem408 = Elements.Problem(question="Where does Sarah Flannery study now?",
                                     answer= "Peterhouse College at Cambridge",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["University of Oxford", "University of Sheffield", "Syracuse University"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

historyProblem409 = Elements.Problem(question="What was the name of the expanded project Sarah Flannery submitted to the ISEF Competition after meeting Dr. Micheal Purser?",
                                     answer= "Cryptography - A New Algorithm Versus the RSA",
                                     problemDisplayType=Enums.ProblemDisplayType.Text(),
                                     problemInputType=Enums.ProblemInputType.MCQ(otherAnswerChoices=["Cryptography and the Future of Secure Communication", "Analysis of Cryptographic Algorithms", "A Study on the Efficiency of Public Key Cryptography"],
                                                                                 numChoices=4,
                                                                                 numAnswers=1))

problemList = [historyProblem101,
               historyProblem102,
               historyProblem103,
               historyProblem104,
               historyProblem105,
               historyProblem106,
               historyProblem107,
               historyProblem108,
               historyProblem109,
               historyProblem110,
               historyProblem111,
               historyProblem112,
               historyProblem113,
               historyProblem114,
               historyProblem115,
               historyProblem116,
               historyProblem117,
               historyProblem118,
               historyProblem119,
               historyProblem120,
               historyProblem121,
               historyProblem122,
               historyProblem201,
               historyProblem202,
               historyProblem203,
               historyProblem204,
               historyProblem205,
               historyProblem206,
               historyProblem207,
               historyProblem208,
               historyProblem209,
               historyProblem210,
               historyProblem211,
               historyProblem212,
               historyProblem213,
               historyProblem214,
               historyProblem215,
               historyProblem216,
               historyProblem301,
               historyProblem302,
               historyProblem303,
               historyProblem304,
               historyProblem305,
               historyProblem306,
               historyProblem307,
               historyProblem308,
               historyProblem309,
               historyProblem310,
               historyProblem311,
               historyProblem312,
               historyProblem401,
               historyProblem402,
               historyProblem403,
               historyProblem404,
               historyProblem405,
               historyProblem406,
               historyProblem407,
               historyProblem408,
               historyProblem409]
import pygame
import Elements
import Expressions
import Screens

import random

import os
import sys

#2023-2024 Year
'''
current_dir = os.path.dirname(__file__)
current_dir = os.path.dirname(current_dir)
folder_dir = os.path.join(current_dir, '2023-2024 Subjects')
sys.path.insert(0, folder_dir)


import AlgebraProblems
import ModProblems
import DoomProblems
import StatProblems

eventDict = {3798: "popUpStats", 3799: "popUpExit", 3800: "popUpInPractice", 3801: "checkExit", 3802: "popUpSettings", 4199: "credits", 4200: "home", 4201: "pracSelect", 4202: "algebra", 4203: "geometry", 4204: "statistics", 4205: "logarithms", 4206: "calculus", 4207: "mod", 4208: "dooms", 6900: "answerInputted", 6901: "newProblem"}
'''

# 2024-2025 Year
current_dir = os.path.dirname(__file__)
current_dir = os.path.dirname(current_dir)
folder_dir = os.path.join(current_dir, '2024-2025 Subjects')
sys.path.insert(0, folder_dir)

import HistoryProblems

eventDict = {3798: "popUpStats", 3799: "popUpExit", 3800: "popUpInPractice", 3801: "checkExit", 3802: "popUpSettings", 4199: "credits", 4200: "home", 4201: "pracSelect", 4202: "history", 6900: "answerInputted", 6901: "answerSelected", 6902: "newProblem"}

class testScreen:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        '''
        self.Switch = Elements.Switch(screen, 500, 500, center_X, center_Y, 50, True, "Multiple Attempts", ["right", 30], Elements.colors, 500, True)
        self.Elements.append(self.Switch)
        self.Interactive.append(self.Switch)
        '''

        self.mcqbutton = Elements.MCQButton(screen, 0, 0, center_X, center_Y, 800, 80, "text", "1. test", 30)
        self.Elements.append(self.mcqbutton)
        self.Interactive.append(self.mcqbutton)

        self.mcqbutton = Elements.MCQButton(screen, 0, 80, center_X, center_Y, 800, 80, "text", "2. test", 30)
        self.Elements.append(self.mcqbutton)
        self.Interactive.append(self.mcqbutton)

        #self.imageTest = Elements.Image(screen, center_X, center_Y, 300, 300, "IntegralSymbol.png", 1, 2, Elements.colors)
        #self.Elements.append(self.imageTest)

    def run(self):
        self.draw()
        self.checkInteractive()

    def draw(self): 
        for element in self.Elements:
            element.draw()
        
    def checkInteractive(self):
        for element in self.Interactive:
            element.mouseOver(pygame.mouse.get_pos())

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)

    def resetMCQs(self):
        for element in self.Elements:
            if (type(element) == Elements.MCQButton):
                element.deselect()
        
class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 70
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", "cX", "cY-260", titleTextSize, self.colors["darkBlue"],"calibri")
        self.textDrawer.add("Math Training Tool", "cX", "cY-200", titleTextSize, self.colors["darkBlue"],"calibri")

        ButtonTextSize = 50
        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        StartButton = Elements.Button(screen, 0, 0, 300, 150, center_X, center_Y, buttonColor, 8, 10, "text", "Start", ButtonTextSize, 4201)
        creditsHelpButton = Elements.Button(screen, 0, 185, 300, 150, center_X, center_Y, buttonColor, 8, 10, "text", "Credits/Help", ButtonTextSize, 4199)

        self.Elements.append(self.textDrawer)
        self.Elements.append(StartButton)
        self.Elements.append(creditsHelpButton)

        self.Interactive.append(StartButton)
        self.Interactive.append(creditsHelpButton)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.textDrawer.recenter(center_X, center_Y)
        for Elements in self.Elements:
            Elements.recenter(center_X, center_Y)

class creditsScreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.Elements.append(self.textDrawer)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        homeButton = Elements.Button(screen, "cX-100", "100-cY", 100, 100, center_X, center_Y, buttonColor, 8, 10, "image", "homeButton.png", 0.23, 4200)

        self.Elements.append(homeButton)
        self.Interactive.append(homeButton)

        titleTextSize = 70
        self.textDrawer.add("Created by:", 50+(self.textDrawer.findLengthOfTextRect("Created by:", titleTextSize, "calibri"))/2, 50, titleTextSize, self.colors["darkBlue"],"calibri")

        normalTextSize = 30
        self.textDrawer.add("- An Kieu", 50+(self.textDrawer.findLengthOfTextRect("- An Kieu", normalTextSize, "calibri"))/2, 100, normalTextSize, self.colors["darkBlue"],"calibri")

        self.textDrawer.add("BHSS 2023-2024 Math Team: ", 50+(self.textDrawer.findLengthOfTextRect("BHSS 2023-2024 Math Team:", titleTextSize, "calibri"))/2, 200, titleTextSize, self.colors["darkBlue"],"calibri")
        self.textDrawer.add("- An Kieu (Captain), Minh Huynh, Edward Choi, Jackson Fries, Jacob Hammond,", 50+(self.textDrawer.findLengthOfTextRect("- An Kieu (Captain), Minh Huynh, Edward Choi, Jackson Fries, Jacob Hammond,", normalTextSize, "calibri"))/2, 270, normalTextSize, self.colors["darkBlue"],"calibri")
        self.textDrawer.add("Will Yi, Dylan Stringer, Shayan Shamsipour, Yelena Zhou, Yucelin Zhou", 50+(self.textDrawer.findLengthOfTextRect("Will Yi, Dylan Stringer, Shayan Shamsipour, Yelena Zhou, Yucelin Zhou", normalTextSize, "calibri"))/2, 320, normalTextSize, self.colors["darkBlue"],"calibri")

        self.textDrawer.add("Notes Link:", 50+(self.textDrawer.findLengthOfTextRect("Notes Link:", titleTextSize, "calibri"))/2, 430, titleTextSize, self.colors["darkBlue"],"calibri")
        self.textDrawer.add("- https://docs.google.com/document/d/1ockbV0BvivHAAlEOwTlSEGRIsPMJ869TA_Aa0GmViF4/edit?usp=sharing", 50+(self.textDrawer.findLengthOfTextRect("- https://docs.google.com/document/d/1ockbV0BvivHAAlEOwTlSEGRIsPMJ869TA_Aa0GmViF4/edit?usp=sharing", normalTextSize, "calibri"))/2, 490, normalTextSize, self.colors["darkBlue"],"calibri")

        self.textDrawer.add("Assigned Subjects:", 50+(self.textDrawer.findLengthOfTextRect("Assigned Subjects:", titleTextSize, "calibri"))/2, 590, titleTextSize, self.colors["darkBlue"],"calibri")
        self.textDrawer.add("- https://docs.google.com/spreadsheets/d/18DLC50YC8_uU0_lGhbcC9ZMmexmqa_q2V47GzfwVNSE/edit#gid=0", 50+(self.textDrawer.findLengthOfTextRect("- https://docs.google.com/spreadsheets/d/18DLC50YC8_uU0_lGhbcC9ZMmexmqa_q2V47GzfwVNSE/edit#gid=0", normalTextSize, "calibri"))/2, 650, normalTextSize, self.colors["darkBlue"],"calibri")


        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.textDrawer.recenter(center_X, center_Y)
        for Elements in self.Elements:
            Elements.recenter(center_X, center_Y)

class practiceSelectScreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []

        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 70
        self.textDrawer.add("Select Practice", "cX", 100, titleTextSize, self.colors["darkBlue"], "calibri")

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])
        
        #Utility Button Sizes
        homeButton = Elements.Button(screen, "cX-100", "100-cY", 100, 100, center_X, center_Y, buttonColor, 8, 10, "image", "homeButton.png", 0.23, 4200)
        settingsButton = Elements.Button(screen, "cX-100", "cY-100", 100, 100, center_X, center_Y, buttonColor, 8, 10, "image", "settingsButton.png", 0.9, 3802)
        statsButton = Elements.Button(screen, "100-cX", "cY-100", 100, 100, center_X, center_Y,buttonColor, 8, 10, "image", "statsButton.png", 0.9, 3798)
        helpButton = Elements.Button(screen, "100-cX", "100-cY", 100, 100, center_X, center_Y, buttonColor, 8, 10, "text", "?", 70, 3798, False)

        #Practice Button Sizes
        practiceButtonTextSize = 40
        practiceButtonX = 350
        practiceButtonY = 100
        practiceSpreadY = 150
        practiceSpreadX = 400
        
        #Creating Utility Buttons
        
        #Adding To Elements
        self.Elements.append(homeButton)
        self.Elements.append(settingsButton)
        self.Elements.append(statsButton)
        self.Elements.append(helpButton)

        self.Elements.append(self.textDrawer)

        #Adding To Interactive
        self.Interactive.append(homeButton)
        self.Interactive.append(settingsButton)
        self.Interactive.append(statsButton)
        self.Interactive.append(helpButton)

        #2023-2024 Year
        '''
        #Creating Practice Buttons
        AlegbraButton = Elements.Button(screen, 0-practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Algebra", practiceButtonTextSize, 4202)
        GeometryButton = Elements.Button(screen, 0, 50-practiceSpreadY, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Geometry", practiceButtonTextSize, 4203)
        StatisticsButton = Elements.Button(screen, 0+practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Statistics", practiceButtonTextSize, 4204)
        LogarithmButton = Elements.Button(screen, 0-practiceSpreadX, 50, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Logarithms", practiceButtonTextSize, 4205)
        CalculusButton = Elements.Button(screen, 0, 50, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Calculus", practiceButtonTextSize, 4206)
        ModButton = Elements.Button(screen, 0+practiceSpreadX, 50, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Modulo Arithemtic", practiceButtonTextSize, 4207)
        DoomsButton = Elements.Button(screen, 0, 50+practiceSpreadY, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "Doomsday Rule", practiceButtonTextSize, 4208)
        
        #Creating Utility Buttons

        #Adding to Elements
        self.Elements.append(AlegbraButton)
        self.Elements.append(GeometryButton)
        self.Elements.append(StatisticsButton)
        self.Elements.append(LogarithmButton)
        self.Elements.append(CalculusButton)
        self.Elements.append(ModButton)
        self.Elements.append(DoomsButton)

        #Adding to interactive
        self.Interactive.append(AlegbraButton)
        self.Interactive.append(GeometryButton)
        self.Interactive.append(StatisticsButton)
        self.Interactive.append(LogarithmButton)
        self.Interactive.append(CalculusButton)
        self.Interactive.append(ModButton)
        self.Interactive.append(DoomsButton)
        '''

        #Creating Practice Buttons
        HistoryButton = Elements.Button(screen, 0-practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, center_X, center_Y, buttonColor, 8, 10, "text", "History", practiceButtonTextSize, 4202)
                
        #Creating Utility Buttons

        #Adding to Elements
        self.Elements.append(HistoryButton)

        #Adding to interactive
        self.Interactive.append(HistoryButton)
        
        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for Elements in self.Elements:
            Elements.recenter(center_X, center_Y)

class problemScreen:

    def __init__(self, screen, center_X, center_Y, problemType):

        self.screen = screen

        self.Elements = []
        self.Interactive = []

        self.InteractiveText = []

        self.problemType = problemType

        self.center_X = center_X
        self.center_Y = center_Y

        self.problemsDone = 0
        self.problemsDoneTracker = []

        # Stylistic Stuff

        self.colors = {"darkBlue": (53, 63, 112), "screenGrey": (230,230,230), "lightBlue":(38, 176, 237)}

        self.titleTextSize = 50

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        # 2023-2024 Year
        '''
        match (Screens.eventDict[self.problemType]):
            case "algebra":
                self.textDrawer.add("Algebra Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "calibri")
            case "mod":
                self.textDrawer.add("Modular Arithmetic Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "calibri")
            case "doom":
                self.textDrawer.add("Doomsday Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "calibri")
            case "statistics":
                self.textDrawer.add("Statistics Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "calibri")
        '''

        # 2024-2025 Year
        match (Screens.eventDict[self.problemType]):
            case "history":
                self.textDrawer.add("Modular Arithmetic Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "calibri")

        # Stylistic Stuff
        self.topDivider = Elements.Divider(screen, "horizontal", center_X, center_Y, 95, 7, self.colors["darkBlue"])
        self.bottomDivider = Elements.Divider(screen, "horizontal", center_X, center_Y, "2*cY-175", 7, self.colors["darkBlue"])
        self.problemNumberBox = Elements.ProblemNumberBox(screen, 25, 140, 60, 60, str(self.problemsDone), self.colors["darkBlue"])

        # Creates Problem Controller
        self.problemController = Elements.ProblemController(screen, self.center_X, self.center_Y, self.colors["darkBlue"])
        self.loadProblem()
        self.Elements.append(self.problemController)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        menuButton = Elements.Button(screen, "cX-50", "50-cY", 68, 68, center_X, center_Y, buttonColor, 6, 10, "image", "menuButton.png", 0.6, 3800)

        self.Elements.append(menuButton)
        self.Interactive.append(menuButton)

        self.checkButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, center_X, center_Y, buttonColor, 6, 10, "text", "Submit", 30, 6900)
        self.nextButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, center_X, center_Y, buttonColor, 6, 10, "image", "arrowButton.png", 0.3, 6901)

        self.Elements.append(self.checkButton)
        self.Interactive.append(self.checkButton)

        self.Elements.append(self.textDrawer)
        self.Elements.append(self.topDivider)
        self.Elements.append(self.bottomDivider)
        self.Elements.append(self.problemNumberBox)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def loadProblem(self):

        self.problemsDone += 1
        self.problemNumberBox.changeNumber(self.problemsDone)
        
        try:
            for textbox in self.problemController.inputElements:
                self.Interactive.append(textbox)
                self.InteractiveText.append(textbox)
        except:
            pass

        self.problemController.reset(self.problemType)
        
        # 2023-2024 Year
        '''
        match (Screens.eventDict[self.problemType]):
            case "algebra":
                self.problem = AlgebraProblems.problemList[random.randint(0, len(AlgebraProblems.problemList)-1)]
            case "mod":
                self.problem = ModProblems.problemList[random.randint(0, len(ModProblems.problemList)-1)]
            case "doom":
                self.problem = DoomProblems.problemList[random.randint(0, len(DoomProblems.problemList)-1)]
            case "statistics":
                self.problem = StatProblems.problemList[random.randint(0, len(StatProblems.problemList)-1)]
        '''

        # 2024-2025 Year
        match (Screens.eventDict[self.problemType]):
            case "history":
                self.problem = HistoryProblems.problemList[random.randint(0, len(HistoryProblems.problemList)-1)]

        self.problem.create()
        self.problemController.loadProblemDisplay(self.problem)
        self.problemController.loadProblemInput(self.problem.answerReceiver)

        for textbox in self.problemController.inputElements:
            self.Interactive.append(textbox)
            self.InteractiveText.append(textbox)

    def swapButton(self):
        if (self.checkButton in self.Elements):
            self.Elements.remove(self.checkButton)
            self.Interactive.remove(self.checkButton)
            self.Elements.append(self.nextButton)
            self.Interactive.append(self.nextButton)
        else:
            self.Elements.remove(self.nextButton)
            self.Interactive.remove(self.nextButton)
            self.Elements.append(self.checkButton)
            self.Interactive.append(self.checkButton)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)
        self.checkButton.recenter(center_X, center_Y)
        self.nextButton.recenter(center_X, center_Y)

    def getType(self):
        return self.problemType    
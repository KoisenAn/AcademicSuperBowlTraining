import pygame
import Elements
import random
import AlgebraProblems

eventDict = {4199: "credits", 4200: "home", 4201: "pracSelect", 4202: "algebra", 4203: "geometry", 4204: "statistics", 4205: "logarithms", 4206: "calculus", 4207: "mod", 4208: "dooms", 6900: "answerInputted"}

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 70
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", "cX", "cY-260", titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Math Training Tool", "cX", "cY-200", titleTextSize, self.colors["darkBlue"],"ariel")

        ButtonTextSize = 50
        
        StartButton = Elements.Button(screen, 0, 0, 300, 150, self.colors["darkBlue"], 8, 10, "text", "Start", ButtonTextSize, center_X, center_Y, 4201, True)
        creditsHelpButton = Elements.Button(screen, 0, 185, 300, 150, self.colors["darkBlue"], 8, 10, "text", "Credits/Help", ButtonTextSize, center_X, center_Y, 4199, True)

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

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.Elements.append(self.textDrawer)

        homeButton = Elements.Button(screen, 500, -260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "homeButton.png", 0.23, center_X, center_Y, 4200, True)

        self.Elements.append(homeButton)
        self.Interactive.append(homeButton)

        titleTextSize = 70
        self.textDrawer.add("Created by:", 175, 50, titleTextSize, self.colors["darkBlue"],"ariel")

        normalTextSize = 40
        self.textDrawer.add("- An Kieu", 105, 100, normalTextSize, self.colors["darkBlue"],"ariel")

        self.textDrawer.add("BHSS 2023-2024 Math Team: ", 390, 200, titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("- An Kieu (Captian), Minh Huynh, Edward Choi, Jackson Fries, Jacob Hammond,", 585, 270, normalTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Will Yi, Dylan Stringer, Shayan Shamsipour, Yelena Zhou, Yucelin Zhou", 540, 330, normalTextSize, self.colors["darkBlue"],"ariel")

        self.textDrawer.add("Notes Link:", 165, 430, titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("- https://docs.google.com/document/d/1ockbV0BvivHAAlEOwTlSEGRIsPMJ869TA_Aa0GmViF4/edit?usp=sharing", 590, 490, normalTextSize-10, self.colors["darkBlue"],"ariel")

        self.textDrawer.add("Assigned Subjects", 255, 590, titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("- https://docs.google.com/spreadsheets/d/18DLC50YC8_uU0_lGhbcC9ZMmexmqa_q2V47GzfwVNSE/edit#gid=0", 575, 650, normalTextSize-10, self.colors["darkBlue"],"ariel")


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

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 70
        self.textDrawer.add("Select Practice", "cX", "cY-260", titleTextSize, self.colors["darkBlue"], "ariel")
        
        #Utility Button Sizes
        homeButton = Elements.Button(screen, 500, -260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "homeButton.png", 0.23, center_X, center_Y, 4200, True)
        settingsButton = Elements.Button(screen, 500, 260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "settingsButton.png", 0.9, center_X, center_Y, 4200, False)
        statsButton = Elements.Button(screen, -500, 260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "statsButton.png", 0.9, center_X, center_Y, 4200, False)

        #Practice Button Sizes
        practiceButtonTextSize = 40
        practiceButtonX = 350
        practiceButtonY = 100
        practiceSpreadY = 150
        practiceSpreadX = 400
        
        #Creating Practice Buttons
        AlegbraButton = Elements.Button(screen, 0-practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Algebra", practiceButtonTextSize, center_X, center_Y, 4202, True)
        GeometryButton = Elements.Button(screen, 0, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Geometry", practiceButtonTextSize, center_X, center_Y, 4203, False)
        StatisticsButton = Elements.Button(screen, 0+practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Statistics", practiceButtonTextSize, center_X, center_Y, 4204, False)
        LogarithmButton = Elements.Button(screen, 0-practiceSpreadX, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Logarithms", practiceButtonTextSize, center_X, center_Y, 4205, False)
        CalculusButton = Elements.Button(screen, 0, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Calculus", practiceButtonTextSize, center_X, center_Y, 4206, False)
        ModButton = Elements.Button(screen, 0+practiceSpreadX, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Modulo Arithemtic", practiceButtonTextSize, center_X, center_Y, 4207, False)
        DoomsButton = Elements.Button(screen, 0, 50+practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Doomsday Rule", practiceButtonTextSize, center_X, center_Y, 4208, False)
        
        #Creating Utility Buttons

        #Adding to Elements
        self.Elements.append(AlegbraButton)
        self.Elements.append(GeometryButton)
        self.Elements.append(StatisticsButton)
        self.Elements.append(LogarithmButton)
        self.Elements.append(CalculusButton)
        self.Elements.append(ModButton)
        self.Elements.append(DoomsButton)

        self.Elements.append(homeButton)
        self.Elements.append(settingsButton)
        self.Elements.append(statsButton)

        self.Elements.append(self.textDrawer)

        #Adding to interactive
        self.Interactive.append(AlegbraButton)
        self.Interactive.append(GeometryButton)
        self.Interactive.append(StatisticsButton)
        self.Interactive.append(LogarithmButton)
        self.Interactive.append(CalculusButton)
        self.Interactive.append(ModButton)
        self.Interactive.append(DoomsButton)

        self.Interactive.append(homeButton)
        self.Interactive.append(settingsButton)
        self.Interactive.append(statsButton)

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

class algebraScreen:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.Elements = []
        self.Interactive = []

        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.problemsDone = 0

        self.colors = {"darkBlue":(53, 63, 112)}

        self.titleTextSize = 50

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.textDrawer.add("Algebra Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "ariel")

        self.topDivider = Elements.divider(screen, "horizontal", center_X, center_Y, 95, 7, self.colors["darkBlue"])
        self.bottomDivider = Elements.divider(screen, "horizontal", center_X, center_Y, "2*cY-175", 7, self.colors["darkBlue"])
        self.problemNumberBox = Elements.problemNumberBox(screen, 25, 140, 60, 60, str(self.problemsDone+1), self.colors["darkBlue"])

        self.problemDisplayer = Elements.problemDisplayer(screen, self.center_X, self.center_Y, self.colors["darkBlue"])
        self.loadProblem()
        self.Elements.append(self.problemDisplayer)

        menuButton = Elements.Button(screen, 550, -310, 68, 68, self.colors["darkBlue"], 6, 10, "image", "menuButton.png", 0.6, center_X, center_Y, 4200, True)

        self.Elements.append(menuButton)
        self.Interactive.append(menuButton)

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

        self.problem = AlgebraProblems.problemList[random.randint(0,1)]
        self.problemDisplayer.loadProblemDisplay(self.problem.problemDisplayType,self.problem.getQuestion())
        self.problemDisplayer.loadProblemInput(self.problem.answerReceiver)

        for textbox in self.problemDisplayer.inputElements:
            self.Interactive.append(textbox)
            self.InteractiveText.append(textbox)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)
import pygame
import Elements
import Expressions
import Screens
import Controllers
import Enums

import random

import os
import sys

# 2024-2025 Year
current_dir = os.path.dirname(__file__)
current_dir = os.path.dirname(current_dir)
folder_dir = os.path.join(current_dir, '2024-2025 Subjects')
sys.path.insert(0, folder_dir)

import HistoryProblems

eventDict = {
    # Pop-ups
    3798: "popUpStats", 
    3799: "popUpExit", 
    3800: "popUpInPractice",
    3801: "checkExit", 
    3802: "popUpSettings", 
    # Practice Selection Events
    4199: "credits", 
    4200: "home", 
    4201: "pracSelect", 
    4202: "history", 
    # In practice events
    6900: "answerInputted", 
    6901: "answerSelected", 
    6902: "newProblem", 
    6903: "Choice A", 
    6904: "Choice B",
    6905: "Choice C",
    6906: "Choice D"}

class Screen:
    def __init__(self, screen = None):
        self.screen = screen
        self.elements = []
        self.interactive = []

    def run(self):
        self.checkInteractive()
        self.draw()

    def checkInteractive(self):
        for element in self.interactive:
            element.mouseOver(pygame.mouse.get_pos())   

    def draw(self):
        for element in self.elements:
            element.draw()

    def recenter(self):
        for elements in self.elements:
            elements.recenter() 

class TestScreen(Screen):

    def __init__(self, screen):

        super().__init__(screen)

        '''
        self.Switch = Elements.Switch(screen, 500, 500, center_X, center_Y, 50, True, "Multiple Attempts", ["right", 30], Elements.colors, 500, True)
        self.elements.append(self.Switch)
        self.interactive.append(self.Switch)
        

        self.mcqbutton = Elements.MCQButton(screen, 0, 0, center_X, center_Y, 800, 80, 0, "text", "1. test", 30)
        self.elements.append(self.mcqbutton)
        self.interactive.append(self.mcqbutton)

        self.mcqbutton = Elements.MCQButton(screen, 0, 80, center_X, center_Y, 800, 80, 1, "text", "2. test", 30)
        self.elements.append(self.mcqbutton)
        self.interactive.append(self.mcqbutton)

        self.imageTest = Elements.Image(screen, center_X, center_Y, 300, 300, "IntegralSymbol.png", 1, 2, Elements.colors)
        self.elements.append(self.imageTest)
        '''

    def resetMCQs(self):
        for element in self.elements:
            if (type(element) == Elements.MCQButton):
                element.deselect()
        
class HomeScreen(Screen):

    def __init__(self, screen=None):

        super().__init__(screen)

        self.title = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.Center(),
                                                                                    xOffset=0, 
                                                                                    yOffset=-175, 
                                                                                    refAnchor=Enums.Anchor.Center()),
                                  string="2024-2025 BHSS Academic Super Bowl Math Training Tool",
                                  font="calibri",
                                  fontSize=60,
                                  alignment=Enums.TextAlignment.Center(),
                                  showingTextBox=False)

        buttonTextSize = 50
        buttonColor = ((53, 63, 112), (230,230,230))

        startButton = Elements.Button(screen=self.screen, 
                                      event=4201, 
                                      sizeX=175, 
                                      sizeY=125, 
                                      positionController=Controllers.PositionController(objectLength=175,
                                                                                        objectHeight=125, 
                                                                                        drawAnchor=Enums.Anchor.Center(),
                                                                                        xOffset=0, 
                                                                                        yOffset=0, 
                                                                                        refAnchor=Enums.Anchor.Center()), 
                                      color=buttonColor, 
                                      labelInformation="Start", 
                                      labelType=Enums.Label.Text(),
                                      labelSize = buttonTextSize,
                                      font = "calibri",
                                      labelColor = (0,0,0))
        creditsHelpButton = Elements.Button(screen=self.screen, 
                                            event=4199, 
                                            positionController=Controllers.PositionController(objectLength=300,
                                                                                        objectHeight=125, 
                                                                                        drawAnchor=Enums.Anchor.Center(),
                                                                                        xOffset=0, 
                                                                                        yOffset=150, 
                                                                                        refAnchor=Enums.Anchor.Center()), 
                                            sizeX=300, 
                                            sizeY=125, 
                                            color=buttonColor, 
                                            labelInformation="Credits/Help", 
                                            labelType=Enums.Label.Text(),
                                            labelSize=buttonTextSize,
                                            font = "calibri",
                                            labelColor = (0,0,0))

        self.elements.append(self.title)
        self.elements.append(startButton)
        self.elements.append(creditsHelpButton)

        self.interactive.append(startButton)
        self.interactive.append(creditsHelpButton)

        self.draw()

class CreditsScreen(Screen):

    def __init__(self, screen=None):

        super().__init__(screen)

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        homeButton = Elements.Button(screen=screen, 
                                     event=4200, 
                                     sizeX=100, 
                                     sizeY=100, 
                                     positionController=Controllers.PositionController(objectLength=100,
                                                                                       objectHeight=100, 
                                                                                       drawAnchor=Enums.Anchor.TopLeft(),
                                                                                       xOffset=-125, 
                                                                                       yOffset=-125, 
                                                                                       refAnchor=Enums.Anchor.BottomRight()), 
                                     color=buttonColor, 
                                     labelInformation="homeIcon.png", 
                                     labelSize = 0.25,
                                     labelType=Enums.Label.Image())        

        self.elements.append(homeButton)
        self.interactive.append(homeButton)

        self.textController = Controllers.TextController(screen=self.screen)

        self.developedByHeading = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.TopLeft(),
                                                                                    xOffset=20, 
                                                                                    yOffset=20, 
                                                                                    refAnchor=Enums.Anchor.TopLeft()),
                                  string="Created By: ",
                                  font="calibri",
                                  fontSize=50,
                                  alignment=Enums.TextAlignment.Left(),
                                  showingTextBox=False) 
        self.developerNames = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.TopLeft(),
                                                                                    xOffset=20, 
                                                                                    yOffset=85, 
                                                                                    refAnchor=Enums.Anchor.TopLeft()),
                                  string=" An Kieu",
                                  font="calibri",
                                  fontSize=30,
                                  alignment=Enums.TextAlignment.Left(),
                                  showingTextBox=False) 
        self.team2324Heading = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.TopLeft(),
                                                                                    xOffset=20, 
                                                                                    yOffset=135, 
                                                                                    refAnchor=Enums.Anchor.TopLeft()),
                                  string="BHSS 2023-2024 Math Team: ",
                                  font="calibri",
                                  fontSize=50,
                                  alignment=Enums.TextAlignment.Left(),
                                  showingTextBox=False) 
        self.team2324Names = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.TopLeft(),
                                                                                    xOffset=22, 
                                                                                    yOffset=200, 
                                                                                    refAnchor=Enums.Anchor.TopLeft()),
                                  string="An Kieu (Captain), Minh Huynh, Edward Choi, Jackson Fries, Jacob Hammond, Will Yi, Dylan Stringer, Shayan Shamsipour, Yelena Zhou, Yucelin Zhou",
                                  font="calibri",
                                  fontSize=30,
                                  lineSpacing=1.5,
                                  alignment=Enums.TextAlignment.Left(),
                                  showingTextBox=False) 
        self.team2425Heading = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.TopLeft(),
                                                                                    xOffset=20, 
                                                                                    yOffset=300, 
                                                                                    refAnchor=Enums.Anchor.TopLeft()),
                                  string="BHSS 2024-2025 Math Team: ",
                                  font="calibri",
                                  fontSize=50,
                                  alignment=Enums.TextAlignment.Left(),
                                  showingTextBox=False) 
        self.team2425Names = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.TopLeft(),
                                                                                    xOffset=22, 
                                                                                    yOffset=365, 
                                                                                    refAnchor=Enums.Anchor.TopLeft()),
                                  string="An Kieu (Captain), Bach Kieu, Edward Choi, Jackson Fries, Jacob Hammond, Will Yi, Jachary Yang, Yelena Zhou, Yucelin Zhou",
                                  font="calibri",
                                  fontSize=30,
                                  alignment=Enums.TextAlignment.Left(),
                                  lineSpacing=1.5,
                                  showingTextBox=False) 
        
        self.textController.add(self.developedByHeading)
        self.textController.add(self.developerNames)
        self.textController.add(self.team2324Heading)
        self.textController.add(self.team2324Names)
        self.textController.add(self.team2425Heading)
        self.textController.add(self.team2425Names)

        self.elements.append(self.textController)

class PracticeSelectScreen(Screen):

    def __init__(self, screen=None):

        super().__init__(screen)

        self.colors = {"darkBlue":(53,63,112), "screenGrey": (230,230,230)}

        self.title = Elements.Text(screen=self.screen,
                                  positionController=Controllers.PositionController(objectLength=1100,
                                                                                    objectHeight=200,
                                                                                    drawAnchor=Enums.Anchor.Center(),
                                                                                    xOffset=0, 
                                                                                    yOffset=-225, 
                                                                                    refAnchor=Enums.Anchor.Center()),
                                  string="Select Practice",
                                  font="calibri",
                                  fontSize=60,
                                  alignment=Enums.TextAlignment.Center(),
                                  showingTextBox=False) 
        self.elements.append(self.title)       

        buttonColor = ((53,63,112), (230,230,230))
        
        #Utility Button Sizes
        homeButton = Elements.Button(screen=screen, 
                                     event=4200, 
                                     sizeX=100, 
                                     sizeY=100, 
                                     positionController=Controllers.PositionController(objectLength=100,
                                                                                       objectHeight=100, 
                                                                                       drawAnchor=Enums.Anchor.TopLeft(),
                                                                                       xOffset=-275, 
                                                                                       yOffset=225, 
                                                                                       refAnchor=Enums.Anchor.Center()), 
                                     color=buttonColor, 
                                     labelInformation="homeIcon.png", 
                                     labelSize = 0.25,
                                     labelType=Enums.Label.Image())
        settingsButton = Elements.Button(screen=screen, 
                                     event=3802, 
                                     sizeX=100, 
                                     sizeY=100, 
                                     positionController=Controllers.PositionController(objectLength=100,
                                                                                       objectHeight=100, 
                                                                                       drawAnchor=Enums.Anchor.TopLeft(),
                                                                                       xOffset=-125, 
                                                                                       yOffset=225, 
                                                                                       refAnchor=Enums.Anchor.Center()), 
                                     color=buttonColor, 
                                     labelInformation="settingsIcon.png", 
                                     labelSize = 0.25,
                                     labelType=Enums.Label.Image())
        helpButton = Elements.Button(screen=screen, 
                                     event=3798, 
                                     sizeX=100, 
                                     sizeY=100, 
                                     positionController=Controllers.PositionController(objectLength=100,
                                                                                       objectHeight=100, 
                                                                                       drawAnchor=Enums.Anchor.TopLeft(),
                                                                                       xOffset=25, 
                                                                                       yOffset=225, 
                                                                                       refAnchor=Enums.Anchor.Center()), 
                                     color=buttonColor, 
                                     labelInformation="questionIcon.png", 
                                     labelSize = 0.25,
                                     labelType=Enums.Label.Image())    
        statsButton = Elements.Button(screen=screen, 
                                     event=3798, 
                                     sizeX=100, 
                                     sizeY=100, 
                                     positionController=Controllers.PositionController(objectLength=100,
                                                                                       objectHeight=100, 
                                                                                       drawAnchor=Enums.Anchor.TopLeft(),
                                                                                       xOffset=175, 
                                                                                       yOffset=225, 
                                                                                       refAnchor=Enums.Anchor.Center()), 
                                     color=buttonColor, 
                                     labelInformation="questionIcon.png", 
                                     labelSize = 0.25,
                                     labelType=Enums.Label.Image())      

        #Adding Utility Buttons
        
        #Adding To Elements
        self.elements.append(homeButton)
        self.elements.append(settingsButton)
        self.elements.append(statsButton)
        self.elements.append(helpButton)

        #Adding To Interactive
        self.interactive.append(homeButton)
        self.interactive.append(settingsButton)
        self.interactive.append(statsButton)
        self.interactive.append(helpButton)

        #Practice Button Sizes
        practicebuttonTextSize = 40

        #Creating Practice Buttons
        quaternionButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        sizeX=230, 
                                        sizeY=100, 
                                        positionController=Controllers.PositionController(objectLength=230,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.Anchor.Center(),
                                                                                          xOffset=0, 
                                                                                          yOffset=-150, 
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        color=buttonColor, 
                                        labelInformation="Quaternions", 
                                        labelSize = practicebuttonTextSize,
                                        labelType=Enums.Label.Text(),
                                        font = "calibri",
                                        labelColor = (0,0,0))        
        graphButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        sizeX=250, 
                                        sizeY=100, 
                                        positionController=Controllers.PositionController(objectLength=250,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.Anchor.Center(),
                                                                                          xOffset=0, 
                                                                                          yOffset=-50, 
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        color=buttonColor, 
                                        labelInformation="Graph Theory", 
                                        labelSize = practicebuttonTextSize,
                                        labelType=Enums.Label.Text(),
                                        font = "calibri",
                                        labelColor = (0,0,0))
        moduloButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        sizeX=345, 
                                        sizeY=100, 
                                        positionController=Controllers.PositionController(objectLength=345,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.Anchor.Center(),
                                                                                          xOffset=0, 
                                                                                          yOffset=50, 
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        color=buttonColor, 
                                        labelInformation="Modulo Arithmetic", 
                                        labelSize = practicebuttonTextSize,
                                        labelType=Enums.Label.Text(),
                                        font = "calibri",
                                        labelColor = (0,0,0))
        historyButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        sizeX=155, 
                                        sizeY=100, 
                                        positionController=Controllers.PositionController(objectLength=155,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.Anchor.Center(),
                                                                                          xOffset=0, 
                                                                                          yOffset=150, 
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        color=buttonColor, 
                                        labelInformation="History", 
                                        labelSize = practicebuttonTextSize,
                                        labelType=Enums.Label.Text(),
                                        font = "calibri",
                                        labelColor = (0,0,0))
        
        #Adding to Elements
        self.elements.append(quaternionButton)
        self.elements.append(graphButton)
        self.elements.append(moduloButton)
        self.elements.append(historyButton)

        #Adding to interactive
        self.interactive.append(quaternionButton)
        self.interactive.append(graphButton)
        self.interactive.append(moduloButton)
        self.interactive.append(historyButton)
        
        self.draw()

class ProblemScreen(Screen):

    def __init__(self, screen=None, problemType=None):

        super().__init__(screen)

        self.problemType = problemType

        self.problemsDone = 0
        self.problemsDoneTracker = []

        # Stylistic Stuff

        self.colors = {"darkBlue": (53, 63, 112), "screenGrey": (230,230,230), "lightBlue":(38, 176, 237)}

        self.titleTextSize = 50

        # 2024-2025 Year
        match (Screens.eventDict[self.problemType]):
            case "history":
                self.title = Elements.Text(screen=self.screen,
                                           positionController=Controllers.PositionController(objectLength=1100,
                                                                                             objectHeight=200,
                                                                                             drawAnchor=Enums.Anchor.TopCenter(),
                                                                                             xOffset=0, 
                                                                                             yOffset=10, 
                                                                                             refAnchor=Enums.Anchor.TopCenter()),
                                           string="History Practice",
                                           font="calibri",
                                           fontSize=self.titleTextSize,
                                           alignment=Enums.TextAlignment.Center(),
                                           showingTextBox=False)    
                self.elements.append(self.title)            

        # Stylistic Stuff
        self.problemNumberBox = Elements.ProblemNumberBox(screen=self.screen, 
                                                          positionController=Controllers.PositionController(objectLength=60,
                                                                                             objectHeight=60,
                                                                                             drawAnchor=Enums.Anchor.TopLeft(),
                                                                                             xOffset=30, 
                                                                                             yOffset=95, 
                                                                                             refAnchor=Enums.Anchor.TopLeft()),
                                                          problemNumber=str(self.problemsDone))
        
        #self.inputController = Controllers.TextBoxController(screen=screen, numTextBoxes=3, y=300, label1="i: ", label2="j: ", label3="k: ")
        self.inputController = Controllers.MCQController(screen=screen, 
                                                         y=300,
                                                         maxSelectable=2, 
                                                         label1="An", 
                                                         label2="Lillian", 
                                                         label4="Ollie")

        self.elements.append(self.inputController)
        self.interactive.append(self.inputController)
        
        # Creates Problem Controller
        #self.problemController = Controllers.ProblemController(screen, self.center_X, self.center_Y, self.colors["darkBlue"], self.elements, self.interactive)
        #self.loadProblem()
        #self.elements.append(self.problemController)
        
        '''
        menuButton = Elements.Button(screen, "cX-50", "50-cY", 68, 68, center_X, center_Y, buttonColor, 6, 10, "image", "menuButton.png", 0.6, 3800)

        self.elements.append(menuButton)
        self.interactive.append(menuButton)

        self.checkButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, center_X, center_Y, buttonColor, 6, 10, "text", "Submit", 30, 6900)
        self.nextButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, center_X, center_Y, buttonColor, 6, 10, "image", "arrowButton.png", 0.3, 6901)

        self.elements.append(self.checkButton)
        self.interactive.append(self.checkButton)
        '''

        self.elements.append(self.problemNumberBox)

        self.draw()

    def loadProblem(self):

        self.problemsDone += 1
        self.problemNumberBox.changeNumber(self.problemsDone)
        
        try:
            for textbox in self.problemController.inputElements:
                self.interactive.append(textbox)
                self.interactiveText.append(textbox)
        except:
            pass

        self.problemController.reset(self.problemType)

        # 2024-2025 Year
        match (Screens.eventDict[self.problemType]):
            case "history":
                self.problem = HistoryProblems.problemList[random.randint(0, len(HistoryProblems.problemList)-1)]

        self.problem.create()
        self.problemController.loadProblemDisplay(self.problem)
        self.problemController.loadProblemInput(self.problem.answerReceiver)

        for inputElement in self.problemController.inputElements:
            self.interactive.append(inputElement)
            self.interactiveText.append(inputElement)

    '''
    def swapButton(self):
        if (self.checkButton in self.elements):
            self.elements.remove(self.checkButton)
            self.interactive.remove(self.checkButton)
            self.elements.append(self.nextButton)
            self.interactive.append(self.nextButton)
        else:
            self.elements.remove(self.nextButton)
            self.interactive.remove(self.nextButton)
            self.elements.append(self.checkButton)
            self.interactive.append(self.checkButton)
    '''

    def recenter(self):
        super().recenter()
        #self.checkButton.recenter(center_X, center_Y)
        #self.nextButton.recenter(center_X, center_Y)

    def getType(self):
        return self.problemType    
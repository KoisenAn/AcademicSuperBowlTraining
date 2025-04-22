import pygame
import random
import os
import sys

import Elements
import Screens
import Controllers
import Enums

# 2024-2025 Year
current_dir = os.path.dirname(__file__)
current_dir = os.path.dirname(current_dir)
folder_dir = os.path.join(current_dir, '2024-2025 Subjects')
sys.path.insert(0, folder_dir)

import HistoryProblems

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
        for element in self.elements:
            element.recenter() 

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
                                                                                    objectHeight=Enums.AUTO_DETERMINE_ATTRIBUTE(),
                                                                                    drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                    xOffset=0, 
                                                                                    yOffset=-175, 
                                                                                    refAnchor=Enums.ANCHOR.CENTER()),
                                  string="2024-2025 BHSS Academic Super Bowl Math Training Tool",
                                  font="calibri",
                                  fontSize=60,
                                  alignment=Enums.TEXT_ALIGNMENT.CENTER(),
                                  showingTextBox=False)
        buttonTextSize = 50

        startButton = Elements.Button(screen=self.screen, 
                                      event=4201, 
                                      length=175, 
                                      height=125, 
                                      positionController=Controllers.PositionController(objectLength=175,
                                                                                        objectHeight=125, 
                                                                                        drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                        xOffset=0, 
                                                                                        yOffset=0, 
                                                                                        refAnchor=Enums.ANCHOR.CENTER()), 
                                      labelInformation="Start", 
                                      labelType=Enums.LABEL_TYPE.TEXT(),
                                      labelSize = buttonTextSize,
                                      font = "calibri",
                                      labelColor = (0,0,0))
        creditsHelpButton = Elements.Button(screen=self.screen, 
                                            event=4199, 
                                            positionController=Controllers.PositionController(objectLength=300,
                                                                                        objectHeight=125, 
                                                                                        drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                        xOffset=0, 
                                                                                        yOffset=150, 
                                                                                        refAnchor=Enums.ANCHOR.CENTER()), 
                                            length=300, 
                                            height=125, 
                                            labelInformation="Credits/Help", 
                                            labelType=Enums.LABEL_TYPE.TEXT(),
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

        homeButton = Elements.Button(screen=screen, 
                                     event=4200, 
                                     length=100, 
                                     height=100, 
                                     positionController=Controllers.PositionController(drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                       xOffset=-125, 
                                                                                       yOffset=-125, 
                                                                                       refAnchor=Enums.ANCHOR.BOTTOM_RIGHT()), 
                                     labelInformation="homeIcon.png", 
                                     labelSize = 0.25,
                                     labelType=Enums.LABEL_TYPE.IMAGE())        

        self.elements.append(homeButton)
        self.interactive.append(homeButton)

        self.textController = Controllers.TextController(screen=self.screen)

        self.developedByHeading = Elements.Text(screen=self.screen,
                                                positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                                  drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                                  xOffset=20, 
                                                                                                  yOffset=20, 
                                                                                                  refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                                string="Created By: ",
                                                font="calibri",
                                                fontSize=50,
                                                alignment=Enums.TEXT_ALIGNMENT.LEFT(),
                                                showingTextBox=False) 
        self.developerNames = Elements.Text(screen=self.screen,
                                            positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                              drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                              xOffset=20, 
                                                                                              yOffset=(lambda: self.developedByHeading.positionController.getOffsets()[1] + self.developedByHeading.positionController.getSize()[1]), 
                                                                                              refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                            string=" An Kieu",
                                            font="calibri",
                                            fontSize=30,
                                            alignment=Enums.TEXT_ALIGNMENT.LEFT(),
                                            showingTextBox=False) 
        self.team2324Heading = Elements.Text(screen=self.screen,
                                             positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                               drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                               xOffset=20, 
                                                                                               yOffset=(lambda: self.developerNames.positionController.getOffsets()[1] + self.developerNames.positionController.getSize()[1]+20), 
                                                                                               refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                             string="BHSS 2023-2024 Math Team: ",
                                             font="calibri",
                                             fontSize=50,
                                             alignment=Enums.TEXT_ALIGNMENT.LEFT(),
                                             showingTextBox=False) 
        self.team2324Names = Elements.Text(screen=self.screen,
                                           positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                             drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                             xOffset=22, 
                                                                                             yOffset=(lambda: self.team2324Heading.positionController.getOffsets()[1] + self.team2324Heading.positionController.getSize()[1]), 
                                                                                             refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                           string="An Kieu (Captain), Minh Huynh, Edward Choi, Jackson Fries, Jacob Hammond, Will Yi, Dylan Stringer, Shayan Shamsipour, Yelena Zhou, Yucelin Zhou",
                                           font="calibri",
                                           fontSize=30,
                                           lineSpacing=1.5,
                                           alignment=Enums.TEXT_ALIGNMENT.LEFT(),
                                           showingTextBox=False) 
        self.team2425Heading = Elements.Text(screen=self.screen,
                                             positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                               drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                               xOffset=20, 
                                                                                               yOffset=(lambda: self.team2324Names.positionController.getOffsets()[1] + self.team2324Names.positionController.getSize()[1]+20),
                                                                                               refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                             string="BHSS 2024-2025 Math Team: ",
                                             font="calibri",
                                             fontSize=50,
                                             alignment=Enums.TEXT_ALIGNMENT.LEFT(),
                                             showingTextBox=False) 
        self.team2425Names = Elements.Text(screen=self.screen,
                                           positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-62),
                                                                                             drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                             xOffset=22, 
                                                                                             yOffset=(lambda: self.team2425Heading.positionController.getOffsets()[1] + self.team2425Heading.positionController.getSize()[1]),
                                                                                             refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                           string="An Kieu (Captain), Bach Kieu, Edward Choi, Jackson Fries, Jacob Hammond, Will Yi, Jachary Yang, Yelena Zhou, Yucelin Zhou",
                                           font="calibri",
                                           fontSize=30,
                                           alignment=Enums.TEXT_ALIGNMENT.LEFT(),
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
                                                                                    drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                    xOffset=0, 
                                                                                    yOffset=-225, 
                                                                                    refAnchor=Enums.ANCHOR.CENTER()),
                                  string="Select Practice",
                                  font="calibri",
                                  fontSize=60,
                                  alignment=Enums.TEXT_ALIGNMENT.CENTER(),
                                  showingTextBox=False) 
        self.elements.append(self.title)       
        
        #Utility Button Sizes
        homeButton = Elements.Button(screen=screen, 
                                     event=4200, 
                                     length=100, 
                                     height=100, 
                                     positionController=Controllers.PositionController(objectLength=100,
                                                                                       objectHeight=100, 
                                                                                       drawAnchor=Enums.ANCHOR.TOP_CENTER(),
                                                                                       xOffset=0,
                                                                                       yOffset=225, 
                                                                                       refAnchor=Enums.ANCHOR.CENTER()), 
                                     labelInformation="homeIcon.png", 
                                     labelSize=0.25,
                                     labelType=Enums.LABEL_TYPE.IMAGE())   

        #Adding Utility Buttons
        
        #Adding To Elements
        self.elements.append(homeButton)

        #Adding To Interactive
        self.interactive.append(homeButton)

        #Practice Button Sizes
        practicebuttonTextSize = 40

        #Creating Practice Buttons
        quaternionButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        length=230, 
                                        height=100, 
                                        positionController=Controllers.PositionController(objectLength=230,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                          xOffset=0, 
                                                                                          yOffset=-150, 
                                                                                          refAnchor=Enums.ANCHOR.CENTER()), 
                                        labelInformation="Quaternions", 
                                        labelSize=practicebuttonTextSize,
                                        labelType=Enums.LABEL_TYPE.TEXT(),
                                        font="calibri",
                                        labelColor=(0,0,0))        
        graphButton = Elements.Button(screen=screen, 
                                      event=4202, 
                                      length=250, 
                                      height=100, 
                                      positionController=Controllers.PositionController(objectLength=250,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                          xOffset=0, 
                                                                                          yOffset=-50, 
                                                                                          refAnchor=Enums.ANCHOR.CENTER()), 
                                        labelInformation="Graph Theory", 
                                        labelSize=practicebuttonTextSize,
                                        labelType=Enums.LABEL_TYPE.TEXT(),
                                        font="calibri",
                                        labelColor=(0,0,0))
        moduloButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        length=345, 
                                        height=100, 
                                        positionController=Controllers.PositionController(objectLength=345,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                          xOffset=0, 
                                                                                          yOffset=50, 
                                                                                          refAnchor=Enums.ANCHOR.CENTER()), 
                                        labelInformation="Modulo Arithmetic", 
                                        labelSize=practicebuttonTextSize,
                                        labelType=Enums.LABEL_TYPE.TEXT(),
                                        font="calibri",
                                        labelColor=(0,0,0))
        historyButton = Elements.Button(screen=screen, 
                                        event=4202, 
                                        length=155, 
                                        height=100, 
                                        positionController=Controllers.PositionController(objectLength=155,
                                                                                          objectHeight=100, 
                                                                                          drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                          xOffset=0, 
                                                                                          yOffset=150, 
                                                                                          refAnchor=Enums.ANCHOR.CENTER()), 
                                        labelInformation="History", 
                                        labelSize=practicebuttonTextSize,
                                        labelType=Enums.LABEL_TYPE.TEXT(),
                                        font="calibri",
                                        labelColor=(0,0,0))
        
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

        # 2024-2025 Year
        match (Enums.eventDict[self.problemType]):
            case "history":
                problemList = HistoryProblems.problemList
                titleText = "History Practice"
                 
        self.problemsDone = 0
        self.problemsDoneTracker = []

        # Stylistic Stuff
        self.colors = {"darkBlue": (53, 63, 112), "screenGrey": (230,230,230), "lightBlue":(38, 176, 237)}

        self.titleTextSize = 50     
        self.title = Elements.Text(screen=self.screen,
                                   positionController=Controllers.PositionController(objectLength=1100,
                                                                                     objectHeight=200,
                                                                                     drawAnchor=Enums.ANCHOR.TOP_CENTER(),
                                                                                     xOffset=0, 
                                                                                     yOffset=10, 
                                                                                     refAnchor=Enums.ANCHOR.TOP_CENTER()),
                                   string=titleText,
                                   font="calibri",
                                   fontSize=self.titleTextSize,
                                   alignment=Enums.TEXT_ALIGNMENT.CENTER(),
                                   showingTextBox=False)    
        self.elements.append(self.title)   

        self.problemNumberBox = Elements.ProblemNumberBox(screen=self.screen, 
                                                          positionController=Controllers.PositionController(objectLength=60,
                                                                                             objectHeight=60,
                                                                                             drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                             xOffset=30, 
                                                                                             yOffset=95, 
                                                                                             refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                                          problemNumber=str(self.problemsDone+1))
        self.elements.append(self.problemNumberBox)
        
        # Creates Problem Controller
        self.problemController = Controllers.ProblemController(screen=screen,
                                                               problemList=problemList)

        self.loadProblem()

    def loadProblem(self):

        self.elements = []
        self.interactive = []

        self.elements.append(self.title)
        self.elements.append(self.problemNumberBox)

        self.problemController.createProblem()

        for element in self.problemController.elements:
            self.elements.append(element)

        for element in self.problemController.interactive:
            self.interactive.append(element)

    def processEvent(self, event):
        if (Enums.eventDict[event] == "answerInputted"):
            self.problemController.answerInputted()
        elif (Enums.eventDict[event] == "newProblem"):
            self.loadProblem()
            self.problemController.newProblem()
            self.problemsDone += 1
            self.problemNumberBox.changeNumber(str(self.problemsDone+1))
        pass    

    def processInputText(self, event):
        self.problemController.problem.inputController.updateTextBoxesText(event)

    def recenter(self):
        super().recenter()
        self.problemController.recenter()

    def getType(self):
        return self.problemType
import pygame
import os

import Enums
import Controllers

#
# The following classes are used to draw/create specifics things to display or for users to interact with
#

# An object that displays text on the screen
class Text:

    def __init__(self, screen = None, positionController=None, string=None, lineSpacing = 1, leftMargin = 20, rightMargin = 20, topMargin = 20, alignment = Enums.TextAlignment.Left, fontSize = 12, color = (0,0,0), font = "calibri", showingTextBox = False):
        
        self.screen = screen

        self.positionController = positionController

        self.string = string

        self.lineSpacing = lineSpacing
        self.leftMargin = leftMargin
        self.rightMargin = rightMargin
        self.topMargin = topMargin
        self.alignment = alignment

        self.maxLength = positionController.getSize()[0] - self.leftMargin - self.rightMargin

        self.fontSize = fontSize
        self.color = color
        self.font = font

        self.showingTextBox = showingTextBox

        self.loadFont(self.font, self.fontSize)

        self.text = []

        self.processText()

        self.outsideTextBoxRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0]-2.5, 
                                              self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1]-2.5, 
                                              self.positionController.getSize()[0]+5,
                                              self.positionController.getSize()[1]+5)

        self.insideTextBoxRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                             self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                             self.positionController.getSize()[0],
                                             self.positionController.getSize()[1])

    def loadFont(self, font, fontSize):
        if (font.endswith("ttf")):
            self.loadedFont = pygame.font.Font(font, fontSize)
            return pygame.font.Font(font, fontSize)
        else:
            self.loadedFont = pygame.font.SysFont(font, fontSize)
            return pygame.font.SysFont(font, fontSize)

    def findLengthOfTextRect(self, string):

        text = self.loadedFont.render(string, True, (0,0,0))
        textRect = text.get_rect()

        return textRect.size[0]

    def processText(self):
        
        wordList = self.string.split(" ")

        line = "" 
        for i in range(len(wordList)):
            if (self.findLengthOfTextRect(line + wordList[i]) > self.maxLength):
                self.text.append(line)
                line = ""
            line += wordList[i] + " "

        self.text.append(line)
        
    def draw(self):

        if (self.showingTextBox):
            pygame.draw.rect(self.screen, colors["black"], self.outsideTextBoxRect, 0)
            pygame.draw.rect(self.screen, colors["screenGrey"], self.insideTextBoxRect, 0)

        for i in range(len(self.text)):
            textLine = self.loadedFont.render(self.text[i], True, self.color)
            textLineRect = textLine.get_rect()
            if (type(self.alignment) == Enums.TextAlignment.Left):
                textLineRect.topleft = (self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0] + self.leftMargin, 
                                        self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1] + self.topMargin + textLineRect.height * i * self.lineSpacing)
            elif (type(self.alignment) == Enums.TextAlignment.Center):
                textLineRect.midtop = (self.positionController.getPosition(positionOnObject=Enums.Anchor.TopCenter())[0], 
                                       self.positionController.getPosition(positionOnObject=Enums.Anchor.TopCenter())[1] + self.topMargin + textLineRect.height * i * self.lineSpacing)
            self.screen.blit(textLine, textLineRect)
    
    def recenter(self):
        self.positionController.recenter()
        
# An interacitve object which returns a event when clicked  
class Button:

    positionController: Controllers.PositionController

    def __init__(self, screen=None, event=None, sizeX=100, sizeY=100, positionController=None, thickness=0, curveRadius=0, labelType=Enums.Label.Text(), labelInformation=None, labelSize=10, isWorking=True, **kwargs):

        # Inputed variables stored in the object
        self.screen = screen
        self.color = [Enums.colors["highlightMCQGrey"], Enums.colors["screenGrey"], Enums.colors["highlightBlue"]] # TODO: Fix button color stuff
        self.colorState = 1
        self.curveRadius = curveRadius
        self.thickness = thickness
        self.string = labelInformation
        self.labelSize = labelSize
        self.labelType = labelType
        self.event = event
        self.isWorking = isWorking

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.positionController = positionController

        #Button Creation
        self.ButtonRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], self.sizeX, self.sizeY)

        self.labels = []
        if (type(self.labelType) == Enums.Label.Text):
            self.label = Label(screen=self.screen, 
                                        size=labelSize, 
                                        labelType=labelType, 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.Center(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        labelInformation=labelInformation,
                                        font = kwargs.get("font"),
                                        color = kwargs.get("labelColor"))
        elif (type(self.labelType) == Enums.Label.Image):
            self.label = Label(screen=screen, 
                                        size=labelSize, 
                                        labelType=labelType, 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.Center(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        labelInformation=labelInformation)
        self.labels.append(self.label)
        if (not isWorking):
            pass # TODO: Add some kind of visual thing for not working stuff

    #Draws everything
    def draw(self):
        pygame.draw.rect(self.screen, self.color[self.colorState], self.ButtonRect, 0, self.curveRadius)
        for label in self.labels:
            label.draw()

    #Runs/check if clicked
    def clicked(self, mousePos):
        if (self.ButtonRect.collidepoint(mousePos)):
            if (self.isWorking):
                CUSTOMEVENT = pygame.event.Event(self.event)
                pygame.event.post(CUSTOMEVENT)
            return True
        else:
            return False
        
    def mouseOver(self, mousePos):
        isMouseOver = self.ButtonRect.collidepoint(mousePos)
        if (isMouseOver):
            self.colorState = 0
            return True
        else:
            self.colorState = 1
            return False

    def recenter(self):
        self.positionController.recenter()
        self.ButtonRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], self.sizeX, self.sizeY)
        for label in self.labels:
            label.recenter()
     
    def getPosition(self):
        return self.positionController

    def getSize(self):
        return self.sizeX, self.sizeY
    
    def changeColor(self, color):
        self.color = color

    def changeLabel(self, change, otherInformation):
        if (change == "text"):
            self.label.changeText(otherInformation)
        if (change == "image"):
            self.label.changeImage(otherInformation)

# A button subclass that handles multiple choice buttons
class MCQButton(Button):
        
    def __init__(self, screen=None, event=None, sizeX=100, sizeY=100, positionController=None, labelType=Enums.Label.Text(), labelInformation=None, labelSize=10, isWorking=True, **kwargs):

        super().__init__(screen=screen, event=event, sizeX=sizeX, sizeY=sizeY, positionController=positionController, labelType=labelType, labelInformation=labelInformation, labelSize=labelSize, isWorking=isWorking, **kwargs )

        self.selected = False

        self.label.positionController.changeRefAnchor(Enums.Anchor.LeftCenter())
        self.label.positionController.changeDrawAnchor(Enums.Anchor.LeftCenter())
        self.label.positionController.changeOffset(newXOffset=20)

    def clicked(self, mousePos):
        if (self.ButtonRect.collidepoint(mousePos)):
            if (self.isWorking):
                CUSTOMEVENT = pygame.event.Event(self.event)
                pygame.event.post(CUSTOMEVENT)
            return True
        else:
            return False

    def draw(self):
        if (self.selected):
            self.colorState = 2
        pygame.draw.rect(self.screen, self.color[self.colorState], self.ButtonRect, 0, 0)

        self.label.draw()

    def isSelected(self):
        return self.selected

    def getNumber(self):
        return self.number

    def changeSelectedState(self, state):
        self.selected = state

    def getValue(self):
        return self.string

# An object which can stick visuals on things like buttons
class Label:

    #Initializing function for labels of text and images 
    def __init__(self, screen=None, positionController = None, size=10, labelType=None, labelInformation = None, **kwargs):

        self.screen = screen
        self.positionController = positionController
        self.type = labelType
        self.labelSize = size

        self.labelInfromation = labelInformation
        
        if (type(self.type) == Enums.Label.Text):
            self.font = kwargs.get("font")
            self.color = kwargs.get("color")

            # TODO: Turn this into a text element
            if (self.font.endswith("ttf")):
                self.loadedFont = pygame.font.Font(self.font, self.labelSize)
            else:
                self.loadedFont = pygame.font.SysFont(self.font, self.labelSize)

            self.text = self.loadedFont.render(self.labelInfromation, True, self.color)
            self.labelRect = self.text.get_rect()

            self.positionController.changeSize(newLength=self.labelRect.width, newHeight=self.labelRect.height) # TODO: change all lengths to widths

        elif (type(self.type) == Enums.Label.Image):

            current_dir = os.path.dirname(__file__)
            current_dir = os.path.dirname(current_dir)
            image_dir = os.path.join(current_dir, 'Images')

            self.image = pygame.image.load(os.path.join(image_dir,self.labelInfromation))
            self.image = pygame.transform.scale_by(self.image, self.labelSize)
            self.labelRect = self.image.get_rect()
    
    def draw(self):
        self.labelRect.center = (self.positionController.getPosition(positionOnObject=Enums.Anchor.Center())[0], 
                                 self.positionController.getPosition(positionOnObject=Enums.Anchor.Center())[1])
        if (type(self.type) == Enums.Label.Text):
            self.screen.blit(self.text, self.labelRect)
        elif (type(self.type) == Enums.Label.Image):
            self.screen.blit(self.image, self.labelRect)
            
    def changeText(self, text):
        self.text = self.loadedFont.render(text, True, self.color)
    
    def changeImage(self, imagePath):
        self.string = imagePath

    def getRect(self):
        return self.labelRect

    def changeColor(self, color):
        self.color = color

    def recenter(self):
        self.positionController.recenter()

# An interactive object that takes in keyboard input and returns it
class InputTextBox:

    def __init__(self, screen=None, length=200, height=50, positionController=None, defaultText="Input", labelText = None):

        self.screen = screen
        self.isActive = False
        self.submitted = False
        self.isCorrect = False

        self.length = length
        self.height = height
        self.positionController = positionController

        self.defaultText = defaultText
        self.labelText = labelText

        self.inputtedText = ""

        textMargin = 15
        labelAndBoxSpacing = 10

        if (self.labelText == None):
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.defaultLabel = Label(screen=self.screen, 
                                        size=20, 
                                        labelType=Enums.Label.Text(), 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=textMargin,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.LeftCenter(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.Anchor.LeftCenter()), 
                                        labelInformation=self.defaultText,
                                        font='calibri',
                                        color=(200,200,200))
            self.defaultLabel.recenter()
        else:
            self.externalLabel = Label(screen=self.screen, 
                                        size=20, 
                                        labelType=Enums.Label.Text(), 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.LeftCenter(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.Anchor.LeftCenter()), 
                                        labelInformation=self.labelText,
                                        font='calibri',
                                        color=(0,0,0))
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.defaultLabel = Label(screen=self.screen, 
                                        size=20, 
                                        labelType=Enums.Label.Text(), 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=textMargin+labelAndBoxSpacing+self.externalLabel.getRect().width,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.LeftCenter(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.Anchor.LeftCenter()), 
                                        labelInformation=self.defaultText,
                                        font='calibri',
                                        color=(200,200,200))

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.insideRect, 0, 3)

        if (self.submitted):
            if (self.isCorrect):
                pygame.draw.rect(self.screen, (140,250,150), self.correctRect, 0, 3)
                self.defaultLabel.changeColor((50, 150, 60))
            else:
                pygame.draw.rect(self.screen, (250,145,145), self.correctRect, 0, 3)
                self.defaultLabel.changeColor((170, 20, 20))

        pygame.draw.rect(self.screen, (100,100,100), self.outsideRect, 3, 3)

        if (self.isActive):
            pygame.draw.rect(self.screen, (55, 190, 245), self.activeRect, 3, 3)
        
        if (self.labelText != None):
            self.externalLabel.draw()

        if (len(self.inputtedText) > 0):
            self.defaultLabel.changeText(self.inputtedText)
            self.defaultLabel.changeColor((0,0,0))
        else:
            if (len(self.inputtedText) == 0):
                self.defaultLabel.changeText(self.defaultText)
                self.defaultLabel.changeColor((200,200,200))
            else: 
                self.defaultLabel.changeText("")

        self.defaultLabel.draw()
        pass

    def clicked(self, mousePos):
        if (self.activeRect.collidepoint(mousePos)):
            self.isActive = True
            return True
        else:
            self.isActive = False
            return False

    def mouseOver(self, mousePos):
        pass

    def inputText(self, event):
        if event.key == pygame.K_RETURN:
            self.isActive = False
            pass
        elif event.key == pygame.K_BACKSPACE:
            if (len(self.inputtedText) == 1):
                self.inputtedText = ""
            else:
                self.inputtedText = self.inputtedText[:-1]
        else:
            self.inputtedText += event.unicode  
            self.defaultLabel.changeText(self.inputtedText)
            if (self.defaultLabel.text.get_rect().width > self.length - 30):
                self.inputtedText = self.inputtedText[:-1]
                self.defaultLabel.changeText(self.inputtedText)

    def recenter(self):
        if (self.labelText == None):
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)        
            self.defaultLabel.recenter()
        else: 
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width, 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width, 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width, 
                                          self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[0] + self.externalLabel.getRect().width, 
                                           self.positionController.getPosition(positionOnObject = Enums.Anchor.TopLeft())[1], 
                                           self.length, 
                                           self.height)
            self.defaultLabel.recenter()
            self.externalLabel.recenter()

    def submit(self, isCorrect):
        self.submitted = True
        self.isCorrect = isCorrect

    def getLength(self):
        if (self.labelText == None):
            return self.insideRect.width
        else:
            return self.externalLabel.getRect().width + self.insideRect.width 

# An object that displays the problem number
class ProblemNumberBox:

    def __init__(self, screen=None, positionController=None, length=60, height=60, problemNumber=None):
        
        self.screen = screen

        self.positionController = positionController

        self.length = length
        self.height = height

        self.color = (0,0,0)

        self.problemNumber = problemNumber

        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)

        self.label = Label(screen=self.screen, 
                                    size=30, 
                                    labelType=Enums.Label.Text(), 
                                    positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                      objectHeight=self.positionController.getSize()[1],
                                                                                      xOffset=0,
                                                                                      yOffset=0,
                                                                                      drawAnchor=Enums.Anchor.Center(),
                                                                                      refObject=self.positionController,
                                                                                      refAnchor=Enums.Anchor.Center()), 
                                    labelInformation=self.problemNumber,
                                    font = 'calibri',
                                    color = self.color)        

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.boxOutlineRect, 0, 3)
        pygame.draw.rect(self.screen, (0,0,0), self.boxOutlineRect, 4, 3)
        self.label.draw()

    def changeNumber(self, number):

        self.label.changeText(number)

    def recenter(self):
        self.positionController.recenter()
        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1], 
                                          self.length, 
                                          self.height)
        self.label.recenter()

# An object that darkens everything underneath it
# DEPRECATED
class ScreenShader:

    def __init__(self, screen, center_X, center_Y, event, popUpRect):

        self.screen = screen

        self.surface = pygame.Surface((2*center_X,2*center_Y), pygame.SRCALPHA)

        self.rect = pygame.Rect(0,0,2*center_X,2*center_Y)
        
        self.event = event

        self.popUpRect = popUpRect

    def draw(self):

        self.screen.blit(self.surface, (0,0))
        pygame.draw.rect(self.surface, (0,0,0,50), self.rect, 0, 0)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.surface = pygame.Surface((2*center_X,2*center_Y), pygame.SRCALPHA)
        self.rect = pygame.Rect(0,0,2*center_X,2*center_Y)

    def clicked(self, mousePos):
        if (self.rect.collidepoint(mousePos) and not self.popUpRect.collidepoint(mousePos)):
            CUSTOMEVENT = pygame.event.Event(self.event)
            pygame.event.post(CUSTOMEVENT)
            return True
        else:
            return False

# An object that displays an image
# DEPRECATED
class Image:

    def __init__(self, screen, center_X, center_Y, X, Y, imageName, scale, thickness, colors):

        self.screen = screen

        self.center_X = center_X
        self.center_Y = center_Y

        self.X = X
        self. Y = Y

        self.imageName = imageName

        self.scale = scale
        
        self.thickness = thickness
        self.colors = colors

        self.XOp = Expressions.locationExpressionValue(self.X, center_X, center_Y)
        self.YOp = Expressions.locationExpressionValue(self.Y, center_X, center_Y)

        current_dir = os.path.dirname(__file__)
        current_dir = os.path.dirname(current_dir)
        image_dir = os.path.join(current_dir, 'Images')

        self.image = pygame.image.load(os.path.join(image_dir, self.imageName))
        self.image = pygame.transform.scale_by(self.image, self.scale)
        self.imageRect = self.image.get_rect()
        self.imageRect.center = (self.XOp, self.YOp)

        self.borderRect = None
        if (self.thickness > 0):
            self.borderRect = pygame.Rect(self.XOp+self.imageRect[0]/2, self.YOp+self.imageRect[1]/2, self.imageRect[0]/2, self.imageRect[1]/2)
            self.border = True
        else:
            self.border = False

    def draw(self):
        
        self.imageRect = self.image.get_rect()
        self.imageRect.center = (self.XOp, self.YOp)

        self.screen.blit(self.image, self.imageRect)

        if (self.border):
            pygame.draw.rect(self.screen, self.colors["darkBlue"], self.borderRect, self.thickness, 0)

    def recenter(self, center_X, center_Y):

        self.center_X = center_X
        self.center_Y = center_Y

        self.XOp = Expressions.locationExpressionValue(self.X, center_X, center_Y)
        self.YOp = Expressions.locationExpressionValue(self.Y, center_X, center_Y)

        current_dir = os.path.dirname(__file__)
        current_dir = os.path.dirname(current_dir)
        image_dir = os.path.join(current_dir, 'Images')

        self.image = pygame.image.load(os.path.join(image_dir, self.imageName))
        self.image = pygame.transform.scale_by(self.image, self.scale)
        self.imageRect = self.image.get_rect()
        self.imageRect.center = (self.XOp, self.YOp)

        self.borderRect = pygame.Rect(self.XOp+self.imageRect[0]/2, self.YOp+self.imageRect[1]/2, self.imageRect[0]/2, self.imageRect[1]/2)

# An object that holds and compares answers
class Answer:

    def __init__(self, answer, secondAnswer=None, thirdAnswer=None, fourthAnswer=None):
        self.answer = answer
        self.secondAnswer = secondAnswer
        self.thirdAnswer = thirdAnswer
        self.fourthAnswer = fourthAnswer

    def __eq__(self, other):
        if (self.answer == other.answer and 
            self.secondAnswer == other.secondAnswer and
            self.thirdAnswer == other.thirdAnswer and
            self.fourthAnswer == other.fourthAnswer):
            return True
        else:
            return False
        
# An object that loads, displays, and processes problems
class Problem: 

    def __init__(self, 
                 question = None, 
                 answer = None, 
                 problemDisplayType=Enums.ProblemDisplayType.Text(), 
                 problemInputType=Enums.ProblemInputType.MCQ()):

        self.elements = []
        self.interactive = []
        self.interactiveText = []

        self.question = question
        self.answer = answer

        self.problemDisplayType = problemDisplayType
        self.problemInputType = problemInputType
        
        self.inputController = None

        self.displayAndInputBorderY = 100

    def loadQuestion(self):
        pass

    def loadDisplay(self, screen):
        if (type(self.problemDisplayType) == Enums.ProblemDisplayType.Text):
            self.problemText = Text(screen=screen,
                                    positionController=Controllers.PositionController(objectLength=1100,
                                                                                      objectHeight=200,
                                                                                      drawAnchor=Enums.Anchor.TopLeft(),
                                                                                      xOffset=30, 
                                                                                      yOffset=95, 
                                                                                      refAnchor=Enums.Anchor.TopLeft()),
                                    string="          "+self.question,
                                    font="calibri",
                                    fontSize=35,
                                    leftMargin=0,
                                    topMargin=12,
                                    alignment=Enums.TextAlignment.Left(),
                                    showingTextBox=False)
            self.elements.append(self.problemText)
    
    def loadInput(self, screen):
        if (type(self.problemInputType) == Enums.ProblemInputType.MCQ):
            self.inputController = Controllers.MCQController(screen=screen, 
                                                             numMCQs=self.problemInputType.getNumMCQs(),
                                                             labelList=self.problemInputType.getAnswerChoices(),
                                                             maxSelectable=1)
        elif (type(self.problemInputType) == Enums.ProblemInputType.TextBox):
            self.inputController = Controllers.TextBoxController(screen=screen, 
                                                                 numTextBoxes=self.problemInputType.getNumTextBoxes())
        self.elements.append(self.inputController)
        self.interactive.append(self.inputController)
    
    def checkCorrect(self):
        input = self.inputController.getInput()

        if (len(input) == 0):
            return False
        elif (type(self.answer) == list):
            if (len(self.answer) != len(input())):
                raise ValueError("Answer and Input Mismatch")
            else:
                isCorrect = True
                self.answer = [str(x) for x in self.answer]
                self.answer.sort()
                self.inputController.sort()
                for i in range(len(self.answer)):
                    if self.answer[i] != input()[i]:
                        isCorrect = False
                        break
                return isCorrect
        else:    
            if (len(input) > 1):
                raise ValueError("Answer and Input Mismatch")
            else:
                return (self.answer == input[0])
        
    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer
import pygame
import os

import Enums
import Controllers

#
# The following classes are used to draw/create specifics things to display or for users to interact with
#

# An object that displays text on the screen
class Text:

    def __init__(self, 
                 screen = None, 
                 positionController=None, 
                 string=None, 
                 lineSpacing = 1, 
                 leftMargin = 20, 
                 rightMargin = 20, 
                 topMargin = 20, 
                 alignment = Enums.TEXT_ALIGNMENT.LEFT, 
                 fontSize = 12, 
                 color = (0,0,0), 
                 font = "calibri", 
                 showingTextBox = False):
        
        self.screen = screen

        self.positionController = positionController
        self.positionController.drawObject = self

        self.string = string

        self.lineSpacing = lineSpacing
        self.leftMargin = leftMargin
        self.rightMargin = rightMargin
        self.topMargin = topMargin
        self.alignment = alignment

        self.fontSize = fontSize
        self.color = color
        self.font = font

        self.showingTextBox = showingTextBox

        self.loadFont(self.font, self.fontSize)

        self.text = []

        self.processText()

        self.outsideTextBoxRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0]-2.5, 
                                              self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1]-2.5, 
                                              self.positionController.getSize()[0]+5,
                                              self.positionController.getSize()[1]+5)

        self.insideTextBoxRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                             self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                             self.positionController.getSize()[0],
                                             self.positionController.getSize()[1])

    def loadFont(self, font, fontSize):
        if (font.endswith("ttf")):
            self.loadedFont = pygame.font.Font(font, fontSize)
        else:
            self.loadedFont = pygame.font.SysFont(font, fontSize)
        return self.loadedFont

    @staticmethod
    def findSizeOfTextRect(font, fontSize, string):

        if (type(font) == str):
            if (font.endswith("ttf")):
                loadedFont = pygame.font.Font(font, fontSize)
            else:
                loadedFont = pygame.font.SysFont(font, fontSize)
        elif (type(font) == pygame.font.Font):
            loadedFont = font

        text = loadedFont.render(string, True, (0,0,0))
        textRect = text.get_rect()

        return textRect.size

    def findHeight(self):
        height = self.topMargin
        for i in range(len(self.text)):
            textLine = self.loadedFont.render(self.text[i], True, self.color)
            textLineRect = textLine.get_rect()
            height += textLineRect.height * self.lineSpacing  
        return height

    def processText(self):
        
        self.text = []

        self.maxLength = self.positionController.getSize()[0] - self.leftMargin - self.rightMargin

        wordList = self.string.split(" ")

        line = "" 
        for i in range(len(wordList)):
            if (self.findSizeOfTextRect(font=self.loadedFont, fontSize=self.fontSize, string=(line + wordList[i]))[0] > self.maxLength):
                self.text.append(line)
                line = ""
            line += wordList[i] + " "

        self.text.append(line)
        
    def draw(self):

        if (self.showingTextBox):
            pygame.draw.rect(self.screen, Enums.colors["black"], self.outsideTextBoxRect, 0)
            pygame.draw.rect(self.screen, Enums.colors["screenGrey"], self.insideTextBoxRect, 0)

        for i in range(len(self.text)):
            textLine = self.loadedFont.render(self.text[i], True, self.color)
            textLineRect = textLine.get_rect()
            if (type(self.alignment) == Enums.TEXT_ALIGNMENT.LEFT):
                textLineRect.topleft = (self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[0] + self.leftMargin, 
                                        self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[1] + self.topMargin + textLineRect.height * i * self.lineSpacing)
            elif (type(self.alignment) == Enums.TEXT_ALIGNMENT.CENTER):
                textLineRect.midtop = (self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_CENTER())[0], 
                                       self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_CENTER())[1] + self.topMargin + textLineRect.height * i * self.lineSpacing)
            self.screen.blit(textLine, textLineRect)
    
    def recenter(self):
        self.positionController.recenter()
        
        self.processText()
        
# An interacitve object which returns a event when clicked  
class Button:

    def __init__(self, 
                 screen=None, 
                 event=None, 
                 length=100, 
                 height=100, 
                 positionController=None, 
                 thickness=0, 
                 curveRadius=0, 
                 labelType=Enums.LABEL_TYPE.TEXT(), 
                 labelInformation=None, 
                 labelSize=10, 
                 isWorking=True, 
                 locked=False, 
                 isActive=True, 
                 **kwargs):

        # Inputed variables stored in the object
        self.screen = screen
        self.color = [Enums.colors["highlightMCQGrey"], Enums.colors["screenGrey"], Enums.colors["highlightBlue"], Enums.colors["rightGreen"], Enums.colors["wrongRed"]] # TODO: Fix button color stuff
        self.colorState = 1
        self.curveRadius = curveRadius
        self.thickness = thickness
        self.string = labelInformation
        self.labelSize = labelSize
        self.labelType = labelType
        self.event = event

        self.locked = locked
        self.isWorking = isWorking
        self.isActive = isActive

        self.length = length
        self.height = height
        self.positionController = positionController
        self.positionController.drawObject = self # TODO: Get rid of all the size parameters for buttons

        #Button Creation
        self.ButtonRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], self.length, self.height)

        self.labels = []
        if (type(self.labelType) == Enums.LABEL_TYPE.TEXT):
            self.label = Label(screen=self.screen, 
                                        size=labelSize, 
                                        labelType=labelType, 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.ANCHOR.CENTER()), 
                                        labelInformation=labelInformation,
                                        font = kwargs.get("font"),
                                        color = kwargs.get("labelColor"))
        elif (type(self.labelType) == Enums.LABEL_TYPE.IMAGE):
            self.label = Label(screen=screen, 
                                        size=labelSize, 
                                        labelType=labelType, 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.ANCHOR.CENTER(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.ANCHOR.CENTER()), 
                                        labelInformation=labelInformation)
        self.labels.append(self.label)
        if (not isWorking):
            pass # TODO: Add some kind of visual thing for not working stuff

    #Draws everything
    def draw(self):
        if (self.isActive):
            pygame.draw.rect(self.screen, self.color[self.colorState], self.ButtonRect, 0, self.curveRadius)
            for label in self.labels:
                label.draw()

    #Runs/check if clicked
    def clicked(self, mousePos):
        if (self.isActive and self.isWorking and not self.locked):
            if (self.ButtonRect.collidepoint(mousePos)):
                CUSTOMEVENT = pygame.event.Event(self.event)
                pygame.event.post(CUSTOMEVENT)
                return True
            else:
                return False
        
    def mouseOver(self, mousePos):
        if (self.isActive and self.isWorking and not self.locked):
            isMouseOver = self.ButtonRect.collidepoint(mousePos)
            if (isMouseOver):
                self.colorState = 0
                return True
            else:
                self.colorState = 1
                return False

    def recenter(self):
        self.positionController.recenter()
        self.ButtonRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], self.length, self.height)
        for label in self.labels:
            label.recenter()
     
    def getPosition(self):
        return self.positionController

    def getSize(self):
        return self.length, self.height
    
    def changeColor(self, colorState):
        self.colorState = colorState

    def changeLabel(self, change, otherInformation):
        if (change == "text"):
            self.label.changeText(otherInformation)
        if (change == "image"):
            self.label.changeImage(otherInformation)

    def setLockState(self, lockState):
        self.locked = lockState

    def setActiveState(self, activeState):
        self.isActive = activeState

# A button subclass that handles multiple choice buttons
class MCQButton(Button):
        
    def __init__(self, 
                 screen=None, 
                 event=None, 
                 length=100, 
                 height=100, 
                 positionController=None, 
                 labelType=Enums.LABEL_TYPE.TEXT(), 
                 labelInformation=None, 
                 labelSize=10, 
                 isWorking=True, 
                 locked=False, 
                 isActive=True,
                 **kwargs):

        super().__init__(screen=screen, 
                         event=event, 
                         length=length, 
                         height=height, 
                         positionController=positionController, 
                         labelType=labelType, 
                         labelInformation=labelInformation, 
                         labelSize=labelSize, 
                         isWorking=isWorking, 
                         locked=locked, 
                         isActive=isActive,
                         **kwargs)

        self.selected = False

        self.label.positionController.changeRefAnchor(Enums.ANCHOR.LEFT_CENTER())
        self.label.positionController.changeDrawAnchor(Enums.ANCHOR.LEFT_CENTER())
        self.label.positionController.changeOffset(newXOffset=20)

    def draw(self):
        if (self.selected and (not self.locked or not self.isWorking)):
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
    def __init__(self, 
                 screen=None, 
                 positionController=None, 
                 size=10, 
                 labelType=None, 
                 labelInformation=None, 
                 labelDrawAnchor=Enums.ANCHOR.CENTER(),
                 **kwargs):

        self.screen = screen
        self.positionController = positionController
        self.type = labelType
        self.labelSize = size
        self.labelInfromation = labelInformation
        self.labelDrawAnchor = labelDrawAnchor
        
        if (type(self.type) == Enums.LABEL_TYPE.TEXT):
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

        elif (type(self.type) == Enums.LABEL_TYPE.IMAGE):

            current_dir = os.path.dirname(__file__)
            current_dir = os.path.dirname(current_dir)
            image_dir = os.path.join(current_dir, 'Images')

            self.image = pygame.image.load(os.path.join(image_dir,self.labelInfromation))
            self.image = pygame.transform.scale_by(self.image, self.labelSize)
            self.labelRect = self.image.get_rect()
    
    def draw(self):
        refPosition = (self.positionController.getPosition(positionOnObject=self.labelDrawAnchor)[0], 
                       self.positionController.getPosition(positionOnObject=self.labelDrawAnchor)[1]) 
        
        if (type(self.labelDrawAnchor) == Enums.ANCHOR.CENTER):
            self.labelRect.center = refPosition
        elif (type(self.labelDrawAnchor) == Enums.ANCHOR.TOP_LEFT):
            self.labelRect.topleft = refPosition
        elif (type(self.labelDrawAnchor) == Enums.ANCHOR.LEFT_CENTER):
            self.labelRect.midleft = refPosition    
            
        if (type(self.type) == Enums.LABEL_TYPE.TEXT):
            self.screen.blit(self.text, self.labelRect)
        elif (type(self.type) == Enums.LABEL_TYPE.IMAGE):
            self.screen.blit(self.image, self.labelRect)
            
    def changeText(self, text):
        self.text = self.loadedFont.render(text, True, self.color)
        self.labelRect = self.text.get_rect()
    
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

    def __init__(self, screen=None, length=200, height=50, positionController=None, defaultText="Input", labelText=None, isLocked=False):

        self.screen = screen
        self.isActive = False
        self.submitted = False
        self.isCorrect = False
        self.isLocked = isLocked

        self.length = length
        self.height = height
        self.positionController = positionController

        self.defaultText = defaultText
        self.labelText = labelText

        self.inputtedText = ""

        textMargin = 15
        labelAndBoxSpacing = 10

        if (self.labelText == None):
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.defaultLabel = Label(screen=self.screen, 
                                      size=20, 
                                      labelType=Enums.LABEL_TYPE.TEXT(), 
                                      positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                        objectHeight=self.positionController.getSize()[1],
                                                                                        xOffset=textMargin,
                                                                                        yOffset=0,
                                                                                        drawAnchor=Enums.ANCHOR.LEFT_CENTER(),
                                                                                        refObject=self.positionController,
                                                                                        refAnchor=Enums.ANCHOR.LEFT_CENTER()), 
                                      labelInformation=self.defaultText,
                                      font='calibri',
                                      color=(200,200,200),
                                      labelDrawAnchor=Enums.ANCHOR.LEFT_CENTER())
            self.defaultLabel.recenter()
        else:
            self.externalLabel = Label(screen=self.screen, 
                                        size=20, 
                                        labelType=Enums.LABEL_TYPE.TEXT(), 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.ANCHOR.LEFT_CENTER(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.ANCHOR.LEFT_CENTER()), 
                                        labelInformation=self.labelText,
                                        font='calibri',
                                        color=(0,0,0))
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width + labelAndBoxSpacing, 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.defaultLabel = Label(screen=self.screen, 
                                        size=20, 
                                        labelType=Enums.LABEL_TYPE.TEXT(), 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=textMargin+labelAndBoxSpacing+self.externalLabel.getRect().width,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.ANCHOR.LEFT_CENTER(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.ANCHOR.LEFT_CENTER()), 
                                        labelInformation=self.defaultText,
                                        font='calibri',
                                        color=(200,200,200),
                                        labelDrawAnchor=Enums.ANCHOR.LEFT_CENTER())

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.insideRect, 0, 3)

        if (self.submitted):
            if (self.isCorrect):
                pygame.draw.rect(self.screen, (140,250,150), self.correctRect, 0, 3)
                self.defaultLabel.changeColor((50, 150, 60))
            else:
                pygame.draw.rect(self.screen, (250,145,145), self.correctRect, 0, 3)
                self.defaultLabel.changeColor((170, 20, 20))

        #pygame.draw.rect(self.screen, (100,100,100), self.outsideRect, 3, 3)
        pygame.draw.rect(self.screen, (0,0,0), self.outsideRect, 3, 3)

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
        if (not self.isLocked):
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
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0], 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)        
            self.defaultLabel.recenter()
        else: 
            self.insideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width, 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.outsideRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width, 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.activeRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width, 
                                          self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
            self.correctRect = pygame.Rect(self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[0] + self.externalLabel.getRect().width, 
                                           self.positionController.getPosition(positionOnObject = Enums.ANCHOR.TOP_LEFT())[1], 
                                           self.length, 
                                           self.height)
            self.defaultLabel.recenter()
            self.externalLabel.recenter()

    def setSubmittedState(self, isCorrect):
        self.submitted = True
        self.isCorrect = isCorrect

    def setLockState(self, lockState):
        self.locked = lockState

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

        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)

        self.label = Label(screen=self.screen, 
                           size=30, 
                           labelType=Enums.LABEL_TYPE.TEXT(), 
                           positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                             objectHeight=self.positionController.getSize()[1],
                                                                             xOffset=0,
                                                                             yOffset=0,
                                                                             drawAnchor=Enums.ANCHOR.CENTER(),
                                                                             refObject=self.positionController,
                                                                             refAnchor=Enums.ANCHOR.CENTER()), 
                           labelInformation=self.problemNumber,
                           font='calibri',
                           color=self.color)        

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.boxOutlineRect, 0, 3)
        pygame.draw.rect(self.screen, (0,0,0), self.boxOutlineRect, 4, 3)
        self.label.draw()

    def changeNumber(self, number):
        self.label.changeText(str(number))

    def recenter(self):
        self.positionController.recenter()
        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[1], 
                                          self.length, 
                                          self.height)
        self.boxOutlineRect = pygame.Rect(self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[0], 
                                          self.positionController.getPosition(positionOnObject=Enums.ANCHOR.TOP_LEFT())[1], 
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
     
# An object that loads, displays, and processes problems
class Problem: 

    def __init__(self, 
                 question=None, 
                 answer=None, 
                 problemDisplayType=Enums.ProblemDisplayType.Text(), 
                 problemInputType=Enums.ProblemInputType.MCQ()):

        self.elements = []
        self.interactive = []

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
                                    positionController=Controllers.PositionController(objectLength=(lambda: pygame.display.get_window_size()[0]-120-30),
                                                                                      objectHeight=200,
                                                                                      drawAnchor=Enums.ANCHOR.TOP_LEFT(),
                                                                                      xOffset=120, 
                                                                                      yOffset=95, 
                                                                                      refAnchor=Enums.ANCHOR.TOP_LEFT()),
                                    string=self.question,
                                    font="calibri",
                                    fontSize=35,
                                    leftMargin=0,
                                    topMargin=12,
                                    alignment=Enums.TEXT_ALIGNMENT.LEFT(),
                                    showingTextBox=False)
            self.elements.append(self.problemText)
    
    def loadInput(self, screen):
        if (type(self.problemInputType) == Enums.ProblemInputType.MCQ):
            self.inputController = Controllers.MCQController(screen=screen, 
                                                             answer=self.answer,
                                                             numChoices=self.problemInputType.getNumChoices(),
                                                             labelList=self.problemInputType.getOtherAnswerChoices(),
                                                             maxSelectable=1)
        elif (type(self.problemInputType) == Enums.ProblemInputType.TextBox):
            self.inputController = Controllers.InputTextBoxController(screen=screen, 
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
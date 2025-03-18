import pygame
import Elements
import Expressions
import Enums
import Controllers

import os

#
# The following classes are used to draw/create specifics things to display or for users to interact with
#

colors = {"white":(255,255,255), "black":(0,0,0), "darkBlue":(53,63,112), "screenGrey":(230,230,230), "highlightMCQGrey": (210,210,210), "highlightBlue": (55, 190, 245, 0.5)}
# TODO: Add color class, fix all color stuff


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

        print(self.positionController.getSize())


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
        print(self.positionController.getSize())
        
# An interacitve object which returns a event when clicked  
class Button:

    positionController: Controllers.PositionController

    def __init__(self, screen=None, event=None, sizeX=100, sizeY=100, positionController=None, color="white", thickness=0, curveRadius=0, labelType="text", labelInformation=None, labelSize=10, isWorking=True, **kwargs):

        # Inputed variables stored in the object
        self.screen = screen
        self.color = [colors["highlightMCQGrey"], colors["screenGrey"], colors["highlightBlue"]] # TODO: Fix button color stuff
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
            self.label = Elements.Label(screen=self.screen, 
                                        size=labelSize, 
                                        labelType=labelType, 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.TopLeft(),
                                                                                          refObject=self.positionController,
                                                                                          refAnchor=Enums.Anchor.Center()), 
                                        labelInformation=labelInformation,
                                        font = kwargs.get("font"),
                                        color = kwargs.get("labelColor"))
        elif (type(self.labelType) == Enums.Label.Image):
            self.label = Elements.Label(screen=screen, 
                                        size=labelSize, 
                                        labelType=labelType, 
                                        positionController=Controllers.PositionController(objectLength=self.positionController.getSize()[0], 
                                                                                          objectHeight=self.positionController.getSize()[1],
                                                                                          xOffset=0,
                                                                                          yOffset=0,
                                                                                          drawAnchor=Enums.Anchor.TopLeft(),
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

    def __init__(self, screen=None, event=None, sizeX=100, sizeY=100, positionController=None, color="white", thickness=0, curveRadius=0, labelType="text", labelInformation=None, labelSize=10, isWorking=True, **kwargs):
        
        super().__init__(self, screen=None, event=None, sizeX=100, sizeY=100, positionController=None, color="white", thickness=0, curveRadius=0, labelType="text", labelInformation=None, labelSize=10, isWorking=True, **kwargs)

    def draw(self):
        if (self.selected):
            self.colorState = 2
        pygame.draw.rect(self.screen, self.color[self.colorState], self.ButtonRect, 0, 0)

        self.label.draw()

    def isSelected(self):
        return self.selected

    def getNumber(self):
        return self.number

    def deselect(self):
        self.selected = False

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

        elif (type(self.type) == Enums.Label.Image):

            current_dir = os.path.dirname(__file__)
            current_dir = os.path.dirname(current_dir)
            image_dir = os.path.join(current_dir, 'Images')

            self.image = pygame.image.load(os.path.join(image_dir,self.labelInfromation))
            self.image = pygame.transform.scale_by(self.image, self.labelSize)
            self.labelRect = self.image.get_rect()
    
    def draw(self):
        self.labelRect.center = (self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0], 
                                 self.positionController.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1])
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

    def __init__(self, screen, center_X, center_Y, X, Y, sizeX, sizeY, textInside):

        self.screen = screen
        self.isActive = False
        self.submitted = False
        self.isCorrect = False

        self.X = X
        self.Y = Y
        self.center_X = center_X
        self.center_Y = center_Y
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.textInside = textInside

        self.inputtedText = ""

        xOp = Expressions.locationExpressionValue(self.X, center_X, center_Y)
        yOp = Expressions.locationExpressionValue(self.Y, center_X, center_Y)
        self.insideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.outsideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.activeRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.correctRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)

        self.label = Elements.Label(screen, 20,"text",center_X+xOp, center_Y+yOp, self.textInside, (200,200,200), 'calibri')
        self.label.recenter(center_X+xOp-(self.sizeX/2-10-self.label.textRect.width/2), center_Y+yOp)

        pass

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.insideRect, 0, 3)

        if (self.submitted):
            if (self.isCorrect):
                pygame.draw.rect(self.screen, (140,250,150), self.correctRect, 0, 3)
                self.label.changeColor((50, 150, 60))
            else:
                pygame.draw.rect(self.screen, (250,145,145), self.correctRect, 0, 3)
                self.label.changeColor((170, 20, 20))

        pygame.draw.rect(self.screen, (100,100,100), self.outsideRect, 3, 3)

        if (self.isActive):
            pygame.draw.rect(self.screen, (55, 190, 245), self.activeRect, 3, 3)
        self.label.draw()

        if (len(self.inputtedText) > 0):
            self.label.changeText(self.inputtedText)
            self.label.changeColor((0,0,0))
        else:
            if (len(self.inputtedText) == 0):
                self.label.changeText(self.textInside)
                self.label.changeColor((200,200,200))
            else: 
                self.label.changeText("")
        pass

    def clicked(self, mousePos):
        if (self.activeRect.collidepoint(mousePos)):
            self.isActive = True
            return True
        else:
            self.isActive = False
            return False
        
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

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        xOp = Expressions.locationExpressionValue(self.X, center_X, center_Y)
        yOp = Expressions.locationExpressionValue(self.Y, center_X, center_Y)
        self.insideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.outsideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.activeRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.correctRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.label.recenter(center_X+xOp-(self.sizeX/2-10-self.label.textRect.width/2), center_Y+yOp)
        pass 

    def submit(self, isCorrect):
        self.submitted = True
        self.isCorrect = isCorrect
        pass

# An object that draws a line across the screen
class Divider:

    def __init__(self, screen, type, center_X, center_Y, cord, thickness, color):

        self.screen = screen
        
        self.type = type

        self.center_X= center_X
        self.center_Y = center_Y

        self.cord = cord

        self.color = color

        self.thickness = thickness

    def draw(self):
        cord = Expressions.locationExpressionValue(self.cord, self.center_X, self.center_Y)
        if (self.type == "horizontal"):
            pygame.draw.line(self.screen, self.color, (0,cord), (2*self.center_X,cord), self.thickness)
        elif (self.type == "vertical"):
            pygame.draw.line(self.screen, self.color, (cord,0), (cord,2*self.center_Y), self.thickness)

    def recenter(self, X, Y):
        self.center_X = X
        self.center_Y = Y

# An object that displays the problem number
# DEPRECATED
class ProblemNumberBox:

    def __init__(self, screen, X, Y, sizeX, sizeY, problemNumber, color):
        
        self.screen = screen
        self.submitted = False

        self.X = X
        self.Y = Y

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.color = color

        self.boxOutlineRect = pygame.Rect(X, Y, sizeX, sizeY)
        self.boxFillRect = pygame.Rect(X, Y, sizeX, sizeY)

        self.label = Elements.Label(screen, 30, "text", X+sizeX/2, Y+sizeY/2, problemNumber, color, 'calibri')

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.boxOutlineRect, 0, 0)
        pygame.draw.rect(self.screen, self.color, self.boxOutlineRect, 7, 0)
        self.label.draw()

    def changeNumber(self, number):

        self.label = Elements.Label(self.screen, 30, "text", self.X+self.sizeX/2, self.Y+self.sizeY/2, str(number), self.color, 'calibri')

    def recenter(self, center_X, center_Y):
        pass

# An object 
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

# An interactive object that can switch in between two states
# DEPRECATED
class Switch:

    def __init__(self, screen, X, Y, center_X, center_Y, size, state, text, locationOfText, colors, event, working):
        
        self.screen = screen

        self.center_X = center_X
        self.center_Y = center_Y

        self.X = X
        self.Y = Y

        self.size = size
        self.borderSize = int(size/10)
        self.fontSize = int(size*2/5)

        self.xOp = Expressions.locationExpressionValue(self.X, center_X, center_Y)
        self.yOp = Expressions.locationExpressionValue(self.Y, center_X, center_Y)

        self.state = state

        self.colors = colors

        self.working = working

        self.event = event

        self.backRect = pygame.Rect(self.xOp-self.size, self.yOp-self.size/2, 2*self.size, self.size)
        
        if (self.state):
            self.moveRect = pygame.Rect(self.xOp-self.size, self.yOp-self.size/2, self.size, self.size)
        else:
            self.moveRect = pygame.Rect(self.xOp, self.yOp-self.size/2, self.size, self.size)

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        self.textDrawer.add("OFF", str(self.X) + "-" + str(self.size/2) + "+" + "5", self.Y, self.fontSize, (100,100,100), "calibri")

        self.textDrawer.add("ON", str(self.X) + "+" + str(self.size/2-5), self.Y, self.fontSize, (240,240,240), "calibri")

        self.text = text
        self.locationOfText = locationOfText

        self.labelSize = int(1.5*self.fontSize)
        if (type(locationOfText) == str):
            if (locationOfText == "left"):
                self.textDrawer.add(self.text, str(self.X) + "-" + str(self.size-self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "calibri")/2-30), self.Y, self.labelSize, self.colors["darkBlue"], "calibri")
            elif (locationOfText == "right"):
                self.textDrawer.add(self.text, str(self.X) + "+" + str(self.size+self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "calibri")/2+30), self.Y, self.labelSize, self.colors["darkBlue"], "calibri")
        elif (type(locationOfText) == list):
            if (locationOfText[0] == "left"):
                self.textDrawer.add(self.text, str(self.X) + "-" + str(self.size-self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "calibri")/2-locationOfText[1]), self.Y, self.labelSize, self.colors["darkBlue"], "calibri")
            elif (locationOfText[0] == "right"):
                self.textDrawer.add(self.text, str(self.X) + "+" + str(self.size+self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "calibri")/2+locationOfText[1]), self.Y, self.labelSize, self.colors["darkBlue"], "calibri")

        else: # Default parameters are to the left and with a 30 pixel spacer
            self.textDrawer.add(self.text, str(self.X) + "-" + str(self.size-self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "calibri")/2-30), self.Y, self.labelSize, self.colors["darkBlue"], "calibri")


    def draw(self):
        if (self.state):
            pygame.draw.rect(self.screen, (70, 170, 250), self.backRect, 0, 15)
        else:
            pygame.draw.rect(self.screen, (175,175,175), self.backRect, 0, 15)
        pygame.draw.rect(self.screen, self.colors["darkBlue"], self.backRect, self.borderSize, 15)

        self.textDrawer.draw()

        pygame.draw.rect(self.screen, (255,255,255), self.moveRect, 0, 15)
        pygame.draw.rect(self.screen, self.colors["darkBlue"], self.moveRect, self.borderSize, 15)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.xOp = Expressions.locationExpressionValue(self.X, center_X, center_Y)
        self.yOp = Expressions.locationExpressionValue(self.Y, center_X, center_Y)
        self.textDrawer.recenter(self.center_X, self.center_Y)
        if (self.state):
            self.moveRect = pygame.Rect(self.xOp-self.size, self.yOp-self.size/2, self.size, self.size)
        else:
            self.moveRect = pygame.Rect(self.xOp, self.yOp-self.size/2, self.size, self.size)
        self.backRect = pygame.Rect(self.xOp-self.size, self.yOp-self.size/2, 2*self.size, self.size)

    def clicked(self, mousePos):
        if (self.moveRect.collidepoint(mousePos)):
            self.state = not self.state
            if (self.state):
                self.moveRect = pygame.Rect(self.xOp-self.size, self.yOp-self.size/2, self.size, self.size)
            else:
                self.moveRect = pygame.Rect(self.xOp, self.yOp-self.size/2, self.size, self.size)
            CUSTOMEVENT = pygame.event.Event(self.event)
            pygame.event.post(CUSTOMEVENT)
            return True
        else:
            return False

# An object that draws a line
# DEPRECATED
class Line:

    def __init__(self, screen, center_X, center_Y, startX, startY, endX, endY, thickness, color):

        self.screen = screen

        self.center_X = center_X
        self.center_Y = center_Y

        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        
        self.thickness = thickness
        self.color = color

        self.startXOp = Expressions.locationExpressionValue(self.startX, center_X, center_Y)
        self.startYOp = Expressions.locationExpressionValue(self.startY, center_X, center_Y)

        self.endXOp = Expressions.locationExpressionValue(self.endX, center_X, center_Y)
        self.endYOp = Expressions.locationExpressionValue(self.endY, center_X, center_Y)

    def draw(self):
        pygame.draw.line(self.screen, self.color, (self.startXOp, self.startYOp), (self.endXOp, self.endYOp), self.thickness)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y

        self.startXOp = Expressions.locationExpressionValue(self.startX, center_X, center_Y)
        self.startYOp = Expressions.locationExpressionValue(self.startY, center_X, center_Y)

        self.endXOp = Expressions.locationExpressionValue(self.endX, center_X, center_Y)
        self.endYOp = Expressions.locationExpressionValue(self.endY, center_X, center_Y)

# An object that displays an image
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

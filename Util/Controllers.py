import pygame
import Elements
import Enums
import Controllers
import Screens

class ProblemController:

    def __init__(self, screen=None, problemList=None):

        self.screen = screen

        self.elements = []
        self.interactive = []

        self.problemList = problemList

        self.createProblem()
        pass

    def reset(self, problemType):
        pass

    def createProblem(self):
        pass

    def updateMCQController(self):
        self.MCQController.updateMCQStates()

    def draw(self):
        for element in self.elements:
            element.draw()
    
    def recenter(self):
        for element in self.elements:
            element.recenter()

    def processEvent(self, event):
        if (Screens.eventDict[event] == ""):
            pass

class InputController:

    def __init__(self, screen=None, y=500, **kwargs):

        self.screen = screen
        self.y = y

        self.elements = []
        self.interactive = []

    def draw(self):
        for element in self.elements:
            element.draw()
    
    def clicked(self, mousePos):
        for element in self.interactive:
            element.clicked(mousePos)

    def mouseOver(self, mousePos):
        for element in self.interactive:
            element.mouseOver(mousePos)

    def recenter(self):
        for element in self.elements:
            element.recenter()    

    def getInput(self):
        pass

    def processEvent(self, event):
        pass

class MCQController(InputController):

    def __init__(self, screen=None, y=500, numMCQs=4, maxSelectable=1, **kwargs):

        self.screen = screen

        self.elements = []
        self.interactive = []

        self.y=y

        self.numMCQs = numMCQs

        self.maxSelectable = maxSelectable

        self.numSelected = 0

        self.labelList = []

        try:
            self.labelList = kwargs["labelList"]
        except:
            for i in range(numMCQs):
                try:
                    self.labelList.append(kwargs["label"+str(i+1)])
                except:
                    self.labelList.append(None)  

        self.createChoices(numMCQs=numMCQs)

    def createChoices(self, numMCQs):

        self.mcqButtonList = []

        for i in range(numMCQs):
            mcqButton = Elements.MCQButton(screen=self.screen, 
                                            event=6903+i, 
                                            sizeX=500, 
                                            sizeY=70, 
                                            positionController=Controllers.PositionController(objectLength=500,
                                                                                              objectHeight=70, 
                                                                                              drawAnchor=Enums.Anchor.TopLeft(),
                                                                                              xOffset=30, 
                                                                                              yOffset=self.y+80*i, 
                                                                                              refAnchor=Enums.Anchor.TopLeft()),  
                                            labelInformation= ["A. ", "B. ", "C. ", "D. "][i] + (lambda x: "" if x is None else x)(self.labelList[i]), 
                                            labelType=Enums.Label.Text(),
                                            labelSize = 20,
                                            font = "calibri",
                                            labelColor = (0,0,0))
            self.elements.append(mcqButton)
            self.interactive.append(mcqButton)

    def updateMCQStates(self):
        pass

    def processEvent(self, event):

        if (self.maxSelectable == 1):
            for mcq in self.elements:
                if (event == mcq.event):
                    mcq.changeSelectedState(not mcq.selected)
                else:
                    mcq.changeSelectedState(False)
        else:
            for mcq in self.elements:
                if (event == mcq.event):
                    if (mcq.isSelected()):
                        mcq.changeSelectedState(False)
                        self.numSelected -= 1
                    else:
                        if (self.numSelected < self.maxSelectable):
                            mcq.changeSelectedState(True)
                            self.numSelected += 1
        pass

    def getInput(self):

        selectedMCQValues = []
        for mcq in self.elements:
            if (mcq.isSelected()):
                selectedMCQValues.append([mcq.getValue()[0], mcq.getValue()[2:]])

        return selectedMCQValues

class TextBoxController(InputController):

    def __init__(self, screen=None, numTextBoxes=3, y=500, **kwargs):

        self.screen = screen
        self.numTextBoxes = numTextBoxes

        self.y = y

        self.elements = []
        self.interactive = []

        self.labelList = []

        try:
            self.labelList = kwargs["labelList"]
        except:
            for i in range(numTextBoxes):
                try:
                    self.labelList.append(kwargs["label"+str(i+1)])
                except:
                    self.labelList.append(None)  

        self.createTextBoxes()

    def createTextBoxes(self):

        self.textBoxList = []

        for i in range(self.numTextBoxes):
            textBox = Elements.InputTextBox(screen=self.screen,
                                            length=200,
                                            height=50,
                                            positionController=Controllers.PositionController(objectLength=200,
                                                                                              objectHeight=50,
                                                                                              drawAnchor=Enums.Anchor.TopLeft(),
                                                                                              xOffset=30+sum((x.getLength()+20) for x in self.elements[0:i]), 
                                                                                              yOffset=self.y, 
                                                                                              refAnchor=Enums.Anchor.TopLeft()),
                                            labelText=self.labelList[i])
            self.elements.append(textBox)
            self.interactive.append(textBox)

    def updateTextBoxesText(self, event):
        for textBox in self.elements:
            if (textBox.isActive):
                textBox.inputText(event)

    def updateTextBoxStates(self):
        pass

    def getInput(self):
        textBoxInputs = []
        for textBox in self.elements:
            textBoxInputs.append(textBox.inputtedText)
        return textBoxInputs

class PositionController:

    def __init__(self, objectLength, objectHeight, xOffset = 0, yOffset = 0, drawAnchor = Enums.Anchor.Center(), refObject = Enums.Screen(), refAnchor = Enums.Anchor.Center()):
        
        self.objectLength = objectLength
        self.objectHeight = objectHeight
        self.drawAnchor = drawAnchor
        
        self.xOffset = xOffset
        self.yOffset = yOffset

        self.refObject = refObject
        self.refAnchor = refAnchor

        self.recenter()
    
    def recenter(self):
        if (type(self.refObject) == Enums.Screen):
            self.refLength, self.refHeight = pygame.display.get_window_size()
        elif (type(self.refObject) == PositionController):
            self.refLength, self.refHeight = self.refObject.getSize()

    def getPosition(self, positionOnObject = None):

        if (type(self.refObject) == Enums.Screen):
            position = [0,0]
        elif (type(self.refObject) == PositionController):
            position = [self.refObject.getPosition(positionOnObject=Enums.Anchor.TopLeft())[0], 
                        self.refObject.getPosition(positionOnObject=Enums.Anchor.TopLeft())[1]]

        # Finding center position
        if (type(self.refAnchor) == Enums.Anchor.Center):
            position[0] += self.refLength/2 + self.xOffset
            position[1] += self.refHeight/2 + self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.TopRight):
            position[0] += self.refLength + self.xOffset
            position[1] += self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.TopLeft):
            position[0] += self.xOffset
            position[1] += self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.BottomRight):
            position[0] += self.refLength + self.xOffset
            position[1] += self.refHeight + self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.BottomLeft):
            position[0] += self.xOffset
            position[1] += self.refHeight + self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.TopCenter):
            position[0] += self.refLength/2 + self.xOffset
            position[1] += self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.BottomCenter):
            position[0] += self.refLength/2 + self.xOffset
            position[1] += self.refHeight + self.yOffset  
        elif (type(self.refAnchor) == Enums.Anchor.RightCenter):
            position[0] += self.refLength + self.xOffset
            position[1] += self.refHeight/2 + self.yOffset
        elif (type(self.refAnchor) == Enums.Anchor.LeftCenter):
            position[0] += self.xOffset
            position[1] += self.refHeight/2 + self.yOffset

        # Offsetting by initial draw anchor

        if (positionOnObject == None):
            return position
        else:
            if (callable(self.objectLength)):
                objectLengthValue = self.objectLength()
            else:
                objectLengthValue = self.objectLength

            if (callable(self.objectHeight)):
                objectHeightValue = self.objectHeight()
            else:
                objectHeightValue = self.objectHeight

            # FInd center position
            if (type(self.drawAnchor) == Enums.Anchor.Center):
                pass
            elif (type(self.drawAnchor) == Enums.Anchor.TopLeft):
                position[0] += objectLengthValue/2
                position[1] += objectHeightValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.BottomLeft):
                position[0] += objectLengthValue/2
                position[1] -= objectHeightValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.TopRight):
                position[0] -= objectLengthValue/2
                position[1] += objectHeightValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.BottomRight):
                position[0] -= objectLengthValue/2
                position[1] -= objectHeightValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.TopCenter):
                position[1] += objectHeightValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.BottomCenter):
                position[1] -= objectHeightValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.RightCenter):
                position[0] -= objectLengthValue/2
            elif (type(self.drawAnchor) == Enums.Anchor.LeftCenter):
                position[0] += objectLengthValue/2                                  

            # From center position find other positions
            if (type(positionOnObject) == Enums.Anchor.Center):
                pass
            elif (type(positionOnObject) == Enums.Anchor.TopRight):
                position[0] += objectLengthValue/2
                position[1] += -objectHeightValue/2
            elif (type(positionOnObject) == Enums.Anchor.TopLeft):
                position[0] += -objectLengthValue/2
                position[1] += -objectHeightValue/2
            elif (type(positionOnObject) == Enums.Anchor.BottomRight):
                position[0] += objectLengthValue/2
                position[1] += objectHeightValue/2
            elif (type(positionOnObject) == Enums.Anchor.BottomLeft):
                position[0] += -objectLengthValue/2
                position[1] += objectHeightValue/2
            elif (type(positionOnObject) == Enums.Anchor.TopCenter):
                position[1] += -objectHeightValue/2
            elif (type(positionOnObject) == Enums.Anchor.BottomCenter):
                position[1] += objectHeightValue/2
            elif (type(positionOnObject) == Enums.Anchor.RightCenter):
                position[0] += objectLengthValue/2
            elif (type(positionOnObject) == Enums.Anchor.LeftCenter):
                position[0] += -objectLengthValue/2

            return position
        
    def getSize(self):
        return (lambda x: x if not callable(x) else x())(self.objectLength), (lambda x: x if not callable(x) else x())(self.objectHeight)
    
    def changeSize(self, newLength=None, newHeight=None):
        if (newLength != None):
            self.objectLength = newLength
        if (newHeight != None):
            self.objectHeight = newHeight

    def changeOffset(self, newXOffset=None, newYOffset=None):
        if (newXOffset != None):
            self.xOffset = newXOffset
        if (newYOffset != None):
            self.yOffset = newYOffset
    
    def changeRefAnchor(self, newRefAnchor):
        self.refAnchor = newRefAnchor
    
    def changeDrawAnchor(self, newDrawAnchor):
        self.drawAnchor = newDrawAnchor

class TextController:

    def __init__(self, screen=None):
        self.screen = screen
        self.texts = []

    def draw(self):
        for text in self.texts:
            text.draw()

    def add(self, text):
        self.texts.append(text)

    def getTexts(self):
        for text in self.texts:
            print(text)
        return self.texts
    
    def clear(self):
        self.texts = []

    def recenter(self):
        for text in self.texts:
            text.recenter()
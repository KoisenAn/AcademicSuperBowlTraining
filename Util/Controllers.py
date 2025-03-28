import pygame
import Elements
import Enums
import Controllers

class ProblemController:

    def __init__(self, screen = None, elementList = None, interactiveList = None):

        self.screen = screen
        self.submitted = False

        self.problemType = None

        self.answer = []
        self.inputElements = []

        self.textBoxLocations = []

        self.elementList = elementList
        self.interactiveList = interactiveList

        #self.MCQController = MCQController(screen, center_X, center_Y, self.elementList, self.interactiveList)
        pass

    def reset(self, problemType):

        self.answer = []
        del self.inputElements[:]
        self.problemType = problemType

    def loadProblemDisplay(self, problem):

        self.problem = problem

        question = problem.getQuestion()

        type = problem.problemDisplayType

        self.questionDisplayType = type

        if (type == "lines"):
            pass

    def loadSolutionDisplay(self, problem):

        self.problem = problem

        answers = problem.getAnswer()

        for i in range(len(self.textBoxLocations)):
            string = "Answer: " + str(answers[i])
            self.TextDrawer.add(string, self.textBoxLocations[i]+(self.TextDrawer.findLengthOfTextRect(string, 25, "calibri"))/2+5, "2*cY-43", 25, self.color, "calibri")

    def loadProblemInput(self, inputType):
        
        self.inputType = inputType

        del self.inputElements[:]

        font = 40

        self.textBoxLocations = []

        print(inputType)

        if (inputType[0] == "textBox"):
            if (inputType[1] == 1):
                text = self.problem.inputTexts[0]

                currEnd  = 50
                lengthFirstText = self.TextDrawer.findLengthOfTextRect(text, font, "calibri")
                self.TextDrawer.add(text, currEnd + lengthFirstText/2, "2*cY-88", font, self.color, "calibri")
                currEnd += lengthFirstText
                currEnd += 30 #Spacer between outside text and textbox

                lengthTextbox = 2 * self.center_X - 250 - lengthFirstText - 30 #Accounting for difference

                self.textBox1 = Elements.InputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox1)

                self.textBoxLocations.append(currEnd)

            elif (inputType[1] == 2):
                
                #Finding sizes
                currEnd = 50
                text1 = text = self.problem.inputTexts[0]
                lengthFirstText = self.TextDrawer.findLengthOfTextRect(text1, font, "calibri")

                text2 = text = self.problem.inputTexts[1]
                lengthSecondText = self.TextDrawer.findLengthOfTextRect(text2, font, "calibri")

                lengthTextbox = (2 * self.center_X - 250 - lengthFirstText - lengthSecondText - 20*2 - 50)/2

                #Drawing texts and boxes
                self.TextDrawer.add(text1, currEnd + lengthFirstText/2, "2*cY-88", font, self.color, "calibri")

                currEnd += lengthFirstText
                currEnd += 20

                self.textBox1 = Elements.InputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox1)

                self.textBoxLocations.append(currEnd)

                currEnd += lengthTextbox
                currEnd += 50

                self.TextDrawer.add(text2, currEnd + lengthSecondText/2, "2*cY-88", font, self.color, "calibri")

                currEnd += lengthSecondText
                currEnd += 20

                self.textBox2 = Elements.InputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox2)

                self.textBoxLocations.append(currEnd)
            elif (inputType[1] == 3):

                #Finding sizes
                currEnd = 50
                text1 = text = self.problem.inputTexts[0]
                lengthFirstText = self.TextDrawer.findLengthOfTextRect(text1, font, "calibri")

                text2 = text = self.problem.inputTexts[1]
                lengthSecondText = self.TextDrawer.findLengthOfTextRect(text2, font, "calibri")

                text3 = text = self.problem.inputTexts[2]
                lengthThirdText = self.TextDrawer.findLengthOfTextRect(text3, font, "calibri")

                lengthTextbox = (2 * self.center_X - 250 - lengthFirstText - lengthSecondText - lengthThirdText - 20*3 - 50*2)/3

                #Drawing texts and boxes
                self.TextDrawer.add(text1, currEnd + lengthFirstText/2, "2*cY-88", font, self.color, "calibri")

                currEnd += lengthFirstText
                currEnd += 20

                self.textBox1 = Elements.InputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox1)

                self.textBoxLocations.append(currEnd)
    
                currEnd += lengthTextbox
                currEnd += 50

                self.TextDrawer.add(text2, currEnd + lengthSecondText/2, "2*cY-88", font, self.color, "calibri")

                currEnd += lengthSecondText
                currEnd += 20

                self.textBox2 = Elements.InputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox2)

                self.textBoxLocations.append(currEnd)
                
                currEnd += lengthTextbox
                currEnd += 50

                self.TextDrawer.add(text3, currEnd + lengthThirdText/2, "2*cY-88", font, self.color, "calibri")

                currEnd += lengthThirdText
                currEnd += 20

                self.textBox3 = Elements.InputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox3)

                self.textBoxLocations.append(currEnd)
        elif (inputType[0] == "mcq"):
            if (inputType[1] == 2):
                self.inputElements = self.MCQController.createChoices(2, 100, True)
            pass
        
    def checkCorrect(self):

        self.submitted = True

        passToProblemRecorder = None # A tuple to be passed into problem recorder (Is the problem correct, type of problem, timed or not timed)

        self.answer = []

        if (self.inputType[0] == "textbox"):
            for textbox in self.inputElements:
                self.answer.append(textbox.inputtedText)
            self.answer.reverse()
            self.correctList = self.problem.checkCorrect(self.answer)
            if (type(self.correctList) == bool):
                for i in range(len(self.inputElements)):
                    (self.inputElements[i]).submit(self.correctList)

                if (self.correctList):
                    passToProblemRecorder = (True, self.problemType, 0)
                else: 
                    passToProblemRecorder = (False, self.problemType, 0)
            else:
                correct = True
                for i in range(len(self.correctList)):
                    (self.inputElements[i]).submit(self.correctList[i])
                    if (correct and not self.correctList[i]):
                        correct = False
                        passToProblemRecorder = (False, self.problemType, 0)

                if (correct):
                    passToProblemRecorder = (True, self.problemType, 0)

        elif (self.inputType[0] == "mcq"):
            for mcq in self.inputElements:
                print(mcq.isSelected())
                if (mcq.isSelected()):
                    self.answer.append(mcq.getNumber())

        print(self.answer)
        passToProblemRecorder = (True, self.problemType, 0)

        #self.loadSolutionDisplay(self.problem)        
        return passToProblemRecorder

    def updateMCQController(self):
        self.MCQController.updateMCQStates()

    def draw(self):
        if (self.questionDisplayType == "lines"):
            self.TextDrawer.draw()

        for element in self.inputElements:
            element.draw()
    
    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.TextDrawer.recenter(center_X, center_Y)

        for element in self.inputElements:
            element.recenter(center_X, center_Y)

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

class MCQController(InputController):

    def __init__(self, screen=None, y=500, numMCQs=4, maxSelectable=1, **kwargs):

        self.screen = screen

        self.elements = []
        self.interactive = []

        self.y=y

        self.numMCQs = numMCQs

        self.maxSelectable = maxSelectable

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
                                            event=6905, 
                                            sizeX=500, 
                                            sizeY=70, 
                                            positionController=Controllers.PositionController(objectLength=500,
                                                                                              objectHeight=70, 
                                                                                              drawAnchor=Enums.Anchor.TopLeft(),
                                                                                              xOffset=30, 
                                                                                              yOffset=self.y+80*i, 
                                                                                              refAnchor=Enums.Anchor.TopLeft()),  
                                            labelInformation= ["A. ", "B. ", "C. ", "D. ", "E. ", "F. "][i] + (lambda x: "" if x is None else x)(self.labelList[i]), 
                                            labelType=Enums.Label.Text(),
                                            labelSize = 20,
                                            font = "calibri",
                                            labelColor = (0,0,0))
            self.elements.append(mcqButton)
            self.interactive.append(mcqButton)

    def updateMCQStates(self):
        pass

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
        print("-------")
        for text in self.texts:
            text.recenter()
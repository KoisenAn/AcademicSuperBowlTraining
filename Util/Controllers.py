import pygame
import Elements
import Enums

class ProblemController:

    def __init__(self, screen, center_X, center_Y, color, elementList, interactiveList):

        self.screen = screen
        self.color = color
        self.submitted = False

        self.problemType = None

        self.answer = []
        self.inputElements = []

        self.textBoxLocations = []

        self.elementList = elementList
        self.interactiveList = interactiveList

        self.center_X = center_X
        self.center_Y = center_Y

        self.TextDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.MCQController = MCQController(screen, center_X, center_Y, self.elementList, self.interactiveList)
        pass

    def reset(self, problemType):

        self.answer = []
        del self.inputElements[:]
        self.TextDrawer.clear()
        self.problemType = problemType

    def loadProblemDisplay(self, problem):

        self.problem = problem

        question = problem.getQuestion()

        type = problem.problemDisplayType

        self.questionDisplayType = type

        if (type == "lines"):

            if (len(question) > 1):

                spacing = 100

                topHieght = -1*float((len(question)-2))/2 * spacing -25

                for i in range(len(question)-1):
                    self.TextDrawer.add(question[i], "cX", "cY+" + str(topHieght+spacing*i), 60, self.color, "calibri")

                self.TextDrawer.add(question[len(question)-1], 120+(self.TextDrawer.findLengthOfTextRect(question[len(question)-1], 60, "calibri"))/2, 175, 60, self.color, "calibri")
            
            else:
                self.TextDrawer.add(question[0], "cX", "cY", 60, self.color, "calibri")

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

class MCQController:

    def __init__(self, screen, centerX, centerY, elementsList, interactiveList):

        self.screen = screen
        self.centerX = centerX
        self.centerY = centerY

        self.elementsList = elementsList
        self.interactiveList = interactiveList

        self.MCQElementList = []

    def createChoices(self, numMCQs, y, choiceType,):

        self.MCQElementList = []

        for i in range(numMCQs):
            MCQButton = Elements.MCQButton(self.screen, 100, y+100*i, self.centerX, self.centerY, 800, 80, i, "text", "test " + str(i), 30)
            self.MCQElementList.append(MCQButton)

        return self.MCQElementList
    
    def updateMCQStates(self):
        pass

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
            if (type(self.drawAnchor) == Enums.Anchor.Center): #TODO: Given a drawAnchor, calculate center position and then calculate all other positions
                if (type(positionOnObject) == Enums.Anchor.Center):
                    pass
                elif (type(positionOnObject) == Enums.Anchor.TopRight):
                    position[0] += self.objectLength/2
                    position[1] += -self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.TopLeft):
                    position[0] += -self.objectLength/2
                    position[1] += -self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.BottomRight):
                    position[0] += self.objectLength/2
                    position[1] += self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.BottomLeft):
                    position[0] += -self.objectLength/2
                    position[1] += self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.TopCenter):
                    position[1] += -self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.BottomCenter):
                    position[1] += self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.RightCenter):
                    position[0] += self.objectLength/2
                elif (type(positionOnObject) == Enums.Anchor.LeftCenter):
                    position[0] += -self.objectLength/2
            elif (type(self.drawAnchor) == Enums.Anchor.TopLeft):
                if (type(positionOnObject) == Enums.Anchor.Center):
                    position[0] += self.objectLength/2
                    position[1] += self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.TopRight):
                    position[0] += self.objectLength/2
                elif (type(positionOnObject) == Enums.Anchor.TopLeft):
                    pass
                elif (type(positionOnObject) == Enums.Anchor.BottomRight):
                    position[0] += self.objectLength
                    position[1] += self.objectHeight
                elif (type(positionOnObject) == Enums.Anchor.BottomLeft):
                    position[1] += self.objectHeight
                elif (type(positionOnObject) == Enums.Anchor.TopCenter):
                    position[0] += self.objectLength/2
                elif (type(positionOnObject) == Enums.Anchor.BottomCenter):
                    position[0] += self.objectLength/2
                    position[1] += self.objectHeight
                elif (type(positionOnObject) == Enums.Anchor.RightCenter):
                    position[0] += self.objectLength
                    position[1] += self.objectHeight/2
                elif (type(positionOnObject) == Enums.Anchor.LeftCenter):
                    position[1] += self.objectHeight/2
        
            return position
        
    def getSize(self):
        return self.objectLength, self.objectHeight
    
    def changeSize(self, newLength = None, newHeight = None):
        if (newLength != None):
            self.objectLength = newLength
        if (newHeight != None):
            self.objectHeight = newHeight
    
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
        pass
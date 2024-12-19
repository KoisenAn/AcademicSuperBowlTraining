import pygame
import Elements
import Expressions

#
# The following classes are used to draw/create specifics things to display or for users to interact with
#

#Draws text on a given screen
#Used for miscellaneous text
#X and Y are operations relative to the center

colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

class TextDrawer:

    def __init__(self, screen, center_X, center_Y):
        self.screen = screen
        self.Texts = []
        self.center_X = center_X
        self.center_Y = center_Y
    
    #Creates a tuple that holds information about individual texts to draw
    def add(self, string, X, Y, size, color, font):
        lines = string.split("\n")
        for i in range(len(lines)):
            if (type(Y) == int):
                width = self.findWidthOfTextRect(lines[i], size, font) * 1.5
                self.Texts.append((lines[i], X, Y-(len(lines)-1)*width/2+i*(width), size, color, font))
            elif (type(Y) == str):
                width = self.findWidthOfTextRect(lines[i], size, font) * 1.5
                self.Texts.append((lines[i], X, Y + "-" + str((len(lines)-1)*width/2) + "+" + str(i*(width)), size, color, font))

    def drawOne(self, string, X, Y, size, color, font):

        if (font.endswith("ttf")):
            self.font = pygame.font.Font(font, size)
        else:
            self.font = pygame.font.SysFont(font, size)
        text = self.font.render(string, True, color)
        textRect = text.get_rect()
    
        xOp = Expressions.locationExpressionValue(X, self.center_X, self.center_Y)
        yOp = Expressions.locationExpressionValue(Y, self.center_X, self.center_Y)

        textRect.center = (xOp,yOp)
        self.screen.blit(text, textRect)

    def draw(self):
        #print(self.Texts)
        for i in range(len(self.Texts)):
            self.drawOne(self.Texts[i][0],self.Texts[i][1],self.Texts[i][2],self.Texts[i][3],self.Texts[i][4],self.Texts[i][5])

    def getTexts(self):
        for textTuple in self.Texts:
            print(textTuple)
        return self.Texts
    
    def findLengthOfTextRect(self, string, size, font):

        testFont = pygame.font.SysFont(font, size)

        text = testFont.render(string, True, (0,0,0))
        textRect = text.get_rect()

        return textRect.size[0]
    
    def findWidthOfTextRect(self, string, size, font):

        testFont = pygame.font.SysFont(font, size)

        text = testFont.render(string, True, (0,0,0))
        textRect = text.get_rect()

        return textRect.size[1]

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
    
    def clear(self):
        self.Texts = []

# Creates a Button object which returns a event when pressed
# Note the drawing of the button is center based    
class Button:

    #Fix: Streamline inputs for button function
    def __init__(self, screen, X, Y, sizeX, sizeY, color, thickness, curveRadius, labelType, string, labelSize, center_X, center_Y, event, isWorking):

        #Initial Variables
        self.runTick = 0

        # Inputed variables stored in the object
        self.screen = screen
        self.color = color
        self.curveRadius = curveRadius
        self.thickness = thickness
        self.sizeY = sizeY
        self.string = string
        self.labelSize = labelSize
        self.labelType = labelType
        self.event = event
        self.isWorking = isWorking

        #Location variables
        self.X = X
        self.Y = Y

        self.center_X = center_X
        self.center_Y = center_Y

        xOp = Expressions.locationExpressionValue(X, self.center_X, self.center_Y)
        yOp = Expressions.locationExpressionValue(Y, self.center_X, self.center_Y)
        self.sizeX = sizeX

        #Button Creation
        self.hasThickness = False
        if (thickness > 0):
            self.ButtonRectOutside = pygame.Rect(center_X+xOp-sizeX/2, center_Y+yOp-sizeY/2, sizeX, sizeY)
            self.hasThickness = True
        self.ButtonRectInside = pygame.Rect(center_X+xOp-sizeX/2, center_Y+yOp-sizeY/2, sizeX, sizeY)

        self.labels = []
        self.label = Elements.Label(screen, labelSize, labelType, center_X+xOp, center_Y+yOp, string, color[2], 'ariel')
        self.labels.append(self.label)
        if (not isWorking):
            self.crossLine = Elements.Label(screen, thickness, "line", center_X+xOp, center_Y+yOp, (sizeX, sizeY), color[0], 'ariel')
            self.labels.append(self.crossLine)

    #Draws everything
    def draw(self):
        pygame.draw.rect(self.screen, self.color[1], self.ButtonRectInside, 0, self.curveRadius)
        if (self.hasThickness):
            pygame.draw.rect(self.screen, self.color[0], self.ButtonRectOutside, self.thickness, self.curveRadius)
        for label in self.labels:
            label.draw()

        #Button waiting after pressed and growing again
        if (self.runTick > 0):
            self.runTick += 1
            if (self.runTick == 10):
                #Makes button large again
                if (self.hasThickness):
                    self.ButtonRectOutside = self.ButtonRectOutside.scale_by(10/9)
                self.ButtonRectInside = self.ButtonRectInside.scale_by(10/9)
                self.label.changeSize(10/9)

                #Creates event to change screen
                #Fix: event creater/processing, don't know how to carry information with events, only can change the event type
                CUSTOMEVENT = pygame.event.Event(self.event)
                pygame.event.post(CUSTOMEVENT)
                self.runTick = 0
        else: 
            xOp = Expressions.locationExpressionValue(self.X, self.center_X, self.center_Y)
            yOp = Expressions.locationExpressionValue(self.Y, self.center_X, self.center_Y)
            self.ButtonRectOutside = pygame.Rect(self.center_X+xOp-self.sizeX/2, self.center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
            self.ButtonRectInside= pygame.Rect(self.center_X+xOp-self.sizeX/2, self.center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)

    #Runs/check if clicked
    def clicked(self, mousePos):
        if (self.ButtonRectOutside.collidepoint(mousePos) and self.runTick == 0):
            if (self.isWorking):
                self.runTick += 1
                self.changeSize(9/10)
            return True
        else:
            return False

    #Changes size of button
    def changeSize(self, scale):
        self.ButtonRectOutside = self.ButtonRectOutside.scale_by(scale)
        self.ButtonRectInside = self.ButtonRectInside.scale_by(scale)
        self.label.changeSize(scale)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        xOp = Expressions.locationExpressionValue(self.X, self.center_X, self.center_Y)
        yOp = Expressions.locationExpressionValue(self.Y, self.center_X, self.center_Y)
        for label in self.labels:
            label.recenter(center_X+xOp, center_Y+yOp)
     
    def getPosition(self):
        return self.X, self.Y

    def getSize(self):
        return self.sizeX, self.sizeY
    
    def changeColor(self, color):
        self.color = color

    def changeLabel(self, change, otherInformation):
        if (change == "text"):
            self.label.changeText(otherInformation)
        if (change == "image"):
            self.label.changeImage(otherInformation)

#Creates a label object which can be stuck on things like buttons
# not center or origin based, you put in the cords of the center of where you want to put the label
class Label:

    #Initializing function for labels of text and images 
    def __init__(self, screen, initSize, type, X, Y, otherInformation, color, font):
        if (type == "text"):

            #Initial Variables
            self.type = "text"

            # Inputed variables stored in the object
            self.screen = screen
            self.string = otherInformation
            self.labelSize = initSize
            self.X = X
            self.Y = Y

            if (font.endswith("ttf")):
                self.font = pygame.font.Font(font, initSize)
            else:
                self.font = pygame.font.SysFont(font, initSize)

            self.color = color
            self.text = self.font.render(otherInformation, True, color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (X, Y)

        elif (type == "image"):

            #Initial Variables
            self.type = "image"

            # Inputed variables stored in the object
            self.screen = screen
            self.string = otherInformation
            self.X = X
            self.Y = Y
            self.size = initSize
            self.image = pygame.image.load(otherInformation)
            self.image = pygame.transform.scale_by(self.image, initSize)
            self.imageRect = self.image.get_rect()
            self.imageRect.center = (X, Y)

        #I really only used this label to cross out buttons that don't work
        #The other information in this case is the size of button
        elif (type == "line"):

            self.screen = screen
            self.thickness = initSize
            self.type = "line"
            self.color = color

            self.X = X
            self.Y = Y
            self.horiDis = int(otherInformation[0]/2)
            self.vertDis = int(otherInformation[1]/2)
    
    def draw(self):
        if (self.type == "text"):
            self.textRect.center = (self.X, self.Y)
            self.screen.blit(self.text, self.textRect)
        elif (self.type == "image"):
            self.imageRect.center = (self.X, self.Y)
            self.screen.blit(self.image, self.imageRect)
        if (self.type == "line"):
            pygame.draw.line(self.screen, self.color, (self.X - self.horiDis +  6, self.Y - self.vertDis + 6), (self.X + self.horiDis -  6, self.Y + self.vertDis - 6), self.thickness)

    #Just changes the size for label, so the shrinking button animation works
    def changeSize(self, scale):
        if (self.type == "text"):
            self.font = pygame.font.SysFont('ariel', int(self.labelSize * scale))
            self.text = self.font.render(self.string, True, self.color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.X, self.Y)
        elif (self.type == "image"):
            self.image = pygame.image.load(self.string)
            self.image = pygame.transform.scale_by(self.image, self.size*scale)
            self.imageRect = self.image.get_rect()
            self.imageRect.center = (self.X, self.Y)
    
    def changeText(self, text):
        self.text = self.font.render(text, True, self.color)
    
    def changeImage(self, imagePath):
        self.string = imagePath

    def changeColor(self, color):
        self.color = color

    def recenter(self, X, Y):
        if (self.type == "text"):
            self.X = X
            self.Y = Y
        elif (self.type == "image"):
            self.X = X
            self.Y = Y
        if (self.type == "line"):
            self.X = X
            self.Y = Y

#Note that this is center-based 
class inputTextBox:

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

class divider:

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

#origin based
class problemNumberBox:

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

        self.label = Elements.Label(screen, 30, "text", X+sizeX/2, Y+sizeY/2, problemNumber, color, 'ariel')

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.boxOutlineRect, 0, 0)
        pygame.draw.rect(self.screen, self.color, self.boxOutlineRect, 7, 0)
        self.label.draw()

    def changeNumber(self, number):

        self.label = Elements.Label(self.screen, 30, "text", self.X+self.sizeX/2, self.Y+self.sizeY/2, str(number), self.color, 'ariel')

    def recenter(self, center_X, center_Y):
        pass

class problemController:

    def __init__(self, screen, center_X, center_Y, color):

        self.screen = screen
        self.color = color
        self.submitted = False

        self.problemType = None

        self.answer = []
        self.inputElements = []

        self.textBoxLocations = []

        self.center_X = center_X
        self.center_Y = center_Y
        self.TextDrawer = TextDrawer(screen, center_X, center_Y)
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
                    self.TextDrawer.add(question[i], "cX", "cY+" + str(topHieght+spacing*i), 60, self.color, "ariel")

                self.TextDrawer.add(question[len(question)-1], 120+(self.TextDrawer.findLengthOfTextRect(question[len(question)-1], 60, "ariel"))/2, 175, 60, self.color, "ariel")
            
            else:
                self.TextDrawer.add(question[0], "cX", "cY", 60, self.color, "ariel")

    def loadSolutionDisplay(self, problem):

        self.problem = problem

        answers = problem.getAnswer()

        for i in range(len(self.textBoxLocations)):
            string = "Answer: " + str(answers[i])
            self.TextDrawer.add(string, self.textBoxLocations[i]+(self.TextDrawer.findLengthOfTextRect(string, 25, "ariel"))/2+5, "2*cY-43", 25, self.color, "ariel")

    def loadProblemInput(self, type):
        
        self.inputType = type

        del self.inputElements[:]

        font = 40

        self.textBoxLocations = []

        if (type[0] == "textBox"):
            if (type[1] == 1):
                text = self.problem.inputTexts[0]

                currEnd  = 50
                lengthFirstText = self.TextDrawer.findLengthOfTextRect(text, font, "ariel")
                self.TextDrawer.add(text, currEnd + lengthFirstText/2, "2*cY-88", font, self.color, "ariel")
                currEnd += lengthFirstText
                currEnd += 30 #Spacer between outside text and textbox

                lengthTextbox = 2 * self.center_X - 250 - lengthFirstText - 30 #Accounting for difference

                self.textBox1 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox1)

                self.textBoxLocations.append(currEnd)

            elif (type[1] == 2):
                
                #Finding sizes
                currEnd = 50
                text1 = text = self.problem.inputTexts[0]
                lengthFirstText = self.TextDrawer.findLengthOfTextRect(text1, font, "ariel")

                text2 = text = self.problem.inputTexts[1]
                lengthSecondText = self.TextDrawer.findLengthOfTextRect(text2, font, "ariel")

                lengthTextbox = (2 * self.center_X - 250 - lengthFirstText - lengthSecondText - 20*2 - 50)/2

                #Drawing texts and boxes
                self.TextDrawer.add(text1, currEnd + lengthFirstText/2, "2*cY-88", font, self.color, "ariel")

                currEnd += lengthFirstText
                currEnd += 20

                self.textBox1 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox1)

                self.textBoxLocations.append(currEnd)

                currEnd += lengthTextbox
                currEnd += 50

                self.TextDrawer.add(text2, currEnd + lengthSecondText/2, "2*cY-88", font, self.color, "ariel")

                currEnd += lengthSecondText
                currEnd += 20

                self.textBox2 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox2)

                self.textBoxLocations.append(currEnd)
            elif (type[1] == 3):

                #Finding sizes
                currEnd = 50
                text1 = text = self.problem.inputTexts[0]
                lengthFirstText = self.TextDrawer.findLengthOfTextRect(text1, font, "ariel")

                text2 = text = self.problem.inputTexts[1]
                lengthSecondText = self.TextDrawer.findLengthOfTextRect(text2, font, "ariel")

                text3 = text = self.problem.inputTexts[2]
                lengthThirdText = self.TextDrawer.findLengthOfTextRect(text3, font, "ariel")

                lengthTextbox = (2 * self.center_X - 250 - lengthFirstText - lengthSecondText - lengthThirdText - 20*3 - 50*2)/3

                #Drawing texts and boxes
                self.TextDrawer.add(text1, currEnd + lengthFirstText/2, "2*cY-88", font, self.color, "ariel")

                currEnd += lengthFirstText
                currEnd += 20

                self.textBox1 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox1)

                self.textBoxLocations.append(currEnd)
    
                currEnd += lengthTextbox
                currEnd += 50

                self.TextDrawer.add(text2, currEnd + lengthSecondText/2, "2*cY-88", font, self.color, "ariel")

                currEnd += lengthSecondText
                currEnd += 20

                self.textBox2 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox2)

                self.textBoxLocations.append(currEnd)
                
                currEnd += lengthTextbox
                currEnd += 50

                self.TextDrawer.add(text3, currEnd + lengthThirdText/2, "2*cY-88", font, self.color, "ariel")

                currEnd += lengthThirdText
                currEnd += 20

                self.textBox3 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, (str(lengthTextbox/2)+"+"+str(currEnd)+"-cX"), "cY-88", lengthTextbox, 50, "Type Answer")
                self.inputElements.append(self.textBox3)

                self.textBoxLocations.append(currEnd)

    def checkCorrect(self):

        self.submitted = True

        passToProblemRecorder = None # A tuple to be passed into problem recorder (Is the problem correct, type of problem, timed or not timed)

        self.answer = []
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

        self.loadSolutionDisplay(self.problem)
        return passToProblemRecorder
    
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

class screenShader:

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
        
class switch:

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

        self.textDrawer.add("OFF", str(self.X) + "-" + str(self.size/2) + "+" + "5", self.Y, self.fontSize, (100,100,100), "ariel")

        self.textDrawer.add("ON", str(self.X) + "+" + str(self.size/2-5), self.Y, self.fontSize, (240,240,240), "ariel")

        self.text = text
        self.locationOfText = locationOfText

        self.labelSize = int(1.5*self.fontSize)
        if (type(locationOfText) == str):
            if (locationOfText == "left"):
                self.textDrawer.add(self.text, str(self.X) + "-" + str(self.size-self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "ariel")/2-30), self.Y, self.labelSize, self.colors["darkBlue"], "ariel")
            elif (locationOfText == "right"):
                self.textDrawer.add(self.text, str(self.X) + "+" + str(self.size+self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "ariel")/2+30), self.Y, self.labelSize, self.colors["darkBlue"], "ariel")
        elif (type(locationOfText) == list):
            if (locationOfText[0] == "left"):
                self.textDrawer.add(self.text, str(self.X) + "-" + str(self.size-self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "ariel")/2-locationOfText[1]), self.Y, self.labelSize, self.colors["darkBlue"], "ariel")
            elif (locationOfText[0] == "right"):
                self.textDrawer.add(self.text, str(self.X) + "+" + str(self.size+self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "ariel")/2+locationOfText[1]), self.Y, self.labelSize, self.colors["darkBlue"], "ariel")

        else: # Default parameters are to the left and with a 30 pixel spacer
            self.textDrawer.add(self.text, str(self.X) + "-" + str(self.size-self.textDrawer.findLengthOfTextRect(self.text, self.labelSize, "ariel")/2-30), self.Y, self.labelSize, self.colors["darkBlue"], "ariel")


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

        self.image = pygame.image.load(self.imageName)
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

        self.image = pygame.image.load(self.imageName)
        self.image = pygame.transform.scale_by(self.image, self.scale)
        self.imageRect = self.image.get_rect()
        self.imageRect.center = (self.XOp, self.YOp)

        self.borderRect = pygame.Rect(self.XOp+self.imageRect[0]/2, self.YOp+self.imageRect[1]/2, self.imageRect[0]/2, self.imageRect[1]/2)

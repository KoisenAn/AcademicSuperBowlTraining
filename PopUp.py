import pygame
import Elements
import PopUp

class popUpRect:

    def __init__ (self, screen, center_X, center_Y, colors, sizeX, sizeY):

        self.screen = screen

        self.colors = colors

        self.center_X = center_X
        self.center_Y = center_Y

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.rect = pygame.Rect(center_X-self.sizeX/2, center_Y-self.sizeY/2, self.sizeX, self.sizeY)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.colors["screenGrey"], self.rect, 0, 10)
        pygame.draw.rect(self.screen, self.colors["darkBlue"], self.rect, 6, 10)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.rect = pygame.Rect(center_X-self.sizeX/2, center_Y-self.sizeY/2, self.sizeX, self.sizeY)

    def getRect(self):
        return self.rect

class popUpInPracticeMenu:

    def __init__(self, screen, center_X, center_Y, practiceInfo):

        self.screen = screen

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.center_X = center_X
        self.center_Y = center_Y

        self.practiceInfo = practiceInfo

        self.Elements = []
        self.Interactive = []

        self.popUpRect = popUpRect(screen, center_X, center_Y, self.colors, 400, 400)
        self.Elements.append(self.popUpRect)

        self.screenShader = Elements.screenShader(screen, center_X, center_Y, 3799, self.popUpRect.getRect())
        self.Elements.append(self.screenShader)
        self.Interactive.append(self.screenShader)


        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.Elements.append(self.popUpRect)

        self.textDrawer.add("Menu", "cX", "cy-155", 50, self.colors["darkBlue"],"ariel")
        
        self.textDrawer.add("Correctly Answered:", "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Correctly Answered:", 30, "ariel")/2-170), "cy-90", 30, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Incorrectly Answered:", "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Incorrectly Answered:", 30, "ariel")/2-170), "cy-40", 30, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Timed Correctly Answered:", "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Timed Correctly Answered:", 30, "ariel")/2-170), "cy+10", 30, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Timed Incorrectly Answered:", "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Timed Incorrectly Answered:", 30, "ariel")/2-170), "cy+60", 30, self.colors["darkBlue"],"ariel")
        
        self.textDrawer.add(str(practiceInfo[0]), "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Correctly Answered:", 30, "ariel")-140), "cy-90", 30, self.colors["darkBlue"],"ariel")
        self.textDrawer.add(str(practiceInfo[1]), "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Incorrectly Answered:", 30, "ariel")-140), "cy-40", 30, self.colors["darkBlue"],"ariel")
        self.textDrawer.add(str(practiceInfo[2]), "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Timed Correctly Answered:", 30, "ariel")-140), "cy+10", 30, self.colors["darkBlue"],"ariel")
        self.textDrawer.add(str(practiceInfo[3]), "cX" + "+" + str(self.textDrawer.findLengthOfTextRect("Timed Incorrectly Answered:", 30, "ariel")-140), "cy+60", 30, self.colors["darkBlue"],"ariel")

        
        self.Elements.append(self.textDrawer)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        self.exitButton = Elements.Button(screen, 75, 150, 100, 50, buttonColor, 6, 10, "text", "Exit", 30, center_X, center_Y, 4201, True)
        self.returnButton = Elements.Button(screen, -75, 150, 100, 50, buttonColor, 6, 10, "text", "Done", 30, center_X, center_Y, 3799, True)

        self.Elements.append(self.exitButton)
        self.Elements.append(self.returnButton)

        self.Interactive.append(self.exitButton)
        self.Interactive.append(self.returnButton)

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X,center_Y)

    def updateNumbers(self):
        pass

class popUpSettings:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.center_X = center_X
        self.center_Y = center_Y

        self.Elements = []
        self.Interactive = []

        self.popUpRect = popUpRect(screen, center_X, center_Y, self.colors, 1000, 600)
        self.Elements.append(self.popUpRect)

        self.screenShader = Elements.screenShader(screen, center_X, center_Y, 3799, self.popUpRect.getRect())
        self.Elements.append(self.screenShader)
        self.Interactive.append(self.screenShader)

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.Elements.append(self.popUpRect)
        
        self.textDrawer.add("Settings", "cX", "cy-245", 70, self.colors["darkBlue"],"ariel")
        self.Elements.append(self.textDrawer)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        self.exitButton = Elements.Button(screen, 400, 250, 100, 50, buttonColor, 6, 10, "text", "Exit", 30, center_X, center_Y, 4201, True)
        self.returnButton = Elements.Button(screen, -400, 250, 100, 50, buttonColor, 6, 10, "text", "Done", 30, center_X, center_Y, 3799, True)

        self.MAswitch = Elements.switch(screen, "cX-400", "cY-175", center_X, center_Y, 50, False, "Multiple Attempts", ["right", 30], Elements.colors, 500, True)
        self.TimerSwitch = Elements.switch(screen, "cX-400", "cY-100", center_X, center_Y, 50, False, "Timer", ["right", 30], Elements.colors, 500, True)
        self.ShowSolutionSwitch = Elements.switch(screen, "cX-400", "cY-25", center_X, center_Y, 50, True, "Show Solution", ["right", 30], Elements.colors, 500, True)

        self.Elements.append(self.exitButton)
        self.Elements.append(self.returnButton)
        self.Elements.append(self.MAswitch)
        self.Elements.append(self.TimerSwitch)
        self.Elements.append(self.ShowSolutionSwitch)

        self.Interactive.append(self.exitButton)
        self.Interactive.append(self.returnButton)
        self.Interactive.append(self.MAswitch)
        self.Interactive.append(self.MAswitch)
        self.Interactive.append(self.TimerSwitch)
        self.Interactive.append(self.ShowSolutionSwitch)

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X,center_Y)

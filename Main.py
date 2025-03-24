import pygame

import sys
import os

current_dir = os.path.dirname(__file__)
folder_dir = os.path.join(current_dir, 'Util')
sys.path.insert(0, folder_dir)

current_dir = os.path.dirname(__file__)
folder_dir = os.path.join(current_dir, '2024-2025 Subjects')
sys.path.insert(0, folder_dir)

import Elements
import Screens
import PopUp

pygame.init()
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
Buttons = []

center_X = 640
center_Y = 360
currScreen = Screens.HomeScreen(screen)
popUp = None

tabDown = False
popUpActive = False

problemsDoneList = []
for i in range(7):
    problemsDoneList.append([0,0,0,0])

while running:
    #Checks for user interactions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Window size is changed
        if event.type == 32778:
            if (pygame.display.get_window_size()[0] < 1280):
                width = 1280
            else:
                width = pygame.display.get_window_size()[0]
            if (pygame.display.get_window_size()[1] < 400):
                height = 400
            else:
                height = pygame.display.get_window_size()[1]
            currScreen.recenter()
            screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
            if (popUp != None):
                popUp.recenter()

        # The mouse is clicked, or well released
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if (popUpActive):
                for interactive in popUp.interactive: #TODO: Combine popUp interactive and screen interactive
                    interactive.clicked(mousePos)
            else:
                for interactive in currScreen.interactive: 
                    interactive.clicked(mousePos)

        # A key is pressed
        if event.type == pygame.KEYDOWN: #TODO: Should not be managed outside
            try:
                currScreen.inputController.updateTextBoxesText(event)
            except:
                pass

            if (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
                tabDown = True
                homeScreenOperPart1 = True

            if (tabDown and event.key == pygame.K_t):
                currScreen = Screens.TestScreen(screen=screen)
            elif (tabDown and event.key == pygame.K_h):
                currScreen = Screens.HomeScreen(screen=screen)
            elif (tabDown and event.key == pygame.K_p):
                currScreen = Screens.PracticeSelectScreen(screen=screen)
            elif (tabDown and event.key == pygame.K_q):
                running = False
            elif (tabDown and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)):
                try:
                    print(currScreen.inputController.getInput())
                except:
                    pass

        # A key is releaseed
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LCTRL or event.key == pygame.K_LCTRL):
                tabDown = False

        #
        # Custom events
        #
    
        # Pop-ups
        if event.type >= 3700 and event.type <= 3900:
            popUpActive = True
            if (Screens.eventDict[event.type] == "popUpExit"):
                popUpActive = False
            elif (Screens.eventDict[event.type] == "popUpInPractice"):
                popUp = PopUp.popUpInPracticeMenu(screen, center_X, center_Y, problemsDoneList[currScreen.getType()-4202])
            elif (Screens.eventDict[event.type] == "popUpSettings"):
                popUp = PopUp.popUpSettings(screen, center_X, center_Y)
            elif (Screens.eventDict[event.type] == "popUpStats"):
                popUp = PopUp.popUpStats(screen, center_X, center_Y, problemsDoneList)

        # Screens
        if event.type >= 4100 and event.type <= 4300:
            popUpActive = False
            if Screens.eventDict[event.type] == "home":
                currScreen = Screens.HomeScreen(screen=screen)
                continue
            elif Screens.eventDict[event.type] == "credits":
                currScreen = Screens.CreditsScreen(screen=screen)
                continue
            elif Screens.eventDict[event.type] == "pracSelect":
                currScreen = Screens.PracticeSelectScreen(screen=screen) 
                continue
            elif event.type >= 4202 and event.type <= 4208:
                currScreen = Screens.ProblemScreen(screen=screen, problemType=event.type)
                continue

        # In practice
        if event.type >= 6900 and event.type <= 7000: # TODO: Problem control should not be handled out in the main loop. Tasks should be delegated to the problem controller
            if (Screens.eventDict[event.type] == "answerInputted"):

                answerRecorder = currScreen.problemController.checkCorrect()

                if (answerRecorder[0]):
                    if (answerRecorder[2] == 0):
                        problemsDoneList[answerRecorder[1]-4202][0] += 1
                    else:
                        problemsDoneList[answerRecorder[1]-4202][2] += 1
                else:
                    if (answerRecorder[2] == 0):
                        problemsDoneList[answerRecorder[1]-4202][1] += 1
                    else:
                        problemsDoneList[answerRecorder[1]-4202][3] += 1

                currScreen.swapButton()

            elif (Screens.eventDict[event.type] == "newProblem"):
                currScreen.loadProblem()
                currScreen.swapButton()  

            elif (Screens.eventDict[event.type] == "newProblem"):
                currScreen.loadProblem()
                currScreen.swapButton()      


    #print("-----------")   
            
    screen.fill((230,230,230))
    
    currScreen.run()
    if (popUpActive):
        popUp.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
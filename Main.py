import pygame

import sys
import os

current_dir = os.path.dirname(__file__)
folder_dir = os.path.join(current_dir, 'Util')
sys.path.insert(0, folder_dir)

current_dir = os.path.dirname(__file__)
folder_dir = os.path.join(current_dir, '2024-2025 Subjects')
sys.path.insert(0, folder_dir)

import Screens
import Enums

pygame.init()
screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
Buttons = []

currScreen = Screens.HomeScreen(screen)
popUp = None

tabDown = False
popUpActive = False

problemsDoneList = []
for i in range(7):
    problemsDoneList.append([0,0,0,0])

while running:
    # Checks for user interactions
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

        # TODO: Pop-ups

        # Screens
        if event.type >= 4100 and event.type <= 4300:
            popUpActive = False
            if Enums.eventDict[event.type] == "home":
                currScreen = Screens.HomeScreen(screen=screen)
                continue
            elif Enums.eventDict[event.type] == "credits":
                currScreen = Screens.CreditsScreen(screen=screen)
                continue
            elif Enums.eventDict[event.type] == "pracSelect":
                currScreen = Screens.PracticeSelectScreen(screen=screen) 
                continue
            elif event.type >= 4202 and event.type <= 4208:
                currScreen = Screens.ProblemScreen(screen=screen, problemType=event.type)
                continue

        # In practice
        if event.type >= 6900 and event.type <= 7000:

            currScreen.processEvent(event.type)            
        
            if (Enums.eventDict[event.type].startswith("Choice")):
                currScreen.problemController.problem.inputController.processEvent(event.type) # TODO: Fix whatever tf this is
            
    screen.fill((230,230,230))
    
    currScreen.run()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
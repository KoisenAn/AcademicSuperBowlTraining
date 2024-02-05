import pygame
import Elements
import Screens

pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
Buttons = []

center_X = 640
center_Y = 360
currScreen = Screens.homescreen(screen, center_X, center_Y)

while running:
    #Checks for user interactions
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

        #Window size is changed
        if event.type == 32778:
            center_X = pygame.display.get_window_size()[0]/2
            center_Y = pygame.display.get_window_size()[1]/2
            currScreen.recenter(center_X,center_Y)

        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            for Button in currScreen.Interactive:
                Button.clicked(mousePos)

        
        if event.type == pygame.KEYDOWN:
            for textbox in currScreen.InteractiveText:
                if (textbox.isActive):
                    textbox.inputText(event)

        #Custom events
        if event.type >= 4100 and event.type <= 4300:
            if Screens.eventDict[event.type] == "home":
                currScreen = Screens.homescreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "credits":
                currScreen = Screens.creditsScreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "pracSelect":
                currScreen = Screens.practiceSelectScreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "algebra":
                currScreen = Screens.algebraScreen(screen, center_X, center_Y)
                continue

        if event.type >= 6900 and event.type <= 7000:
            pass

    #print("-----------")   

    screen.fill((230,230,230))
    
    currScreen.run()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
#June 6, 2018
#Pygame summative: stray to home

import pygame, random, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
pygame.display.set_caption('Stray To Home')
clock = pygame.time.Clock()
screenBg = (0,0,0)

catMinSize = 282
catMaxSize = 500
newItemRate = 60
playerMoveRate = 6

def menu():
    global playButton
    global instructionsButton
    global stopButton

    pygame.mixer.music.stop()
    pygame.mixer.music.load("menu.ogg")
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((900, 708),0,32)
    screen.fill(screenBg)
    
    background = pygame.image.load('menu.gif')
    screen.blit(background,(0,0))

    play = pygame.image.load('play.png')
    playButton = play.get_rect()
    playButton.move_ip(50, 350)
    screen.blit(play, playButton)

    instructions = pygame.image.load('howToPlay.png')
    instructionsButton = instructions.get_rect()
    instructionsButton.move_ip(50, 450)
    screen.blit(instructions, instructionsButton)

    stop = pygame.image.load('quit.png')
    stopButton = stop.get_rect()
    stopButton.move_ip(50, 550)
    screen.blit(stop, stopButton)

    title = pygame.image.load('title.gif')
    titleImage = title.get_rect()
    titleImage.move_ip(100, 20)
    screen.blit(title, titleImage)

    pygame.display.flip()

def sprites():
    global boxRect
    global boxImage
    global yarnImage
    global yarnSize
    global yarnSpeed
    global fishImage
    global fishSize
    global fishSpeed
    global appleImage
    global appleSize
    global appleSpeed
    global dogImage
    global dogSize
    global dogSpeed

    boxImage = pygame.image.load('box.gif')
    boxRect = boxImage.get_rect()
    
    yarnImage = pygame.image.load('yarn.gif')
    yarnSize = 50
    yarnSpeed = 4

    fishImage = pygame.image.load('fish.gif')
    fishSize = 60
    fishSpeed = 4

    appleImage = pygame.image.load('apple.png')
    appleSize = 50
    appleSpeed = 3

    dogImage = pygame.image.load('dog.png')
    dogSize = 50
    dogSpeed = 3

def story1():
    global doneButton
    global backButton

    pygame.mixer.music.stop()
    
    screen = pygame.display.set_mode((540,708),0,32)
    background = pygame.image.load('story1.png')
    screen.blit(background,(0,0))

    done = pygame.image.load('done.png')
    doneButton = done.get_rect()
    doneButton.move_ip(300, 600)
    screen.blit(done, doneButton)

    back = pygame.image.load('back.png')
    backButton = back.get_rect()
    backButton.move_ip(20, 20)
    screen.blit(back, backButton)
    
    pygame.display.flip()

def story2():
    global done2Button
    global backButton
    global screen

    pygame.mixer.music.stop()
    
    screen = pygame.display.set_mode((750,563),0,32)
    screen.fill(screenBg)
    background = pygame.image.load('story2.png')
    screen.blit(background,(0,0))

    done = pygame.image.load('done.png')
    done2Button = done.get_rect()
    done2Button.move_ip(500, 475)
    screen.blit(done, done2Button)

    back = pygame.image.load('back.png')
    backButton = back.get_rect()
    backButton.move_ip(20, 20)
    screen.blit(back, backButton)
    
    pygame.display.flip()

def level1():
    global windowWidth
    global windowHeight
    global level
    global screen

    pygame.mixer.music.stop()
    pygame.mixer.music.load("level1.ogg")
    pygame.mixer.music.play(-1)

    level = 1

    windowWidth = 500
    windowHeight = 708
    screen = pygame.display.set_mode((900,708),0,32)
    sidebar()
    
    pygame.display.flip()

    gameLoop()

def level2():
    global windowWidth
    global windowHeight
    global level
    global screen

    pygame.mixer.music.stop()
    pygame.mixer.music.load("level2.ogg")
    pygame.mixer.music.play(-1)

    level = 2

    windowWidth = 500
    windowHeight = 708
    screen = pygame.display.set_mode((900,708),0,32)
    sidebar()
    
    pygame.display.flip()

    gameLoop()


def puzzles():
    #called if level 2 failed. 2 puzzles must be completed in order to go back to level 2.
    #initialize maze screen, maze tree images, and cat (player) image
    #puzzle originally set to 1, loads puzzle 1 and music/position for puzzle 1
    #after puzzle 1 completed, add 1 to puzzle to go into puzzle 2
    #once puzzle 2 completed, go back to level 2
    global menuButton
    global mazeImage
    global mazeScreen
    global catsRect
    global cats
    global puzzle
    
    mazeScreen = pygame.display.set_mode((639,480),0,32)

    mazeImage =  pygame.image.load('mazeTree.png')

    cats = pygame.image.load('walk.png')
    catsRect = cats.get_rect()
    screen.blit(cats,catsRect)
    pygame.display.flip()

    if puzzle == 1:
        catsRect.centerx = (200)
        catsRect.centery = (70)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("puzzle1.ogg")
        pygame.mixer.music.play(-1)

    if puzzle == 2:
        catsRect.centerx = (10)
        catsRect.centery = (70)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("puzzle2.ogg")
        pygame.mixer.music.play(-1)

    if puzzle == 3:
        level2()

    puzzleBackground()
    catMove()

def puzzleBackground():
    #if first puzzle, set background to image for first puzzle and call first puzzle
    #if puzzle == 2, set background image for the second puzzle and call second puzzle
    global level

    if puzzle == 1:
        mazeBackground = pygame.image.load('puzzle1.png')
        mazeScreen.blit(mazeBackground,(0,0))
        maze1()
        
    if puzzle == 2:
        mazeBackground = pygame.image.load('puzzle2.png')
        mazeScreen.blit(mazeBackground,(0,0))
        maze2()


def catMove():
    #loop for cat moving, when left key pressed, subtract 2 from cat's x value
    #when right key pressed, add 2 from cat's x value
    #when down key pressed, add 2 from cat's y value
    #when up key pressed, subtract 2 from cat's y value
    #create rect to collide with to win puzzle
    global catsRect
    global cats
    global puzzle
    
    catMove = True
    endRect = pygame.Rect(600,405,30,30)
    rectColour = (0,0,0)
    pygame.draw.rect(mazeScreen, rectColour, endRect)

    while catMove:
        for event in pygame.event.get():
            if event.type == QUIT:
                catMove = False
                catGame = False
                quitGame()
        

        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        if keyinput[pygame.K_LEFT]:
            puzzleBackground()
            drawMaze(mazeScreen, mazeImage)
            pygame.draw.rect(mazeScreen, rectColour, endRect)
            catsRect.centerx -= 2
            
        elif keyinput[pygame.K_RIGHT]:
            puzzleBackground()
            drawMaze(mazeScreen, mazeImage)
            pygame.draw.rect(mazeScreen, rectColour, endRect)
            catsRect.centerx += 2
            
        elif keyinput[pygame.K_UP]:
            puzzleBackground()
            drawMaze(mazeScreen, mazeImage)
            pygame.draw.rect(mazeScreen, rectColour, endRect)
            catsRect.centery -= 2
            
        elif keyinput[pygame.K_DOWN]:
            puzzleBackground()
            drawMaze(mazeScreen, mazeImage)
            pygame.draw.rect(mazeScreen, rectColour, endRect)
            catsRect.centery += 2
                
        screen.blit(cats,catsRect)
        pygame.display.flip()


        #if cat collides with the trees/maze walls, exit function so cat doesnt move and go to menu
        if catsRect.colliderect(mazeImageRect):
            catMove = False
            menu()

        #if cat collides with end rect, add 1 to puzzle to go to the next puzzle
        if catsRect.colliderect(endRect):
            mazeScreen.fill(screenBg)
            puzzle += 1
            puzzles()
                

            

def maze1():
    #layout for first puzzle
    #M = columns
    #N = rows
    global M
    global N
    global maze
    
    M = 15
    N = 11
    maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
             0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,
             1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,
             1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,
             1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,
             1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,
             1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,
             1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,
             1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,
             1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,
             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]


    drawMaze(mazeScreen, mazeImage)

def maze2():
    #layout for second puzzle
    #M = columns
    #N = rows
    global M
    global N
    global maze
    
    M = 15
    N = 12
    maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
             1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,
             1,0,0,1,0,1,0,0,1,0,1,1,0,1,1,
             1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,
             1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,
             1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,
             1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,
             1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,
             1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,
             1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,
             1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,]


    drawMaze(mazeScreen, mazeImage)


def drawMaze(mazeScreen, mazeImage):
    #called with screen and image of trees
    #goes through every column for every row in maze
    #if it comes accross a 1 from the maze, blit an image of a tree there
    #make image of trees a rect in order to detect collisions with catRect
   global mazeImageRect

   x = y = 0
   for i in range(0,M*N):
       if maze[ x + (y*M) ] == 1:
           mazeScreen.blit(mazeImage,(x*44, y*44))
           mazeImageRect = mazeImage.get_rect()

       x = x+1
       if x > M-1:
           x = 0 
           y = y + 1

   pygame.display.flip()


def sidebar():
    global sidebarRect
    global backButton
    
    sidebarColour = (255,102,102)
    sidebarRect = pygame.draw.rect(screen,sidebarColour,(645,365,400,708))

    sidebar = pygame.image.load('sidebar.png')
    screen.blit(sidebar, (500,0))

    back = pygame.image.load('back.png')
    backButton = back.get_rect()
    backButton.move_ip(650, 600)
    screen.blit(back, backButton)

def quitGame():
    pygame.quit()

def gameInstructions():
    #window for game instructions
    #called when "how to play" button is pressed
    #background image has instructions
    #back button goes to menu
    global backButton
    
    screen = pygame.display.set_mode((626,626),0,32)

    background = pygame.image.load('brick.png')
    screen.blit(background,(0,0))

    back = pygame.image.load('back.png')
    backButton = back.get_rect()
    backButton.move_ip(20, 20)
    screen.blit(back, backButton)

    pygame.display.flip()


def endingScreen():
    #window for ending scene, very end of game, cat gets adopted
    #background image has ending scene
    #back button goes to home
    #stop button quits the program
    #titleImage adds game logo
    global stopButton
    global backButton

    pygame.mixer.music.stop()
    pygame.mixer.music.load("menu.ogg")
    pygame.mixer.music.play(0)

    screen = pygame.display.set_mode((900, 708),0,32)
    screen.fill(screenBg)
    
    background = pygame.image.load('ending.png')
    screen.blit(background,(0,0))

    stop = pygame.image.load('quit.png')
    stopButton = stop.get_rect()
    stopButton.move_ip(50, 600)
    screen.blit(stop, stopButton)

    back = pygame.image.load('back.png')
    backButton = back.get_rect()
    backButton.move_ip(50, 50)
    screen.blit(back, backButton)

    title = pygame.image.load('title.gif')
    titleImage = title.get_rect()
    titleImage.move_ip(100, 20)
    screen.blit(title, titleImage)

    pygame.display.flip()

def buttonLoop():
    global level
    Buttons = True
    
    while Buttons:
        for event in pygame.event.get():
            if event.type == QUIT:             
                catGame = False
                quitGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("buttonClick.ogg")
                    pygame.mixer.music.play(0)
                    mousePos = event.pos  
                    if playButton.collidepoint(mousePos):
                        print('button was pressed at {0}'.format(mousePos))
                        story1()

                    elif instructionsButton.collidepoint(mousePos):
                        print('button was pressed at {0}'.format(mousePos))
                        gameInstructions()

                    elif stopButton.collidepoint(mousePos):
                        print('button was pressed at {0}'.format(mousePos))
                        catGame = False
                        quitGame()

                    elif backButton.collidepoint(mousePos):
                        print('button was pressed at {0}'.format(mousePos))
                        menu()
                        
                    elif doneButton.collidepoint(mousePos):
                        print('button was pressed at {0}'.format(mousePos))
                        level1()
                        
                    elif done2Button.collidepoint(mousePos):
                        print('button was pressed at {0}'.format(mousePos))
                        level2()
                        
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                        catGame = False
                        quitGame()


def gameLoop():
    #Loop called when a level starts
    global lives
    global score
    global level
    global puzzle

    game = True                     #sets game to true for while loop
    items = []                      #create list for items
    score = 0                       #set score to 0 outside of loop
    moveLeft = moveRight = 0        #moveLeft and moveRight are empty (not true or false)
    boxRect.topleft = (windowWidth/2, windowHeight-75)  #set position of box to middle of screen
    itemAddCounter = 0              #set variable for adding items
    font = pygame.font.SysFont('Comic Sans MS', 50)
    fontColour = (255,255,255)
    lives = 3                       #set 3 lives
    
    while game:
        itemAddCounter += 1         #every time while loop loops, add another item

        def catInBox(boxRect, items):  
            global score
            global lives
            global windowHeight
            
            for x in items:
                if boxRect.colliderect(x['rect']):      #if box collides with an item
                    if x['speed'] == 4:                 #good items have speed of 4
                        score += 50                     #add score if collide with good item
                        pygame.mixer.music.load("pickUp.ogg")   #play sound effect when picking up item
                        pygame.mixer.music.play(0)
                        items.remove(x)                 #remove item when collides with box
                    elif x['speed'] == 3:               #bad items have speed of 3
                        lives -= 1                      #take away a life if collide with bad item
                        pygame.mixer.music.load("death.ogg")    #play sound when lose live
                        pygame.mixer.music.play(0)
                        items.remove(x)                 #remove item when collides with box

        for event in pygame.event.get():        
            if event.type == KEYDOWN:
                if event.key == K_LEFT:     #if left key pressed, set moveLeft to true and moveRight to false
                    moveRight = False
                    moveLeft = True 
                if event.key == K_RIGHT:    #if right key pressed, set moveLeft to false and moveRight to true
                    moveLeft = False
                    moveRight = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:   #if esc key pressed, exit loop and quit game
                        game = False
                        quitGame()
                if event.key == K_LEFT:     #when left key is let go of, stop moving left
                    moveLeft = False
                if event.key == K_RIGHT:    #when right key is let go of, stop moving right
                    moveRight = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                if backButton.collidepoint(mousePos):   #if back button clicked, exit loop, clear items, and go to menu
                    game = False
                    items.clear()
                    menu()
                
        if itemAddCounter == newItemRate:       #if item add counter is 60, then reset to 0
            itemAddCounter = 0

            x = random.randint(0,3)

            if x == 0:                   #if x is 0, set variables for yarn
                size = yarnSize
                image = yarnImage
                speed = yarnSpeed
                
            elif x == 1:                  #if x is 0, set variables for fish
                size = fishSize
                image = fishImage
                speed = fishSpeed

            elif x == 2:                  #if x is 0, set variables for apple
                size = appleSize
                image = appleImage
                speed = appleSpeed

            elif x == 3:                  #if x is 0, set variables for dog
                size = dogSize
                image = dogImage
                speed = dogSpeed

            catInBox(boxRect, items)

            
            #set position of item that falls and speed and surface according to the item defined as x
            newItem = {'rect': pygame.Rect(random.randint(0, windowWidth-size), 0 - size, size, size),
                        'speed': speed,
                        'surface':pygame.transform.scale(image, (size, size)),
                        }

            items.append(newItem)       #add item to items list
           
        if moveLeft and boxRect.left > 0:               #if moveLeft is true and the box is within the screen on the left side
            boxRect.move_ip(-1 * playerMoveRate, 0)     #move to box left and a rate of 6 (in the x direction)
        if moveRight and boxRect.right < windowWidth:   #if moveRight is true and the box is within the window on the right side
            boxRect.move_ip(playerMoveRate, 0)          #move to box right and a rate of 6 (in the x direction)

        for x in items:
            x['rect'].move_ip(0, x['speed'])        #items move at the predefined speed for each item
            
        for x in items[:]:
            if x['rect'].top > windowHeight:        #if the item falls beyond the screen, remove it
                items.remove(x)

        textsurface = font.render('%s' % (score), True, fontColour)     #display the score using text
        sidebar()                                   #call the sidebar

        screen.blit(textsurface, sidebarRect)       #blit the score text to the sidebar


        if lives == 3:                              #if player has 3 lives, display all 3 hearts
            life1 = pygame.image.load('heart.gif')
            screen.blit(life1, (550, 500))

            life2 = pygame.image.load('heart.gif')
            screen.blit(life2, (660, 500))

            life3 = pygame.image.load('heart.gif')
            screen.blit(life3, (770, 500))

        elif lives == 2:                            #if player has 2 lives, display 2 hearts
            life1 = pygame.image.load('heart.gif')
            screen.blit(life1, (550, 500))

            life2 = pygame.image.load('heart.gif')
            screen.blit(life2, (660, 500))

        elif lives == 1:                            #if player has 1 life, display 1 heart
            life1 = pygame.image.load('heart.gif')
            screen.blit(life1, (550, 500))

        else:
            if level == 1:          #if no lives left and in the first level, exit the loop, clear the items, and go to the menu
                game = False
                items.clear()
                menu()
                
            if level == 2:          #if no lives left and in the second level, exit the loop, clear items, set puzzle to 1, and start the puzzles
                game = False
                items.clear()
                puzzle = 1
                puzzles()
        

        for x in items:
            screen.blit(x['surface'], x['rect'])        #blit the surface(image) of each item to its rect

        screen.blit(boxImage, boxRect)                  #blit the image of the box to the rect

            
        pygame.display.flip()                           #update the screen


        if level == 1:              
            background = pygame.image.load('level1.gif')    #set bg image for first level
            screen.blit(background,(0,0))

            if score >= 1000:       #if 1000 points (goal) achieved, exit game, clear items, and go to story 2
                game = False
                items.clear()
                story2()

        elif level == 2:
            background = pygame.image.load('level2.png')    #set bg image for second level
            screen.blit(background,(0,0))

            if score >= 1500:       #if 1500 points (goal) achieved, level completed, add one to level
                level += 1

        elif level == 3:            #if level 2 completed, qut game, clear items, and go to the ending screen
            game = False
            items.clear()
            endingScreen()


menu()              #initially call menu, sprites, and button loop
sprites()
buttonLoop()















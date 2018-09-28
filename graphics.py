import pygame, sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import random

pygame.init()

# dimensions for surface and shapes
windowWidth = 800
windowHeight = 800
rectX = 10.0
rectY = 10.0
rectendX = 30.0
rectendY = 20.0
rectXmv = 1
rectYmv = 1

# set background image

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background("C:\Users\Student\Documents\pythongamesdevday\images\darts.jpg", [0,0])

dart = pygame.image.load('images/dart_small.png')

# add music

pygame.mixer.music.load("images\Bullseye-Theme-Tune-Long.mp3")
pygame.mixer.music.play(-1)

# collision detection



# set surface size
surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Pygame Keyboard!')

#clock initalisation

clock = pygame.time.Clock()

# Square Variables
playerSize = 50
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 100.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 0.2

# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False



# color choices
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# create quitgame fucntion
def quitgame():
    pygame.quit()
    sys.exit()

def move():

    global playerX, playerY, playerVX, playerVY, haveJumped, gravity

    # Move left
    if leftDown:
        #If we're already moving to the right, reset the moving speed and invert the direction
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX
        # Make sure our square doesn't leave our window to the left
        if playerX > 0:
            playerX += playerVX

    # Move right
    if rightDown:
        # If we're already moving to the left reset the moving speed again
        if playerVX < 0.0:
            playerVX = moveSpeed
        # Make sure our square doesn't leave our window to the right
        if playerX + playerSize < windowWidth:
            playerX += playerVX

    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else :
        playerVY = 0.0
        haveJumped = False

    # Is our square in the air? Better add some gravity to bring it back down!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
    else :
        playerY = windowHeight - playerSize
        gravity = 1.0

    playerY -= playerVY

    if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
        if haveJumped == False:
            playerVX = playerVX * 1.1




direction = 1
while True:
    surface.fill((0,0,0))
    # screen.fill([255, 255, 255])
    surface.blit(BackGround.image, BackGround.rect)


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # pygame.draw.rect(surface, (255, 0, 0), (playerX, playerY, playerSize, playerSize))
    surface.blit(dart, (playerX, playerY, playerSize, playerSize))

    # Get a list of all events that happened since the last redraw
    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped:
                    haveJumped = True
                    playerVY += jumpHeight
            if event.key == pygame.K_ESCAPE:
                quitGame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                gravity = 0
                moveSpeed = 0

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()


    move()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # pygame.draw.rect(surface, WHITE, (rectX, rectY, rectendX, rectendY))
    # if rectX > windowWidth:
    #     direction = -1
    # if rectX < 0:
    #     direction = 1
    # rectX += direction * random.randint(1, 10)
    #
    # if rectY > windowHeight:
    #     direction = -1
    # if rectY < 0:
    #     direction = 1
    # rectY += direction * random.randint(1, 10)
    #
    # # rectendX += 1
    # # rectendY += 1
    #
    # #draw an O
    # pygame.draw.circle(surface, RED, (200, 60), 50, 10)
    #
    # # draw a W
    # pygame.draw.lines(surface, BLUE, False, [(300,0), (350,100), (400,0), (450,100), (500,0)], 5)
    #
    # pygame.draw.polygon(surface, GREEN, [(300,0), (350,100), (400,0), (450,100), (500,0)])


    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quitgame()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitgame()
    clock.tick(30)
    pygame.display.update()


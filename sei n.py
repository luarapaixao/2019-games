import pygame

# initialize the pygame
pygame.init()


# doll and clothes
def doll(screen, x, y):
    image = pygame.image.load("doll.png")
    screen.blit(image, (x, y))
    pygame.display.flip()


def blusa(screen, x, y):
    image1 = pygame.image.load("blusa.png")
    screen.blit(image1, (x, y))
    pygame.display.flip()

def oito(screen, x, y):
    image1b = pygame.image.load("8.png")
    screen.blit(image1b, (x, y))
    pygame.display.flip()


def sapato(screen, x, y):
    image2 = pygame.image.load("sapato.png")
    screen.blit(image2, (x, y))
    pygame.display.flip()


def um(screen, x, y):
    image2b = pygame.image.load("1.png")
    screen.blit(image2b, (x, y))
    pygame.display.flip()

def dois(screen, x, y):
    image3b = pygame.image.load("2.png")
    screen.blit(image3b, (x, y))
    pygame.display.flip()

def sapatinho(screen, x, y):
    image3 = pygame.image.load("sapatinho.png")
    screen.blit(image3, (x, y))
    pygame.display.flip()


def allstar(screen, x, y):
    image4 = pygame.image.load("allstar.png")
    screen.blit(image4, (x, y))
    pygame.display.flip()

def tres(screen, x, y):
    image4b = pygame.image.load("3.png")
    screen.blit(image4b, (x, y))
    pygame.display.flip()

def jeans(screen, x, y):
    image5 = pygame.image.load("jeans.png")
    screen.blit(image5, (x, y))
    pygame.display.flip()

def quatro(screen, x, y):
    image5b = pygame.image.load("4.png")
    screen.blit(image5b, (x, y))
    pygame.display.flip()

def saia(screen, x, y):
    image6 = pygame.image.load("saia.png")
    screen.blit(image6, (x, y))
    pygame.display.flip()

def cinco(screen, x, y):
    image6b = pygame.image.load("5.png")
    screen.blit(image6b, (x, y))
    pygame.display.flip()

def top(screen, x, y):
    image7 = pygame.image.load("top.png")
    screen.blit(image7, (x, y))
    pygame.display.flip()

def seis(screen, x, y):
    image7b = pygame.image.load("6.png")
    screen.blit(image7b, (x, y))
    pygame.display.flip()

def vestido(screen, x, y):
    image8 = pygame.image.load("vestido.png")
    screen.blit(image8, (x, y))
    pygame.display.flip()

def sete(screen, x, y):
        image8b = pygame.image.load("7.png")
        screen.blit(image8b, (x, y))
        pygame.display.flip()


# create the screen
screen = pygame.display.set_mode([700, 650])

# background
background = pygame.image.load("background.png")

# screen.fill([0,0,0])
screen.blit(background, (0, 0))

# caption and icon
pygame.display.set_caption("doll dressup")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# positions
continuar = True

x = 30
y = 140
doll(screen, x, y)

x = 290
y = 70
blusa(screen, x, y)

x = 380
y = 180
oito(screen, x, y)

x = 270
y = 530
sapato(screen, x, y)

x = 307
y = 480
um(screen, x, y)

x = 425
y = 560
sapatinho(screen, x, y)

x = 458
y = 505
dois(screen, x, y)

x = 570
y = 580
allstar(screen, x, y)

x = 600
y = 530
tres(screen, x, y)

x = 565
y = 410
jeans(screen, x, y)

x = 600
y = 350
quatro(screen, x, y)

x = 422
y = 435
saia(screen, x, y)

x = 460
y = 370
cinco(screen, x, y)

x = 287
y = 435
top(screen, x, y)

x = 300
y = 370
seis(screen, x, y)

x = 520
y = 200
vestido(screen, x, y)

x = 565
y = 135
sete(screen, x, y)


while continuar:
    pygame.display.flip()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        continuar = False
        # break
        # pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            x = 101
            y = 530
            sapato(screen, x, y)
        if event.key == pygame.K_2:
            x = 100
            y = 560
            sapatinho(screen, x, y)
        if event.key == pygame.K_3:
            x = 100
            y = 585
            allstar(screen, x, y)
        if event.key == pygame.K_4:
            x = 95
            y = 464
            jeans(screen, x, y)
        if event.key == pygame.K_5:
            x = 96
            y = 450
            saia(screen, x, y)
        if event.key == pygame.K_6:
            x = 118
            y = 390
            top(screen, x, y)
        if event.key == pygame.K_7:
            x = 92
            y = 360
            vestido(screen, x, y)
        if event.key == pygame.K_8:
            x = 45
            y = 177
            blusa(screen, x, y)
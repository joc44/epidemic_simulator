import pygame
import sys
from random import randint

# Constants
SCREEN_SIZE = WIDTH, HEIGHT = (1280, 720)
NUMBER_OF_PEOPLE = 10
PERSON_SPEED = 15
PERSON_COLOR_CLEAR = (200, 150, 0)
PERSON_COLOR_INFECTED = (200, 0, 0)
PERSON_COLOR_IMMUNE = (200, 150, 0)
PERSON_AURA = 10
ILLNESS_TIME = 500
IMMUNE_TIME = 800
INFECTION_PROBALITY_WITH_MASK = 50
INFECTION_PROBALITY_WITHOUT_MASK = 2


# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Epidemic Simulator 1.0")
fps = pygame.time.Clock()
pause = False

# Person class
class Person:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = randint(-1, 1)
        self.dy = randint(-1, 1)
        self.illness = 0
        self.immune = 0
        self.mask = False

    def move(self):

        if randint(1, 30) == 1:
            self.dx = randint(-1, 1)
        if randint(1, 30) == 1:
            self.dy = randint(-1, 1)

        if PERSON_AURA < self.x + self.dx < WIDTH - PERSON_AURA:
            self.x += self.dx
        if PERSON_AURA < self.y + self.dy < HEIGHT - PERSON_AURA:
            self.y += self.dy

    def cure(self):

        if self.illness > 0:
            self.illness -= 1
            if self.illness == 0:
                self.immune = IMMUNE_TIME
        if self.immune > 0:
            self.immune -= 1



def modify(people):
    for person in people:
        person.move()
        person.cure()



def draw(people):

    screen.fill((0, 0, 0))

    for person in people:
        pygame.draw.circle(screen, PERSON_COLOR_CLEAR,(person.x, person.y), PERSON_AURA, 0)

    pygame.display.update()
    fps.tick(PERSON_SPEED)


# Create people
main_people_list = [Person(randint(50, WIDTH-50), randint(50, HEIGHT-50)) for i in range(NUMBER_OF_PEOPLE )]

#Main program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
    if not pause:
        modify(main_people_list)
        draw(main_people_list)


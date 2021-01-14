import pygame

from pygame.locals import(
	RLEACCEL,
	QUIT,
	KEYDOWN,
	K_ESCAPE,
	MOUSEBUTTONDOWN
	)

pygame.init()

#color variables
RED = (212, 6, 6)
YELLOW = (235, 229, 59)
BLUE = (50, 52, 168)
GREEN = (16, 173, 26)
PURPLE = (123, 16, 173)
PINK = (209, 100, 207)
ORANGE = (222, 115, 0)
LGRAY = (176, 175, 174)
DGRAY = (97, 97, 97)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

vec = pygame.math.Vector2

running = True

pygame.mouse.set_visible(True)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1600,800))

screen.fill(WHITE)

colornum = 1

color = BLUE

while running:
	clock.tick(100)
	
	mousecords = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
			if event.button == 4:
				colornum += 0.5
			if event.button == 5:
				colornum -= 0.5
		
		mousepress = pygame.mouse.get_pressed()
		if mousepress[0] == 1:
			pygame.draw.circle(screen, color, (int(mousecords[0]),int(mousecords[1])), 10)

	if colornum >= 12:
		colornum = 1
	elif colornum <= 0:
		colornum = 11
	if colornum == 1:
		color = BLUE
	elif colornum == 2:
		color = GREEN
	elif colornum == 3:
		color = YELLOW
	elif colornum == 4:
		color = ORANGE
	elif colornum == 5:
		color = RED
	elif colornum == 6:
		color = PURPLE
	elif colornum == 7:
		color = PINK
	elif colornum == 8:
		color = WHITE
	elif colornum == 9:
		color = LGRAY
	elif colornum == 10:
		color = DGRAY
	elif colornum == 11:
		color = BLACK

	pygame.draw.rect(screen, color, pygame.Rect(0,0,1600,20))

	pygame.display.update()


	pygame.display.flip()

pygame.quit()

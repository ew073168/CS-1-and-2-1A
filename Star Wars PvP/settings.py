#imports
import pygame
import random
import os

from pygame.locals import(
	RLEACCEL,
	K_w,
	K_s,
	K_a,
	K_d,
	K_e,
	K_q,
	K_m,
	K_1,
	K_2,
	K_3,
	K_DOWN,
	K_UP,
	K_LEFT,
	K_RIGHT,
	K_SPACE,
	K_ESCAPE,
	KEYUP,
	KEYDOWN,
	QUIT,
)

pygame.init()
pygame.mixer.init()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

shoot_sound = pygame.mixer.Sound('laser_shoot.wav')

height = 600
width = 800

vec = pygame.math.Vector2

p1class = 0
p2class = 0

def show_start_screen():
	start_screen = pygame.image.load(os.path.join(img_folder, 'start_screen.png')).convert()
	screen.blit(start_screen, [0,0])
	draw_text(screen, "Star Wars PvP", 50, width/2, height/4, (182,189,49))
	waiting = True
	while waiting:
		clock.tick(30)
		draw_text(screen, "Press any key to continue...", 20, width/2, height/4+75, (182, 189, 49))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYDOWN:
				waiting = False

	waitscreen1 = pygame.image.load(os.path.join(img_folder, 'hangar1.jpg')).convert()
	waitscreen1 = pygame.transform.scale(waitscreen1, (800, 600))
	wait1 = True
	screen.blit(waitscreen1, (0,0))
	screen.blit(tie1image, (100, 150))
	screen.blit(tie2image, (500, 150))
	screen.blit(tie3image, (310, 400))
	draw_text(screen, "P1, choose your class...", 40,  width/2, 30, (12, 245, 39))
	draw_text(screen, "Class 1", 35, 200, 115, (12, 245, 39))
	draw_text(screen, "Class 2", 35, 600, 115, (12, 245, 39))
	draw_text(screen, "Class 3", 35, 400, 365, (12, 245, 39))
	pygame.display.flip()
	while wait1:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYUP:
				if event.key == K_1:
					p1class = 1
					wait1 = False
				if event.key == K_2:
					p1class = 2
					wait1 = False
				if event.key == K_3:
					p1class = 3
					wait1 = False

	waitscreen2 = pygame.image.load(os.path.join(img_folder, 'hangar2.png')).convert()
	waitscreen2 = pygame.transform.scale(waitscreen2, (800, 600))
	wait2 = True
	screen.blit(waitscreen2, (0,0))
	screen.blit(xwingimage, (100, 150))
	screen.blit(ywingimage, (500, 150))
	screen.blit(awingimage, (300, 400))
	draw_text(screen, "P2, choose your class...", 40, width/2, 30, (7, 22, 232))
	draw_text(screen, "Class 1", 35, 200, 115, (7, 22, 232))
	draw_text(screen, "Class 2", 35, 600, 115, (7, 22, 232))
	draw_text(screen, "Class 3", 35, 400, 365, (7, 22, 232))
	pygame.display.flip()
	while wait2:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYUP:
				if event.key == K_1:
					p2class = 1
					wait2 = False
				if event.key == K_2:
					p2class = 2
					wait2 = False
				if event.key == K_3:
					p2class = 3
					wait2 = False

	global pclass
	pclass = [0,0]
	pclass[0] = p1class
	pclass[1] = p2class
	return pclass

def rebel():
	end = True
	while end:
		screen.blit(rebelWin, (0,0))
		draw_text(screen, "Victory for the Rebellion", 40, 400, 150, (7, 22, 232))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
def empire():
	end = True
	while end:
		screen.blit(empireWin, (0,0))
		draw_text(screen, "The Empire prevails", 40, 400, 150, (12, 245, 39))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()

screen = pygame.display.set_mode((width,height))

all_sprites = pygame.sprite.Group()
bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
powerups = pygame.sprite.Group()
explosions = pygame.sprite.Group()
shields1 = pygame.sprite.Group()
shields2 = pygame.sprite.Group()

tie1image = pygame.image.load(os.path.join(img_folder, 'tie.png')).convert()
tie1image = pygame.transform.scale(tie1image, (200, 200))
tie1image.set_colorkey((0,0,0), RLEACCEL)
tie2image = pygame.image.load(os.path.join(img_folder, 'tie2.png')).convert()
tie2image = pygame.transform.scale(tie2image, (200, 200))
tie2image.set_colorkey((0,0,0), RLEACCEL)
tie3image = pygame.image.load(os.path.join(img_folder, 'tie3.png')).convert()
tie3image = pygame.transform.scale(tie3image, (200, 200))
tie3image.set_colorkey((0,0,0), RLEACCEL)

xwingimage = pygame.image.load(os.path.join(img_folder, 'x-wing.png')).convert()
xwingimage = pygame.transform.scale(xwingimage, (200, 200))
xwingimage.set_colorkey((0,0,0), RLEACCEL)
ywingimage = pygame.image.load(os.path.join(img_folder, 'ywing.png')).convert()
ywingimage = pygame.transform.scale(ywingimage, (200, 200))
ywingimage.set_colorkey((0,0,0), RLEACCEL)
awingimage = pygame.image.load(os.path.join(img_folder, 'a-wing.png')).convert()
awingimage = pygame.transform.scale(awingimage, (200, 200))
awingimage.set_colorkey((0,0,0), RLEACCEL)

empireWin = pygame.image.load(os.path.join(img_folder, 'deathstarshoot.jpg')).convert()
empireWin = pygame.transform.scale(empireWin, (800, 600))
rebelWin = pygame.image.load(os.path.join(img_folder, 'deathstarexplosion.jpg')).convert()
rebelWin = pygame.transform.scale(rebelWin, (800, 600))

from bullet1 import Bullet1
from torpedo1 import Torpedo1
from player1 import Player
from bullet2 import Bullet2
from torpedo2 import Torpedo2
from player2 import Player2
from explosion import Explosion
from shieldpu import ShieldPU
from shield import Shield


player = Player(p1class) 
player2 = Player2(p2class)

background_image = pygame.image.load(os.path.join(img_folder, 'space.jpg')).convert()
background_image = pygame.transform.scale(background_image,(800,700))
background_image.set_colorkey((0,0,0), RLEACCEL)

death_star = pygame.image.load(os.path.join(img_folder, 'deathstar.png')).convert()
death_star = pygame.transform.scale(death_star, (100,100))
death_star.set_colorkey((0,0,0), RLEACCEL)


all_sprites.add(player)
all_sprites.add(player2)

players = pygame.sprite.Group()
players.add(player)
players.add(player2)



POWERUP =pygame.USEREVENT + 1
ptime = 18000
pygame.time.set_timer(POWERUP, ptime)

running = True
start = True

clock = pygame.time.Clock()

p1 = False
p2 = False
p1shield = False
p2shield = False

font_name = pygame.font.match_font("arial")
def draw_text(screen, text, size, x, y, color):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.center = (x,y)
	screen.blit(text_surface, text_rect)

#imports
import pygame
import random

from pygame.locals import(
	RLEACCEL,
	K_w,
	K_s,
	K_a,
	K_d,
	K_e,
	K_1,
	K_2,
	K_3,
	K_DOWN,
	K_UP,
	K_LEFT,
	K_RIGHT,
	K_SPACE,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)

pygame.init()
pygame.mixer.init()

shoot_sound = pygame.mixer.Sound('laser_shoot.wav')

height = 600
width = 800

vec = pygame.math.Vector2

p1class = 0

def show_start_screen():
	start_screen = pygame.image.load('start_screen.png')
	screen.blit(start_screen, [0,0])
	draw_text(screen, "Star Wars PvP", 50, width/2, height/4, (182,189,49))
	waiting = True
	var = 0
	while waiting:
		clock.tick(30)
		draw_text(screen, "Press any key to continue...", 20, width/2, height/4+75, (182, 189, 49))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYDOWN:
				waiting = False
	wait1 = True
	screen.fill((34,72,92))
	draw_text(screen, "P1, choose your class...", 40,  width/2, 30, (255,255,255))
	pygame.display.flip()
	while wait1:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYDOWN:
				if event.key == K_1:
					p1class = 1
					wait1 = False
				if event.key == K_2:
					p1class = 2
					wait1 = False
				if event.key == K_3:
					p1class = 3
					wait1 = False

screen = pygame.display.set_mode((width,height))

from bullet1 import Bullet1
from bullet2 import Bullet2
from explosion import Explosion
from shieldpu import ShieldPU
from shield import Shield
from player1 import Player
from player2 import Player2

player = Player() 
player2 = Player2()

background_image = pygame.image.load('space.jpg')
background_image = pygame.transform.scale(background_image,(800,700))
background_image.set_colorkey((0,0,0), RLEACCEL)

death_star = pygame.image.load('deathstar.png')
death_star = pygame.transform.scale(death_star, (100,100))
death_star.set_colorkey((0,0,0), RLEACCEL)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)

players = pygame.sprite.Group()
players.add(player)
players.add(player2)

bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
powerups = pygame.sprite.Group()
explosions = pygame.sprite.Group()
shields1 = pygame.sprite.Group()
shields2 = pygame.sprite.Group()

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

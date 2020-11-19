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

height = 600
width = 800

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.image = pygame.image.load('tie.png')
		self.image.set_colorkey((0,0,0), RLEACCEL)
		self.rect = self.image.get_rect(center=(0,height/2))
		self.shoot_delay = 750
		self.last_shot = pygame.time.get_ticks()

	def update(self, pressed_keys):
		if pressed_keys[K_w]:
			self.rect.move_ip(0,-5)
		if pressed_keys[K_s]:
			self.rect.move_ip(0,5)
		if pressed_keys[K_a]:
			self.rect.move_ip(-5,0)
		if pressed_keys[K_d]:
			self.rect.move_ip(5,0)
		if pressed_keys[K_e]:
			self.shoot()

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > 400:
			self.rect.right = 400
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= height:
			self.rect.bottom = height

	def shoot(self):
		now = pygame.time.get_ticks()
		if now - self.last_shot > self.shoot_delay:
			self.last_shot = now
			bullet = Bullet1(self.rect.right+10, self.rect.centery+16)
			all_sprites.add(bullet)
			bullets1.add(bullet)

	def getcords(self):
		return vec(self.rect.centerx, self.rect.centery)

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super(Player2, self).__init__()
		self.image = pygame.image.load('x-wing.png')
		self.image.set_colorkey((0,0,0), RLEACCEL)
		self.rect = self.image.get_rect(center=(width,height/2))
		self.shoot_delay = 750
		self.last_shot = pygame.time.get_ticks()

	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0,-5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0,5)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5,0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5,0)
		if pressed_keys[K_SPACE]:
			self.shoot()

		if self.rect.left < 400:
			self.rect.left = 400
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= height:
			self.rect.bottom = height

	def shoot(self):
		now = pygame.time.get_ticks()
		if now - self.last_shot > self.shoot_delay:
			self.last_shot = now
			bullet2 = Bullet2(self.rect.left-10, self.rect.centery+16)
			all_sprites.add(bullet2)
			bullets2.add(bullet2)

	def getcords(self):
		return vec(self.rect.centerx, self.rect.centery)

class Bullet1(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.lasers = (
			pygame.image.load('laser20.png').convert(),
			pygame.image.load('laser21.png').convert(),
			pygame.image.load('laser22.png').convert()
			)
		self.laser_count = 0
		
		self.image = self.lasers[self.laser_count] 
		self.image = pygame.transform.scale(self.image, (22,22))
		self.image.set_colorkey((0,0,0), RLEACCEL)

		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = 15

	def update(self):
		self.image = self.lasers[self.laser_count]
		self.image = pygame.transform.scale(self.image, (22,22))
		self.image.set_colorkey((0,0,0), RLEACCEL)

		self.laser_count += 1
		if self.laser_count > 2:
			self.laser_count = 0

		self.rect.x += self.speedy
		if self.rect.right >= width:
			self.kill()

class Bullet2(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.lasers = (
			pygame.image.load('laser0.png').convert(),
			pygame.image.load('laser1.png').convert(),
			pygame.image.load('laser2.png').convert()
			)
		self.laser_count = 0

		self.image = self.lasers[self.laser_count]
		self.image = pygame.transform.scale(self.image, (22,22))
		self.image.set_colorkey((0,0,0), RLEACCEL)

		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -15

	def update(self):
		self.image = self.lasers[self.laser_count]
		self.image = pygame.transform.scale(self.image, (22,22))
		self.image.set_colorkey((0,0,0), RLEACCEL)

		self.laser_count += 1
		if self.laser_count > 2:
			self.laser_count = 0

		self.rect.x += self.speedy
		if self.rect.left == 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.explosions = (
			pygame.image.load('e1.png').convert(),
			pygame.image.load('e2.png').convert(),
			pygame.image.load('e3.png').convert(),
			pygame.image.load('e4.png').convert(),
			pygame.image.load('e5.png').convert()
			)
		self.explosion_count = 0

		self.image = self.explosions[self.explosion_count]
		self.image = pygame.transform.scale(self.image, (32, 32))
		self.image.set_colorkey((0,0,0))

		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.left = x

	def update(self):
		self.image = self.explosions[self.explosion_count]
		self.image = pygame.transform.scale(self.image, (32, 32))
		self.image.set_colorkey((0,0,0))

		self.explosion_count += 1
		if self.explosion_count > 4:
			self.kill()

class ShieldPU(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('shieldpu.png').convert()
		self.image = pygame.transform.scale(self.image, (18,18))
		self.image.set_colorkey((0,0,0))
		
		self.rect = self.image.get_rect()
		self.rect.centery = 0
		self.rect.centerx = random.randint(300,500)
		self.speedy = 5

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top == 600:
			self.kill()

class Shield(pygame.sprite.Sprite):
	def __init__(self, x, y, p):
		pygame.sprite.Sprite.__init__(self)
		if p == 1:
			self.image = pygame.image.load('shield1.png').convert()
			self.image.set_colorkey((0,0,0))
		elif p == 2:
			self.image = pygame.image.load('shield2.png').convert()
			self.image.set_colorkey((0,0,0))

		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x

	def update(self, x, y):
		self.rect.centery = y
		self.rect.centerx = x

font_name = pygame.font.match_font("arial")
def draw_text(screen, text, size, x, y):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, (255,255,255))
	text_rect = text_surface.get_rect()
	text_rect.center = (x,y)
	screen.blit(text_surface, text_rect)

screen = pygame.display.set_mode((width,height))

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
ptime = 1000
pygame.time.set_timer(POWERUP, ptime)

running = True

clock = pygame.time.Clock()

p1 = False
p2 = False
p1shield = False
p2shield = False

#game loop
while running == True:

	clock.tick(30)

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False
		elif event.type == POWERUP:
			shield = ShieldPU()
			all_sprites.add(shield)
			powerups.add(shield)

	pressed_keys = pygame.key.get_pressed()

	ploc = player.getcords()
	p2loc = player2.getcords()

	players.update(pressed_keys)
	bullets1.update()
	bullets2.update()
	explosions.update()
	powerups.update()
	shields1.update(ploc.x, ploc.y)
	shields2.update(p2loc.x, p2loc.y)
	screen.blit(background_image, [0,0])
	screen.blit(death_star, [100,100])
	all_sprites.draw(screen)

	if pygame.sprite.groupcollide(bullets1, powerups, True, True, collided = None):
		p1shield = True
		p1shieldt = 5000
		start1 = pygame.time.get_ticks()

	if pygame.sprite.groupcollide(bullets2, powerups, True, True, collided = None):
		p2shield = True
		p2shieldt = 5000
		start2 = pygame.time.get_ticks()

	if pygame.sprite.spritecollideany(player, bullets2):
		p2 = True
		ploc = player.getcords()
		explosion = Explosion(ploc.x-16, ploc.y+16)
		all_sprites.add(explosion)
		explosions.add(explosion)
		player.kill()

	if pygame.sprite.spritecollideany(player2, bullets1):
		p1 = True
		p2loc = player2.getcords()
		explosion = Explosion(p2loc.x-16, p2loc.y+16)
		all_sprites.add(explosion)
		explosions.add(explosion)
		player2.kill()

	if p1shield == True:
		shield1 = Shield(ploc.x, ploc.y, 1)
		shields1.add(shield1)
		all_sprites.add(shield1)
		now = pygame.time.get_ticks()
		if now - start1 > 5000:
			shield1.kill()
			p1shield = False

	if p2shield == True:
		shield2 = Shield(p2loc.x, p2loc.y, 2)
		shields2.add(shield2)
		all_sprites.add(shield2)
		now = pygame.time.get_ticks()
		if now - start2 > 5000:
			shield2.kill()
			p2shield = False

	if p2 == True:
		draw_text(screen, "X-WING WON!", 50, 400, 50)

	if p1 == True:
		draw_text(screen, "TIE INTERCEPTOR WON!", 50, 400, 50)

	pygame.display.flip()

pygame.quit
from settings import *

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
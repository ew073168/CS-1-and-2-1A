from settings import *

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

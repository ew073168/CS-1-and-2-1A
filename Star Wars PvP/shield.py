from settings import *

class Shield(pygame.sprite.Sprite):
	def __init__(self, x, y, p):
		pygame.sprite.Sprite.__init__(self)
		if p == 1:
			self.image = pygame.image.load(os.path.join(img_folder, 'shield1.png')).convert()
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
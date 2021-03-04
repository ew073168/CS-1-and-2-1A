from settings import *

class Torpedo1(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, 'tietorpedo.png.'))
		self.image.set_colorkey((0,0,0), RLEACCEL)

		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = 22

	def update(self):
		self.rect.x += self.speedy
		if self.rect.x >= width:
			self.kill()
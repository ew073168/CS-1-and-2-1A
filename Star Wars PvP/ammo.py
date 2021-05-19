from settings import *

class Ammo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, 'ammopu.png')).convert()
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
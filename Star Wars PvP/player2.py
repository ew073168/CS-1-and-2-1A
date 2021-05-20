from settings import *

class Player2(pygame.sprite.Sprite):
	def __init__(self, p2class):
		super(Player2, self).__init__()
		self.p2class = p2class
		self.speed = 5
		self.shoot_delay = 750
		self.image = pygame.image.load(os.path.join(img_folder, 'x-wing.png')).convert()
		self.image.set_colorkey((0,0,0), RLEACCEL)
		if p2class == 1:
			self.image = pygame.image.load(os.path.join(img_folder, 'x-wing.png')).convert()
			self.image.set_colorkey((0,0,0), RLEACCEL)
			self.shoot_delay = 750
			self.speed = 7
		elif p2class == 2:
			self.image = pygame.image.load(os.path.join(img_folder, 'ywing.png')).convert()
			self.image.set_colorkey((0,0,0))
			self.shoot_delay = 750
			self.speed = 5
		elif p2class == 3:
			self.image = pygame.image.load(os.path.join(img_folder, 'a-wing.png')).convert()
			self.image = pygame.transform.scale(self.image, (40,40))
			self.image.set_colorkey((0,0,0), RLEACCEL)
			self.shoot_delay = 500
			self.speed = 5
		self.rect = self.image.get_rect(center=(width,height/2))
		self.last_shot = pygame.time.get_ticks()
		self.last_torpedo = pygame.time.get_ticks()
		self.torpedo_delay = 5000
		self.health = 4
		self.magazine = 10

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
		if pressed_keys[K_m]:
			if self.p2class == 2:
				self.torpedo()

		if self.rect.left < 400:
			self.rect.left = 400
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= height:
			self.rect.bottom = height

	def shoot(self):
		if self.magazine > 0:
			now = pygame.time.get_ticks()
			if now - self.last_shot > self.shoot_delay:
				self.last_shot = now
				shoot_sound.play()
				bullet2 = Bullet2(self.rect.left-10, self.rect.centery+16)
				all_sprites.add(bullet2)
				bullets2.add(bullet2)
				self.magazine -= 1

	def torpedo(self):
		now = pygame.time.get_ticks()
		if now - self.last_torpedo > self.torpedo_delay:
			self.last_torpedo = now
			torpedo = Torpedo2(self.rect.left-10, self.rect.centery)
			all_sprites.add(torpedo)
			bullets2.add(torpedo)

	def getcords(self):
		return vec(self.rect.centerx, self.rect.centery)

	def setPlayerClass(self, p2class):
		self.p2class = p2class
		if p2class == 1:
			self.image = pygame.image.load(os.path.join(img_folder, 'x-wing.png')).convert()
			self.image.set_colorkey((0,0,0), RLEACCEL)
			self.shoot_delay = 750
			self.speed = 7
		elif p2class == 2:
			self.image = pygame.image.load(os.path.join(img_folder, 'ywing.png')).convert()
			self.image.set_colorkey((0,0,0))
			self.shoot_delay = 750
			self.speed = 5
		elif p2class == 3:
			self.image = pygame.image.load(os.path.join(img_folder, 'a-wing.png')).convert()
			self.image = pygame.transform.scale(self.image, (25,25))
			self.image.set_colorkey((0,0,0), RLEACCEL)
			self.shoot_delay = 500
			self.speed = 5

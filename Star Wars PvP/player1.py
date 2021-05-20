from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,p1class):
		super(Player, self).__init__()
		self.p1class = p1class
		self.speed = 5
		self.shoot_delay = 500
		self.image = pygame.image.load(os.path.join(img_folder, 'tie.png')).convert()
		self.image.set_colorkey((0,0,0), RLEACCEL)
		if p1class == 1:
			self.image = pygame.image.load(os.path.join(img_folder, 'tie.png')).convert()
			self.image.set_colorkey((0,0,0), RLEACCEL)
			self.shoot_delay = 750
			self.speed = 7
		elif p1class == 2:
			self.image = pygame.image.load(os.path.join(img_folder, 'tie2.png')).convert()
			self.image.set_colorkey((0,0,0))
			self.shoot_delay = 750
			self.speed = 5
		elif p1class == 3:
			self.image = pygame.image.load(os.path.join(img_folder, 'tie3.png')).convert()
			self.image.set_colorkey((0,0,0), RLEACCEL)
			self.shoot_delay = 500
			self.speed = 5
		self.rect = self.image.get_rect(center=(0,height/2))
		self.torpedo_delay = 5000
		self.last_shot = pygame.time.get_ticks()
		self.last_torpedo = pygame.time.get_ticks()
		self.health = 4
		self.magazine = 10

	def shoot(self):
		if self.magazine > 0:
			now = pygame.time.get_ticks()
			if now - self.last_shot > self.shoot_delay:
				self.last_shot = now
				shoot_sound.play()
				bullet = Bullet1(self.rect.right+10, self.rect.centery+16)
				all_sprites.add(bullet)
				bullets1.add(bullet)
				self.magazine -= 1
	
	def torpedo(self):
		now = pygame.time.get_ticks()
		if now - self.last_torpedo > self.torpedo_delay:
			self.last_torpedo = now
			torpedo = Torpedo1(self.rect.right+10, self.rect.centery)
			all_sprites.add(torpedo)
			bullets1.add(torpedo)
			

	def update(self, pressed_keys):

		if self.p1class == 1:
			self.image = pygame.image.load(os.path.join(img_folder, 'tie.png')).convert()
			self.image.set_colorkey((0,0,0))
			self.shoot_delay = 750
			self.speed = 7
		elif self.p1class == 2:
			self.image = pygame.image.load(os.path.join(img_folder, 'tie2.png')).convert()
			self.image.set_colorkey((0,0,0))
			self.shoot_delay = 750
			self.speed = 5
		elif self.p1class == 3:
			self.image = pygame.image.load(os.path.join(img_folder, 'tie3.png')).convert()
			self.image.set_colorkey((0,0,0))
			self.shoot_delay = 500
			self.speed = 5

		if pressed_keys[K_w]:
			self.rect.move_ip(0,-self.speed)
		if pressed_keys[K_s]:
			self.rect.move_ip(0,self.speed)
		if pressed_keys[K_a]:
			self.rect.move_ip(-self.speed,0)
		if pressed_keys[K_d]:
			self.rect.move_ip(self.speed,0)
		if pressed_keys[K_e]:
			self.shoot()
		if pressed_keys[K_q]:
			if self.p1class == 2:
				self.torpedo()

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > 400:
			self.rect.right = 400
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= height:
			self.rect.bottom = height

	def getcords(self):
		return vec(self.rect.centerx, self.rect.centery)

	def setPlayerClass(self, p1class):
		self.p1class = p1class

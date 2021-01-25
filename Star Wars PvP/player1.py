from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.image = pygame.image.load('tie.png')
		if p1class == 1:
			self.image = pygame.image.load('tie.png')
			self.shoot_delay = 750
			self.speed = 7
		elif p1class == 2:
			self.image = pygame.image.load('tie2.png')
			self.shoot_delay = 750
			self.speed = 5
		elif p1class == 3:
			self.image = pygame.image.load('tie3.png')
			self.shoot_delay = 500
			self.speed = 5
		self.image.set_colorkey((0,0,0), RLEACCEL)
		self.rect = self.image.get_rect(center=(0,height/2))
		self.last_shot = pygame.time.get_ticks()

	def update(self, pressed_keys):
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
			shoot_sound.play()
			bullet = Bullet1(self.rect.right+10, self.rect.centery+16)
			all_sprites.add(bullet)
			bullets1.add(bullet)

	def getcords(self):
		return vec(self.rect.centerx, self.rect.centery)
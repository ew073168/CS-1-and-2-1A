from settings import *

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
			shoot_sound.play()
			bullet2 = Bullet2(self.rect.left-10, self.rect.centery+16)
			all_sprites.add(bullet2)
			bullets2.add(bullet2)

	def getcords(self):
		return vec(self.rect.centerx, self.rect.centery)

from settings import *

hintshow = False

#game loop
while running == True:

	clock.tick(30)

	if start:
		pclass = show_start_screen()
		p1class = pclass[0]
		p2class = pclass[1]
		player.setPlayerClass(p1class)
		player2.setPlayerClass(p2class)
		start = False
		
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			if event.key == K_1:
				music1()
			if event.key == K_2:
				music2()
			if event.key == K_h:
				if hintshow == True:
					hintshow = False
				elif hintshow == False:
					hintshow = True
		elif event.type == QUIT:
			running = False
		elif event.type == POWERUP:
			pu = random.randint(1,3)
			if pu == 1:
				shield = ShieldPU()
				all_sprites.add(shield)
				powerups.add(shield)
			if pu == 2:
				health = Health()
				all_sprites.add(health)
				pups.add(health)
			if pu == 3:
				ammo = Ammo()
				all_sprites.add(ammo)
				ammopups.add(ammo)

	pressed_keys = pygame.key.get_pressed()
	
	ploc = player.getcords()
	p2loc = player2.getcords()

	players1.update(pressed_keys)
	players2.update(pressed_keys)
	bullets1.update()
	bullets2.update()
	explosions.update()
	powerups.update()
	pups.update()
	ammopups.update()
	shields1.update(ploc.x+10, ploc.y)
	shields2.update(p2loc.x-10, p2loc.y)
	screen.blit(background_image, [0,0])
	screen.blit(death_star, [100,100])
	if player.health == 1:
		screen.blit(empireHealth1, [25, 25])
	if player.health == 2:
		screen.blit(empireHealth2, [25, 25])
	if player.health == 3:
		screen.blit(empireHealth3, [25, 25])
	if player.health == 4:
		screen.blit(empireHealth4, [25, 25])

	if player2.health == 1:
		screen.blit(rebelHealth1, [675, 25])
	if player2.health == 2:
		screen.blit(rebelHealth2, [675, 25])
	if player2.health == 3:
		screen.blit(rebelHealth3, [675, 25])
	if player2.health == 4:
		screen.blit(rebelHealth4, [675, 25])

	all_sprites.draw(screen)
	if hintshow == True:
		hint()

	if pygame.sprite.groupcollide(bullets1, powerups, True, True, collided = None) or pygame.sprite.groupcollide(players1, powerups, False, True, collided = None):
		p1shield = True

	if pygame.sprite.groupcollide(bullets2, powerups, True, True, collided = None) or pygame.sprite.groupcollide(players2, powerups, False, True, collided = None):
		p2shield = True

	if pygame.sprite.groupcollide(bullets1, pups, True, True, collided = None) or  pygame.sprite.groupcollide(players1, pups, False, True, collided = None):
		player.health += 2
		if player.health > 4:
			player.health = 4

	if pygame.sprite.groupcollide(bullets2, pups, True, True, collided = None) or  pygame.sprite.groupcollide(players2, pups, False, True, collided = None):
		player2.health += 2
		if player2.health > 4:
			player2.health = 4

	if pygame.sprite.groupcollide(bullets1, ammopups, True, True, collided = None) or pygame.sprite.groupcollide(players1, ammopups, False, True, collided = None):
		player.magazine += 10

	if pygame.sprite.groupcollide(bullets2, ammopups, True, True, collided = None) or pygame.sprite.groupcollide(players2, ammopups, False, True, collided = None):
		player2.magazine += 10

	if pygame.sprite.groupcollide(players1, bullets2, False, True):
		player.health -=1
	if player.health == 0:
		rebel()

	if pygame.sprite.groupcollide(players2, bullets1, False, True):
		player2.health -= 1
	if player2.health == 0:
		empire()

	if pygame.sprite.groupcollide(shields1, bullets2, True, True, collided = None):
		pass

	if pygame.sprite.groupcollide(shields2, bullets1, True, True, collided = None):
		pass

	if p1shield == True:
		ploc = player.getcords()
		shield1 = Shield(ploc.x, ploc.y, 1)
		shields1.add(shield1)
		all_sprites.add(shield1)
		p1shield = False

	if p2shield == True:
		p2loc = player2.getcords()
		shield2 = Shield(p2loc.x, p2loc.y, 2)
		shields2.add(shield2)
		all_sprites.add(shield2)
		p1shield = False

	pygame.display.flip()

pygame.quit
from settings import *



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
		elif event.type == QUIT:
			running = False
		elif event.type == POWERUP:
			shield = ShieldPU()
			all_sprites.add(shield)
			powerups.add(shield)

	pressed_keys = pygame.key.get_pressed()
	
	ploc = player.getcords()
	p2loc = player2.getcords()


	players.update(pressed_keys)
	bullets1.update()
	bullets2.update()
	explosions.update()
	powerups.update()
	shields1.update(ploc.x+10, ploc.y)
	shields2.update(p2loc.x-10, p2loc.y)
	screen.blit(background_image, [0,0])
	screen.blit(death_star, [100,100])
	all_sprites.draw(screen)

	if pygame.sprite.groupcollide(bullets1, powerups, True, True, collided = None):
		p1shield = True

	if pygame.sprite.groupcollide(bullets2, powerups, True, True, collided = None):
		p2shield = True

	if pygame.sprite.spritecollideany(player, bullets2):
		p2 = True
		ploc = player.getcords()
		explosion = Explosion(ploc.x-16, ploc.y+16)
		all_sprites.add(explosion)
		explosions.add(explosion)
		player.kill()

	if pygame.sprite.spritecollideany(player2, bullets1):
		p1 = True
		p2loc = player2.getcords()
		explosion = Explosion(p2loc.x-16, p2loc.y+16)
		all_sprites.add(explosion)
		explosions.add(explosion)
		player2.kill()

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

	if p2 == True:
		draw_text(screen, "VICTORY TO THE REBELLION!", 50, 400, 50, (255,255,255))

	if p1 == True:
		draw_text(screen, "THE EMPIRE PREVAILS!", 50, 400, 50, (255,255,255))

	pygame.display.flip()

pygame.quit
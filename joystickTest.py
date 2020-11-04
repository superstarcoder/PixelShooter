import pygame
import random

""" ALL FUNCTIONS GO HERE """

place = "menu"
sound_bool = True
music_bool = True
# initialize everything
def initialize():
	global damage, h100, h95, h90, h85, h80, h70, h60, h50, h40, h30, h20, h10, h0, hwidth, hheight, spider
	global fps, width, height, size, screen, clock, done, ship, pos, xv, yv, direction, star, speed, pos2
	global shipb, bullets, rock1, rock2, rocks, shoot_s, bug, bugb, aliens, xv2, yv2, explosion, health
	global alien_b, score, bullets2, shoot2, scoreBoard, chance1, chance2, place, pixel1, menu
	global play_b, settings_b, exit_b, p1_1, p1_2, p1_3, p1, p2, p3, exit_b2, easy_b
	global medium_b, hard_b, extreme_b, insane_b, p2_1, p2_2, p2_3, p2_4, p2_5
	global np1, np2, np3, np4, np5, menu_b, back_b, pause_b, size_b3, siz_b4
	global p, nnp1, nnp2, sound_b, no_sound_b, music_b, no_music_b, back_b2
	global BLACK, WHITE, GREEN, RED, YELLOW, ORANGE, BLUE, mode
	global nnnp1, nnnp2, nnnp3, sound_bool, music_bool
	global checked_scores, centrep, size_b
	global press, joystick1, joystick2
	global jx1, jy1, jx2, jy2
	star_render()

	bullets2 = []
	rocks = []
	bullets = []
	aliens = []
	pos2 = [957, 510]

	chance1 = 50
	chance2 = 150
	health = 100
	speed = 0
	xv = 0
	yv = 0
	fps = 20
	width = 1900
	height = 1050
	jx1 = 1600
	jy1 = 700
	jx2 = 1650
	jy2 = 850

	done = False
	checked_scores = False
	direction = "up"

	size = (0, 0)
	#size = (width, height)
	screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
	#screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	clock = pygame.time.Clock()
	pygame.init()

	pygame.display.set_caption("Space Ship Game")
	ship = pygame.image.load('ship.png')
	shipb = pygame.image.load('shipb.png')
	bug = pygame.image.load('bug.png')
	alien_b = pygame.image.load('bugb.png')
	star = pygame.image.load('star.png')
	rock1 = pygame.image.load('rock1.png')
	rock2 = pygame.image.load('rock2.png')
	spider = pygame.image.load('spider.png')
	scoreBoard = pygame.image.load('scoreBoard.png')
	exit_b = pygame.image.load('exit_b.png')
	exit_b2 = pygame.image.load('exit_b.png')
	play_b = pygame.image.load('play_b.png')
	settings_b = pygame.image.load('settings_b.png')
	easy_b = pygame.image.load('easy_b.png')
	medium_b = pygame.image.load('medium_b.png')
	hard_b = pygame.image.load('hard_b.png')
	extreme_b = pygame.image.load('extreme_b.png')
	insane_b = pygame.image.load('insane_b.png')
	pause_b = pygame.image.load('pause_b.png')
	back_b = pygame.image.load('back_b.png')
	menu_b = pygame.image.load('menu_b.png')
	music_b = pygame.image.load('music_b.png')
	joystick1 = pygame.image.load('joystick1.png')
	joystick2 = pygame.image.load('joystick2.png')
	hwidth = pygame.Surface.get_width(joystick1)
	hheight = pygame.Surface.get_height(joystick2)
	
	no_music_b = pygame.image.load('no_music_b.png')
	sound_b = pygame.image.load('sound_b.png')
	no_sound_b = pygame.image.load('no_sound_b.png')
	back_b2 = pygame.image.load('back_b2.png')

	h100 = pygame.image.load('h100.png')
	h95 = pygame.image.load('h95.png')
	h90 = pygame.image.load('h90.png')
	h85 = pygame.image.load('h85.png')
	h80 = pygame.image.load('h80.png')
	h70 = pygame.image.load('h70.png')
	h60 = pygame.image.load('h60.png')
	h50 = pygame.image.load('h50.png')
	h40 = pygame.image.load('h40.png')
	h30 = pygame.image.load('h30.png')
	h20 = pygame.image.load('h20.png')
	h10 = pygame.image.load('h10.png')
	h0 = pygame.image.load('h0.png')

	hwidth = pygame.Surface.get_width(h100)
	hheight = pygame.Surface.get_height(h100)

	h100 = pygame.transform.scale(h100, (hwidth+300, hheight+100))
	h95 = pygame.transform.scale(h95, (hwidth+300, hheight+100))
	h90 = pygame.transform.scale(h90, (hwidth+300, hheight+100))
	h85 = pygame.transform.scale(h85, (hwidth+300, hheight+100))
	h80 = pygame.transform.scale(h80, (hwidth+300, hheight+100))
	h70 = pygame.transform.scale(h70, (hwidth+300, hheight+100))
	h60 = pygame.transform.scale(h60, (hwidth+300, hheight+100))
	h50 = pygame.transform.scale(h50, (hwidth+300, hheight+100))
	h40 = pygame.transform.scale(h40, (hwidth+300, hheight+100))
	h30 = pygame.transform.scale(h30, (hwidth+300, hheight+100))
	h20 = pygame.transform.scale(h20, (hwidth+300, hheight+100))
	h10 = pygame.transform.scale(h10, (hwidth+300, hheight+100))
	h0 = pygame.transform.scale(h0, (hwidth+300, hheight+100))
	scoreBoard = pygame.transform.scale(scoreBoard, (hwidth+300, hheight+100))

	pixel1 = pygame.mixer.Sound('bossfight.wav')
	shoot_s = pygame.mixer.Sound('shoot2.wav')
	shoot2_s = pygame.mixer.Sound('shoot.wav')
	explosion = pygame.mixer.Sound('explosion.wav')
	damage = pygame.mixer.Sound('damage.wav')
	shoot2 = pygame.mixer.Sound('shoot.wav')
	menu = pygame.mixer.Sound('menu.wav')
	press = pygame.mixer.Sound('press.wav')

	width2 = 0.5 * play_b.get_rect().width
	height2 = 0.5 * play_b.get_rect().height
	width3 = 0.5 * easy_b.get_rect().width
	height3 = 0.5 * easy_b.get_rect().height

	p1_1 = (width/2-width2, height/2-height2 - 200)
	p1_2 = (width/2-width2, height/2-height2)
	p1_3 = (width/2-width2, height/2-height2 + 200)

	p2_1 = (width/2-width3, height/2-height3 - 300)
	p2_2 = (width/2-width3, height/2-height3 - 150)
	p2_3 = (width/2-width3, height/2-height3)
	centrep = height/2-height3
	p2_4 = (width/2-width3, height/2-height3 + 150)
	p2_5 = (width/2-width3, height/2-height3 + 300)

	size_b = play_b.get_rect().size
	size_b2 = easy_b.get_rect().size #same size as option buttons
	size_b3 = pause_b.get_rect().size
	size_b4 = back_b.get_rect().size

	p1 = pygame.Rect(p1_1, size_b)
	p2 = pygame.Rect(p1_2, size_b)
	p3 = pygame.Rect(p1_3, size_b)

	np1 = pygame.Rect(p2_1, size_b2)
	np2 = pygame.Rect(p2_2, size_b2)
	np3 = pygame.Rect(p2_3, size_b2)
	np4 = pygame.Rect(p2_4, size_b2)
	np5 = pygame.Rect(p2_5, size_b2)

	p = pygame.Rect((0, 0), size_b3)
	nnp1 = pygame.Rect((0, 0), size_b4)
	nnp2 = pygame.Rect((0, 200), size_b4)

	nnnp1 = pygame.Rect(p2_2, size_b2)
	nnnp2 = pygame.Rect(p2_3, size_b2)
	nnnp3 = pygame.Rect(p2_4, size_b2)

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	YELLOW = (236, 239, 55) 
	ORANGE = (255, 191, 1)
	BLUE = (0, 22, 255)

	centre(ship)

def get_high_score(txtfile):
	# Default high score
	thehigh_score = 0
 
	# Try to read the high score from a file
	try:
		high_score_file = open(txtfile, "r")
		thehigh_score = int(high_score_file.read())
		high_score_file.close()
		#print("The high score is", thehigh_score)
	except IOError:
		# Error reading file, no high score
		pass
		#print("There is no high score yet.")
	except ValueError:
		# There's a file there, but we don't understand the number.
		pass
		#print("I'm confused. Starting with no high score.")

	return thehigh_score
 
 
def save_high_score(txtfile):
	global score
	try:
		# Write the file to disk
		high_score_file = open(txtfile, "w")
		high_score_file.write(str(score))
		high_score_file.close()
	except IOError:
		# Hm, can't write it.
		pass
		#print("Unable to save the high score.")

# blits the image in the centre
def cblit(img):
	iwidth = 0.5 * img.get_rect().width
	iheight = 0.5 * img.get_rect().height
	posd = [width/2-iwidth, height/2-iheight]	
	screen.blit(img, posd)

# centres an image
def centre(img):
	global pos
	iwidth = 0.5 * img.get_rect().width
	iheight = 0.5 * img.get_rect().height
	pos = [width/2-iwidth, height/2-iheight]	

def ship_control(img):
	global xv, yv, direction, health, damage, score
	key = pygame.key.get_pressed()
	if key[pygame.K_DOWN]:
		direction = "down"
		yv += 1
	if key[pygame.K_UP]:
		direction = "up"
		yv -= 1
	if key[pygame.K_RIGHT]:
		direction = "right"
		xv += 1
	if key[pygame.K_LEFT]:
		direction = "left"
		xv -= 1
	pos[0] += xv
	pos[1] += yv
	pos2[0] += xv
	pos2[1] += yv
	xv = xv * 0.9
	yv = yv * 0.9

	loop2 = 0
	for alien in aliens:
		if alien[2] == "bug":
			posd = []
			posd.append(alien[0])
			posd.append(alien[1])
			size = pygame.Surface.get_size(bug) #find size of bug
			rect1 = pygame.Rect(posd, size) #find rect of bug
			size2 = pygame.Surface.get_size(ship) #find size of ship
			posd = []
			posd.append(pos[0]) #append x position
			posd.append(pos[1]) #append y position
			rect2 = pygame.Rect(posd, size2)
			if rect1.colliderect(rect2):
				health -= 0.5
				check_play(damage)
				#explosion.play()
		if alien[2] == "spider1" or alien[2] == "spider2":
			posd = []
			posd.append(alien[0])
			posd.append(alien[1])
			size = pygame.Surface.get_size(spider) #find size of bug
			rect1 = pygame.Rect(posd, size) #find rect of bug
			size2 = pygame.Surface.get_size(ship) #find size of ship
			posd = []
			posd.append(pos[0]) #append x position
			posd.append(pos[1]) #append y position
			rect2 = pygame.Rect(posd, size2)
			if rect1.colliderect(rect2):
				health -= 0.5
				check_play(damage)
		loop2 += 1

	loop2 = 0
	for bullet in bullets2:
		posd = []
		posd.append(bullet[0])
		posd.append(bullet[1])
		size = pygame.Surface.get_size(shipb) #find size of bullet
		rect1 = pygame.Rect(posd, size) #find rect of bullet
		size2 = pygame.Surface.get_size(ship) #find size of ship
		posd = []
		posd.append(pos[0]) #append x position
		posd.append(pos[1]) #append y position
		rect2 = pygame.Rect(posd, size2)
		if rect1.colliderect(rect2):
			health -= 0.5
			check_play(damage)
		loop2 += 1

	loop2 = 0
	for rock in rocks:
		posd = []
		posd.append(rock[0])
		posd.append(rock[1])
		size = pygame.Surface.get_size(rock1) #find size of rock
		rect1 = pygame.Rect(posd, size) #find rect of rock
		size2 = pygame.Surface.get_size(ship) #find size of ship
		posd = []
		posd.append(pos[0]) #append x position
		posd.append(pos[1]) #append y position
		rect2 = pygame.Rect(posd, size2)
		if rect1.colliderect(rect2):
			health -= 0.5
			check_play(explosion)
		loop2 += 1

	img = pygame.image.load('ship.png')
	if direction == "down":
		img = pygame.transform.rotate(img, 180)
	if direction == "right":
		img = pygame.transform.rotate(img, -90)
	if direction == "left":
		img = pygame.transform.rotate(img, 90)
	return img

#this adds the stars to the stars list
def star_render():
	global star, stars
	stars = []
	for x in range(0, 100):
		xv = random.randint(0, 1900)
		yv = random.randint(0, 1000)
		stars.append([xv, yv])

#this draws the stars and moves it back
def draw_stars():
	global star, stars, speed
	speed += 0.005
	loop = 0
	for pos in stars:
		screen.blit(star, pos)
		stars[loop][1] += speed
		if stars[loop][1] >= 1000:
			stars[loop][1] = 0
		loop += 1
# this adds a bullet in the list bullets
def shoot(pos2):
	global shipb #ship bullet
	global bullets
	pos3 = []
	pos3.append(pos2[0])
	pos3.append(pos2[1])
	bullets.append([pos3, direction])

def move_bullets():
	global shipb
	global bullets, pos2, pos, rocks, rock1, alien, score
	loop = 0
	for bullet in bullets:
		bullet2 = []
		bullet2.append(bullet[0][0])
		bullet2.append(bullet[0][1])

		img2 = pygame.image.load('shipb.png')
		if bullet[1] == "up":
			bullets[loop][0][1] -= 15
		if bullet[1] == "down":
			bullets[loop][0][1] += 15
		if bullet[1] == "left":
			bullets[loop][0][0] -= 15
			img2 = pygame.transform.rotate(img2, 90)
		if bullet[1] == "right":
			bullets[loop][0][0] += 15
			img2 = pygame.transform.rotate(img2, -90)

		screen.blit(img2, bullet2)

		loop2 = 0
		for rock in rocks:
			posd = []
			posd.append(rock[0])
			posd.append(rock[1])
			size = pygame.Surface.get_size(rock1) #find size of rock
			rect1 = pygame.Rect(posd, size) #find rect of rock
			size2 = pygame.Surface.get_size(shipb) #find size of ship bullet
			posd = []
			posd.append(bullet[0][0]) #append x position
			posd.append(bullet[0][1]) #append y position
			rect2 = pygame.Rect(posd, size2)
			if rect1.colliderect(rect2):
				rocks[loop2][2] -= 1
			loop2 += 1

		loop2 = 0
		for alien in aliens:
			if alien[2] == "bug":
				posd = []
				posd.append(alien[0])
				posd.append(alien[1])
				size = pygame.Surface.get_size(bug) #find size of bug
				rect1 = pygame.Rect(posd, size) #find rect of bug
				size2 = pygame.Surface.get_size(shipb) #find size of ship bullet
				posd = []
				posd.append(bullet[0][0]) #append x position
				posd.append(bullet[0][1]) #append y position
				rect2 = pygame.Rect(posd, size2)
				if rect1.colliderect(rect2):
					score += 100
					aliens.pop(loop2)
					check_play(explosion)
				loop2 += 1

			if alien[2] == "spider1" or alien[2] == "spider2":
				posd = []
				posd.append(alien[0])
				posd.append(alien[1])
				size = pygame.Surface.get_size(spider) #find size of bug
				rect1 = pygame.Rect(posd, size) #find rect of bug
				size2 = pygame.Surface.get_size(shipb) #find size of ship bullet
				posd = []
				posd.append(bullet[0][0]) #append x position
				posd.append(bullet[0][1]) #append y position
				rect2 = pygame.Rect(posd, size2)
				if rect1.colliderect(rect2):
					score += 500
					aliens.pop(loop2)
					check_play(explosion)
				loop2 += 1

		if bullet[0][1] < 0:
			bullets.remove(bullet)
		if bullet[0][0] < 0:
			bullets.remove(bullet)
		if bullet[0][0] > 1900:
			bullets.remove(bullet)
		if bullet[0][1] > 1000:
			bullets.remove(bullet)
		loop += 1

def rock_render():
	global rocks
	loop = 0
	chance = random.randint(1, 20)
	if chance == 5:
		x = random.randint(0, 1900)
		y = 0
		rocks.append([x, y, 2])

def draw_rock():
	global rock1, rock2, rocks, speed
	try:
		loop = 0
		for rock in rocks:
			rocks[loop][1] += speed * 2
			if rocks[loop][1] >= 1000:
				rocks.pop(loop)
			if rocks[loop][2] == 2:
				posd = []
				posd.append(rocks[loop][0])
				posd.append(rocks[loop][1])
				screen.blit(rock1, posd)
			if rocks[loop][2] == 1:
				posd = []
				posd.append(rocks[loop][0])
				posd.append(rocks[loop][1])
				screen.blit(rock2, posd)
			if rocks[loop][2] <= 0:
				rocks.pop(loop)
			loop += 1
	except:
		pass

def bug_render():
	global aliens, chance1
	chance = random.randint(1, chance1)
	if chance == 5:
		x = random.randint(0, 1700)
		y = 200
		aliens.append([x, y, "bug"])

def draw_bug():
	global aliens, pos
	try:
		xv = round(pos[0], 0)
		yv = round(pos[1], 0)
		loop = 0
		for alien in aliens:
			if alien[2] == "bug":
				xv2 = alien[0]
				yv2 = alien[1]
				if xv < xv2:
					aliens[loop][0] -= 5
				if xv > xv2:
					aliens[loop][0] += 5
				if yv < yv2:
					aliens[loop][1] -= 5
				if yv > yv2:
					aliens[loop][1] += 5
				screen.blit(bug, (xv2, yv2))
			loop += 1
	except:
		pass

def draw_hp():
	global health, h100, h95, h90, h85, h80, h70, h60, h50, h40, h30, h20, h10, h0
	width2 = 0.5 * pygame.Surface.get_width(h100)

	if health > 95:
		screen.blit(h100, (width/2 - width2, 900))
	elif health > 90:
		screen.blit(h95, (width/2 - width2, 900))
	elif health > 85:
		screen.blit(h90, (width/2 - width2, 900))
	elif health > 80:
		screen.blit(h85, (width/2 - width2, 900))
	elif health > 70:
		screen.blit(h80, (width/2 - width2, 900))
	elif health > 60:
		screen.blit(h70, (width/2 - width2, 900))
	elif health > 50:
		screen.blit(h60, (width/2 - width2, 900))
	elif health > 40:
		screen.blit(h50, (width/2 - width2, 900))
	elif health > 30:
		screen.blit(h40, (width/2 - width2, 900))
	elif health > 20:
		screen.blit(h30, (width/2 - width2, 900))
	elif health > 10:
		screen.blit(h20, (width/2 - width2, 900))
	elif health > 0:
		screen.blit(h10, (width/2 - width2, 900))
	elif health <= 0:
		screen.blit(h0, (width/2 - width2, 900))

def spider_render():
	global aliens, chance2
	chance = random.randint(1, chance2)
	stype = random.randint(1, 3)
	if chance == 5:
			if stype == 1:
				x = random.randint(100, 1700)
				y = 800
				aliens.append([x, y, "spider1"])
			if stype == 2:
				x = random.randint(100, 1700)
				y = 100
				aliens.append([x, y, "spider2"])

def draw_spider():
	global aliens, pos, bullets2
	move_bullets2()
	try:
		#xv = round(pos[0], 1)
		#yv = round(pos[1], 1)
		xv = (pos[0])
		yv = (pos[1])
		loop = 0
		for alien in aliens:
			if alien[2] == "spider1" or alien[2] == "spider2":
				xv2 = alien[0]
				yv2 = alien[1]
				if xv == xv2:
					pass
				if yv == yv2:
					pass
				elif xv < xv2:
					aliens[loop][0] -= 5
				elif xv > xv2:
					aliens[loop][0] += 5

				if alien[2] == "spider1" :
					chance = random.randint(1, 10)
					screen.blit(spider, (xv2, yv2))
					if chance == 5:
						check_play(shoot2)
						posd = []
						posd.append(xv2)
						posd.append(yv2)
						bullets2.append([xv2 + 50, yv2, "up"])
				if alien[2] == "spider2" :
					img = pygame.transform.rotate(spider, 180)
					chance = random.randint(1, 10)
					if chance == 5:
						check_play(shoot2)
						posd = []
						posd.append(xv2)
						posd.append(yv2)
						bullets2.append([xv2 + 50, yv2, "down"])
					screen.blit(img, (xv2, yv2))

			loop += 1

	except:
		pass

def move_bullets2():
	global bullets2
	loop = 0
	for bullet in bullets2:
		if bullet[2] == "up":
			bullets2[loop][1] -= 20
		else:
			bullets2[loop][1] += 20
		posd = []
		posd.append(bullet[0])
		posd.append(bullet[1])
		screen.blit(alien_b, posd)
		if bullet[1] < 0:
			bullets2.pop(loop)
		loop += 1

def score_board():
	global scoreBoard, score
	score2 = str(score)
	width2 = 0.5 * pygame.Surface.get_width(scoreBoard)
	screen.blit(scoreBoard, (width/2 - width2, 0))

	font = pygame.font.SysFont('aharoni', 50, True, False)
	text = font.render(score2, True, BLUE)
	width2 = 0.5 * text.get_rect().width
	screen.blit(text, (width/2 - width2, 30))

def stop_play(stop, play):
	stop.stop()

def play(music):
	global music_bool
	if music_bool == True:
		if not pygame.mixer.get_busy():
			music.play()
	else:
		music.stop()

def check_play(sound):
	global sound_bool
	if sound_bool == True:
		sound.play()

initialize()

"""                 game loop                  """

#pixel1.stop()
#menu.play()
while not done:


	if place == "menu":
		play(menu)
		fps = 1000
		screen.fill(BLACK)
		draw_stars()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if p1.collidepoint(position):
					place = "menu2"
					check_play(press)
				if p2.collidepoint(position):
					check_play(press)
					place = "settings"
				if p3.collidepoint(position):
					check_play(press)
					done = True
		screen.blit(play_b, p1_1)
		screen.blit(settings_b, p1_2)
		screen.blit(exit_b, p1_3)

	elif place == "menu2":
		play(menu)
		fps = 1000
		screen.fill(BLACK)
		draw_stars()
		play(menu)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if np1.collidepoint(position):
					check_play(press)
					stop_play(menu, pixel1)
					initialize()
					chance1 = 150
					chance2 = 300
					place = "game"
					mode = "easy"
					score = 0
				if np2.collidepoint(position):
					check_play(press)
					stop_play(menu, pixel1)
					initialize()
					chance1 = 100
					chance2 = 200
					place = "game"
					mode = "medium"
					score = 0
				if np3.collidepoint(position):
					check_play(press)
					stop_play(menu, pixel1)
					initialize()
					chance1 = 50
					place = "game"
					chance2 = 100
					mode = "hard"
					score = 0
				if np4.collidepoint(position):
					check_play(press)
					stop_play(menu, pixel1)
					initialize()
					chance1 = 30
					chance2 = 70
					place = "game"
					mode = "extreme"
					score = 0
				if np5.collidepoint(position):
					check_play(press)
					stop_play(menu, pixel1)
					initialize()
					chance1 = 20
					chance2 = 50
					place = "game"
					mode = "insane"
					score = 0
					

		screen.blit(easy_b, p2_1)
		screen.blit(medium_b, p2_2)
		screen.blit(hard_b, p2_3)
		screen.blit(extreme_b, p2_4)
		screen.blit(insane_b, p2_5)

	elif place == "settings":
		screen.fill(BLACK)
		draw_stars()
		play(menu)
		fps = 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if nnnp1.collidepoint(position):
					check_play(press)
					if sound_bool == True:
						sound_bool = False
					else:
						sound_bool = True
				if nnnp2.collidepoint(position):
					check_play(press)
					if music_bool == True:
						music_bool = False
					else:
						music_bool = True
				if nnnp3.collidepoint(position):
					check_play(press)
					place = "menu"

		if sound_bool == True:
			screen.blit(sound_b, p2_2)
		else:
			screen.blit(no_sound_b, p2_2)
		if music_bool == True:
			screen.blit(music_b, p2_3)
		else:
			screen.blit(no_music_b, p2_3)
		screen.blit(back_b2, p2_4)

	elif place == "pause":
		pixel1.stop()
		fps = 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if nnp1.collidepoint(position):
					check_play(press)
					place = "game"
				if nnp2.collidepoint(position):
					check_play(press)
					place = "menu"
		screen.blit(back_b, (0, 0))
		screen.blit(menu_b, (0, 200))


	elif place == "scores":
		screen.fill(BLACK)
		fps = 1000
		draw_stars()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if npos.collidepoint(position):
					check_play(press)
					place = "menu"

		if checked_scores == False:
			if mode == "easy":
				high_score = get_high_score("easy_score.txt")
				checked_scores = high_score
				if score > high_score:
					save_high_score("easy_score.txt")

			if mode == "medium":
				high_score = get_high_score("medium_score.txt")
				checked_scores = high_score
				if score > high_score:
					save_high_score("medium_score.txt")

			if mode == "hard":
				high_score = get_high_score("hard_score.txt")
				checked_scores = high_score
				if score > high_score:
					save_high_score("hard_score.txt")

			if mode == "extreme":
				high_score = get_high_score("extreme_score.txt")
				checked_scores = high_score
				if score > high_score:
					save_high_score("extreme_score.txt")

			if mode == "insane":
				high_score = get_high_score("insane_score.txt")
				checked_scores = high_score
				if score > high_score:
					save_high_score("insane_score.txt")

		if score > checked_scores:
			font = pygame.font.SysFont('aharoni', 100, True, False)
			text = font.render("Congratulations!", True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep-200))

			text = font.render("YOU BEAT THE HIGH SCORE!", True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep-100))

			text = font.render("OLD HIGH SCORE: %i" % (checked_scores), True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep))

			text = font.render("NEW HIGH SCORE: %i" % (score), True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep+100))

		else:
			font = pygame.font.SysFont('aharoni', 100, True, False)
			text = font.render("WELL PLAYED!", True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep-100))

			text = font.render("HIGH SCORE: %i" % (checked_scores), True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep))

			text = font.render("SCORE: %i" % (score), True, BLUE)
			width2 = 0.5 * text.get_rect().width
			screen.blit(text, (width/2 - width2, centrep+100))

		width2 = 0.5 * menu_b.get_rect().width
		npos = pygame.Rect((width/2 - width2, centrep+300), size_b)
		screen.blit(menu_b, (width/2 - width2, centrep+300))

	elif place == "game":
		size_j1 = joystick1.get_rect().size
		j1_r = pygame.Rect((jx1, jy1), size_j1) 
		size_j2 = joystick2.get_rect().size
		j2_r = pygame.Rect((jx2, jy2), size_j2) 
		play(pixel1)
		fps = 20

		screen.fill(BLACK)
		score+= 1
		if score % 100 == 0:
			if not chance1 == 5:
				chance1 -= 1
			if not chance2 == 10:
				chance2 -= 1

		if health <= 0:
			place = "scores"
			pixel1.stop()
			initialize()
		#draw and move stars
		draw_stars()
		#render and draw rocks
		rock_render()
		draw_rock()
		#draw and move bullets
		move_bullets()
		#render bug
		bug_render()
		draw_bug()
		#control the ship
		ship = ship_control(ship)
		screen.blit(ship, pos)
		#render and draw spiders
		spider_render()
		draw_spider()
		#draw hp bars
		draw_hp()
		#score_board
		score_board()

	
		widthj = joystick1.get_rect().width
		heightj = joystick1.get_rect().width
		# check event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				drag = True
				position = pygame.mouse.get_pos()
				if p.collidepoint(position):
					check_play(press)
					place = "pause"
			elif event.type == pygame.MOUSEBUTTONUP:
				drag = False

			elif event.type == pygame.MOUSEMOTION:
				if drag:
					x_dist = 1650
					y_dist = 850
					mouse_x, mouse_y = event.pos
					if mouse_x-50 < jx1-100: #if joystick is on the right
						x_change = -70
						if mouse_x-350 > jx1-100: #if joystick is on the left
							x_change = 70
							if mouse_y-350 < jy1-100: #if joystick is down
								y_change = -300
								if mouse_y-350 > jy1-100: #if joystick is up
									y_change = 70

					if not mouse_x-50 < jx1-100 and not mouse_x-350 > jx1-100 and not mouse_y+50 < jy1 and not mouse_y-350 > jy1-100:
						jx2 = mouse_x - 50
						jy2 = mouse_y - 50
						x_change = (x_dist-mouse_x + 40) * -1
						y_change = (y_dist-mouse_y + 40) * -1

					try:
						print (x_change, y_change)
						pos[0] += x_change / 10
						pos[1] += y_change / 10
						pos2[0] += x_change / 10
						pos2[1] += y_change / 10

						if x_change/5 > 0:
							direction = "right"
						if x_change/5 < 0:
							direction = "left"
						if y_change > 50:
							direction = "down"
						if y_change < -50:
							direction = "up"

						img = pygame.image.load('ship.png')
						if direction == "down":
							img = pygame.transform.rotate(img, 180)
						if direction == "right":
							img = pygame.transform.rotate(img, -90)
						if direction == "left":
							img = pygame.transform.rotate(img, 90)

					except:
						pass

									#cblit(img)
				else:
					jx2 = 1650
					jy2 = 850

			#if some key is pressed
			if event.type == pygame.KEYDOWN:
				#if the key pressed is space
				if event.key == pygame.K_SPACE:
					check_play(shoot_s)
					pos2.append(direction)
					shoot(pos2)
					pos2.remove(direction)

		screen.blit(joystick1, (jx1, jy1))
		screen.blit(joystick2, (jx2, jy2))

		screen.blit(pause_b, (0,0))
	
	clock.tick(fps)
	pygame.display.update()


import pygame

import random

import sys

pygame.init()

# creating a screen

width = 850

length = 600

#color
background_color = (0, 0, 0)
red = (255, 0, 4)
blue = (12, 108, 242)
yellow = (255, 255, 0)
green = (0, 255, 0)
white = (255, 255, 255)

rect_size = 50

#player

player_pos = [(width - rect_size) / 2, (length - 2 * rect_size)]

#enemy

enemy_pos = [random.randint(0, width - rect_size), 0]
speed = 10
enemy_list = []

screen = pygame.display.set_mode((width, length))

game_over = False

clock = pygame.time.Clock()

score = 0
myfont = pygame.font.SysFont("monospace", 35, bold=False, italic=True, constructor = None)

def create_enemy(enemy_list):

	delay = random.random()
	if(len(enemy_list) < 10) and delay < 0.1:
		x_pos = random.randint(0, width - rect_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def update_enemy(enemy_list,score,speed):
	i = 0
	for enemy_pos in enemy_list:
		if enemy_pos[1] >= 0 and enemy_pos[1] <= length:
			enemy_pos[1] += speed
		else:
			enemy_list.pop(i)
			score  = score + 1
		i = i + 1
	return score

def draw_enemy(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, blue, (enemy_pos[0], enemy_pos[1] , rect_size, rect_size))

def detect_collision(player_pos,enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + rect_size)) or (p_x >= e_x and p_x <= (e_x + rect_size)):
		if (e_y >= p_y and e_y < (p_y + rect_size)) or (p_y >= e_y and p_y < (e_y + rect_size)):
			return True
	return False 

def collision_checker(player_pos, enemy_list):
	for enemy_pos in enemy_list:
		if detect_collision(player_pos, enemy_pos):
			return True
	return False

def level(score, speed):
	if score < 20:
		speed = 5
	elif score < 40:
		speed = 10
	elif score < 60:
		speed = 15
	else:
		speed = 20
	return speed


while not game_over:
	for event in pygame.event.get():
		
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type in (pygame.KEYDOWN, pygame.KEYUP):
			key = pygame.key.name(event.key)
			x = player_pos[0]
			y = player_pos[1]

			if event.type == pygame.KEYDOWN:

				if key == "left":
					x = x - rect_size
				elif key == "right":
					x = x + rect_size

			if x >= 0 and x <= (width-rect_size):
				player_pos = [x, y]
		
	screen.fill(background_color)

	create_enemy(enemy_list)

	score = update_enemy(enemy_list, score,speed)

	text = "Score " + str(score)
	label = myfont.render(text,1,yellow)
	screen.blit(label, (width-200,length-80))

	speed = level(score, speed)

	if collision_checker(player_pos,enemy_list):
		game_over = True
		break

	draw_enemy(enemy_list)
	
	pygame.draw.rect(screen, red, (player_pos[0], player_pos[1] , rect_size, rect_size))

	clock.tick(30)
	
	pygame.display.update()	

exit = False

# result screen
while not exit:
	screen.fill(background_color)
	for event in pygame.event.get():
		if event.type ==  pygame.QUIT:
			sys.exit()

	text = "GAME OVER"
	label = myfont.render(text,1,green)
	screen.blit(label,(width-540,length-380))

	text = "SCORE: " + str(score)
	label = myfont.render(text,1,yellow)
	screen.blit(label, (width-530,length-340))

	text = "Press Enter to Exit"
	label = myfont.render(text,1,white)
	screen.blit(label,(width-620,length-300))

	pygame.display.update()
	
	if event.type in (pygame.KEYDOWN, pygame.KEYUP):
		key = pygame.key.name(event.key)
	if event.type == pygame.KEYDOWN:
		if key=="return":
			sys.exit()



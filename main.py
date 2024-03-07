import pygame
import math
import random
from constants import WHITE,BLACK,BLUE
from words import words
import sys 

#functions
def draw_mainscreen():
	win.fill(WHITE)

	#title 
	text = TITLE_FONT.render("Hangman",1,BLACK)
	win.blit(text,(WIDTH/2 - text.get_width()/2,20))

	#draw word 
	display_word =""
	for letter in word:
		if letter in guessend:
			display_word += letter + " "
		else:
			display_word += "_ "
	text = MIDDEL_FONT.render(display_word,1,BLACK)
	win.blit(text,(400,200))



	#draw buttons
	for letter in letters:
		x, y, ltr, visable = letter
		if visable:
			pygame.draw.circle(win,BLACK,(x,y), RADIUS,3)
			text = LETTER_FONT.render(ltr,1, BLACK)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

	win.blit(hangman_images[hangman_status],(150,100))
	pygame.display.update()


def draw_homescreen(): #drawing the homescreen
		win.fill(WHITE)
		text = TITLE_FONT.render("Hangman",1,BLACK)
		win.blit(text,(WIDTH/2 - text.get_width()/2, 20))

		xx = WIDTH/2 - game_gui.get_width()/2
		yy = HEIGHT/2 - game_gui.get_height()/2
		rect_width = game_gui.get_width()
		rect_height = game_gui.get_height()
		pygame.draw.rect(win,WHITE,(xx,yy,rect_width,rect_height))

		win.blit(game_gui,(WIDTH/2 - game_gui.get_width()/2, HEIGHT/2 - game_gui.get_height()/2))
		pygame.display.update()
	
def homescreen(): #running the homescreen
	FPS = 60 
	clock = pygame.time.Clock()
	run = True 
	clock.tick(FPS)
	while run:
		draw_homescreen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				xx = WIDTH/2 - game_gui.get_width()/2
				yy = HEIGHT/2 - game_gui.get_height()/2
				if m_x >=  xx and m_x <= xx + game_gui.get_width() and m_y >= yy and m_y <= yy + game_gui.get_height():
					main()
			

def display_message(message): #display win or lose
		pygame.time.delay(1000)
		win.fill(WHITE)
		text = MIDDEL_FONT.render(message,1, BLACK)
		win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
		pygame.display.update()
		pygame.time.delay(3000)

def main():
#variables
	global hangman_status
	FPS = 60 
	clock = pygame.time.Clock()
	run = True 
#running the game 
	while run: 
		clock.tick(FPS)

		draw_mainscreen() #drawing the game/main screen

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				for letter in letters:
					x,y,ltr, visable = letter
					if visable:
						dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessend.append(ltr)
							if ltr not in word:
								hangman_status += 1

		won = True
		for letter in word:
			if letter not in guessend:
				won = False
				break

		if won:
			display_message("You won!")	
			break			

		if hangman_status == 6:
			display_message("You lost... :-( The word was")
			break


#set up display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40)
MIDDEL_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicans',70)


#button variables 
RADIUS = 20
GAP = 15
letters = []
A = 65
startx = round((WIDTH - (RADIUS*2 + GAP) * 13)/2)
starty = 400
for i in range(26):
	x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
	y = starty + ((i// 13) *(GAP + RADIUS * 2 ))
	letters.append([x,y, chr(A + i), True])


#load images
hangman_images = []
for i in range(7):
	hangman_image = pygame.image.load("images/hangman" + str(i) + ".png")
	hangman_images.append(hangman_image)
game_gui = pygame.image.load("images/game_gui/play.png")


#game variables
hangman_status = 0 
word = random.choice(words)
guessend =[]
	

while True:
	FPS = 60 
	clock = pygame.time.Clock()
	run = True 
	clock.tick(FPS)
	while run:
		draw_homescreen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				xx = WIDTH/2 - game_gui.get_width()/2
				yy = HEIGHT/2 - game_gui.get_height()/2
				if m_x >=  xx and m_x <= xx + game_gui.get_width() and m_y >= yy and m_y <= yy + game_gui.get_height():
					main()	
	break
		
pygame.quit()


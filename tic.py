import pygame
from game_logic import *
#Classes and functions

def clip(Rect):
	print(type(Rect))
	return pygame.Rect.clip(Rect)

class Block(pygame.Rect):
	def __int__(self):
		return self.value

	def __init__(self, top, left):
		self.h, self.w = height/div, width/div
		super().__init__((top, left), (self.h, self.w))
		self.value = 0
		self.top = top
		self.left = left

		# self.draw()
		# self.draw_x()
	def draw_o(self):
		centre = (self.top + int(self.h/2), self.left + int(self.h/2))
		pygame.draw.circle(screen, BLACK, centre, int(self.h/2)-7)
		pygame.draw.circle(screen, WHITE, centre, int(self.h/2)-10)


	def draw_x(self): 
		padding = 20
		top_left = (self.top + padding, self.left + padding)
		top_right = (self.top + padding, self.left + self.w - padding)
		bottom_right = (self.top + self.h - padding, self.left + self.w - padding)
		bottom_left = (self.top + self.h - padding , self.left + padding) 

		pygame.draw.line(screen, BLACK, top_right, bottom_left, 5)
		pygame.draw.line(screen, BLACK, top_left, bottom_right, 5)

	def draw(self):
		#create a new temporary rect so that it does not interfere with the original  
		temp_rect = self.copy()		
		temp_rect.inflate_ip(1,1)

		pygame.draw.rect(screen, BLACK, temp_rect)

		temp_rect.inflate_ip(-5,-5)

		pygame.draw.rect(screen, WHITE, temp_rect)	
		pygame.display.flip()

#SETUP

pygame.init()

width, height = 500 , 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')

#DISPLAY/FRONT-END
BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pygame.Surface((width,height))
screen.fill(WHITE)
win.blit(screen, (0,0))

div = 3

unit = width/div

def update_screen():
	win.blit(screen, (0,0))
	pygame.display.flip()

def create_game_blocks():
	blocks = []
	for i in range(div):
		top = unit * i
		left = 0
		for j in range(div):
			left = unit * j
			my_block = Block(top,left)
			print(i,j)
			my_block.draw()
			blocks.append(my_block)

	return blocks

def reset_board():
	default = [
	[0,0,0],
	[0,0,0],
	[0,0,0]
	]
	return default

block_list = create_game_blocks()
update_screen()

Game = Board(reset_board())
print(Game)

#LOGIC/BACK-END
turn = True
run = True
while run:

	for event in pygame.event.get():
		#Check to quit
		if event.type == pygame.QUIT:
			run = False
		#Place movement
		if event.type == pygame.MOUSEBUTTONUP:

			pos = pygame.mouse.get_pos()
			y,x = pos
			pos = x,y
			 
			for block in block_list:

				if block.collidepoint(pos):

					y,x = (round(block.top/unit), round(block.left/unit))
					if turn:
						block.draw_x()
						player = 1
					else:
						block.draw_o()
						player = 2
					
					Game.move(player, x,y)
					winner = Game.check_winners()

					if winner:
						print(f'Congratuluations player {winner} has won')
						run = False

					turn = not(turn)
	update_screen()

pygame.quit()
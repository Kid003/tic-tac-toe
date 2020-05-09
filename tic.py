import pygame

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
		pygame.draw.circle(screen, BLACK, centre, int(self.h/2))
		pygame.draw.circle(screen, WHITE, centre, int(self.h/2)-5)


	def draw_x(self): 
		top_right = (self.top, self.left)
		top_left = (self.top, self.left + self.w)
		bottom_right = (self.top + self.h, self.left)
		bottom_left = (self.top + self.h, self.left + self.w) 

		pygame.draw.line(screen, BLACK, top_right, bottom_left, 3)
		pygame.draw.line(screen, BLACK, top_left, bottom_right, 3)

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
game = []

def print_board(game):
	for row in game:
		print([int(item) for item in row])

def update_screen():
	win.blit(screen, (0,0))
	pygame.display.flip()

def create_game():
	board = []
	for i in range(div):
		board.append([])
		top = unit * i
		left = 0
		for j in range(div):
			left = unit * j
			my_block = Block(top,left)
			my_block.draw()
			# my_block.draw_o()
			board[i].append(my_block)

	return board

game = create_game()
print_board(game)
update_screen()

#LOGIC/BACK-END
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			y,x = pos
			pos = x,y 
			for row in game:
				for block in row:
					if block.collidepoint(pos):
						block.draw_x()

	update_screen()
pygame.quit()
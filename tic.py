import pygame

#Classes and functions

def clip(Rect):
	print(type(Rect))
	return pygame.Rect.clip(Rect)

class Block:
	def __int__(self):
		return self.value

	def __init__(self, top, left):
		self.value = 0
		self.top = top
		self.left = left
		self.color = (0,0,0)
		self.Rect = pygame.Rect((self.top, self.left), (width/div, height/div))

	def inflate(self):
		self.Rect.inflate_ip(-3,-3)

	def draw(self):
		pygame.draw.rect(screen, BLACK, self.Rect)
		self.inflate()
		pygame.draw.rect(screen, WHITE, self.Rect)	
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

def create_game():
	board = []
	for i in range(div):
		board.append([])
		top = unit * i
		for j in range(div):
			left = unit * j
			my_block = Block(top,left)
			my_block.draw()
			board[i].append(my_block)

	return board

game = create_game()
print_board(game)

win.blit(screen, (0,0))
pygame.display.flip()

#LOGIC/BACK-END
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
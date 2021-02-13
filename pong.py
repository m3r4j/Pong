import pygame # Main module which displays the gui and functionality
import tkinter 
from tkinter import messagebox # Used for the messageboxes and needs tkinter to show it
import random # Randomly generates where the ball will be

# Check if it can initialize
pygame.init()

# RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255) # This is only for easier use for looking at the ball, its not actually used in the game

score_to_win = 11 # The amount needed to win

width, height = 800, 400 # Width and height

win = pygame.display.set_mode((width, height)) # The main window

pygame.display.set_caption('Pong') # The title of the game

gameIcon = pygame.image.load('icons/icon.ico') # Get the game icon
pygame.display.set_icon(gameIcon) # Set the game icon


# A function to handle the left paddle
def handle_racket_left(keys, racket_left):
	global racket_left_y

	# If the user presses W then go up
	if keys[pygame.K_w] and racket_left.y > 10:
		racket_left_y -= vel

	# If the user presses S then go down
	if keys[pygame.K_s] and racket_left.y <= 335:
		racket_left_y += vel



def handle_racket_right(keys, racket_right):
	global racket_right_y

	# If the user presses W then go up
	if keys[pygame.K_UP] and racket_right.y > 10:
		racket_right_y -= vel

	# If the user presses S then go down
	if keys[pygame.K_DOWN] and racket_right.y <= 335:
		racket_right_y += vel


# The sounds class
class sounds:
	# Initializes mixer
	pygame.mixer.init()

	# Paddle sound, when the ball hits the paddle
	def paddle():
		pygame.mixer.music.load('sounds/paddle.mp3')
		pygame.mixer.music.play()

	# Wall sound, when the ball hits the wall
	def wall():
		pygame.mixer.music.load('sounds/wall.mp3')
		pygame.mixer.music.play()

	# Score sound, when right or left scores a point make this sound
	def score():
		pygame.mixer.music.load('sounds/score.mp3')
		pygame.mixer.music.play()




# This is the class for all the numbers that get displayed on the left side
class l:
	def zero():
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (250, 20, 6, 50))
		pygame.draw.rect(win, white, (250, 70, 40, 6))
		pygame.draw.rect(win, white, (284, 20, 6, 50))

	def one():
		pygame.draw.rect(win, white, (250, 20, 6, 50))

	def two():
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (284, 20, 6, 35))
		pygame.draw.rect(win, white, (250, 50, 40, 6))
		pygame.draw.rect(win, white, (250, 50, 6, 35))
		pygame.draw.rect(win, white, (250, 80, 40, 6))

	def three():
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (284, 20, 6, 35))
		pygame.draw.rect(win, white, (250, 50, 40, 6))
		pygame.draw.rect(win, white, (284, 50, 6, 35))
		pygame.draw.rect(win, white, (250, 80, 40, 6))

	def four():
		pygame.draw.rect(win, white, (250, 20, 6, 35))
		pygame.draw.rect(win, white, (250, 50, 40, 6))
		pygame.draw.rect(win, white, (284, 20, 6, 60))

	def five():
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (250, 20, 6, 35))
		pygame.draw.rect(win, white, (250, 50, 40, 6))
		pygame.draw.rect(win, white, (284, 50, 6, 35))
		pygame.draw.rect(win, white, (250, 80, 40, 6))


	def six():
		pygame.draw.rect(win, white, (250, 20, 6, 60))
		pygame.draw.rect(win, white, (250, 80, 40, 6))
		pygame.draw.rect(win, white, (284, 50, 6, 35))
		pygame.draw.rect(win, white, (250, 50, 40, 6))

	def seven():
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (284, 20, 6, 60))

	def eight():
		pygame.draw.rect(win, white, (250, 20, 6, 70))
		pygame.draw.rect(win, white, (284, 20, 6, 70))
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (250, 85, 40, 6))
		pygame.draw.rect(win, white, (250, 53, 40, 6))

	def nine():
		pygame.draw.rect(win, white, (250, 20, 40, 6))
		pygame.draw.rect(win, white, (250, 20, 6, 35))
		pygame.draw.rect(win, white, (284, 20, 6, 35))
		pygame.draw.rect(win, white, (250, 50, 40, 6))
		pygame.draw.rect(win, white, (284, 50, 6, 35))


	def ten():
		l.one()
		pygame.draw.rect(win, white, (284, 20, 40, 6))
		pygame.draw.rect(win, white, (284, 20, 6, 50))
		pygame.draw.rect(win, white, (284, 65, 40, 6))
		pygame.draw.rect(win, white, (318, 20, 6, 50))

	def eleven():
		l.one()
		pygame.draw.rect(win, white, (284, 20, 6, 50))

# This is the class for all the numbers that get displayed on the right side
class r:
	def zero():
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (510, 20, 6, 50))
		pygame.draw.rect(win, white, (510, 70, 40, 6))
		pygame.draw.rect(win, white, (544, 20, 6, 50))

	def one():
		pygame.draw.rect(win, white, (510, 20, 6, 50))

	def two():
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (544, 20, 6, 35))
		pygame.draw.rect(win, white, (510, 50, 40, 6))
		pygame.draw.rect(win, white, (510, 50, 6, 35))
		pygame.draw.rect(win, white, (510, 80, 40, 6))

	def three():
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (544, 20, 6, 35))
		pygame.draw.rect(win, white, (510, 50, 40, 6))
		pygame.draw.rect(win, white, (544, 50, 6, 35))
		pygame.draw.rect(win, white, (510, 80, 40, 6))

	def four():
		pygame.draw.rect(win, white, (510, 20, 6, 35))
		pygame.draw.rect(win, white, (510, 50, 40, 6))
		pygame.draw.rect(win, white, (544, 20, 6, 60))

	def five():
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (510, 20, 6, 35))
		pygame.draw.rect(win, white, (510, 50, 40, 6))
		pygame.draw.rect(win, white, (544, 50, 6, 35))
		pygame.draw.rect(win, white, (510, 80, 40, 6))


	def six():
		pygame.draw.rect(win, white, (510, 20, 6, 60))
		pygame.draw.rect(win, white, (510, 80, 40, 6))
		pygame.draw.rect(win, white, (544, 50, 6, 35))
		pygame.draw.rect(win, white, (510, 50, 40, 6))

	def seven():
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (544, 20, 6, 60))

	def eight():
		pygame.draw.rect(win, white, (510, 20, 6, 70))
		pygame.draw.rect(win, white, (544, 20, 6, 70))
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (510, 85, 40, 6))
		pygame.draw.rect(win, white, (510, 53, 40, 6))

	def nine():
		pygame.draw.rect(win, white, (510, 20, 40, 6))
		pygame.draw.rect(win, white, (510, 20, 6, 35))
		pygame.draw.rect(win, white, (544, 20, 6, 35))
		pygame.draw.rect(win, white, (510, 50, 40, 6))
		pygame.draw.rect(win, white, (544, 50, 6, 35))


	def ten():
		r.one()
		pygame.draw.rect(win, white, (544, 20, 40, 6))
		pygame.draw.rect(win, white, (544, 20, 6, 50))
		pygame.draw.rect(win, white, (544, 65, 40, 6))
		pygame.draw.rect(win, white, (578, 20, 6, 50))

	def eleven():
		r.one()
		pygame.draw.rect(win, white, (544, 20, 6, 50))



running = True # This tells the game loop to keep running

vel = 10 # This is the speed that the paddles will go in

fps = 60 # The fps count, usually it should be 60

ball_speed = 5 # The ball speed should be as fast as the paddles

pts_left = 0 # These are the points for the left side

pts_right = 0 # These are the points for the right side

ball_x = 398 # This is the x coordinate for the ball

ball_y = random.randint(1, 400) # The y coordinate for the ball which is randomly generated

# Racket left and right y cords
racket_left_y = 150 
racket_right_y = 150

right = random.choice([True, False]) # Determine whether its going right or left

adding = random.choice([True, False]) # Determine whether its going up or down

reset = False # Reset will reset some variables or options in the program

clock = pygame.time.Clock() # The clock which will be used for the fps count


while running:
	clock.tick(fps)

	# Quit event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Background color
	win.fill(black)


	# Draw the left and right rackets
	racket_left = pygame.draw.rect(win, white, (100, racket_left_y, 6, 40))
	racket_right = pygame.draw.rect(win, white, (700, racket_right_y, 6, 40))

	# Draw the white line which appears in the middle
	white_line = pygame.draw.rect(win, white, (400, 0, 6, 400))

	# Draw the white ball which starts somewhere in the middle
	ball = pygame.draw.rect(win, white, (ball_x, ball_y, 10, 10))


	# If it tries to escape from the bottom then bounce
	if ball_x < 780 and ball_y > 380:
		sounds.wall()
		adding = False

	# If it tries to escape from the top then bounce
	elif ball_x < 780 and ball_y < 10:
		sounds.wall()
		adding = True

	# Check if the right missed the ball
	if ball_x > 780:
		sounds.score() # Make the score sound
		pts_left += 1
		reset = True

	# Check if the left missed the ball
	elif ball_x < 10:
		sounds.score() # Make the score sound
		pts_right += 1
		reset = True

	# Check if the ball hits the left paddle
	if ball_x in range(racket_left.x, racket_left.x + 6) and ball_y in range(racket_left.y, racket_left.y + 40):
		sounds.paddle()
		right = not right # Make it go the opposite direction

	# Check if the ball hits the right paddle
	if ball_x in range(racket_right.x, racket_right.x + 6) and ball_y in range(racket_right.y, racket_right.y + 40):
		sounds.paddle()
		right = not right # Make it go the opposite direction


		
	# Check if it needs a reset (reset some variables to keep on going)
	if reset:
		ball_x = 398
		ball_y = random.randint(1, 400)
		right = random.choice([True, False])
		adding = random.choice([True, False])
		reset = False

	# Check if the ball is going right, if so then add
	if right:
		ball_x += ball_speed

	# Else minus to go left
	else:
		ball_x -= ball_speed

	# If adding to the y cordinate
	if adding == True:
		ball_y += 1

	else:
		ball_y -= 1



	# Get all the key presses
	keys = pygame.key.get_pressed()

	# Handle the left and right rackets
	handle_racket_left(keys, racket_left)
	handle_racket_right(keys, racket_right)



	# Points for the left side
	if pts_left == 0:
		l.zero()

	elif pts_left == 1:
		l.one()

	elif pts_left == 2:
		l.two()

	elif pts_left == 3:
		l.three()

	elif pts_left == 4:
		l.four()

	elif pts_left == 5:
		l.five()

	elif pts_left == 6:
		l.six()

	elif pts_left == 7:
		l.seven()

	elif pts_left == 8:
		l.eight()

	elif pts_left == 9:
		l.nine()

	elif pts_left == 10:
		l.ten()

	elif pts_left == 11:
		l.eleven()



	# Points for the right side
	if pts_right == 0:
		r.zero()

	elif pts_right == 1:
		r.one()

	elif pts_right == 2:
		r.two()

	elif pts_right == 3:
		r.three()

	elif pts_right == 4:
		r.four()

	elif pts_right == 5:
		r.five()

	elif pts_right == 6:
		r.six()

	elif pts_right == 7:
		r.seven()

	elif pts_right == 8:
		r.eight()

	elif pts_right == 9:
		r.nine()

	elif pts_right == 10:
		r.ten()

	elif pts_right == 11:
		r.eleven()



	# Keep updating the screen
	pygame.display.update()


	if pts_left == score_to_win: # Check if the left won
		tkinter.Tk().wm_withdraw()
		messagebox.showinfo('Winner', 'Left has won the game!') # Show a messagebox
		running = False # Set running to false to exit the event loop or game

	elif pts_right == score_to_win: # Check if the right won
		tkinter.Tk().wm_withdraw()
		messagebox.showinfo('Winner', 'Right has won the game!') # Show a messagebox
		running = False # Set running to false to exit the event loop or game



	

pygame.quit() # Quit from the screen
quit() # Quit from the program


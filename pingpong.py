import pygame
from random import randint, random
pygame.init()

WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Ping Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255,192,203)
myfont = pygame.font.SysFont('monospace', 50)

print("Maëline Richier, 1°2")
screen.fill(BLACK)
title = myfont.render("Single Player Pong", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)

screen.fill(BLACK)
pygame.display.update()

radius = 10
x = WIDTH//2
y = HEIGHT//2

pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.
for i in range(3, 0, -1):
    screen.fill(BLACK)
    chrono_text = myfont.render(str(i), False, GREEN)
    screen.blit(chrono_text, (WIDTH//8- chrono_text.get_width()//8, HEIGHT//8- chrono_text.get_height()//8))
    pygame.display.update()
    pygame.time.delay(1000)


paddle = {
  "width": 200,
  "height": 20,
  "color": BLUE,
  "x": 0,
  "y": HEIGHT
}
colour=[
GREEN, WHITE, RED, BLUE, YELLOW, PINK, ]
paddle["x"] = WIDTH//2 - paddle["width"]//2
paddle["y"] = HEIGHT - paddle["height"]
pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
trueEnd=False
speed = 3
speedPaddle = 5
x_sens = y_sens = 1
pause = False
points=0
end = False
while not end:
  screen.fill(BLACK)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      end = True

  key = pygame.key.get_pressed()

  if key[pygame.K_SPACE]:
    pause = True

  if key[pygame.K_RETURN]:
    pause = False

  if key[pygame.K_m]:
    auto = False

  if not pause:

    if paddle["x"]>0 and key[pygame.K_LEFT]:
      #print('bruh')
        paddle["x"] -= int(speedPaddle)


  if paddle["x"]< WIDTH-paddle["width"] and key[pygame.K_RIGHT]:
    #print('bruh')
    paddle["x"] += int(speedPaddle)

  # change x direction if the ball hits the left or right edge
  if x >= WIDTH - radius or x - radius <= 0:
    x_sens = -x_sens

  # change y direction if the ball hits the top edge
  if y - radius <= 0:
    y_sens = -y_sens

    # if the ball hits the paddle top
  if y>=paddle["y"]-radius and x>=paddle["x"] and x <= paddle['x'] + paddle["width"]:
    y_sens= -y_sens
    points+=1
    speed+=0.5
    paddle["color"]=colour[randint(0,len(colour)-1)]
  titre=myfont.render("Points :"+ str(points), False, GREEN)
  screen.blit(titre,(10, 10))
  #titpe=myfont.render("Best :"+ str(meilleur), False, GREEN)
  #screen.blit(titpe,(1000, 1000))
      # if the ball is between the x paddle begin and the x paddle end

          # change y direction
          # if the ball comes out of the screen from below, end the game
  if y > HEIGHT:
    end = True
    screen.fill(BLACK)
    fin=myfont.render("Final points: "+str(points),False, RED)
    screen.blit(fin, (WIDTH // 2 - fin.get_width() // 2, HEIGHT // 2 - fin.get_height() * 2))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.fill(BLACK)
    fin=myfont.render("Final points: "+str(points),False, RED)
    screen.blit(fin, (WIDTH // 2 - fin.get_width() // 2, HEIGHT // 2 - fin.get_height() * 2))
    fin=myfont.render("RIP",False, RED)
    screen.blit(fin,(WIDTH // 1.35 - title.get_width() // 2, HEIGHT//1.6 - title.get_height() * 2))

  # compute the new ball coordinates


  x = x + x_sens * speed
  y = y + y_sens * speed

        # redraw ball and paddle
  pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius)
  pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

        # update screen
  pygame.display.update()
  pygame.time.delay(10)
'''rip=myfont.render("Pour rejouer, appuyer sur X",False, GREEN)
screen.blit(rip, (WIDTH // 2 - rip.get_width() // 2, HEIGHT // 2 - rip.get_height() * 2))
while not key:
  if key:

    if key[pygame.K_x]:
      trueEnd = False
    else:
trueEnd=True'''


pygame.time.delay(3000)
pygame.quit()

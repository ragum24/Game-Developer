import pgzrun,random
WIDTH=1000
HEIGHT=1000
TITLE="Mothers' Day Hunt"
game_over=False
count=0

#https://forms.gle/MKb9hnVQhAEP1FKE6

flock=["bird_1","bird_2","bird_3"]
current_frame=0
bird=Actor(flock[0])
bird.pos=(200,200)
blue=Actor("blue")
blue.pos=(HEIGHT/2,WIDTH/2)
heart=Actor("hearttt.png")
heart.pos=(HEIGHT/2,WIDTH/2)
purple=Actor("purple.png")
purple.pos=(HEIGHT/2,WIDTH/2)

def animate_bird():
    global current_frame

    current_frame = (current_frame + 1) % len(flock)
    bird.image = flock[current_frame]

def draw():
    screen.blit("gar",(0,0))
    blue.draw()
    heart.draw()
    purple.draw()
    bird.draw()
    screen.draw.text("Points- "+str(count),color="gold",center=(50,50))
    if game_over:
      screen.blit("mothers_day.png",(0,0)) 
      screen.draw.text("Score:"+str(count),fontname="times",fontsize=30,color="black",center=(80,20))

def update():
   global count
   if keyboard.left:
      bird.x-=2
   if keyboard.right:
      bird.x+=2
   if keyboard.up:
      bird.y-=2
   if keyboard.down:
      bird.y+=2
   if bird.colliderect(blue):
      count+=1
      blue.pos=random.randint(100,450),random.randint(100,450)
   if bird.colliderect(heart):
      count+=1
      heart.pos=random.randint(10,450),random.randint(10,450)
   if bird.colliderect(purple):
      count+=1
      purple.pos=random.randint(70,450),random.randint(70,450)

def time_is_up():
   global game_over
   game_over=True

clock.schedule(time_is_up,30)


clock.schedule_interval(animate_bird, 0.1)   
pgzrun.go()
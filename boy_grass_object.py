from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x,self.y = random.randint(0,100),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Zombie:
    def __init__(self):
        self.x,self.y = 100,170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame*frame_width,0,frame_width,frame_height,self.x,self.y,frame_width//2,frame_height//2)

class Balloon:
    def __init__(self):
        self.x,self.y = random.randint(41,750),30
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(10,20)
        self.is_at_Top = False
        self.size = random.randint(41,70)
        self.direction = 1
        #1 = up -1 = down
        self.count = 0

    def update(self):
        if(self.y >= 610 - self.size and not self.is_at_Top):
            self.is_at_Top = True

        if(not self.is_at_Top and self.direction == 1):
            self.y += (self.speed * self.direction)

        if(self.is_at_Top and self.direction == 1):
            self.direction = -1
            self.y += (self.speed * self.direction)
            return

        if(self.is_at_Top and self.direction == -1):
            self.direction = 1
            self.y += (self.speed * self.direction)
            return


    def draw(self):
        self.image.clip_draw(0,0,41,41,self.x,self.y,self.size,self.size)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running

    global world
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    balls = [Balloon() for i in range(21)]
    world += balls

    running = True



def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()

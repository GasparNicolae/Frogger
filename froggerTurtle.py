import turtle
import math

sc = turtle.Screen()
sc.cv._rootwindow.resizable(False, False)
sc.title("Frogger -- Nicolae")
sc.setup(800, 600)
sc.bgcolor("green")
sc.bgpic("background.gif")
sc.tracer(0)

shapes = ["car1.gif", "car2.gif", "car3.gif", "car4.gif", "car5.gif", "car6.gif", "life.gif", "float1.gif", 
    "float2.gif", "float3.gif", "float4.gif", "float5.gif", "float6.gif", "frog1.gif", "frog2.gif", "home.gif",
    "winner.gif", "game-over.gif", "ouch.gif"]
    
for shape in shapes:
    sc.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()
        
    def update(self):
        pass
        
    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.collision = False
        self.frogs_home = 0
        self.lives = 3
        
    def up(self):
        if player.lives == 0 or player.frogs_home == 3:
            message.hide();
            player.lives = 3
            player.frogs_home = 0
        elif player.lives < 3 and player.lives > 0:
            message.hide();
            self.y += 40
            self.image = "frog2.gif"
        else:
            self.y += 40
            self.image = "frog2.gif"

    def down(self):
        self.y -= 40

    def right(self):
        if player.lives < 3 and player.lives > 0:
            message.hide();
        self.x += 40
        self.image = "frog2.gif"

    def left(self):
        if player.lives < 3 and player.lives > 0:
            message.hide();
        self.x -= 40
        self.image = "frog2.gif"

    def nojump(self):
        self.image = "frog1.gif"
        
    def update(self):
        self.x += self.dx
        
        if self.x < -365 or self.x > 365:
            self.x = 0
            self.y = -280
            
        if self.y < -280:
            self.y = -280
            
    def go_home(self):
        self.dx = 0
        self.x = 0
        self.y = -280

class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        if self.x < -440:
            self.x = 440
            
        if self.x > 440:
            self.x = -440

class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        if self.x < -440:
            self.x = 440
            
        if self.x > 440:
            self.x = -440

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        if self.x < -440:
            self.x = 440
            
        if self.x > 440:
            self.x = -440      

class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0

class Message(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0

    def hide(self):
        self.image = "blank"
        
    def win(self):
        self.image = "winner.gif"
        
    def lose(self):
        self.image = "game-over.gif"

    def ouch(self):
        self.image = "ouch.gif"
                    
player = Player(0, -325, 40, 40, "frog1.gif")
message = Message(0, 0, 40, 40, "blank")

level_1 = [
    Car(0, -235, 50, 30, "car1.gif", -0.1),
    Car(221, -235, 50, 30, "car1.gif", -0.1),
    Car(421, -235, 50, 30, "car1.gif", -0.1),
    Car(-221, -235, 50, 30, "car1.gif", -0.1),
    
    Car(0, -195, 50, 30, "car2.gif", 0.2),
    Car(221, -195, 50, 30, "car2.gif", 0.2),
    Car(421, -195, 50, 30, "car2.gif", 0.2),
    Car(-221, -195, 50, 30, "car2.gif", 0.2),
    
    Car(0, -155, 50, 30, "car3.gif", -0.2),
    Car(221, -155, 50, 30, "car3.gif", -0.2),
    Car(421, -155, 50, 30, "car3.gif", -0.2),
    Car(-221, -155, 50, 30, "car3.gif", -0.2),
    
    Car(0, -115, 50, 30, "car4.gif", 0.2),
    Car(221, -115, 50, 30, "car4.gif", 0.2),
    Car(421, -115, 50, 30, "car4.gif", 0.2),
    Car(-221, -115, 50, 30, "car4.gif", 0.2),
    
    Car(0, -75, 50, 30, "car5.gif", -0.1),
    Car(221, -75, 50, 30, "car5.gif", -0.1),
    Car(421, -75, 50, 30, "car5.gif", -0.1),
    Car(-221, -75, 50, 30, "car5.gif", -0.1),

    Car(0, -35, 50, 30, "car6.gif", 0.3),
    Car(221, -35, 50, 30, "car6.gif", 0.3),
    Car(421, -35, 50, 30, "car6.gif", 0.3),
    Car(-221, -35, 50, 30, "car6.gif", 0.3),

    Turtle(0, 40, 80, 30, "float1.gif", -0.3),
    
    Log(100, 80, 80, 30, "float2.gif", 0.4),
    Log(400, 80, 80, 30, "float2.gif", 0.4),

    Turtle(-250, 120, 80, 30, "float3.gif", -0.25),
    Turtle(250, 120, 80, 30, "float3.gif", -0.25),
    
    Log(-100, 160, 80, 30, "float4.gif", 0.2),
    Log(400, 160, 80, 30, "float4.gif", 0.2),

    Turtle(-55, 200, 80, 30, "float5.gif", -0.15),
    Turtle(255, 200, 80, 30, "float5.gif", -0.15)
    ]

homes = [ 
    Home(-100, 275, 30, 30, "home.gif"),
    Home(0, 275, 30, 30, "home.gif"),
    Home(100, 275, 30, 30, "home.gif")
    ]

sprites = level_1 + homes
sprites.append(player)
sprites.append(message)

sc.listen()
sc.onkeypress(player.up, "Up")
sc.onkeyrelease(player.nojump, "Up")
sc.onkeypress(player.down, "Down")
sc.onkeypress(player.right, "Right")
sc.onkeyrelease(player.nojump, "Right")
sc.onkeypress(player.left, "Left")
sc.onkeyrelease(player.nojump, "Left")

while True:
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()

    pen.goto(-360, 280)
    pen.shape("life.gif")
    for life in range(player.lives):
        pen.goto(-360 + (life * 30), 280)
        pen.stamp()

    player.dx = 0
    player.collision = False
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.lives -= 1
                message.ouch();
                player.go_home()
                break
            elif isinstance(sprite, Log) or isinstance(sprite, Turtle):
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Home):
                player.go_home()
                sprite.image = "frog1.gif"
                player.frogs_home += 1
                break
            
    if (player.x > 360 or player.x < -360) and player.collision == True:
        player.lives -= 1
        message.ouch();
        player.go_home()

    if player.y > 0 and player.y < 240 and player.collision != True:
        player.lives -= 1
        message.ouch();
        player.go_home()

    if player.frogs_home == 3:
        message.win();
        player.go_home()
        for home in homes:
            home.image = "home.gif"
    
    if player.lives == 0:
        message.lose();
        player.go_home()
        player.frogs_home = 0
        for home in homes:
            home.image = "home.gif" 
    
    sc.update()
    
    pen.clear()

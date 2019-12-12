#Psuedocode
# '''5 walls
# for range(walls):
#     turn 90 degrees left & right
# '''
#imports details to trtl
import random
import turtle as trtl

shape= "turtle"
maze_printer= trtl.Turtle(shape=shape)
maze_printer.speed(0)
maze_printer.ht()

player=trtl.Turtle()
player.speed(5)
player.color("blue")
player.shape("triangle")




number_walls= 25
wall_width= 15
door_width = 10
distance = 30
wall_color = "red"
maze_printer.pencolor(wall_color)
count= 0

def drawDoor():
    #draw door
    maze_printer.penup()
    maze_printer.forward(door_width*3)
    maze_printer.pendown()

def drawBarrier():
    #draw barrier
    maze_printer.left(90)
    maze_printer.forward(wall_width*2)
    maze_printer.backward(wall_width*2)
    maze_printer.right(90)
def up():
    player.setheading(90)
    player.forward(10)
def down():
    player.setheading(270)
    player.forward(10)
def right():
    player.setheading(00)
    player.forward(10)

def left():
    player.setheading(180)
    player.forward(10)
    


#this creates opening in the maze
while count < number_walls:

    count +=1
    if(count > 4):
        door = random.randint(door_width, distance- door_width)
        barrier = random.randint(door_width, distance- door_width)
        
        if door < barrier:
            maze_printer.forward(door)
            drawDoor()
            maze_printer.forward(barrier - door - door_width)
            drawBarrier()
            maze_printer.forward(distance - barrier)

        else:      
            maze_printer.forward(barrier)
            drawBarrier()
            maze_printer.forward(door-barrier)
            drawDoor()
            maze_printer.forward(distance - door - door_width)


        

    maze_printer.left(90)
    distance += wall_width
wn = trtl.Screen()   
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")


wn.listen()
wn.mainloop()
from turtle import *


#we want to paint a house

#step 1:  draw a square 
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

#drawing a door

forward(30)
color("yellow")
left(90)
forward(100)        #heightof the door
right(90)
forward(60)
right(90)
forward(100)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
color("green")
goto(160, 160)
pendown()

right(60)
forward(56)
left(90)
forward(56)
left(90)
forward(56)
left(90)
forward(56)
left(90)
forward(28)
left(90)
forward(56)
left(90)
forward(28)
left(90)
forward(28)
left(90)
forward(56)

penup()
forward(101)
left(90)
forward(129)
pendown()
right(90)
forward(200)
left(180)
forward(20)

color("brown")
left(90)
forward(100)

color("green")
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
forward(50)
right(90)
forward(50)
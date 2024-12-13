import turtle
import random


score = 0

screen = turtle.Screen()

screen.setup(800,800)

screen.bgcolor('red')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle() #All About Me
t2.penup()
t3 = turtle.Turtle()
t3.hideturtle()
t3.speed(2000)# scoreboard
t4 = turtle.Turtle()
t4.hideturtle()
t4.speed(2000)
t4.penup()
t4. goto(0,150)
t2. fillcolor("red")
t2. hideturtle()
t. hideturtle()
t2. penup()
t2.goto(0,100)


t3.penup()
t3.goto(0,200)
#hide t3 eventually
t.speed(2000)
t.penup()
t.goto(0,50)
t.pendown()
t.write("All About Me",font=("arial",30,"bold"),align="center")
t. penup()
t.goto(0,-50)
t.pendown()
t.write("Julian Noone",font=("arial",30,"bold"),align="center")
enter = input("press enter to begin")
t.showturtle()
t.clear()
t.pencolor("black")
screen.bgcolor('green')
t.penup()
t.goto(0,250)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")


turtle.addshape("steak.gif")
t2.shape("steak.gif")
t2.goto(150,150)

a = t2.stamp()
t.hideturtle()
t2.goto(150,200)
t.goto(150,200)
t.write("Steak", font=("arial", 30, "bold"), align="center")


turtle.addshape("tacos.gif")
t2.shape("tacos.gif")
t2.goto(0,-200)
b = t2.stamp()
t2.goto(0,-200)
t.goto(0,-200)

t.write("tacos", font=("arial", 30, "bold"), align="center")
turtle.addshape("porkchop.gif")
t2.shape("porkchop.gif")
t2.goto(-150,150)
c = t2.stamp()
t2.goto(-150,0)
t.goto(-150,200)
t.write("porkchop", font=("arial", 30, "bold"), align="center")





enter = input("press enter to begin")
t2.clearstamps()
t2.clear()
t.clear()


t.showturtle()
t.pencolor("black")
screen.bgcolor('magenta')
t.penup()
t.goto(0,250)
t.write("My favorite hobbies", font=("arial", 30, "bold"), align="center")


turtle.addshape("playstation.gif")
t2.shape("playstation.gif")
t2.goto(150,150)

d = t2.stamp()
t.hideturtle()
t2.goto(150,200)
t.goto(150,200)
t.write("playstation", font=("arial", 30, "bold"), align="center")


turtle.addshape("basketball.gif")
t2.shape("basketball.gif")
t2.goto(100,-200)
e = t2.stamp()
t2.goto(100,-50)
t.goto(100,-50)

t.write("basketball", font=("arial", 30, "bold"), align="center")
turtle.addshape("dirtbike.gif")
t2.shape("dirtbike.gif")
t2.goto(-150,150)
f = t2.stamp()
t2.goto(-150,0)
t.goto(-150,200)
t.write("dirtbike", font=("arial", 30, "bold"), align="center")

turtle.addshape("suitcase.gif")
t2.shape("suitcase.gif")
t2.goto(-150,-200)
g = t2.stamp()
t2.goto(-150,-200)
t.goto(-150,-200)
t.write("travel", font=("arial", 30, "bold"), align="center")



enter = input("press enter to begin")
t2.clearstamps()
t2.clear()
t.clear()







t.showturtle()
t.pencolor("white")
screen.bgcolor('blue')
t.penup()
t.goto(0,250)
t.write("My favorite movie", font=("arial", 30, "bold"), align="center")


turtle.addshape("mazerunner.gif")
t2.shape("mazerunner.gif")
t2.goto(0,50)

l = t2.stamp()
t.hideturtle()
t2.goto(0,175)
t.goto(0,175)
t.write("the maze runner", font=("arial", 30, "bold"), align="center")



enter = input("press enter to begin")
t2.clearstamps()
t2.clear()
t.clear()







t.showturtle()
t.pencolor("white")
screen.bgcolor('purple')
t.penup()
t.goto(0,250)
t.write("My favorite sport", font=("arial", 30, "bold"), align="center")


turtle.addshape("basketballsport.gif")
t2.shape("basketballsport.gif")
t2.goto(0,0)

m = t2.stamp()
t.hideturtle()
t2.goto(0,100)
t.goto(0,100)
t.write("basketball", font=("arial", 30, "bold"), align="center")




turtle.done()


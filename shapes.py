import turtle
p= turtle.Turtle()

p.circle(120) # circle with its radius
p.goto(0,120) # a line have the x and y coordinates
p.dot(40) # filled circle passing with its diameter
p.home()
p.circle(150)
p.penup()
p.forward(200)
p.pendown()
p.forward(190)
p.right(90)
p.forward(70)
p.right(90)
p.forward(190)
p.right(90)
p.forward(70)
p.penup()
p.left(90)
p.forward(500)
p.pendown()
p.forward(200)
p.right(140)
p.forward(140)
p.right(85)
p.forward(130)

p.hideturtle() # for hiding the turtle

turtle.done()
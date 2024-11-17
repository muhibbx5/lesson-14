import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(500,600)
Heptagon=turtle.Turtle()
sides=7
sides_length=80
angle=360.0/sides
 
 
for i in range(sides):
   Heptagon.forward(sides_length)
   Heptagon.left(angle)
   
turtle.done()

import turtle as t
import random

t.bgcolor("black")
t.speed(0)
t.colormode(255)
t.pensize(3)

for i in range(456): 
    for j in range(600):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        v = random.randint(0, 255)
        t.color(a, b, v)
        t.forward(j)
        t.left(89)
        
t.mainloop()

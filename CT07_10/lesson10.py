import turtle
window=turtle.Screen()
window.setup(width=600,height=400)
t=turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
for i in range(4):
    t.forward(100)
    t.right(90)
window.mainloop()

def isElderly(age):
    if (age>65):
        return 1 
    return 0 

age=input("")


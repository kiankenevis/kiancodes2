import turtle
t=turtle.Pen()
red=int(input("megdar rang germes ra vared konid"))
green=int(input("megdar rang sabz ra vared konid"))
blue=int(input("megdar rang abi ra vared konid"))
def moraba(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    for x in range(4):
        t.fd(100)
        t.lt(90)
    
t.end_fill()
moraba(red,green,blue)

    

import turtle

for x,y,r in [(200,200,50), (-200, -200, 30), (100, 100, 50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write(str((x,y)))

#x와 y는 int형이지만 (x,y)는 tuple 된다.
#따라서 str((x,y))는 str(tuple)이므로 문자열로 출력이 된다.

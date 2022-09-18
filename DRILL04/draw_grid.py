import turtle

# draw horizonal lines - 가로줄 그리기

y = 0
while y <= 500:
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto(500, y)
    y += 100


# draw vertical lines - 세로줄 그리기

x = 0
while x <= 500:
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.goto(x, 500)
    x += 100

#테스트 리드타임
#->뒤쪽 코드의 버그및 수정을 확인하기 위해 앞쪽 코드를 실행시키는 시간
#->개발 시간이 엄청나게 늘어남

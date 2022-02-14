import turtle
import random

# 座標と半径、ペンの色・サイズを指定して円を描く関数を定義
def draw_circle(drawer, pos, radius, pencolor, pensize):
    pos_org = drawer.pos()
    pen_org = drawer.pen()
    drawer.penup()
    drawer.setpos(pos)
    drawer.pendown()
    drawer.pen(pencolor=pencolor, pensize=pensize)
    drawer.circle(radius)
    drawer.penup()
    drawer.setpos(pos_org)
    drawer.pen(pen_org)

# オリンピックマークの各円の座標と色を表す辞書のリストを作成
olympic_circles = [
    {"pos": (-100, 0), "color": "blue"},
    {"pos": (0, 0), "color": "black"},
    {"pos": (100, 0), "color": "red"},
    {"pos": (-50, -90), "color": "yellow"},
    {"pos": (50, -90), "color": "green"},
]

# turtleオブジェクトを作成
t = turtle.Turtle(visible=False)

# 辞書のリストに基づき複数の円を描画
for circle in olympic_circles:
    draw_circle(t, circle["pos"], 60, circle["color"], 5)

# キャンバスのリセット
t.clear()


# レースを行うカメのクラスを定義
class Turtle():
    def __init__(self, pos, color, start=0, end=200):
        self.__initpos = pos
        self.__color = color
        self.__start = start
        self.__end = end
        self.__drawer = turtle.Turtle()
        self.initialize()
    
    def initialize(self):
        self.__drawer.reset()
        self.__drawer.color(self.__color)
        self.__drawer.pencolor(self.__color)
        self.__drawer.shape("turtle")
        self.__drawer.penup()
        self.__drawer.setpos(self.__initpos)
        self.__progress = self.__start
    
    def update(self):
        self.__progress += random.randint(0, 50)
        self.__drawer.setpos(self.__initpos[0] + self.__progress, self.__initpos[1])
    
    def draw_finishcircle(self, radius, pensize):
        draw_circle(
            self.__drawer, 
            (self.__initpos[0] + self.__end + radius, self.__initpos[1] - radius), 
            radius,
            self.__color, 
            pensize
        )
    
    def is_finished(self):
        return self.__progress >= self.__end

# カメのインスタンスを作成
turtles = [
    Turtle((-100, 50), "red"),
    Turtle((-100, -50), "blue"),
]

# ゴールを表す円を描画
for turtle in turtles:
    turtle.draw_finishcircle(30, 5)

# どちらかのカメがゴールするまでupdateを繰り返す
while True:
    for turtle in turtles:
        turtle.update()
        if turtle.is_finished():
            break
    else:
        continue
    break

# カメを初期化する
for turtle in turtles:
    turtle.initialize()

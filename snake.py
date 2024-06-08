import turtle
import time
import random

posponer = 0.1
score = 0
highScore = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
#esta linea quita el rastro del objeto al moverse
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente
trozosDeCuerpo = []

#Score
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0           High Score: 0", align= "center", font=("Courier", 16, "normal"))

#Funciones
def moverArriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def moverAbajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def moverDerecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def moverIzquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#Teclado
window.listen()
window.onkeypress(moverArriba, "Up")
window.onkeypress(moverAbajo, "Down")
window.onkeypress(moverDerecha, "Right")
window.onkeypress(moverIzquierda, "Left")

while True:
    window.update()

    #Chocar con el borde de la pantalla
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        score = 0
        texto.clear()
        texto.write("Score: {}           High Score: {}".format(score, highScore), align= "center", font=("Courier", 16, "normal"))
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #Borrar los trozos del cuerpo
        for trozoDeCuerpo in trozosDeCuerpo:
            trozoDeCuerpo.hideturtle()
            
        trozosDeCuerpo.clear()
    

    #Colisiones con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-14,14)*20
        y = random.randint(-14,14)*20
        comida.goto(x, y)
        nuevoTrozoDeCuerpo = turtle.Turtle()
        nuevoTrozoDeCuerpo.speed(0)
        nuevoTrozoDeCuerpo.shape("square")
        nuevoTrozoDeCuerpo.color("lightgreen")
        nuevoTrozoDeCuerpo.penup()
        trozosDeCuerpo.append(nuevoTrozoDeCuerpo)
        score += 1

        if score > highScore:
            highScore = score
        texto.clear()
        texto.write("Score: {}           High Score: {}".format(score, highScore), align= "center", font=("Courier", 16, "normal"))

    #Moviendo el cuerpo de la snake
    totalTrozosDeCuerpo = len(trozosDeCuerpo)
        
    for i in range(totalTrozosDeCuerpo -1, 0, -1):
        x = trozosDeCuerpo[i-1].xcor()
        y = trozosDeCuerpo[i-1].ycor()
        trozosDeCuerpo[i].goto(x,y)
    if totalTrozosDeCuerpo > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        trozosDeCuerpo[0].goto(x,y)



    movimiento()

    #Chocar con la propia serpiente
    for trozoDeCuerpo in trozosDeCuerpo:
        if trozoDeCuerpo.distance(cabeza) < 20:
            time.sleep(1)
            score = 0
            texto.clear()
            texto.write("Score: {}           High Score: {}".format(score, highScore), align= "center", font=("Courier", 16, "normal"))
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            #Borrar los trozos del cuerpo
            for trozoDeCuerpo in trozosDeCuerpo:
                trozoDeCuerpo.hideturtle()
                
            trozosDeCuerpo.clear()

    time.sleep(posponer)
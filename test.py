import tkinter
from threading import *
import time
import random

# globalizo  y creo la ventana

global Ven1, Ven2, NIVELES1, mapa1, VN1, gasolina, p, i, j, Game_Over, pxcar1, pycar1, pxcar2, pycar2, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2

Ven1 = tkinter.Tk()
Ven1.geometry("1200x680+100+0")
Ven1.config(bg="black")
Ven1.title("Avoid Cars")
Ven1.maxsize(1200, 680)
Ven1.minsize(1200, 680)

fondo32 = tkinter.PhotoImage(file="C:\graficos\\instrucciones2.png")


## se crea un boton en el menu principal que permite ver las instrucciones del juego
def info():
    global Ven1, Ven2, mapa1, info
    info = tkinter.Toplevel(Ven1)
    info.geometry("700x700+100+0")
    info.config(bg="black")
    info.title("Avoid Cars INSTRUCCIONES")
    lblinstrucciones = tkinter.Label(info, image=fondo32).place(x=0, y=0)
    info.mainloop()


## en esta ventana se encuentran los niveles disponibles
def segundaventana():
    global Ven1, Ven2, NIVELES1, mapa1, info
    """ se  crea una ventana hija para hacer el menu de niveles"""
    Ven2 = tkinter.Toplevel(Ven1)
    Ven1.iconify()
    Ven2.geometry("1200x720+100+0")
    Ven2.title("Avoid Cars")
    Ven2.maxsize(1200, 680)
    Ven2.minsize(1200, 680)
    niveles = tkinter.PhotoImage(file="C:\graficos\\FONDO2.gif")
    NIVELES = tkinter.Label(Ven2, image=niveles).place(x=0, y=0)

    # SELECCION DE NIVELES POR BOTONES

    imanivel1 = tkinter.PhotoImage(file="C:\graficos\\NIVEL1.gif")
    nivel1 = tkinter.Button(Ven2, image=imanivel1, command=nivel_1).place(x=200, y=120)

    imanivel2 = tkinter.PhotoImage(file="C:\graficos\\NIVEL2.gif")
    nivel2 = tkinter.Button(Ven2, image=imanivel2, command=nivel_2).place(x=500, y=120)

    imanivel3 = tkinter.PhotoImage(file="C:\graficos\\NIVEL3.gif")
    nivel3 = tkinter.Button(Ven2, image=imanivel3, command=nivel_3).place(x=800, y=120)

    imanivel4 = tkinter.PhotoImage(file="C:\graficos\\NIVEL4.gif")
    nivel4 = tkinter.Button(Ven2, image=imanivel4, command=nivel_4).place(x=350, y=400)

    imanivel5 = tkinter.PhotoImage(file="C:\graficos\\NIVEL5.gif")
    nivel5 = tkinter.Button(Ven2, image=imanivel5, command=nivel_5).place(x=650, y=400)

    Ven2.mainloop()


# AQUI SE HACE UN CONTEO REGRESIVO PARA INICIAR EL JUEGO 3 , 2 , 1
def tres():
    """Se crea la funcion que genera el numero 3 en la pantalla del lvl 1 de esta manera
      creamos una cuenta regresiva"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, gasolina, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    three = tkinter.PhotoImage(file="C:\graficos\\THREE.gif")
    three_1 = VN1.create_image(343, 200, image=three)
    three2 = tkinter.PhotoImage(file="C:\graficos\\THREE.gif")
    three_2 = VN1.create_image(1050, 200, image=three)
    t = Timer(1.0, dos)
    t.start()


def dos():
    """cambia a la funcion dos() para poner imagen en pantalla"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, gasolina, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VN1.delete(three_1)
    VN1.delete(three_2)
    two = tkinter.PhotoImage(file="C:\graficos\\TWO.gif")
    two_1 = VN1.create_image(343, 200, image=two)
    two2 = tkinter.PhotoImage(file="C:\graficos\\TWO.gif")
    two_2 = VN1.create_image(1050, 200, image=two)
    t2 = Timer(1.0, uno)
    t2.start()


##ESTA VENTANA ES MAS ESPECIAL YA QUE LLAMA A LAS FUNCIONES DE PUNTAJE, GASOLINA Y EL TIEMPO QUE DURA EL MAPA
## ADEMAS GUARDA ALGUNAS VARIABLES
def uno():
    """cambia a la funcion uno() para poner imagen en pantalla"""
    global Ven1, Ven2, NIVELES1, mapa1, puntaje, masgas, tiempo, pxcar1, pycar1, pxcar2, pycar2, velocidad, k1, k2, puntaje1, VN1, gasolina, gasolina2, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VN1.delete(two_1)
    VN1.delete(two_2)
    one = tkinter.PhotoImage(file="C:\graficos\\ONE.gif")
    one_1 = VN1.create_image(343, 200, image=one)
    one2 = tkinter.PhotoImage(file="C:\graficos\\ONE.gif")
    one_2 = VN1.create_image(1050, 200, image=one)
    velocidad = 1
    tiempo = 60
    gasolina2 = 100
    masgas = 0
    gasolina = 100
    puntaje = 0
    puntaje1 = 0
    k1 = 0
    k2 = 0
    t1 = Timer(1.0, puntaje_1).start()
    t2 = Timer(1.0, puntaje_2).start()
    t3 = Timer(1.0, gasolina_1).start()
    t4 = Timer(1.0, gasolina_2).start()
    t5 = Timer(1.0, tiempo_1).start()
    t7 = Timer(1.0, Velocidad_1).start()
    t8 = Timer(1.0, Car_Puntos).start()
    t9 = Timer(1.0, Car_enemigo1).start()
    t10 = Timer(1.0, Car_enemigo2).start()
    t11 = Timer(1.0, Car_enemigo3).start()
    t13 = Timer(1.0, Car_Puntos2).start()
    t14 = Timer(1.0, Car_enemigo21).start()
    t15 = Timer(1.0, Car_enemigo22).start()
    t16 = Timer(1.0, Car_enemigo23).start()
    t17 = Timer(1.0, FONDO_MOV).start()


## LA PUNTUACION SE MANEJARA EN UN MISMO NIVEL SUMANDO DE 100  EN 100, PARA QUE UN JUGADOR TENGA MAS PUNTAJE
## NO DEBE CHOCARSE YA QUE AL CHOCAR CON AUTOS SIN TOMAR EN CUENTA EL CAMION SU PUNTAJE DISMINUIRA EN 200
def puntaje_1():
    """puntaje"""
    global Ven1, Ven2, NIVELES1, mapa1, puntos, puntaje, puntaje1, VN1, gasolina, gasolina2, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    while (vel_map > 0):
        if (puntaje < 100000):
            time.sleep(1.0)
            puntaje = puntaje + 100
            puntaje_1 = tkinter.Label(VN1, text=int(puntaje), font=("Forte", 10), bg="#BFFFBF ", fg="red",
                                      width=5).place(x=580, y=42)
            VN1.delete(puntaje_1)
        if (vel_map == 0):
            VN1.delete(puntaje_1)
            puntaje = puntaje
            puntaje_1 = tkinter.Label(VN1, text=int(puntaje), font=("Forte", 10), bg="#BFFFBF ", fg="red",
                                      width=5).place(x=580, y=42)


def puntaje_2():
    """puntaje"""
    global Ven1, Ven2, NIVELES1, mapa1, puntos, puntaje, puntaje1, VN1, gasolina, gasolina2, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    while (vel_map > 0):
        if (puntaje1 < 100000):
            time.sleep(1.0)
            puntaje1 = puntaje1 + 100
            puntaje_2 = tkinter.Label(VN1, text=int(puntaje1), font=("Forte", 10), bg="#BFFFBF ", fg="red",
                                      width=5).place(x=580, y=396)
            VN1.delete(puntaje_1)
        if (vel_map == 0):
            VN1.delete(puntaje_1)
            puntaje1 = puntaje1
            puntaje_2 = tkinter.Label(VN1, text=int(puntaje1), font=("Forte", 10), bg="#BFFFBF ", fg="red",
                                      width=5).place(x=580, y=396)


## LA GASOLINA COMENZARA EN 100 Y DISMINUIRA CADA SEGUNDO, PARA AUMENTAR LA GASOLINA EL JUGADOR DEBE
## COGER EL CARRO DE BONIFICACION, ESTE AUMENTARA LA GASOLINA EN 50
def gasolina_1():
    """ la gasolina sera variable, al llegar a "0" el juego habra terminado para cualquiera de los jugadores"""
    global Ven1, Ven2, NIVELES1, puntos, masgas, posx_compuntos, posy_compuntos, velocidad, mapa1, posx_comc1, posy_comc1, i, i2, VN1, velocidad1, velocidad2, gasolina, p, i, j, singas, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    while (vel_map > 0):
        if (gasolina <= 100):
            time.sleep(0.8)
            gasolina = gasolina - 2
            gasolina_1 = tkinter.Label(VN1, text=int(gasolina), font=("Forte", 12), bg="#BFFFBF ", fg="red",
                                       width=3).place(x=580, y=190)
            VN1.delete(gasolina_1)
        if (gasolina == 0 or (gasolina == 0 and gasolina > 0)):
            VN1.delete(gasolina_1)
            gasolina_1 = tkinter.Label(VN1, text=int(0), font=("Forte", 12), bg="#BFFFBF ", fg="red", width=3).place(
                x=580, y=190)
            OutGas_1 = VN1.create_image(343, 200, image=singas)
            vel_map = 0
            i = None
            i2 = None
            VN1.delete(velocidad1)
            VN1.delete(velocidad2)
            velocidad1 = tkinter.Label(VN1, text=str(0) + "km/h", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
                x=575, y=255)
            velocidad2 = tkinter.Label(VN1, text=str(0) + "km/h", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
                x=575, y=610)


def gasolina_2():
    """ la gasolina sera variable, al llegar a "0" el juego habra terminado para cualquiera de los jugadores """
    global Ven1, Ven2, NIVELES1, puntos, mapa1, velocidad, VN1, i, i2, velocidad1, velocidad2, gasolina, gasolina2, singas, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    while (vel_map > 0):
        if (gasolina2 <= 100):
            time.sleep(0.8)
            gasolina2 = gasolina2 - 2
            gasolina_2 = tkinter.Label(VN1, text=int(gasolina2), font=("Forte", 12), bg="#BFFFBF ", fg="red",
                                       width=3).place(x=580, y=545)
            VN1.delete(gasolina_2)
        if (gasolina == 0 or (gasolina2 == 0 and gasolina > 0)):
            VN1.delete(gasolina_2)
            gasolina_2 = tkinter.Label(VN1, text=int(0), font=("Forte", 12), bg="#BFFFBF ", fg="red", width=3).place(
                x=580, y=545)
            OutGas_1 = VN1.create_image(1050, 200, image=singas)
            vel_map = 0
            i = None
            i2 = None
            VN1.delete(velocidad1)
            VN1.delete(velocidad2)
            velocidad1 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
                x=575, y=255)
            velocidad2 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
                x=575, y=610)


## el tiempo sera de 60 segundos y de esto dependera si el jugador gana o no, si pasa los 60 segundos sin chocarse en
## las carreteras o con los camiones, tambien si su gasolina le es suficiente pasara el nivel, el tiempo solo sera uno
## ya que si alguno de los dos choca o se acaba su gasolina el juego terminara
def tiempo_1():
    """ la gasolina sera """
    global Ven1, Ven2, NIVELES1, puntos, velocidad, mapa1, velocidad1, velocidad2, VN1, k1, k2, pos_car1, p, pos_car2, tiempo, gasolina, gasolina2, singas, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    while (vel_map > 0):
        if (tiempo <= 60):
            time.sleep(1.0)
            tiempo = tiempo - 1
            k1 = k1 + 1
            k2 = k2 + 1
            poscarrito1 = tkinter.Label(VN1, image=pos_car1, bg="#22F8F8").place(x=542 + k1, y=319)
            poscarrito2 = tkinter.Label(VN1, image=pos_car2, bg="#22F8F8").place(x=542 + k1, y=344)
            VN1.delete(poscarrito1)
            VN1.delete(poscarrito2)
        if (tiempo == 0):
            VN1.delete(poscarrito1)
            VN1.delete(poscarrito2)
            poscarrito1 = tkinter.Label(VN1, image=pos_car1).place(x=650, y=200)
            poscarrito2 = tkinter.Label(VN1, image=pos_car2).place(x=650, y=210)
            vel_map = 0
            VN1.delete(velocidad1)
            VN1.delete(velocidad2)
            velocidad1 = tkinter.Label(VN1, text=str(0) + "km/h", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
                x=575, y=255)
            velocidad2 = tkinter.Label(VN1, text=str(0) + "km/h", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
                x=575, y=610)


def Velocidad_1():
    """velocidad"""
    global Ven1, Ven2, NIVELES1, mapa1, puntos, velocidad, velocidad1, velocidad2, puntaje, puntaje1, VN1, gasolina, gasolina2, p, i, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    if (0 < velocidad and velocidad < 200):
        time.sleep(0.03)
        velocidad = velocidad + 10
        velocidad1 = tkinter.Label(VN1, text=str(velocidad) + "km/h", font=("Arial", 12), bg="#BFFFBF ",
                                   fg="red").place(x=575, y=255)
        velocidad2 = tkinter.Label(VN1, text=str(velocidad) + "km/h", font=("Arial", 12), bg="#BFFFBF ",
                                   fg="red").place(x=575, y=610)
        VN1.delete(velocidad1)
        VN1.delete(velocidad2)
        Velocidad_1()
    elif (velocidad == 201):
        VN1.delete(velocidad1)
        VN1.delete(velocidad2)
        velocidad1 = tkinter.Label(VN1, text=str(200) + "km/h", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
            x=575, y=255)
        velocidad2 = tkinter.Label(VN1, text=str(200) + "km/h", font=("Arial", 12), bg="#BFFFBF ", fg="red").place(
            x=575, y=610)


### el carro de puntos configurar no olvideis
def Car_Puntos():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, masgas, pluspun, VN1, gasolina, puntaje, i, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75]
    listat = [20.0, 23.3, 18.3, 20.6, 30.8]
    time2 = random.choice(listat)
    cont_pu1 = random.choice(lista)
    cont_pu2 = 0
    cont2_pun1 = 0
    cont2_pun2 = 0
    posx_puntos = 343
    posy_puntos = -10
    posx_puntos2 = 1050
    posy_puntos2 = -10
    if (0 < tiempo <= 60):
        time.sleep(time2)
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            if ((posx_puntos + cont_pu1) == (pxcar1 + i) and (posy_puntos + cont_pu2) == (pycar1 + j)):
                VN1.delete(puntos1)
                gasolina += 20
                puntaje += 200
                time.sleep(0.5)
                Car_Puntos()
            else:
                VN1.delete(puntos1)
                time.sleep(time2)
                Car_Puntos()


def Car_Puntos2():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, masgas, VN1, gasolina2, puntaje1, i, pxcar2, pycar2, pxcar2, pycar2, pos_car1, p, pos_car2, i2, Game_Over, singas, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75]
    listat = [20.0, 23.3, 18.3, 20.6, 30.8]
    time2 = random.choice(listat)
    cont_pu1 = random.choice(lista)
    cont_pu2 = 0
    cont2_pun1 = 0
    cont2_pun2 = 0
    posx_puntos = 1050
    posy_puntos = -10
    if (0 < tiempo <= 60):
        time.sleep(time2)
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            time.sleep(pluspun)
            VN1.delete(puntos1)
            cont_pu2 += 65
        if (vel_map != 0):
            puntos1 = VN1.create_image(posx_puntos + cont_pu1, posy_puntos + cont_pu2, image=carro_puntos)
            if ((posx_puntos + cont_pu1) == (pxcar2 + i2) and (posy_puntos + cont_pu2) == (pycar2 + j2)):
                VN1.delete(puntos1)
                gasolina2 += 20
                puntaje1 += 200
                time.sleep(0.5)
                Car_Puntos()
            else:
                VN1.delete(puntos1)
                time.sleep(time2)
                Car_Puntos2()


def Car_enemigo1():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, enemigo1, x, masgas, VN1, plusene1, gasolina, i, i2, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75]
    tiemporandom = [2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4]
    salida = random.choice(tiemporandom)
    cont_en1 = random.choice(lista)
    cont_en2 = 0
    posx_ene1 = 343
    posy_ene2 = -120
    if (0 < tiempo <= 60):
        time.sleep(salida)
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            enemigox_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
            if ((posx_ene1 + cont_en1) == (pxcar1 + i) and (posy_ene2 + cont_en2) == 600):
                VN1.delete(enemigo_1)
                VN1.delete(x)
                GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
                x = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=Explosion)
                velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=255)
                velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=610)
                i = None
                i2 = None
                vel_map = 0
            else:
                cont_en2 += 15
                enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
                time.sleep(plusene1)
                if ((posx_ene1 + cont_en1) == (pxcar1 + i) and (posy_ene2 + cont_en2) == 615):
                    VN1.delete(enemigo_1)
                    VN1.delete(x)
                    GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
                    x = VN1.create_image(((posx_ene1 + cont_en1) - 10), posy_ene2 + cont_en2, image=Explosion)
                    velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=255)
                    velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=610)
                    i = None
                    i2 = None
                    vel_map = 0
                else:
                    VN1.delete(enemigo_1)
                    time.sleep(salida)
                    Car_enemigo1()


def Car_enemigo21():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, enemigo1, x, masgas, plusene1, VN1, gasolina, i, i2, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75]
    tiemporandom = [2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4]
    salida = random.choice(tiemporandom)
    cont_en1 = random.choice(lista)
    cont_en2 = 0
    posx_ene1 = 1050
    posy_ene2 = -120
    if (0 < tiempo <= 60):
        time.sleep(salida)
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            enemigox_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1 + plusene1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0 + plusene1):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0 + plusene1):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
        if (vel_map != 0):
            enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
            time.sleep(plusene1)
            VN1.delete(enemigo_1)
            cont_en2 += 60
            if ((posx_ene1 + cont_en1) == (pxcar2 + i2) and (posy_ene2 + cont_en2) == 600):
                VN1.delete(enemigo_1)
                VN1.delete(y)
                GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
                y = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=Explosion)
                velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=255)
                velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=610)
                i = None
                i2 = None
                vel_map = 0
            else:
                cont_en2 += 15
                enemigo_1 = VN1.create_image(posx_ene1 + cont_en1, posy_ene2 + cont_en2, image=enemigo1)
                time.sleep(plusene1)
                if ((posx_ene1 + cont_en1) == (pxcar2 + i2) and (posy_ene2 + cont_en2) == 615):
                    VN1.delete(enemigo_1)
                    VN1.delete(y)
                    GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
                    y = VN1.create_image(((posx_ene1 + cont_en1) - 10), posy_ene2 + cont_en2, image=Explosion)
                    velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=255)
                    velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=610)
                    i = None
                    i2 = None
                    vel_map = 0
                else:
                    VN1.delete(enemigo_1)
                    time.sleep(salida)
                    Car_enemigo1()


def Car_enemigo2():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, enemigo2, x, puntaje, VN1, plusene2, gasolina, cont_ene21, i, i2, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75, 0, 0, 75, -75, -75, 0, 75, 75]
    lista2 = [-75, 75, 0, -75, 75, 0, 75, -75, 0]
    tiemporandom = [1.7, 1.8, 1.9, 2.0, 2.1]
    salida = random.choice(tiemporandom)
    cont_ene21 = random.choice(lista2)
    cont_ene2 = random.choice(lista)
    cont_ene22 = 0
    posx_ene2 = 343
    posy_ene2 = -120
    if (0 < tiempo <= 60):
        time.sleep(5.0)
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
            if ((posx_ene2 + cont_ene21) == (pxcar1 + i) and (posy_ene2 + cont_ene22) == 600):
                VN1.delete(enemigo_2)
                VN1.delete(x)
                GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
                x = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=Explosion)
                velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=255)
                velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=610)
                i = None
                i2 = None
                vel_map = 0
            else:
                cont_ene22 += 15
                enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
                time.sleep(plusene2)
                if ((posx_ene2 + cont_ene21) == (pxcar1 + i) and (posy_ene2 + cont_ene22) == 615):
                    VN1.delete(enemigo_2)
                    VN1.delete(x)
                    GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
                    x = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=Explosion)
                    velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=255)
                    velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=610)
                    i = None
                    i2 = None
                    vel_map = 0
                else:
                    VN1.delete(enemigo_2)
                    time.sleep(salida)
                    Car_enemigo2()


def Car_enemigo22():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, enemigo2, x, puntaje, plusene2, VN1, gasolina, cont_ene21, i, i2, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75, 0, 0, 75, -75, -75, 0, 75, 75]
    lista2 = [-75, 75, 0, -75, 75, 0, 75, -75, 0]
    tiemporandom = [1.7, 1.8, 1.9, 2.0, 2.1]
    salida = random.choice(tiemporandom)
    cont_ene21 = random.choice(lista2)
    cont_ene2 = random.choice(lista)
    cont_ene22 = 0
    posx_ene2 = 1050
    posy_ene2 = -120
    if (0 < tiempo <= 60):
        time.sleep(5.0)
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene2, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
        if (vel_map != 0):
            enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
            time.sleep(plusene2)
            VN1.delete(enemigo_2)
            cont_ene22 += 60
            if ((posx_ene2 + cont_ene21) == (pxcar2 + i2) and (posy_ene2 + cont_ene22) == 600):
                VN1.delete(enemigo_2)
                VN1.delete(y)
                GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
                y = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=Explosion)
                velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=255)
                velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=610)
                i = None
                i2 = None
                vel_map = 0
            else:
                cont_ene22 += 15
                enemigo_2 = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=enemigo2)
                time.sleep(plusene2)
                if ((posx_ene2 + cont_ene21) == (pxcar2 + i2) and (posy_ene2 + cont_ene22) == 615):
                    VN1.delete(enemigo_2)
                    VN1.delete(y)
                    GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
                    y = VN1.create_image(posx_ene2 + cont_ene21, posy_ene2 + cont_ene22, image=Explosion)
                    velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=255)
                    velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=610)
                    i = None
                    i2 = None
                    vel_map = 0
                else:
                    VN1.delete(enemigo_2)
                    time.sleep(salida)
                    Car_enemigo22()


def Car_enemigo3():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, enemigo3, x, plusene3, puntaje, VN1, gasolina, i, i2, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75, 0, 0, 75, -75, -75, 0, 75, 75]
    lista2 = [-75, 75, 0, -75, 75, 0, 75, -75, 0]
    tiemporandom = [1.0, 1.2, 1.3, 1.4, 1.6]
    salida = random.choice(tiemporandom)
    cont_ene31 = random.choice(lista2)
    cont_ene3 = random.choice(lista)
    cont_ene32 = 0
    posx_ene3 = 343
    posy_ene3 = -120
    if (0 < tiempo <= 60):
        time.sleep(salida)
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + i, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + i, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
            if ((posx_ene3 + cont_ene31) == (pxcar1 + i) and (posy_ene3 + cont_ene32) == 600):
                VN1.delete(enemigo_3)
                VN1.delete(x)
                GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
                x = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=Explosion)
                velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=255)
                velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=610)
                i = None
                i2 = None
                vel_map = 0
            else:
                cont_ene32 += 15
                enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
                time.sleep(plusene3)
                if ((posx_ene3 + cont_ene31) == (pxcar1 + i) and (posy_ene3 + cont_ene32) == 615):
                    VN1.delete(enemigo_3)
                    VN1.delete(x)
                    GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
                    x = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=Explosion)
                    velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=255)
                    velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=610)
                    i = None
                    i2 = None
                    vel_map = 0
                else:
                    VN1.delete(enemigo_3)
                    time.sleep(salida)
                    Car_enemigo3()


def Car_enemigo23():
    """se crea el auto que genera gasolina"""
    global Ven1, Ven2, NIVELES1, mapa1, enemigo3, x, puntaje, plusene3, VN1, gasolina, i, i2, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    lista = [75, 0, -75, 0, 0, 75, -75, -75, 0, 75, 75]
    lista2 = [-75, 75, 0, -75, 75, 0, 75, -75, 0]
    tiemporandom = [1.0, 1.2, 1.3, 1.4, 1.6]
    salida = random.choice(tiemporandom)
    cont_ene31 = random.choice(lista2)
    cont_ene3 = random.choice(lista)
    cont_ene32 = 0
    posx_ene3 = 1050
    posy_ene3 = -120
    if (0 < tiempo <= 60):
        time.sleep(salida)
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene3, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + i, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + i, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
        if (vel_map != 0):
            enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
            time.sleep(plusene3)
            VN1.delete(enemigo_3)
            cont_ene32 += 60
            if ((posx_ene3 + cont_ene31) == (pxcar2 + i2) and (posy_ene3 + cont_ene32) == 600):
                VN1.delete(enemigo_3)
                VN1.delete(y)
                GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
                y = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=Explosion)
                velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=255)
                velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                           width=7).place(x=575, y=610)
                i = None
                i2 = None
                vel_map = 0
            else:
                cont_ene32 += 15
                enemigo_3 = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=enemigo3)
                time.sleep(plusene3)
                if ((posx_ene3 + cont_ene31) == (pxcar2 + i2) and (posy_ene3 + cont_ene32) == 615):
                    VN1.delete(enemigo_3)
                    VN1.delete(y)
                    GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
                    y = VN1.create_image(posx_ene3 + cont_ene31, posy_ene3 + cont_ene32, image=Explosion)
                    velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=255)
                    velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                               width=7).place(x=575, y=610)
                    i = None
                    i2 = None
                    vel_map = 0
                else:
                    VN1.delete(enemigo_3)
                    time.sleep(salida)
                    Car_enemigo23()


## aqui se hace uso de keysym que detecta la tecla pulsada y esta genera una accion
def Mov_Carro1(event):
    """se crea la funcion que permite mover al carro1 en las direcciones (derecha) (izquierda) """
    global Ven1, Ven2, NIVELES1, puntos, mapa1, VN1, velocidad, pxcar1, pycar1, velocidad1, velocidad2, gasolina, p, i, i2, j, Game_Over, CARRO1, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    if (event.keysym == "d" or event.keysym == "D"):
        if (i < 75):
            VN1.delete(x)
            i = i + 75
            x = VN1.create_image(pxcar1 + i, pycar1 + j, image=CARRO1)
        else:
            VN1.delete(x)
            x = VN1.create_image(380 + i, 640 + j, image=Explosion)
            vel_map = 0
            GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
            i = None
            i2 = None
            VN1.delete(velocidad1)
            VN1.delete(velocidad2)
            velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=255)
            velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=610)

    if (event.keysym == "a" or event.keysym == "A"):
        if (i > -75):
            VN1.delete(x)
            i = i - 75
            x = VN1.create_image(pxcar1 + i, pycar1 + j, image=CARRO1)
        else:
            VN1.delete(x)
            x = VN1.create_image(300 + i, 640 + j, image=Explosion)
            vel_map = 0
            GameOver_1 = VN1.create_image(343, 200, image=Game_Over)
            i = None
            i2 = None
            velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=255)
            velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=610)


def Mov_Carro2(event):
    """se crea la funcion que permite mover al carro2 en las direcciones (derecha) (izquierda) """
    global Ven1, Ven2, NIVELES1, mapa1, VN1, velocidad, p, velocidad1, pxcar2, pycar2, velocidad2, puntos, i, j, Game_Over, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    if (event.keysym == "Right"):
        if (i2 < 75):
            VN1.delete(y)
            i2 = i2 + 75
            y = VN1.create_image(pxcar2 + i2, pycar2 + j2, image=CARRO2)
        else:
            VN1.delete(y)
            y = VN1.create_image(1087 + i2, 640 + j2, image=Explosion)
            vel_map = 0
            GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
            i2 = None
            i = None
            velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=255)
            velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=610)

    if (event.keysym == "Left"):
        if (i2 > -75):
            VN1.delete(y)
            i2 = i2 - 75
            y = VN1.create_image(pxcar2 + i2, pycar2 + j2, image=CARRO2)
        else:
            VN1.delete(y)
            y = VN1.create_image(1007 + i2, 640 + j2, image=Explosion)
            vel_map = 0
            GameOver_1 = VN1.create_image(1050, 200, image=Game_Over)
            i2 = None
            i = None
            velocidad3 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=255)
            velocidad4 = tkinter.Label(VN1, text=str(0) + "km/H", font=("Arial", 12), bg="#BFFFBF ", fg="red",
                                       width=7).place(x=575, y=610)


def return_1():
    """devuelve al menu"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, enemigo1, plusene1, plusene2, plusene3, pluspun, enemigo2, enemigo3, derrape_1, derrape_2, derrape2_1, derrape2_2, carro_puntos, pausa_1, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VenNivel1.destroy()
    Ven1.deiconify()


# se crea el nivel uno con sus respectivas dimensiones y graficos
def nivel_1():
    """se crea la ventana de nivel 1"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, enemigo1, plusene1, plusene2, plusene3, pluspun, enemigo2, enemigo3, derrape_1, derrape_2, derrape2_1, derrape2_2, carro_puntos, pausa_1, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VenNivel1 = tkinter.Toplevel(Ven1)
    VenNivel1.geometry("1200x718+100+0")
    VenNivel1.maxsize(1200, 718)
    VenNivel1.minsize(1200, 718)
    Ven2.destroy()
    i = 0
    j = 0
    i2 = 0
    j2 = 0
    plusene1 = 0.7
    plusene2 = 0.6
    plusene3 = 0.5
    pluspun = 0.5
    pxcar1 = 343
    pycar1 = 640
    pxcar2 = 1050
    pycar2 = 640
    vel_map = 5
    volver = tkinter.PhotoImage(file="C:\graficos\\back.gif")
    Game_Over = tkinter.PhotoImage(file="C:\graficos\\gameover.png")
    NIVELES1 = tkinter.PhotoImage(file="C:\graficos\\NIVEL1completo.gif")
    CARRO1 = tkinter.PhotoImage(file="C:\graficos\\carro1.png")
    CARRO2 = tkinter.PhotoImage(file="C:\graficos\\carro2.png")
    Explosion = tkinter.PhotoImage(file="C:\graficos\\explosion.png")
    singas = tkinter.PhotoImage(file="C:\graficos\\singasolina.png")
    pos_car1 = tkinter.PhotoImage(file="C:\graficos\\posx.png")
    pos_car2 = tkinter.PhotoImage(file="C:\graficos\\posy.png")
    carro_puntos = tkinter.PhotoImage(file="C:\graficos\\puntos.png")
    enemigo1 = tkinter.PhotoImage(file="C:\graficos\\enemigo1.png")
    enemigo2 = tkinter.PhotoImage(file="C:\graficos\\enemigo2.png")
    enemigo3 = tkinter.PhotoImage(file="C:\graficos\\enemigo3.png")
    VN1 = tkinter.Canvas(VenNivel1, bg="red", width=1200, height=720)
    VN1.pack()
    x = VN1.create_image(pxcar1, pycar1, image=CARRO1)
    y = VN1.create_image(pxcar2, pycar2, image=CARRO2)
    p = VN1.create_image(602, -2200, image=NIVELES1)
    estadisticas = tkinter.PhotoImage(file="C:\graficos\\estadisticas.png")
    estadisticas_1 = tkinter.Label(VN1, image=estadisticas).place(x=496, y=0)
    NombreJugador1 = tkinter.Label(VN1, textvariable=entradaJ1, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=125)
    NombreJugador2 = tkinter.Label(VN1, textvariable=entradaJ2, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=478)
    botonback = tkinter.Button(VenNivel1, image=volver, command=return_1).place(x=1100, y=10)
    VN1.lower(p)
    tres()
    VenNivel1.mainloop()


# esto es lo que permite al mapa moverse y llama las teclas para poder mover los carros
def FONDO_MOV():
    """ se crea un ciclo de recursion para poder mover el mapa, vel_map = a los pixeles en el eje de y que se mueve"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, p, i, x, y, posx, posy, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VN1.delete(one_1)
    VN1.delete(one_2)
    VN1.bind_all("<KeyPress-a>", Mov_Carro1)
    VN1.bind_all("<KeyPress-d>", Mov_Carro1)
    VN1.bind_all("<KeyPress-A>", Mov_Carro1)
    VN1.bind_all("<KeyPress-D>", Mov_Carro1)
    VN1.bind_all("<KeyPress-Left>", Mov_Carro2)
    VN1.bind_all("<KeyPress-Right>", Mov_Carro2)
    VN1.focus_set()
    cont1 = 0
    cont2 = 0
    if (cont1 < 5):
        VN1.move(p, 0, vel_map)
        cont1 = cont1 + 1
        cont2 = cont2 + 1
        VenNivel1.after(1, FONDO_MOV)
    if (VN1.coords(p)[1] > 2500):
        VN1.move(p, 0, -VN1.coords(p)[1])


def nivel_2():
    """se crea la ventana de nivel 2"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, enemigo1, plusene1, plusene2, plusene3, pluspun, enemigo2, enemigo3, derrape_1, derrape_2, derrape2_1, derrape2_2, carro_puntos, pausa_1, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VenNivel1 = tkinter.Toplevel(Ven1)
    VenNivel1.geometry("1200x718+100+0")
    VenNivel1.maxsize(1200, 718)
    VenNivel1.minsize(1200, 718)
    Ven2.destroy()
    plusene1 = 0.6
    plusene2 = 0.5
    plusene3 = 0.4
    pluspun = 0.4
    i = 0
    j = 0
    i2 = 0
    j2 = 0
    pxcar1 = 343
    pycar1 = 640
    pxcar2 = 1050
    pycar2 = 640
    vel_map = 6
    volver = tkinter.PhotoImage(file="C:\graficos\\back.gif")
    Game_Over = tkinter.PhotoImage(file="C:\graficos\\gameover.png")
    NIVELES1 = tkinter.PhotoImage(file="C:\graficos\\NIVEL2completo.gif")
    CARRO1 = tkinter.PhotoImage(file="C:\graficos\\carro1.png")
    CARRO2 = tkinter.PhotoImage(file="C:\graficos\\carro2.png")
    Explosion = tkinter.PhotoImage(file="C:\graficos\\explosion.png")
    singas = tkinter.PhotoImage(file="C:\graficos\\singasolina.png")
    pos_car1 = tkinter.PhotoImage(file="C:\graficos\\posx.png")
    pos_car2 = tkinter.PhotoImage(file="C:\graficos\\posy.png")
    carro_puntos = tkinter.PhotoImage(file="C:\graficos\\puntos.png")
    enemigo1 = tkinter.PhotoImage(file="C:\graficos\\enemigo1.png")
    enemigo2 = tkinter.PhotoImage(file="C:\graficos\\enemigo2.png")
    enemigo3 = tkinter.PhotoImage(file="C:\graficos\\enemigo3.png")
    VN1 = tkinter.Canvas(VenNivel1, bg="red", width=1200, height=720)
    VN1.pack()
    x = VN1.create_image(pxcar1, pycar1, image=CARRO1)
    y = VN1.create_image(pxcar2, pycar2, image=CARRO2)
    p = VN1.create_image(602, -2200, image=NIVELES1)
    estadisticas = tkinter.PhotoImage(file="C:\graficos\\estadisticas.png")
    estadisticas_1 = tkinter.Label(VN1, image=estadisticas).place(x=496, y=0)
    NombreJugador1 = tkinter.Label(VN1, textvariable=entradaJ1, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=125)
    NombreJugador2 = tkinter.Label(VN1, textvariable=entradaJ2, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=478)
    botonback = tkinter.Button(VenNivel1, image=volver, command=return_1).place(x=1100, y=10)
    VN1.lower(p)
    tres()
    VenNivel1.mainloop()


# esto es lo que permite al mapa moverse y llama las teclas para poder mover los carros

def nivel_3():
    """se crea la ventana de nivel 3"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, enemigo1, plusene1, volver, plusene2, plusene3, pluspun, enemigo2, enemigo3, derrape_1, derrape_2, derrape2_1, derrape2_2, carro_puntos, pausa_1, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VenNivel1 = tkinter.Toplevel(Ven1)
    VenNivel1.geometry("1200x718+100+0")
    VenNivel1.maxsize(1200, 718)
    VenNivel1.minsize(1200, 718)
    Ven2.destroy()
    plusene1 = 0.5
    plusene2 = 0.4
    plusene3 = 0.3
    pluspun = 0.3
    i = 0
    j = 0
    i2 = 0
    j2 = 0
    pxcar1 = 343
    pycar1 = 640
    pxcar2 = 1050
    pycar2 = 640
    vel_map = 7
    volver = tkinter.PhotoImage(file="C:\graficos\\back.gif")
    Game_Over = tkinter.PhotoImage(file="C:\graficos\\gameover.png")
    NIVELES1 = tkinter.PhotoImage(file="C:\graficos\\NIVEL3completo.png")
    CARRO1 = tkinter.PhotoImage(file="C:\graficos\\carro1.png")
    CARRO2 = tkinter.PhotoImage(file="C:\graficos\\carro2.png")
    Explosion = tkinter.PhotoImage(file="C:\graficos\\explosion.png")
    singas = tkinter.PhotoImage(file="C:\graficos\\singasolina.png")
    pos_car1 = tkinter.PhotoImage(file="C:\graficos\\posx.png")
    pos_car2 = tkinter.PhotoImage(file="C:\graficos\\posy.png")
    carro_puntos = tkinter.PhotoImage(file="C:\graficos\\puntos.png")
    enemigo1 = tkinter.PhotoImage(file="C:\graficos\\enemigo1.png")
    enemigo2 = tkinter.PhotoImage(file="C:\graficos\\enemigo2.png")
    enemigo3 = tkinter.PhotoImage(file="C:\graficos\\enemigo3.png")
    VN1 = tkinter.Canvas(VenNivel1, bg="red", width=1200, height=720)
    VN1.pack()
    x = VN1.create_image(pxcar1, pycar1, image=CARRO1)
    y = VN1.create_image(pxcar2, pycar2, image=CARRO2)
    p = VN1.create_image(602, -2200, image=NIVELES1)
    estadisticas = tkinter.PhotoImage(file="C:\graficos\\estadisticas.png")
    estadisticas_1 = tkinter.Label(VN1, image=estadisticas).place(x=496, y=0)
    NombreJugador1 = tkinter.Label(VN1, textvariable=entradaJ1, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=125)
    NombreJugador2 = tkinter.Label(VN1, textvariable=entradaJ2, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=478)
    botonback = tkinter.Button(VenNivel1, image=volver, command=return_1).place(x=1100, y=10)
    VN1.lower(p)
    tres()
    VenNivel1.mainloop()


def nivel_4():
    """se crea la ventana de nivel 4"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, enemigo1, plusene1, plusene2, plusene3, pluspun, enemigo2, enemigo3, derrape_1, derrape_2, derrape2_1, derrape2_2, carro_puntos, pausa_1, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VenNivel1 = tkinter.Toplevel(Ven1)
    VenNivel1.geometry("1200x718+100+0")
    VenNivel1.maxsize(1200, 718)
    VenNivel1.minsize(1200, 718)
    Ven2.destroy()
    plusene1 = 0.4
    plusene2 = 0.3
    plusene3 = 0.2
    pluspun = 0.2
    i = 0
    j = 0
    i2 = 0
    j2 = 0
    pxcar1 = 343
    pycar1 = 640
    pxcar2 = 1050
    pycar2 = 640
    vel_map = 8
    volver = tkinter.PhotoImage(file="C:\graficos\\back.gif")
    Game_Over = tkinter.PhotoImage(file="C:\graficos\\gameover.png")
    NIVELES1 = tkinter.PhotoImage(file="C:\graficos\\NIVEL4completo.png")
    CARRO1 = tkinter.PhotoImage(file="C:\graficos\\carro1.png")
    CARRO2 = tkinter.PhotoImage(file="C:\graficos\\carro2.png")
    Explosion = tkinter.PhotoImage(file="C:\graficos\\explosion.png")
    singas = tkinter.PhotoImage(file="C:\graficos\\singasolina.png")
    pos_car1 = tkinter.PhotoImage(file="C:\graficos\\posx.png")
    pos_car2 = tkinter.PhotoImage(file="C:\graficos\\posy.png")
    carro_puntos = tkinter.PhotoImage(file="C:\graficos\\puntos.png")
    enemigo1 = tkinter.PhotoImage(file="C:\graficos\\enemigo1.png")
    enemigo2 = tkinter.PhotoImage(file="C:\graficos\\enemigo2.png")
    enemigo3 = tkinter.PhotoImage(file="C:\graficos\\enemigo3.png")
    VN1 = tkinter.Canvas(VenNivel1, bg="red", width=1200, height=720)
    VN1.pack()
    x = VN1.create_image(pxcar1, pycar1, image=CARRO1)
    y = VN1.create_image(pxcar2, pycar2, image=CARRO2)
    p = VN1.create_image(602, -2200, image=NIVELES1)
    estadisticas = tkinter.PhotoImage(file="C:\graficos\\estadisticas.png")
    estadisticas_1 = tkinter.Label(VN1, image=estadisticas).place(x=496, y=0)
    NombreJugador1 = tkinter.Label(VN1, textvariable=entradaJ1, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=125)
    NombreJugador2 = tkinter.Label(VN1, textvariable=entradaJ2, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=478)
    botonback = tkinter.Button(VenNivel1, image=volver, command=return_1).place(x=1100, y=10)
    VN1.lower(p)
    tres()
    VenNivel1.mainloop()


def nivel_5():
    """se crea la ventana de nivel 5"""
    global Ven1, Ven2, NIVELES1, mapa1, VN1, enemigo1, plusene1, plusene2, plusene3, pluspun, enemigo2, enemigo3, derrape_1, derrape_2, derrape2_1, derrape2_2, carro_puntos, pausa_1, pxcar1, pycar1, pxcar2, pycar2, pos_car1, p, pos_car2, i, Game_Over, singas, j, i2, j2, CARRO1, CARRO2, Explosion, Posx_Carro1, x, y, VenNivel1, vel_map, info, three, two, one, three_1, one_1, two_1, three2, two2, one2, three_2, one_2, two_2
    VenNivel1 = tkinter.Toplevel(Ven1)
    VenNivel1.geometry("1200x718+100+0")
    VenNivel1.maxsize(1200, 718)
    VenNivel1.minsize(1200, 718)
    Ven2.destroy()
    plusene1 = 0.3
    plusene2 = 0.2
    plusene3 = 0.1
    pluspun = 0.1
    i = 0
    j = 0
    i2 = 0
    j2 = 0
    pxcar1 = 343
    pycar1 = 640
    pxcar2 = 1050
    pycar2 = 640
    vel_map = 9
    volver = tkinter.PhotoImage(file="C:\graficos\\back.gif")
    Game_Over = tkinter.PhotoImage(file="C:\graficos\\gameover.png")
    NIVELES1 = tkinter.PhotoImage(file="C:\graficos\\NIVEL5completo.gif")
    CARRO1 = tkinter.PhotoImage(file="C:\graficos\\carro1.png")
    CARRO2 = tkinter.PhotoImage(file="C:\graficos\\carro2.png")
    Explosion = tkinter.PhotoImage(file="C:\graficos\\explosion.png")
    singas = tkinter.PhotoImage(file="C:\graficos\\singasolina.png")
    pos_car1 = tkinter.PhotoImage(file="C:\graficos\\posx.png")
    pos_car2 = tkinter.PhotoImage(file="C:\graficos\\posy.png")
    carro_puntos = tkinter.PhotoImage(file="C:\graficos\\puntos.png")
    enemigo1 = tkinter.PhotoImage(file="C:\graficos\\enemigo1.png")
    enemigo2 = tkinter.PhotoImage(file="C:\graficos\\enemigo2.png")
    enemigo3 = tkinter.PhotoImage(file="C:\graficos\\enemigo3.png")
    VN1 = tkinter.Canvas(VenNivel1, bg="red", width=1200, height=720)
    VN1.pack()
    x = VN1.create_image(pxcar1, pycar1, image=CARRO1)
    y = VN1.create_image(pxcar2, pycar2, image=CARRO2)
    p = VN1.create_image(602, -2200, image=NIVELES1)
    estadisticas = tkinter.PhotoImage(file="C:\graficos\\estadisticas.png")
    estadisticas_1 = tkinter.Label(VN1, image=estadisticas).place(x=496, y=0)
    NombreJugador1 = tkinter.Label(VN1, textvariable=entradaJ1, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=125)
    NombreJugador2 = tkinter.Label(VN1, textvariable=entradaJ2, font=("Forte", 12), bg="#BFFFBF").place(x=546, y=478)
    botonback = tkinter.Button(VenNivel1, image=volver, command=return_1).place(x=1100, y=10)
    VN1.lower(p)
    tres()
    VenNivel1.mainloop()


# COMENZAMOS COLOCANDO EL FONDO ARTESANAL
FondoPantalla = tkinter.PhotoImage(file="C:\graficos\\FONDO.gif")
lblImagen = tkinter.Label(Ven1, image=FondoPantalla).place(x=0, y=0)

# Ven1 DE JUGADORES
# jugador1
JUGADOR1 = tkinter.PhotoImage(file="C:\graficos\\JUGADOR1.gif")
lbljugador1 = tkinter.Label(Ven1, image=JUGADOR1).place(x=10, y=500)
entradaJ1 = tkinter.StringVar()
entradaJ1.set("")
txtjUGADOR1 = tkinter.Entry(Ven1, textvariable=entradaJ1).place(x=205, y=520)

# jugador2
JUGADOR2 = tkinter.PhotoImage(file="C:\graficos\\JUGADOR2.gif")
lbljugador2 = tkinter.Label(Ven1, image=JUGADOR2).place(x=10, y=600)
entradaJ2 = tkinter.StringVar()
entradaJ2.set("")
txtjUGADOR1 = tkinter.Entry(Ven1, textvariable=entradaJ2).place(x=205, y=620)

# CREACION DE BOTON EMPEZAR
fondoboton = tkinter.PhotoImage(file="C:\graficos\\PLAY.gif")
btnInicio = tkinter.Button(Ven1, image=fondoboton, command=segundaventana).place(x=540, y=480)
# CREACION DE BOTON SALIR
fondoboton2 = tkinter.PhotoImage(file="C:\graficos\\SALIR.gif")
btnSalir = tkinter.Button(Ven1, image=fondoboton2, command=Ven1.destroy).place(x=780, y=530)

# COMO JUGAR
fondoboton3 = tkinter.PhotoImage(file="C:\graficos\\instrucciones.png")
btnInstruc = tkinter.Button(Ven1, image=fondoboton3, command=info).place(x=1110, y=10)

Ven1.mainloop()






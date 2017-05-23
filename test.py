import tkinter
from time import sleep
#globalizo  y creo la ventana

global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,fondo32,uno,two,one,contador

Ven1=tkinter.Tk()
Ven1.geometry("1200x680+100+0")
Ven1.config(bg="black")
Ven1.title("Avoid Cars")
Ven1.maxsize(1200, 680)
Ven1.minsize(1200, 680)

fondo32=tkinter.PhotoImage(file="instrucciones2.png")

def info():
  global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,fondo32,uno,two,contador
  info=tkinter.Toplevel(Ven1)
  info.geometry("700x700+100+0")
  info.config(bg="black")
  info.title("Avoid Cars INSTRUCCIONES")
  lblinstrucciones=tkinter.Label(info,image=fondo32).place(x=0,y=0)
  info.mainloop()

def segundaventana():
  global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,uno,two,contador
  """ se  crea una ventana hija para hacer el menu de niveles"""
  Ven2 =tkinter.Toplevel(Ven1)
  Ven1.iconify()
  Ven2.geometry("1200x720+100+0")
  Ven2.title("Avoid Cars")
  Ven2.maxsize(1200, 680)
  Ven2.minsize(1200, 680)
  niveles=tkinter.PhotoImage(file="FONDO2.gif")
  NIVELES=tkinter.Label(Ven2,image=niveles).place(x=0,y=0)

  #SELECCION DE NIVELES

  imanivel1=tkinter.PhotoImage(file="NIVEL1.gif")
  nivel1=tkinter.Button(Ven2,image=imanivel1,command=nivel_1).place(x=200,y=120)

  imanivel2=tkinter.PhotoImage(file="NIVEL2.gif")
  nivel2=tkinter.Button(Ven2,image=imanivel2,command=nivel_2).place(x=500,y=120)


  imanivel3=tkinter.PhotoImage(file="NIVEL3.gif")
  nivel3=tkinter.Button(Ven2,image=imanivel3,command=nivel_3).place(x=800,y=120)


  imanivel4=tkinter.PhotoImage(file="NIVEL4.gif")
  nivel4=tkinter.Button(Ven2,image=imanivel4,command=nivel_4).place(x=350,y=400)


  imanivel5=tkinter.PhotoImage(file="NIVEL5.gif")
  nivel5=tkinter.Button(Ven2,image=imanivel5,command=nivel_5).place(x=650,y=400)

  Ven2.mainloop()


#funcion de conteo regresivo
def tres():
  """Se crea la funcion que genera el numero 3 en la pantalla del lvl 1"""
  global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,three,two,one,three_1,one_1,two_1
  three   = tkinter.PhotoImage(file="THREE.gif")
  three_1 = VN1.create_image(343,200,image=three)
def dos():
  """sasa"""
  global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,three,two,one,three_1,one_1,two_1
  VN1.delete(three_1)
  two = tkinter.PhotoImage(file="TWO.gif")
  two_1 =VN1.create_image(343,200,image=two)
def uno():
  """sasas"""
  global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,three,two,one,three_1,one_1,two_1
  VN1.delete(two_1)
  one = tkinter.PhotoImage(file="ONE.gif")
  one_1 =VN1.create_image(343,200,image=one)

def cuenta_cuentaregresiva():
  """SASA"""
  global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,three,two,one,three_1,one_1,two_1
  tres()
  sleep(0.2)
  dos()
  sleep(0.2)
  uno()
  sleep(0.2)
  VN1.delete(one_1)
  FONDO_MOV()

i = 0
posx1 = 50
posy1 = 50
posx2 = 250
posy2 = 400

NIVELES1 = tkinter.PhotoImage(file="NIVEL1completo.gif")
CARRO1   = tkinter.PhotoImage(file="carro1.png")
CARRO2   = tkinter.PhotoImage(file="carro2.png")

def nivel_1():
    """se define el nivel 1 """
    global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,three
    VenNivel1 = tkinter.Toplevel(Ven1)
    VenNivel1.geometry("1200x720+100+0")
    Ven2.destroy()
#se coloca la imagen
    VN1 = tkinter.Canvas(VenNivel1,bg="red",width=1200, height=720)
    VN1.pack()

    x   = VN1.create_image(343,640,image=CARRO1)
    y   = VN1.create_image(1050,640,image=CARRO2)
    p = VN1.create_image(602,-2200,image=NIVELES1)
    VN1.lower(p)
    cuenta_cuentaregresiva()
    VenNivel1.mainloop()

def FONDO_MOV():
    """ se crea un ciclo de recursion para poder mover el mapa"""
    global Ven1,Ven2,NIVELES1,mapa1,VN1,p,i,posx1,posy1,posx2,posy2,VenNivel1,velmap,info,three

    velmap = 2.5
    cont1=0
    cont2=0
    if(cont1<5):
        VN1.move(p,0,velmap)
        cont1=cont1+1
        cont2=cont2+1
        VenNivel1.after(1,FONDO_MOV)
    if(VN1.coords(p)[1]>2500):
        VN1.move(p,0,-VN1.coords(p)[1])

def nivel_2():
  print ("sanchez gay")

def nivel_3():
  print ("sanchez gay")

def nivel_4():
  print ("sanchez gay")

def nivel_5():
  print ("sanchez gay")

#COMENZAMOS COLOCANDO EL FONDO ARTESANAL
FondoPantalla=tkinter.PhotoImage(file="FONDO.gif")
lblImagen=tkinter.Label(Ven1,image=FondoPantalla).place(x=0,y=0)

#Ven1 DE JUGADORES
#jugador1
JUGADOR1=tkinter.PhotoImage(file="JUGADOR1.gif")
lbljugador1=tkinter.Label(Ven1,image=JUGADOR1).place(x=10,y=500)
entradaJ1=tkinter.StringVar()
entradaJ1.set("")
txtjUGADOR1=tkinter.Entry(Ven1,textvariable=entradaJ1).place(x=205,y=520)


#jugador2
JUGADOR2=tkinter.PhotoImage(file="JUGADOR2.gif")
lbljugador2=tkinter.Label(Ven1, image=JUGADOR2).place(x=10,y=600)
entradaJ2=tkinter.StringVar()
entradaJ2.set("")
txtjUGADOR1=tkinter.Entry(Ven1,textvariable=entradaJ2).place(x=205,y=620)

#CREACION DE BOTON EMPEZAR
fondoboton=tkinter.PhotoImage(file="PLAY.gif")
btnInicio=tkinter.Button(Ven1, image=fondoboton,command=segundaventana).place(x=540,y=480)
#CREACION DE BOTON SALIR
fondoboton2=tkinter.PhotoImage(file="SALIR.gif")
btnSalir=tkinter.Button(Ven1, image=fondoboton2,command=Ven1.destroy).place(x=780,y=530)

#COMO JUGAR
fondoboton3=tkinter.PhotoImage(file="instrucciones.png")
btnInstruc=tkinter.Button(Ven1, image=fondoboton3,command=info).place(x=1110,y=10)

Ven1.mainloop()

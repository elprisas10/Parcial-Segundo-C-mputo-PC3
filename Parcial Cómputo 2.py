#INTEGRANTES: Jonathan Elias Gamez Larin SMIS017821
            #Saúl Oswaldo López Hernández SMIS108421
         
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Radiobutton, IntVar


#Creamos la ventana con su tamaño

ventana1= Tk()
ventana1.geometry("500x500")


#Añadimos las imagenes para ser mostradas agregando un efecto y ajustando su tamaño

pre1 = Image.open("Carne Asada.jpg")
pre1 = pre1.resize((70,70), Image.ANTIALIAS)

img = ImageTk.PhotoImage(pre1)
pre1 = Label(ventana1, image = img)


pre2 = Image.open("pollo asado.jpg")
pre2= pre2.resize((70,70), Image.ANTIALIAS)

img2 = ImageTk.PhotoImage(pre2)
pre2 = Label(ventana1, image = img2)


pre3 = Image.open("lasagna-receta.jpg")
pre3 = pre3.resize((70,70), Image.ANTIALIAS)

img3 = ImageTk.PhotoImage(pre3)
pre3 = Label(ventana1, image = img3)


pre4 = Image.open("Ensalada de Vegetales y Nueces.jpg")
pre4= pre4.resize((70,70), Image.ANTIALIAS)

img4 = ImageTk.PhotoImage(pre4)
pre4 = Label(ventana1, image = img4)


pre5 = Image.open("Coditos.jpg")
pre5 = pre5.resize((70,70), Image.ANTIALIAS)

img5 = ImageTk.PhotoImage(pre5)
pre5 = Label(ventana1, image = img5)


pre6 = Image.open("ensalada-rusa.jpg")
pre6 = pre6.resize((70,70), Image.ANTIALIAS)

img6 = ImageTk.PhotoImage(pre6)
pre6 = Label(ventana1, image = img6)


pre7 = Image.open("Gaseosa.jpeg")
pre7 = pre7.resize((70,70), Image.ANTIALIAS)

img7 = ImageTk.PhotoImage(pre7)
pre7 = Label(ventana1, image = img7)


pre8 = Image.open("Refrescos.webp")
pre8 = pre8.resize((70,70), Image.ANTIALIAS)

img8 = ImageTk.PhotoImage(pre8)
pre8 = Label(ventana1, image = img8)


pre9 = Image.open("Cafe.jpeg")
pre9 = pre9.resize((70,70), Image.ANTIALIAS)

img9 = ImageTk.PhotoImage(pre9)
pre9 = Label(ventana1, image = img9)

#Almacenamos las variables

eva = IntVar()
eva2 = IntVar()
eva3 = IntVar()

#Creamos la funcion para mostrar el total de la comida, bebida y ensalada

def Total():

    if eva.get() == 1:
        comida = "Carne asada"
        precioC_1 = 2.50
    elif eva.get() == 2:
        comida = "Pollo guisado"
        precioC_1 = 2.25
    elif eva.get() == 3:
        comida = "Lasaña"
        precioC_1 = 3.00
    

    if eva2.get() == 1:
        ensalada = "Fresca"
        precioE_2 = 0.25
    elif eva2.get() == 2:
        ensalada = "Coditos"
        precioE_2 = 0.25
    elif eva2.get() == 3:
        ensalada = "Rusa"
        precioE_2 = 0.25


    if eva3.get() == 1:
        bebida ="Gaseosa"
        precioB_3= 0.75
    elif eva3.get() == 2:
        bebida ="Frescos"
        precioB_3= 0.50
    elif eva3.get() == 3:
        bebida ="cafe"
        precioB_3= 0.65

    #Evaluamos los resultados

    precio_f = precioC_1 + precioE_2 + precioB_3

    print("---------------Factura de los Platos, Ensaladas y Bebidas---------------")
    print("Comida: ",comida, "Precio $: ", precioC_1)
    print("Ensalada: ",ensalada,"Precio: $",precioE_2 )
    print("Bebida: ",bebida, "Precio: $", precioB_3)
    print("Total: $", precio_f)
    print("------------------------------------------------------")


#Creamos los labels de cada aditamiento

labl1=Label(ventana1, bg = "#AED4E6",text="Comida")

labl2=Label(ventana1, bg = "#AED4E6", text="Ensaladas")

labl3=Label(ventana1, bg = "#AED4E6", text="Bebidas")

#Creamos los radio button

rdb1 = Radiobutton(ventana1, bg = "#83E8BA",text="Carne Asada", value=1, variable=eva)
rdb2 = Radiobutton(ventana1, bg = "#83E8BA",text="Pollo Guisado", value=2, variable=eva)
rdb3 = Radiobutton(ventana1, bg = "#83E8BA",text="Lasaña", value=3, variable=eva)

rdb4 = Radiobutton(ventana1, bg = "#B8B8F3",text="Fresca", value=1, variable=eva2)
rdb5 = Radiobutton(ventana1, bg = "#B8B8F3",text="Coditos", value=2, variable=eva2)
rdb6 = Radiobutton(ventana1, bg = "#B8B8F3",text="Rusa", value=3, variable=eva2)

rdb7 = Radiobutton(ventana1, bg = "#74B3CE",text="Gaseosa", value=1, variable=eva3)
rdb8 = Radiobutton(ventana1, bg = "#74B3CE",text="Fresco", value=2, variable=eva3)
rdb9 = Radiobutton(ventana1, bg = "#74B3CE",text="Cafe", value=3, variable=eva3)


#Creamos el boton para poder imprimir la factura

btn1 = Button(ventana1,text="Imprimir factura",command=Total)
ventana1.configure(bg='#427AA1')
ventana1.title("Cafeteria El Amigos")


labl1.place(y=10, x=230)
labl2.place(y=150, x=230)
pre1.place(y=50, x=70)
pre2.place(y=50, x=200)
pre3.place(y=50, x=350)
pre4.place(y=180, x=70)
pre5.place(y=180, x=200)
pre5.place(y=180, x=200)
pre6.place(y=180, x=350)
pre7.place(y=310, x=70)
pre8.place(y=310, x=200)
pre9.place(y=310, x=350)
labl3.place(y=280, x=230)
rdb1.place(y=120, x=50)
rdb2.place(y=120, x=180)
rdb3.place(y=120, x=340)
rdb4.place(y=255, x=50)
rdb5.place(y=255, x=180)
rdb6.place(y=255, x=340)
rdb7.place(y=390, x=50)
rdb8.place(y=390, x=180)
rdb9.place(y=390, x=340)
btn1.place(y=420, x=400)


ventana1.mainloop()
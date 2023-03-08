from tkinter import *
from datetime import *
from CalcSalario import *
#para el formato de peso
import locale
locale.setlocale(locale.LC_ALL, '')
#Salario minimo
SLMV = 1000000

today = date.today()
hoy = today.strftime("%d-%m-%Y")
print(hoy)


window = Tk()

window.title("Presupuesto Personal")
window.minsize(width=500,height=350)


def button_clicked():
    print("Boton presionado OK")
    #La funcion esta en flotante, la variable salario debe ser flotante. SI NO GENERA ERROR!
    salario = float(input.get())

    #Instancia----------------------------------#
    inscalc = CalcSalario(salario)
    varsalud = inscalc.calculaSalud()
    varpension = inscalc.calculaPension()
    varsolidario = inscalc.calculaSolidario()
    vartotal = inscalc.totalSueldo(varsalud,varpension,varsolidario)


    #Labels resultados-------------------------------------#
    lsueldores.config(text=(locale.currency(salario,grouping=True)))
    lsaludres.config(text=(locale.currency(varsalud,grouping=True)))
    lpension.config(text=(locale.currency(varpension,grouping=True)))
    #Aporte solidario son 4 salarios minimos
    if salario >= (SLMV*4):
        lsolidario.config(text=(locale.currency(varsolidario,grouping=True)))
    else:
        lsolidario.config(text="N/A")

    ltotal.config(text=(locale.currency(vartotal,grouping=True)))
    #para dar formato a moneda locale.currency
    #print(locale.currency(vartotal, grouping=True))



    input.delete(0, END)
    #print(salario)

#------------LABEL PRESENTACIÓN---------------------------------------
my_label1 = Label(text="Calculadora salarial", font=("Arial", 24, "bold"))
my_label1.pack()
my_label2 = Label(text="Ingrese salario", font=("Arial", 15))
my_label2.pack()

#------------labels sueldo----------------------

lsueldo = Label(text="Salario: ")
lsueldo.pack()
lsueldo.place(x=100,y=180)
#label de salario ingresado
lsueldores = Label(text="")
lsueldores.pack()
lsueldores.place(x=300,y=180)

#------------labels salud----------------------

#salud
lsalud = Label(text="Aporte a salud: ")
lsalud.pack()
lsalud.place(x=100,y=200)

#label salud ingresada:
lsaludres = Label(text="")
lsaludres.pack()
lsaludres.place(x=300,y=200)

#------------labels pension----------------------

#pension
lpension = Label(text="Aporte a pension: ")
lpension.pack()
lpension.place(x=100,y=220)

#label salud ingresada:
lpension = Label(text="")
lpension.pack()
lpension.place(x=300,y=220)

#------------labels Solidario----------------------

#solidario
lsolidario = Label(text="Aporte solidario: ")
lsolidario.pack()
lsolidario.place(x=100,y=240)

#label salud ingresada:
lsolidario = Label(text="")
lsolidario.pack()
lsolidario.place(x=300,y=240)

#------------labels Total----------------------
#total
ltotal = Label(text="Total Deducido: ")
ltotal.pack()
ltotal.place(x=100,y=260)

#label salud ingresada:
ltotal = Label(text="")
ltotal.pack()
ltotal.place(x=300,y=260)

#Label de fecha
ldate = Label(text="Fecha: "+ hoy)
ldate.pack()



#entrada
input = Entry(width=50)
input.pack()
button = Button(text="Ingrese el valor",command=button_clicked)
button.pack()

#funcion para boton de cierre y boton
def salir():
    window.destroy()

exit_button = Button(window, text="salir",command=salir)
exit_button.pack()
exit_button.place(x=230,y=300)



#Cierre loop de ventana
window.mainloop()

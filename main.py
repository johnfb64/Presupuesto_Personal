from tkinter import *
from datetime import *

today = date.today()
hoy = today.strftime("%d-%m-%Y")
print(hoy)
#concepto = []

window = Tk()

window.title("Presupuesto Personal")
window.minsize(width=500,height=300)

def button_clicked():
    #print("He sido presionado")
    new_text = input.get()
    my_label1.config(text=new_text)
    #concepto.append(new_text)
    #limpia el entry
    input.delete(0, END)

my_label1 = Label(text="Calculadora salarial", font=("Arial", 24, "bold"))
my_label1.pack()
my_label2 = Label(text="Ingrese salario", font=("Arial", 15))
my_label2.pack()

ldate = Label(text="Fecha: "+ hoy)
ldate.pack()



#entrada
input = Entry(width=50)
input.pack()
button = Button(text="Ingrese el valor",command=button_clicked)
button.pack()



window.mainloop()

#consola
# for i in concepto:
#     print(i)


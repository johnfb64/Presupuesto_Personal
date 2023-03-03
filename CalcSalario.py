import math
class CalcSalario:
    SMLV = 1300000
    def __init__(self,sueldo):
        self._sueldo = sueldo


    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo



    def calculaSalud(self):
        salud = self._sueldo *0.04
        #este metodo quita los decimales
        print(math.trunc(salud))

    def calculaPension(self):
        pension = self._sueldo *0.04
        #este metodo quita los decimales
        print(math.trunc(pension))

    def calculaSolidario(self):
        solidario = self._sueldo *0.01
        #este metodo quita los decimales
        print(math.trunc(solidario))


    def totalSueldo(self,slmv):
        if slmv >= (slmv*4):
            ## todo Definir esta funcion de calculo de salario y revisar que los valores sean correctos. 


##################### TESTING ####################################
salario = 100

parafisc = CalcSalario(salario)

salud = parafisc.calculaSalud()
pension = parafisc.calculaPension()
solidario = parafisc.calculaSolidario()



print(salud)
print(pension)
print(solidario)





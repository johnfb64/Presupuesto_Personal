import math
SMLV = 1000000
class CalcSalario:

    def __init__(self,sueldo):
        self._sueldo = sueldo


    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo



    def calculaSalud(self):
        salud = self.sueldo *0.04
        #este metodo quita los decimales
        return(math.trunc(salud))

    def calculaPension(self):
        pension = self.sueldo *0.04
        #este metodo quita los decimales
        return(math.trunc(pension))

    def calculaSolidario(self):
        solidario = self.sueldo *0.01
        #este metodo quita los decimales
        return(math.trunc(solidario))


    def totalSueldo(self,salud,pension,solidario):
        if self.sueldo >= (SMLV*4):
            tot = self.sueldo - (salud + pension + solidario)
            return tot
        else:
            tot = self.sueldo - (salud + pension)
            return tot

#########TESTING - SI NO SE DEJA COMENTARIADO DAÑA EL CODIGO, SOLO PARA TEST####################################
# salario = 5000000
#
# parafisc = CalcSalario(salario)
#
# salud = parafisc.calculaSalud()
# pension = parafisc.calculaPension()
# solidario = parafisc.calculaSolidario()
#
# deducido = parafisc.totalSueldo()
#
#
# print(salud)
# print(pension)
# print(solidario)
# print(deducido)
#
# print("-------------------FINALIZA TESTING 1---------------------")




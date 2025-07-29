#herramientasanti
class Herra:

    def __init__(self, listaaplicar):
        assert len(listaaplicar) != 0, "La lista no puede estar vacía"
        if type(listaaplicar)!= list:
             raise ValueError ("El input debe ser una lista")
        for i in listaaplicar:
             assert isinstance(i,(int,float)), "La lista sólo puede contener números"
        assert len(listaaplicar) != 0, "La lista no puede estar vacía"

        self.listaaplica=listaaplicar

        

    def primar(self):
         listadeprimos=[]
         for i in self.listaaplica:
            listadeprimos.append(self.__primar(i))
         return listadeprimos
    
                   
    def __primar(self,n):           
        primo=True
        for div in range(2, n):     
            if (n % div == 0):       
                primo = False
                break
        else:
            primo = True
  
        return primo
    
    def resolver(self):                  
        elementos_unicos=[]
        elementos_repetidos=[]
        for elemento in self.listaaplica:
            if elemento in elementos_unicos:
                i= elementos_unicos.index(elemento)
                elementos_repetidos[i]+=1

            else:
             elementos_unicos.append(elemento)
             elementos_repetidos.append(1)
        modamayor=max(elementos_repetidos)
        ind=elementos_repetidos.index(modamayor)
        numconmayormoda=elementos_unicos[ind]
        return numconmayormoda, modamayor
    

    def convertir(self,origen,destino):   
         assert origen in("°K","°C","°F"),"Unidad de origen incorrectar utilizar °K,°C o °F"
         assert destino in("°K","°C","°F"),"Unidad de destino incorrectar utilizar °K,°C o °F"
         for n in self.listaaplica:
              print(n,"grados",origen,"son",self.__convertir(n,origen,destino))



    def __convertir(self,numero,origen,destino):           
            if  origen=="°F":
                    if destino == "°F":
                            return numero, "°F"
                    elif destino == "°K":
                        res=(numero-32)* 5/9 + 273.15
                        return res,"°K"
                    elif destino == "°C":
                        res= (numero - 32)* 5/9
                        return res, "°C"
                    
                
            elif origen=="°K":
                    if destino == "°F":
                        res=(numero- 273.15) * 9/5 + 32
                        return res, "°F"
                    elif destino == "°K":
                        return numero, "°K"
                    elif destino == "°C":
                        res= numero- 273.15
                        return res, "°C"
                  
            elif origen=="°C":
                   if destino=="°C":
                        return numero, "°C"
                   elif destino=="°K":
                         res= numero + 273.15
                         return res, "°K"
                   elif destino == "°F":
                         res= (numero  * 9/5 + 32)
                         return res, "°F"
               
               
            


    def factorial(self):                             
         for num in self.listaaplica:
              assert num>=0, "No se puede sacar factorial de numero negativos ESSSHHH IMPOSHHHIBLEE!!!"
              print("El factorial de",num,"es",self.__factorial(num))
    def __factorial(self,num):
        if num == 0:
            num=1
        

        if num > 1:
            num=num* self.__factorial(num-1)
        return num
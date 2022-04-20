from ayuda import agregarEdades


class PromedioEdades():
    
    def __init__(self):
        self.n=int(input("Ingrese cantidad de personas a evaluar:"))
        self.genero="masculino","femenino"
        self.edadesHombre=[]
        self.edadesMujer=[]
        self.Mujertreinta=[]
        self.Edadesingresadas=(list(i+j for (i,j) in zip(self.edadesHombre,self.edadesMujer)))   
      
    def aregarEdades(self,p):
        f=int(input("ingrese edad en el sexo"+ " " +  str(p)+ ":"))
    
        if p=="femenino":
            self.edadesMujer.append(f)
            if f>30:
                self.Mujertreinta.append(f)      
        else:
                self.edadesHombre.append(f)
                
    def imprimir(self):
        print("Promedio de edades:", sum(self.Edadesingresadas)/self.n)
        print("Promedio edades Hombre", sum(self.edadesHombre)/len(self.edadesHombre))
        print("Promedio edades Mujer", sum(self.edadesMujer)/len(self.edadesMujer))
        print("Cantidad de mujeres mayor a 30: ", len(self.Mujertreinta))
        print("Mayor edad ingresada", max(self.Edadesingresadas))
                
    
def main():
    caso1=PromedioEdades()
    caso1.aregarEdades("masculino")
    caso1.imprimir()
    
main()
   
   
   
        
       
          
      
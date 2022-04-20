genero="masculino", "femenino"
edadesHombre=[]
edadesMujer=[]
Mujertreinta=[]
def agregarEdades(p):
    f=int(input("ingrese edad en el sexo"+ " " +  str(p)+ ":"))
    
    if p=="femenino":
        edadesMujer.append(f)
        if f>30:
         Mujertreinta.append(f)      
    else:
        edadesHombre.append(f)
        
     
n=int(input("Ingrese cantidad de personas a evaluar:"))
for   i in range(n):
       for i in genero:
           agregarEdades(i)
        
Edadesingresadas=(list(i+j for (i,j) in zip(edadesHombre,edadesMujer)))
print("Promedio de edades:", sum(Edadesingresadas)/n)
print("Promedio edades Hombre", sum(edadesHombre)/len(edadesHombre))
print("Promedio edades Mujer", sum(edadesMujer)/len(edadesMujer))
print("Cantidad de mujeres mayor a 30: ", len(Mujertreinta))
print("Mayor edad ingresada", max(Edadesingresadas))
    
    
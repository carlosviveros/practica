from datetime import datetime
from datetime import date


def dia():
    return datetime.today().strftime('%Y-%m-%d')
    


def hora(x):
    while True:
        try:
            h = input("Ingrese la hora en que se realizó la venta número #" +str(x+1)+ " en  formato HH:MM : ")
            datetime.strptime(h, "%H:%M")
            return h
        except ValueError:
            print("Hora inválida") 
            

def promedio(arr):
    return sum(arr)/len(arr)


def get_data():
    totalVentas=[]
    n_venta=int(input("ingrese número de ventas realizadas en el transcurso del día: "))
    for i in range(n_venta):
        hora_Venta=hora(i)
        n=int(input("ingrese cantidad de pasteles vendidos a las "+ str(hora_Venta)+ ":"))  
        totalVentas.append(n)
        
    return totalVentas

def main():
    
    print("Ventas del día ", dia())
    cantidadVentas=get_data()
    print("Total ventas realizadas:", len(cantidadVentas))    
    print("Promedio de ventas:",promedio(cantidadVentas))
    print("Mayor venta:", max(cantidadVentas))
    print("Menor venta",min(cantidadVentas))
    
main()
    

import csv

#FUNCION PARA INGRESAR EL NOMBRE DEL EMPLEADO.

def input_empleado(name):
        name = str(input('Escriba su apellido: '))
        if name in lista_empleados:

            opcion = str(input(f'Bienvenido {name}, seleccione la opcion CONSULTAR, AGREGAR o escriba FIN para salir: ')).upper()

        else:
            print('El apellido no corresponde a un empleado')
            pass

        return name, opcion 

#FUNCION PARA CREAR ARCHIVO CSV DE STOCK INICIAL
def creacion_csv():
    
    csvfile = open('stockintegral.csv', 'w', newline='')

    header = ['CODIGO', 'PRENDA', 'TALLE' ,'CANTIDAD']
    
    writer = csv.DictWriter(csvfile, fieldnames=header)

    mi_codigo = '001'
    mi_prenda = 'remera'
    mi_talle = 'small'
    mi_cantidad = '10'

    writer.writeheader()
    fila = {'CODIGO': mi_codigo, 'PRENDA': mi_prenda, 'TALLE': mi_talle ,'CANTIDAD': mi_cantidad}
    writer.writerow(fila)
    

  

    csvfile.close()


#FUNCION PARA CONSULTAR STOCK POR CODIGO
def consultarstock_csv():
    
        csvfile= open('stockintegral.csv')
        stock_actual   = list(csv.DictReader(csvfile))

        print(stock_actual)


        csvfile.close()



#FUNCION PARA AGREGAR STOCK
def agregar_stock():
    header = [ 'CODIGO', 'PRENDA', 'TALLE', 'CANTIDAD']
    csvfile = open('stockintegral.csv','a')
    writer = csv.DictWriter(csvfile, fieldnames=header)
    nuevo_ingreso = {'CODIGO':(int(input('Escriba el codigo del producto: '))) , 'PRENDA':(str(input('Escriba el tipo de prenda: '))), 'TALLE':(str(input('Escriba el talle del producto: '))), 'CANTIDAD':(int(input('Escriba la cantidad de unidades a agregar: ')))}

    writer.writerow(nuevo_ingreso)

    
    csvfile.close()



if __name__=='__main__':
    creacion_csv()
    print('Bienvenido al sistema de Stock Granero')


    lista_empleados = ['GRANERO', 'SAMAD']
    name = None
      

    while True:
        name, opcion_empleado = input_empleado(name)
        print(f'Estimado/a {name}, su opcion elegida es {opcion_empleado}')

    
            
        if opcion_empleado == 'FIN':
                break 

        elif opcion_empleado == 'CONSULTAR':
                consultarstock_csv()
 
        elif opcion_empleado == 'AGREGAR':
                agregar_stock()
        else: 
                print('La opcion seleccionada es erronea, intente nuevamente')
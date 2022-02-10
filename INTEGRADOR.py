
import csv

#FUNCION PARA INGRESAR EL NOMBRE DEL EMPLEADO.

def input_empleado():
        name = str(input('Ingrese su apellido: '))

        return name

def input_opcion():
        opcion = str(input(f'Bienvenido {name} eleccione la opcion CONSULTAR AGREGAR O FIN para terminar la consulta: ')).upper()

        return opcion 


#FUNCION PARA CREAR ARCHIVO CSV DE STOCK INICIAL
def creacion_csv():
    
    csvfile = open('stockintegral.csv', 'w', newline='')

    header = ['CODIGO', 'PRENDA', 'TALLE' ,'CANTIDAD']
    
    writer = csv.DictWriter(csvfile, fieldnames=header)

    mi_codigo = '111'
    mi_prenda = 'remera'
    mi_talle = 'small'
    mi_cantidad = '10'

    writer.writeheader()
    fila = {'CODIGO': mi_codigo, 'PRENDA': mi_prenda, 'TALLE': mi_talle ,'CANTIDAD': mi_cantidad}
    writer.writerow(fila)
    writer.writerow({'CODIGO': '222', 'PRENDA': 'remera', 'TALLE': 'medium', 'CANTIDAD': '12'})

  

    csvfile.close()            


#FUNCION PARA CONSULTAR STOCK POR CODIGO
def consultarstock_csv():
    
        csvfile= open('stockintegral.csv')
        datos   = list(csv.DictReader(csvfile))

        cantidad_filas = len(datos)

        
        cod_producto = str(input('Escriba el codigo de producto que desea consultar:'))
        
        
        for producto in range(cantidad_filas):
                id_producto = datos[producto]['CODIGO']
                stock_producto = datos[producto]['CANTIDAD']

                if cod_producto == id_producto:
                        print('El stock del producto numero', cod_producto , 'es de', stock_producto, 'u')
                        break
                else:
                        print('El codigo ingresado no corresponde a un producto')
                        
                


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
    name = None


name = input_empleado()
while True:        
        opcion = input_opcion()
        print(f'Estimado/a {name}, su opcion elegida es {opcion}')
    

        if opcion == 'FIN':
                 break 

        elif opcion == 'CONSULTAR':
                        consultarstock_csv()
 
        elif opcion == 'AGREGAR':
                        agregar_stock()
        else: 
                        print('La opcion seleccionada es erronea, intente nuevamente')
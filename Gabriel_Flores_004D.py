#Inicialización de Variables
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

#Funciones
def stock_marca(marca:str):
    """La función recibe como parametro un str que indica el modelo a buscar en stock.\n
    Se asigna a "contador" el valor 0. Con el iterador for se asigna a "modelo" e "informacion" las keys y valores respectivos del diccionario productos. Luego se asigna a marca_modelo la marca almacenada en la informacion correspondiente, se realiza una comparación entre la marca consultada y la existente utilizando lower. Si son iguales se suma al contador el stock del modelo ubicado en el diccionario stock. Al final se retorna el contador."""
    contador = 0
    for modelo, informacion in productos.items():
        marca_modelo = informacion[0]
        if marca.lower() == marca_modelo.lower():
            contador += stock[modelo][1]
    return contador
def busqueda_precio(p_min:int,p_max:int,):
    """La función recibe como parametros dos enteros, el primero representa el limite inferior y el segundo el limite superior.\n
    Primero se asigna a la variable "modelos" una lista vacia. Luego con for se asigna iteradamente "modelo" e "informacion" a cada key y valor del diccionario "stock", se asigna "precio" y "cantidad" los valores almacenados en "informacion", si la cantidad es mayor a 0 y el precio se encuentra entre el mínimo y máximo establecido: se agrega un string "marca--modelo" a la lista "modelos". Finalmente ordena la lista alfabeticamente, y si la lista tiene datos los retorna, pero si no muestra en pantalla el mensaje "No hay notebooks en ese rango de precios." """
    modelos = []
    for modelo, informacion in stock.items():
        precio, cantidad = informacion
        if cantidad > 0 and p_min <= precio <= p_max:
            modelos.append(productos[modelo][0]+"--"+modelo)
    modelos.sort()
    if modelos:
        return modelos
    else:
        print("No hay notebooks en ese rango de precios.")
def actualizar_precio(modelo:str, p:int):
    """La función recibe como parámetros un str que indica el modelo y un entero que indica el nuevo precio.\n
    Si el modelo se encuentra en el diccionario "Stock" se asigna al valor almacenado el nuevo precio y se retorna True, de lo contrario se retorna False."""
    if modelo in stock:
        stock[modelo][0] = p
        return True
    return False
def validar_entero_positivo(mensaje:str):
    """La función recibe el mensaje que se utilizará junto con el input.\n
    Se establece un bucle while con la condición True y se hace uso de excepciones para controlar posibles errores en la entrada del usuario. Se transforma la entrada del usuario en un dato de tipo int, se revisa si este dato es menor o igual a 0, de serlo se muestra por pantalla el siguiente mensaje: "¡Ingrese un número entero mayor que 0!". En el caso contrario se retorna el numero de entrada. Ante Errores de Valor muestra en pantalla el mensaje: "¡Debe ingresar valores enteros!"."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero <= 0:
                print("¡Ingrese un número entero mayor que 0!")
            else:
                return numero
        except ValueError:
            print("¡Debe ingresar valores enteros!")
def menu():
    """Esta función no recibe parámetros.\n
    Se muestra en pantalla el nombre y las opciones del menu principal. Se manejan errores de valor con try. Se pide entrada del usuario correspondiente a la opción del menu. Si la opcion es igual a 1 se hace uso de la función stock_marca(marca) y se muestra el valor entregado por esta. De ser igual a 2 se hace uso de validar_entero_positivo(mensaje) para recibir datos y busqueda_de_precios(p_min,p_max) para generar la lista correspondiente a esos datos, si la lista generada tiene algún dato se muestra en pantalla. Para la opcion 3 se establece un ciclo while con la condición True y se recibe el modelo, se usa validar_entero_positivo(mensaje) para recibir el nuevo precio y se utiliza actualizar_precio(modelo, p) para almacenar True en caso de que se actualice y False en caso contrario. Si es True se muestra en pantalla el éxito de la operación y de ser False la inexistencia del modelo ingresado. Se muestra en pantalla si el usario quiere realizar otra actualización y se recibe su respuesta, si es no se rompe el bucle while. La opcion 4 es el cierre del programa mostrando en pantalla un mensaje. Cualquier otro numero entero envia un mensaje correspondiente y cualquier dato diferente a un entero también."""
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.Stock marca.")
        print("2.Búsqueda por precio.")
        print("3.Actualizar precio.")
        print("4.Salir")

        try:
            opcion = int(input("\nIngrese opción: "))

            if opcion == 1:
                cantidad_marca = stock_marca(input("Ingrese marca a consultar: "))
                print(f"El stock es: {cantidad_marca}")
            elif opcion == 2:
                precio_minimo = validar_entero_positivo("Ingrese precio mínimo: ")
                precio_maximo = validar_entero_positivo("Ingrese precio máximo: ")
                lista_notebooks = busqueda_precio(precio_minimo, precio_maximo)
                if lista_notebooks:
                    print(f"Los notebooks entre los precios consultados son: {lista_notebooks}")
            elif opcion == 3:
                while True:
                    actualizar_modelo = input("Ingrese modelo a actualizar: ")
                    nuevo_precio = validar_entero_positivo("Ingrese precio nuevo: ")
                    actualizado = actualizar_precio(actualizar_modelo,nuevo_precio)
                    if actualizado:
                        print("¡Precio actualizado!\n")
                    else:
                        print("¡El modelo no existe!\n")
                    continuar = input("¿Desea actualizar otro precio? (escriba \"no\" para salir): ")
                    if continuar.lower() == "no":
                        break
            elif opcion == 4:
                print("Programa Finalizado.")
                break
            else:
                print("¡Ingrese una opción válida!")
        except ValueError:
            print("¡Debe ingresar valores enteros!")

#Programa
menu()
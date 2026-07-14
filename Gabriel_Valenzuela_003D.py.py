def validar_texto(texto):
    return len(texto.strip()) > 0

def validar_pantalla(valor):
    try:
        return float(valor)>=0
    except:
        return False
    
def validar_plan(valor):
    try:
        return int(valor) >= 0
    except:
        return False
    
def validar_stock(valor):
    try:
        return int(valor) >= 0
    except:
        return False

#----


def buscar_codigo(codigo, diccinario):
    return codigo.upper().strip() in diccinario

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error, del 1-6")
        except:
            print("Error, ponga numero del 1-6")

def detalle_plan(codigo, plans, bodega):
    cod = codigo.upper().strip()
    if buscar_codigo(cod, plans):
        nombre, tipo, duracion, marca, graf, pant = plans[cod]
        plan = bodega[cod][0]
        stock = bodega[cod][1]
        print(f"nombreelo: {nombre}, plan: {plan}, Stock disponible: {stock}")
    else:
        print("plan no enconctrado")

def busqueda_plan(plan_min, plan_max, bodega, plans):
    encontrados = []
    for cod, datos in bodega.items():
        plan, stock = datos[0], datos[1]
        if plan_min <= plan <= plan_max and stock > 0:
            nombreelo = plans[cod][0]
            encontrados.append(f"Codigo: {cod}, nombreelo: {nombreelo}, plan: {plan}, Stock: {stock}")
    if encontrados:
        print(" / ".join(encontrados))
    else:
        print("No se encontraron en el rango de plan")

def actualizar_plan(codigo, nuevo_plan, bodega):
    cod = codigo.upper().strip()
    if buscar_codigo(cod, bodega):
        bodega[cod][0] = int(nuevo_plan)
        return True
    return False

def agregar_plan(codigo, nombreelo, tipo, duraciono, marca_grafica, grafica, dimension_pantalla, plan, stock, plans, bodega):
    cod = codigo.upper().strip()
    if buscar_codigo(cod, plans):
        return False

    plans[cod] = [nombreelo, tipo, duraciono, marca_grafica, grafica, float(dimension_pantalla)]
    bodega[cod] = [int(plan), int(stock)]
    return True

def eliminar_plan(codigo, plans, bodega):
    cod = codigo.upper().strip()
    if buscar_codigo(cod, plans):
        plans.pop(cod)
        bodega.pop(cod)
        return True
    return False

#---

Plans = {
    '1': ['', '', '', '', '', '']
}

bodega = {
    '1':[189999, 8]
}

while True:
    print("=====Menu=====")
    print("[1] - Cupos por tipo de plan")
    print("[2] - Busqueda de planes por rango de plan")
    print("[3] - actualizar plan plan")
    print("[4] - agregar plan")
    print("[5] - eliminar plan")
    print("[6] - Salir")
    print("===============")

    opcion = leer_opcion()

    if opcion == 1:
        cod = input("Cupos por tipo de plan: ")
        if len(cod.strip()) == 0:
            print("Error está vacio")
        else:
            detalle_plan(cod, Plans, bodega)
    elif opcion == 2:
        while True:
            try:
                p_min = float(input("Ingrese prcio minimo: "))
                p_max = float(input("Ingrese plan maximo: "))
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    busqueda_plan(p_min, p_max, bodega, Plans)
                    break
                else:
                    print("Error valores no valids")
            except:
                print("Error, por favor ingrese numeros validos")
    elif opcion == 3:
        while True:
            cod = input("Ingrese codigo: ")
            try:
                nuevo_p = input("Ingrese nuevo incluye_clasesi: ")
                if validar_plan(nuevo_p):
                    if actualizar_plan(cod, nuevo_p, bodega):
                        print("plan actualizado")
                    else:
                        print("Codigo no existe")
                else:
                    print("incluye_clasesi no valido")
            except:
                print("Error de datos we")
            repetir = input("Desea actualizar otro plan s/n?").upeer().strip()
            if repetir == 'n':
                break
    elif opcion == 4:
        cod = input("ingrese codigo del plan: ").upper().strip()
        nombre = input("ingrese nombre: ")
        tipo = input("Ingrese tipo: ")
        duracion = input("ingrese duracion: ")
        acceso_piscina = input("Ingrese acceso_piscina:")
        incluye_clases = input("Ingrese incluye_clases:")
        horario = input("Ingrese horario:")
        precio = input("Ingrese precio:")
        cupos = input("Ingrese cupos:")
        stock = input("Ingrese stock:")
        if (validar_texto(cod) and not buscar_codigo(cod, Plans) and validar_texto(nombre) and validar_texto(tipo) and validar_texto(duracion) and validar_texto(acceso_piscina) and validar_texto(incluye_clases) and validar_texto(stock)) and validar_texto(horario) and validar_texto(precio) and validar_texto(cupos):
            agregar_plan(cod, nombre, tipo, duracion, acceso_piscina, incluye_clases,horario, precio, cupos, stock, Plans, bodega)
            print("Plan agregado")
        else:
            print("Error de datos")
    elif opcion == 5:
        cod = input("Ingrese codigo a eliminar: ")
        if buscar_codigo(cod, Plans):
            confirmar = input(f"¿Seguro de eliminar plan {cod}? s/n: ").lower().strip()
            if confirmar == "s":
                eliminar_plan(cod, Plans, bodega)
                print("Plan elminado")
            else:
                print("Operacion cancelada")
        else:
            print("El codigo no existe")
    elif opcion == 6:
        print("Programa finalizado.")
        break
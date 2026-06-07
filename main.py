# IMPORTACIONES
# =========================
import csv


# =========================
# CONFIGURACIÓN GENERAL
# =========================
ARCHIVO_CSV = "paises.csv"


# =========================
# FUNCIONES DE ARCHIVO CSV
# =========================
def cargar_paises():
    paises = []

    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                if validar_fila_csv(fila):
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip().capitalize()
                    }

                    paises.append(pais)
                else:
                    print("Se encontró una fila inválida en el CSV y fue ignorada.")

    except FileNotFoundError:
        print("No se encontró el archivo paises.csv. Se iniciará con una lista vacía.")

    except Exception as error:
        print("Ocurrió un error al leer el archivo CSV:", error)

    return paises

def guardar_paises(paises):
    try:
        with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]

            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for pais in paises:
                escritor.writerow(pais)

        print("Los datos fueron guardados correctamente.")

    except Exception as error:
        print("Ocurrió un error al guardar los datos:", error)

def validar_fila_csv(fila):
    try:
        campos_obligatorios = ["nombre", "poblacion", "superficie", "continente"]

        for campo in campos_obligatorios:
            if campo not in fila:
                return False

            if fila[campo].strip() == "":
                return False

        if int(fila["poblacion"]) <= 0:
            return False

        if int(fila["superficie"]) <= 0:
            return False

        return True

    except (ValueError, KeyError):
        return False


# =========================
# FUNCIONES DE VALIDACIÓN
# =========================
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: este campo no puede quedar vacío.")
        else:
            return texto


def pedir_entero_positivo(mensaje):
    while True:
        dato = input(mensaje).strip()

        try:
            numero = int(dato)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def pedir_rango(mensaje_min, mensaje_max):
    while True:
        minimo = pedir_entero_positivo(mensaje_min)
        maximo = pedir_entero_positivo(mensaje_max)

        if minimo > maximo:
            print("Error: el valor mínimo no puede ser mayor que el valor máximo.")
        else:
            return minimo, maximo


# =========================
# FUNCIONES PARA MOSTRAR DATOS
# =========================
def mostrar_pais(pais):
    print("----------------------------------------")
    print("Nombre:", pais["nombre"])
    print("Población:", pais["poblacion"])
    print("Superficie:", pais["superficie"], "km²")
    print("Continente:", pais["continente"])


def mostrar_lista_paises(paises):
    if len(paises) == 0:
        print("No hay países para mostrar.")
    else:
        for pais in paises:
            mostrar_pais(pais)


# =========================
# FUNCIONALIDADES PRINCIPALES
# =========================
def agregar_pais(paises):
    print("\n--- AGREGAR PAÍS ---")

    nombre = pedir_texto("Ingrese el nombre del país: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: ese país ya está cargado.")
            return

    poblacion = pedir_entero_positivo("Ingrese la población: ")
    superficie = pedir_entero_positivo("Ingrese la superficie en km²: ")
    continente = pedir_texto("Ingrese el continente: ").capitalize()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_paises(paises)

    print("País agregado correctamente.")

def actualizar_pais(paises):
    print("\n--- ACTUALIZAR PAÍS ---")

    nombre_buscado = pedir_texto(
        "Ingrese el nombre del país que desea actualizar: "
    )

    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():

            print("\nDatos actuales:")
            mostrar_pais(pais)

            nueva_poblacion = pedir_entero_positivo(
                "Ingrese la nueva población: "
            )

            nueva_superficie = pedir_entero_positivo(
                "Ingrese la nueva superficie en km²: "
            )

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            guardar_paises(paises)

            print("País actualizado correctamente.")
            return

    print("No se encontró un país con ese nombre.")

def buscar_pais(paises):
    print("\n--- BUSCAR PAÍS ---")

    nombre_buscado = pedir_texto("Ingrese el nombre o parte del nombre del país: ")

    resultados = []

    for pais in paises:
        if nombre_buscado.lower() in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países con ese nombre.")
    else:
        print("\nPaíses encontrados:")
        mostrar_lista_paises(resultados)


# =========================
# FILTROS
# =========================
def filtrar_por_continente(paises):
    print("\n--- FILTRAR POR CONTINENTE ---")

    continente_buscado = pedir_texto("Ingrese el continente: ")

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente_buscado.lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países en ese continente.")
    else:
        mostrar_lista_paises(resultados)


def filtrar_por_poblacion(paises):
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")

    minimo, maximo = pedir_rango(
        "Ingrese la población mínima: ",
        "Ingrese la población máxima: "
    )

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de población.")
    else:
        mostrar_lista_paises(resultados)


def filtrar_por_superficie(paises):
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    minimo, maximo = pedir_rango(
        "Ingrese la superficie mínima: ",
        "Ingrese la superficie máxima: "
    )

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de superficie.")
    else:
        mostrar_lista_paises(resultados)


# =========================
# ORDENAMIENTOS
# =========================
def ordenar_paises(paises):
    print("\n--- ORDENAR PAÍSES ---")

    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")

    opcion = input("Seleccione una opción: ")

    if opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        return

    sentido = input(
        "Ingrese A para ascendente o D para descendente: "
    ).upper()

    if sentido not in ["A", "D"]:
        print("Opción inválida.")
        return

    descendente = sentido == "D"

    if opcion == "1":
        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["nombre"].lower(),
            reverse=descendente
        )

    elif opcion == "2":
        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"],
            reverse=descendente
        )

    else:
        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"],
            reverse=descendente
        )

    mostrar_lista_paises(paises_ordenados)


# =========================
# ESTADÍSTICAS
# =========================
def mostrar_estadisticas(paises):
    print("\n--- ESTADÍSTICAS ---")

    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

    total_poblacion = 0
    total_superficie = 0

    cantidad_por_continente = {}

    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    print("País con mayor población:")
    mostrar_pais(pais_mayor_poblacion)

    print("\nPaís con menor población:")
    mostrar_pais(pais_menor_poblacion)

    print("\nPromedio de población:", round(promedio_poblacion, 2))
    print("Promedio de superficie:", round(promedio_superficie, 2), "km²")

    print("\nCantidad de países por continente:")

    for continente in cantidad_por_continente:
        print(continente + ":", cantidad_por_continente[continente])


# =========================
# MENÚS
# =========================
def menu_principal():
    print("\n========================================")
    print(" SISTEMA DE GESTIÓN DE PAÍSES")
    print("========================================")
    print("1. Agregar país")
    print("2. Actualizar población y superficie")
    print("3. Buscar país por nombre")
    print("4. Filtrar por continente")
    print("5. Filtrar por rango de población")
    print("6. Filtrar por rango de superficie")
    print("7. Ordenar países")
    print("8. Mostrar estadísticas")
    print("9. Mostrar todos los países")
    print("10. Guardar cambios")
    print("11. Salir")
    print("========================================")


def ejecutar_programa():
    paises = cargar_paises()

    while True:
        menu_principal()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_por_continente(paises)

        elif opcion == "5":
            filtrar_por_poblacion(paises)

        elif opcion == "6":
            filtrar_por_superficie(paises)

        elif opcion == "7":
            ordenar_paises(paises)

        elif opcion == "8":
            mostrar_estadisticas(paises)

        elif opcion == "9":
            mostrar_lista_paises(paises)

        elif opcion == "10":
            guardar_paises(paises)

        elif opcion == "11":
            guardar_paises(paises)
            print("Programa finalizado. Los cambios fueron guardados.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# =========================
# INICIO DEL PROGRAMA
# =========================
if __name__ == "__main__":
    ejecutar_programa()
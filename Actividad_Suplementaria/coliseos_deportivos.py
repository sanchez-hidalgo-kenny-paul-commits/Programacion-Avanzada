"""
Módulo: coliseos_deportivos.py
--------------------------------
Define la clase ColiseoDeportivo y funciones para crear objetos
de forma dinámica usando entrada por teclado...
"""

class ColiseoDeportivo:
    """
    Representa un coliseo deportivo.
    Puedes adaptar o ampliar los atributos según tus necesidades
    """

    def __init__(self, nombre, ciudad, capacidad, deporte_principal, es_techado, anio_inauguracion):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.deporte_principal = deporte_principal
        self.es_techado = es_techado
        self.anio_inauguracion = anio_inauguracion

    def __str__(self):
        return (
            f"ColiseoDeportivo(nombre='{self.nombre}', "
            f"ciudad='{self.ciudad}', "
            f"capacidad={self.capacidad}, "
            f"deporte_principal='{self.deporte_principal}', "
            f"es_techado={self.es_techado}, "
            f"anio_inauguracion={self.anio_inauguracion})"
        )


def crear_coliseo_desde_input():
    """
    Crea un objeto ColiseoDeportivo pidiendo los datos al usuario por consola.
    """
    print("=== Crear nuevo Coliseo Deportivo ===")
    nombre = input("Nombre del coliseo: ")
    ciudad = input("Ciudad: ")

    while True:
        try:
            capacidad = int(input("Capacidad (número de espectadores): "))
            break
        except ValueError:
            print("⚠ Por favor, ingresa un número entero para la capacidad.")

    deporte_principal = input("Deporte principal (ej: fútbol sala, básquet, vóley): ")

    while True:
        es_techado_str = input("¿Es techado? (s/n): ").strip().lower()
        if es_techado_str in ("s", "n"):
            es_techado = es_techado_str == "s"
            break
        print("⚠ Responde solo con 's' (sí) o 'n' (no).")

    while True:
        try:
            anio_inauguracion = int(input("Año de inauguración (ej: 1998): "))
            break
        except ValueError:
            print("⚠ Por favor, ingresa un año válido (número entero).")

    coliseo = ColiseoDeportivo(
        nombre=nombre,
        ciudad=ciudad,
        capacidad=capacidad,
        deporte_principal=deporte_principal,
        es_techado=es_techado,
        anio_inauguracion=anio_inauguracion,
    )

    print("\n✅ Coliseo creado correctamente:")
    print(coliseo)
    return coliseo


def crear_varios_coliseos():
    """
    Crea dinámicamente varios coliseos pidiendo datos al usuario hasta que decida terminar.
    """
    coliseos = []
    print("=== Registro dinámico de Coliseos Deportivos ===")

    while True:
        coliseo = crear_coliseo_desde_input()
        coliseos.append(coliseo)

        continuar = input("\n¿Deseas registrar otro coliseo? (s/n): ").strip().lower()
        if continuar != "s":
            break

    return coliseos


def mostrar_coliseos(coliseos):
    """
    Muestra por pantalla la información de una lista de coliseos...
    """
    print("\n=== Lista de Coliseos Registrados ===")
    if not coliseos:
        print("No hay coliseos registrados")
        return

    for i, c in enumerate(coliseos, start=1):
        print(f"#{i}: {c}")


if __name__ == "__main__":
    """
    Bloque principal de prueba.
    Si ejecutas este archivo directamente:
        python coliseos_deportivos.py
    podrás crear varios coliseos de forma interactiva.
    """
    lista_coliseos = crear_varios_coliseos()
    mostrar_coliseos(lista_coliseos)

import sqlite3
from pymongo import MongoClient

# -----------------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------------

SQLITE_DB_FILE = "ciudad_servicios.db"   # archivo de SQLite3
MONGO_URI = "mongodb://localhost:27017/" # URL de Mongo
MONGO_DB_NAME = "ciudad_servicios_norel" # nombre BD en Mongo


# -----------------------------------
# PARTE A: BASE DE DATOS RELACIONAL (SQLite3)
# -----------------------------------

def crear_bd_sqlite():
    """
    Crea la BD ciudad_servicios.db con las tablas:
    - clinicas_particulares
    - parques_recreativos
    y carga datos de ejemplo.
    """
    conn = sqlite3.connect(SQLITE_DB_FILE)
    cursor = conn.cursor()

    # Script con definición de tablas
    script_sql = """
    -- Tabla de Clínicas Particulares
    CREATE TABLE IF NOT EXISTS clinicas_particulares (
        id_clinica INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        direccion TEXT,
        ciudad TEXT,
        telefono TEXT,
        tipo_servicio TEXT,
        horario TEXT,
        num_consultorios INTEGER,
        tiene_emergencias INTEGER  -- 0 = False, 1 = True
    );

    -- Tabla de Parques Recreativos
    CREATE TABLE IF NOT EXISTS parques_recreativos (
        id_parque INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        direccion TEXT,
        ciudad TEXT,
        area_m2 INTEGER,
        tipo_parque TEXT,
        tiene_juegos_infantiles INTEGER, -- 0/1
        tiene_parqueadero INTEGER,       -- 0/1
        precio_entrada REAL,
        horario TEXT
    );
    """

    cursor.executescript(script_sql)

    # Limpio datos para que no se dupliquen al probar muchas veces
    cursor.execute("DELETE FROM clinicas_particulares;")
    cursor.execute("DELETE FROM parques_recreativos;")

    # Datos de ejemplo
    clinicas = [
        (
            "Clínica Santa María",
            "Av. Siempre Viva 123",
            "Quito",
            "022345678",
            "Medicina general",
            "08:00-20:00",
            10,
            1
        ),
        (
            "Centro Médico Vida Sana",
            "Calle 10 de Agosto 456",
            "Guayaquil",
            "042223344",
            "Pediatría",
            "09:00-18:00",
            6,
            0
        )
    ]

    parques = [
        (
            "Parque La Alegría",
            "Av. Los Álamos s/n",
            "Quito",
            15000,
            "Infantil",
            1,
            1,
            0.0,
            "07:00-19:00"
        ),
        (
            "Aventura Park",
            "Km 5 Vía a la Costa",
            "Guayaquil",
            25000,
            "Acuático",
            1,
            1,
            5.50,
            "09:00-18:00"
        )
    ]

    cursor.executemany("""
        INSERT INTO clinicas_particulares
        (nombre, direccion, ciudad, telefono, tipo_servicio,
         horario, num_consultorios, tiene_emergencias)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, clinicas)

    cursor.executemany("""
        INSERT INTO parques_recreativos
        (nombre, direccion, ciudad, area_m2, tipo_parque,
         tiene_juegos_infantiles, tiene_parqueadero,
         precio_entrada, horario)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, parques)

    conn.commit()
    conn.close()
    print("✅ SQLite3: BD creada y datos cargados.\n")


def sqlite_mostrar_clinicas():
    conn = sqlite3.connect(SQLITE_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clinicas_particulares;")
    filas = cursor.fetchall()
    print("📋 CLÍNICAS PARTICULARES (SQLite3):")
    for fila in filas:
        print(f"  ID: {fila[0]} | Nombre: {fila[1]} | Ciudad: {fila[3]} | Emergencias: {'Sí' if fila[8] == 1 else 'No'}")
    conn.close()
    print()


def sqlite_mostrar_parques():
    conn = sqlite3.connect(SQLITE_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM parques_recreativos;")
    filas = cursor.fetchall()
    print("🌳 PARQUES RECREATIVOS (SQLite3):")
    for fila in filas:
        print(f"  ID: {fila[0]} | Nombre: {fila[1]} | Ciudad: {fila[3]} | Precio entrada: {fila[8]}")
    conn.close()
    print()


def sqlite_parques_gratis():
    conn = sqlite3.connect(SQLITE_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, ciudad
        FROM parques_recreativos
        WHERE precio_entrada = 0;
    """)
    filas = cursor.fetchall()
    print("🎫 PARQUES GRATUITOS (SQLite3):")
    for nombre, ciudad in filas:
        print(f"  - {nombre} ({ciudad})")
    conn.close()
    print()


# -----------------------------------
# PARTE B: BASE DE DATOS NO RELACIONAL (MongoDB)
# -----------------------------------

def mongo_conectar():
    """
    Devuelve la BD de MongoDB (ciudad_servicios_norel).
    """
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return client, db


def mongo_poblar():
    """
    Crea colecciones de MongoDB, borra datos anteriores y carga datos de ejemplo.
    """
    client, db = mongo_conectar()

    clinicas = db["clinicas_particulares"]
    parques = db["parques_recreativos"]

    # Eliminar datos antiguos
    clinicas.delete_many({})
    parques.delete_many({})

    clinicas_docs = [
        {
            "nombre": "Clínica Santa María",
            "direccion": "Av. Siempre Viva 123",
            "ciudad": "Quito",
            "telefono": "022345678",
            "tipo_servicio": "Medicina general",
            "horario": "08:00-20:00",
            "num_consultorios": 10,
            "tiene_emergencias": True
        },
        {
            "nombre": "Centro Médico Vida Sana",
            "direccion": "Calle 10 de Agosto 456",
            "ciudad": "Guayaquil",
            "telefono": "042223344",
            "tipo_servicio": "Pediatría",
            "horario": "09:00-18:00",
            "num_consultorios": 6,
            "tiene_emergencias": False
        }
    ]

    parques_docs = [
        {
            "nombre": "Parque La Alegría",
            "direccion": "Av. Los Álamos s/n",
            "ciudad": "Quito",
            "area_m2": 15000,
            "tipo_parque": "Infantil",
            "tiene_juegos_infantiles": True,
            "tiene_parqueadero": True,
            "precio_entrada": 0.0,
            "horario": "07:00-19:00"
        },
        {
            "nombre": "Aventura Park",
            "direccion": "Km 5 Vía a la Costa",
            "ciudad": "Guayaquil",
            "area_m2": 25000,
            "tipo_parque": "Acuático",
            "tiene_juegos_infantiles": True,
            "tiene_parqueadero": True,
            "precio_entrada": 5.50,
            "horario": "09:00-18:00"
        }
    ]

    clinicas.insert_many(clinicas_docs)
    parques.insert_many(parques_docs)

    client.close()
    print("✅ MongoDB: datos insertados en colecciones clinicas_particulares y parques_recreativos.\n")


def mongo_mostrar_clinicas():
    client, db = mongo_conectar()
    clinicas = db["clinicas_particulares"]
    print("📋 CLÍNICAS PARTICULARES (MongoDB):")
    for doc in clinicas.find():
        print(f"  - {doc['nombre']} ({doc['ciudad']}) | Emergencias: {'Sí' if doc.get('tiene_emergencias') else 'No'}")
    client.close()
    print()


def mongo_mostrar_parques_gratis():
    client, db = mongo_conectar()
    parques = db["parques_recreativos"]
    print("🎫 PARQUES GRATUITOS (MongoDB):")
    for doc in parques.find({"precio_entrada": 0.0}):
        print(f"  - {doc['nombre']} ({doc['ciudad']})")
    client.close()
    print()


# -----------------------------------
# MENÚ PRINCIPAL
# -----------------------------------

def menu():
    while True:
        print("=== APLICACIÓN BD RELACIONAL (SQLite3) + NO RELACIONAL (MongoDB) ===")
        print("1) Crear BD SQLite3 y cargar datos")
        print("2) Ver clínicas (SQLite3)")
        print("3) Ver parques (SQLite3)")
        print("4) Ver parques gratuitos (SQLite3)")
        print("5) Poblar MongoDB con datos de ejemplo")
        print("6) Ver clínicas (MongoDB)")
        print("7) Ver parques gratuitos (MongoDB)")
        print("8) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_bd_sqlite()
        elif opcion == "2":
            sqlite_mostrar_clinicas()
        elif opcion == "3":
            sqlite_mostrar_parques()
        elif opcion == "4":
            sqlite_parques_gratis()
        elif opcion == "5":
            mongo_poblar()
        elif opcion == "6":
            mongo_mostrar_clinicas()
        elif opcion == "7":
            mongo_mostrar_parques_gratis()
        elif opcion == "8":
            print("👋 Saliendo de la aplicación...")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.\n")


if __name__ == "__main__":
    menu()

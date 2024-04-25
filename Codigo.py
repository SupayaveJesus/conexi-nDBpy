import psycopg2
from psycopg2 import sql

# Crear la conexión a la base de datos
connection = psycopg2.connect(
    host="localhost",
    database="registrostudent",
    user="postgres",
    password="postgres",
)
cursor = connection.cursor()


# Función para registrar un nuevo estudiante
def registrar_estudiante(nombre_completo, fecha_nacimiento, carrera):
    cursor.execute(
        """
        INSERT INTO estudiantes(nombre_completo, fecha_nacimiento, carrera)
        VALUES(%s, %s, %s)
        RETURNING id_estudiante;
        """,
        (nombre_completo, fecha_nacimiento, carrera),
    )
    id_estudiante = cursor.fetchone()[0]
    connection.commit()
    print(f"Estudiante registrado con ID: {id_estudiante}")
    return id_estudiante


# Función para registrar una nueva materia
def registrar_materia(nombre_materia, creditos):
    cursor.execute(
        """
        INSERT INTO materias(nombre_materia, creditos)
        VALUES(%s, %s)
        RETURNING id_materia;
        """,
        (nombre_materia, creditos),
    )
    id_materia = cursor.fetchone()[0]
    connection.commit()
    print(f"Materia registrada con ID: {id_materia}")
    return id_materia


def inscribir_estudiante(id_estudiante, id_materia):
    try:
        cursor.execute(
            """
            INSERT INTO inscripciones(id_estudiante, id_materia)
            VALUES(%s, %s)
            RETURNING id_inscripcion;
            """,
            (id_estudiante, id_materia),
        )
        id_inscripcion = cursor.fetchone()[0]
        connection.commit()
        print(f"Estudiante con ID {id_estudiante} inscrito en la materia con ID {id_materia}")
        return id_inscripcion
    except Exception as e:
        print(f"Error al inscribir al estudiante: {e}")
        return None

def agregar_nota(id_inscripcion, nota):
    cursor.execute(
        """
        INSERT INTO notas(id_inscripcion, nota)
        VALUES(%s, %s)
        """,
        (id_inscripcion, nota),
    )
    connection.commit()
    print(f"Nota agregada a la inscripción con ID {id_inscripcion}")


def ver_notas_estudiante(id_estudiante):
    cursor.execute(
        """
        SELECT materias.nombre_materia, notas.nota
        FROM materias
        JOIN inscripciones ON materias.id_materia = inscripciones.id_materia
        JOIN notas ON inscripciones.id_inscripcion = notas.id_inscripcion
        WHERE inscripciones.id_estudiante = %s
        """,
        (id_estudiante,),
    )
    notas = cursor.fetchall()
    for nota in notas:
        print(nota)

# -- --------------------------------------------------
# Función para ver la lista de estudiantes registrados
def ver_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    for estudiante in estudiantes:
        print(estudiante)


# Función para ver las materias en las que está inscrito un estudiante específico
def ver_materias_estudiante(id_estudiante):
    cursor.execute(
        """
        SELECT materias.nombre_materia
        FROM materias
        JOIN inscripciones ON materias.id_materia = inscripciones.id_materia
        WHERE inscripciones.id_estudiante = %s
        """,
        (id_estudiante,),
    )
    materias = cursor.fetchall()
    for materia in materias:
        print(materia)


# Función para calcular el promedio de notas de un estudiante en una materia específica
def calcular_promedio_notas(id_estudiante, id_materia):
    cursor.execute(
        """
        SELECT AVG(notas.nota)
        FROM notas
        JOIN inscripciones ON notas.id_inscripcion = inscripciones.id_inscripcion
        WHERE inscripciones.id_estudiante = %s AND inscripciones.id_materia = %s
        """,
        (id_estudiante, id_materia),
    )
    promedio = cursor.fetchone()
    print(promedio)


# Función para actualizar la información de un estudiante
def actualizar_estudiante(id, nombre_completo, fecha_nacimiento, carrera):
    cursor.execute(
        """
        UPDATE estudiantes
        SET nombre_completo = %s, fecha_nacimiento = %s, carrera = %s
        WHERE id_estudiante = %s
        """,
        (nombre_completo, fecha_nacimiento, carrera, id),
    )
    connection.commit()
    print(f"Información del estudiante con ID {id} actualizada.")

# Función para actualizar la información de una materia
def actualizar_materia(id, nombre, creditos):
    cursor.execute(
        """
        UPDATE materias
        SET nombre_materia = %s, creditos = %s
        WHERE id_materia = %s
        """,
        (nombre, creditos, id),
    )
    connection.commit()
    print(f"Información de la materia con ID {id} actualizada.")

# Función para eliminar un estudiante de la base de datos
def eliminar_estudiante(id):
    # se elimina todas las inscripciones del estudiante
    cursor.execute("DELETE FROM inscripciones WHERE id_estudiante = %s", (id,))
    # eliminamos al estudiante
    cursor.execute("DELETE FROM estudiantes WHERE id_estudiante = %s", (id,))
    connection.commit()
    print(f"Estudiante con ID {id} eliminado.")

# Función para eliminar una materia de la base de datos
def eliminar_materia(id):
    # se elimina  todas las inscripciones de la materia
    cursor.execute("DELETE FROM inscripciones WHERE id_materia = %s", (id,))
    # despues  eliminams la materia
    cursor.execute("DELETE FROM materias WHERE id_materia = %s", (id,))
    connection.commit()
    print(f"Materia con ID {id} eliminada.")

def ver_todas_las_notas():
    cursor.execute("SELECT * FROM notas")
    todas_las_notas = cursor.fetchall()
    for nota in todas_las_notas:
        print(nota)

# Función para calcular el promedio de notas de un estudiante en una materia específica
def calcular_promedio_notas(id_estudiante, id_materia):
    cursor.execute(
        """
        SELECT notas.nota
        FROM notas
        JOIN inscripciones ON notas.id_inscripcion = inscripciones.id_inscripcion
        WHERE inscripciones.id_estudiante = %s AND inscripciones.id_materia = %s
        """,
        (id_estudiante, id_materia),
    )
    notas = cursor.fetchall()
    if notas:
        promedio = sum(nota[0] for nota in notas) / len(notas)
        print(f"El promedio de notas del estudiante con ID {id_estudiante} en la materia con ID {id_materia} es {promedio}")
    else:
        print(f"El estudiante con ID {id_estudiante} no tiene notas registradas para la materia con ID {id_materia}")


# Interfaz de usuario
def main():
    while True:
        print("\n1. Registrar un nuevo estudiante y sus materias")
        print("2. Ver la lista de estudiantes registrados")
        print("3. Ver las materias en las que está inscrito un estudiante específico")
        print("4. Calcular el promedio de notas de un estudiante en una materia específica")
        print("5. Actualizar la información de un estudiante")
        print("6. Actualizar la información de una materia")
        print("7. Eliminar un estudiante de la base de datos")
        print("8. Eliminar una materia de la base de datos")
        print("9. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            nombre_completo = input("Ingrese el nombre completo del estudiante: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            id_estudiante = registrar_estudiante(
                nombre_completo, fecha_nacimiento, carrera
            )

            materias = input("Ingrese los nombres de las materias, separados por comas: ").split(
                ","
            )
            creditos_list = input(
                "Ingrese los créditos de las materias, en el mismo orden y separados por comas: "
            ).split(",")
            notas = input("Ingrese las notas de las materias, en el mismo orden y separados por comas: ").split(",")

            for i in range(len(materias)):
                nombre_materia = materias[i].strip()
                creditos = creditos_list[i].strip()

                id_materia = registrar_materia(nombre_materia, creditos)
                id_inscripcion = inscribir_estudiante(id_estudiante, id_materia)
                if id_inscripcion is not None:
                    agregar_nota(id_inscripcion, notas[i].strip())
                else:
                    print("Error: No se pudo obtener un ID de inscripción válido.")

        elif opcion == "2":
            ver_estudiantes()

        elif opcion == "3":
            id_estudiante = input("Ingrese el id del estudiante: ")
            ver_materias_estudiante(id_estudiante)

        elif opcion == "4":
            id_estudiante = input("Ingrese el id del estudiante: ")
            id_materia = input("Ingrese el id de la materia: ")
            calcular_promedio_notas(id_estudiante, id_materia)

        elif opcion == "5":
            id = input("Ingrese el id del estudiante: ")
            nombre_completo = input("Ingrese el nuevo nombre completo del estudiante: ")
            fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del estudiante: ")
            carrera = input("Ingrese la nueva carrera del estudiante: ")
            actualizar_estudiante(id, nombre_completo, fecha_nacimiento, carrera)

        elif opcion == "6":
            id = input("Ingrese el id de la materia: ")
            nombre = input("Ingrese el nuevo nombre de la materia: ")
            creditos = input("Ingrese los nuevos créditos de la materia: ")
            actualizar_materia(id, nombre, creditos)

        elif opcion == "7":
            id_estudiante = input("Ingrese el ID del estudiante que desea eliminar: ")
            eliminar_estudiante(id_estudiante)

        elif opcion == "8":
            id_materia = input("Ingrese el ID de la materia que desea eliminar: ")
            eliminar_materia(id_materia)

        elif opcion == "9":
            print("Saliendo del programa...")
            connection.close()
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

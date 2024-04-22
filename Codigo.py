import psycopg2
import  tkinter as tk
# Crear la conexión a la base de datos
connection = psycopg2.connect(
    host = "localhost",
    database="registrostudent",
    user="postgres",
    password="postgres"
)
cursor = connection.cursor()

'''root = tk.Tk()
root.title("Registro de estudiantes")

label = tk.Label(root, text="Bienvenidos al Registro de estudiantes")
label.pack()'''

# Función para registrar un nuevo estudiante
def registrar_estudiante(nombre_completo, fecha_nacimiento, carrera):
    cursor.execute("""
        INSERT INTO Estudiantes(nombre_completo, fecha_nacimiento, carrera)
        VALUES(%s, %s, %s)
        RETURNING id_estudiante;
        """, (nombre_completo, fecha_nacimiento, carrera))
    id_estudiante = cursor.fetchone()[0]
    connection.commit()
    print(f"Estudiante registrado con ID: {id_estudiante}")
    return id_estudiante  # Devuelve el id del estudiante registrado


# Función para registrar una nueva materia
def registrar_materia(nombre_materia, creditos):
    cursor.execute("""
        INSERT INTO public.materias(nombre_materia, creditos)
        VALUES(%s, %s)
        RETURNING id_materia;
        """, (nombre_materia, creditos))
    id_materia = cursor.fetchone()[0]
    connection.commit()
    print(f"Materia registrada con ID: {id_materia}")
    return id_materia  # Devuelve el id de la materia registrada

def inscribir_estudiante(id_estudiante, id_materia):
    cursor.execute("""
        INSERT INTO public.inscripciones(id_estudiante, id_materia)
        VALUES(%s, %s)
        RETURNING id_inscripcion;
        """, (id_estudiante, id_materia))
    id_inscripcion = cursor.fetchone()[0]
    connection.commit()
    print(f"Estudiante con ID {id_estudiante} inscrito en la materia con ID {id_materia}")

def agregar_nota(id_inscripcion, calificacion):
    cursor.execute("""
        INSERT INTO public.notas(id_inscripcion, calificacion)
        VALUES(%s, %s)
        """, (id_inscripcion, calificacion))
    connection.commit()
    print(f"Nota agregada a la inscripción con ID {id_inscripcion}")

def ver_notas_estudiante(id_estudiante):
    cursor.execute("""
    SELECT materias.nombre_materia, notas.calificacion
    FROM public.materias
    JOIN public.inscripciones ON materias.id_materia = inscripciones.id_materia
    JOIN public.notas ON inscripciones.id_inscripcion = notas.id_inscripcion
    WHERE inscripciones.id_estudiante = %s
    """, (id_estudiante,))
    notas = cursor.fetchall()
    for nota in notas:
        print(nota)

# -- --------------------------------------------------
# Función para ver la lista de estudiantes registrados
def ver_estudiantes():
    cursor.execute("SELECT * FROM Estudiantes")
    estudiantes = cursor.fetchall()
    for estudiante in estudiantes:
        print(estudiante)

'''# Función para agregar una nueva materia
def agregar_materia(nombre_materia, creditos, id_estudiante):
    cursor.execute("""
        INSERT INTO public.materias(nombre_materia, creditos)
        VALUES(%s, %s)
        RETURNING id_materia;
        """, (nombre_materia, creditos))
    id_materia = cursor.fetchone()[0]
    connection.commit()
    print(f"Materia agregada con ID: {id_materia}")
    inscribir_estudiante(id_estudiante, id_materia)

def inscribir_estudiante(id_estudiante, id_materia):
    cursor.execute("""
        INSERT INTO public.inscripciones(id_estudiante, id_materia)
        VALUES(%s, %s)
        RETURNING id_inscripcion;
        """, (id_estudiante, id_materia))
    id_inscripcion = cursor.fetchone()[0]
    connection.commit()
    print(f"Estudiante con ID {id_estudiante} inscrito en la materia con ID {id_materia}")
'''
# Función para ver las materias en las que está inscrito un estudiante específico
def ver_materias_estudiante(id_estudiante):
    cursor.execute("""
    SELECT materias.nombre_materia
    FROM public.materias
    JOIN public.inscripciones ON materias.id_materia = inscripciones.id_materia
    WHERE inscripciones.id_estudiante = %s
    """, (id_estudiante,))
    materias = cursor.fetchall()
    for materia in materias:
        print(materia)

# Función para calcular el promedio de notas de un estudiante en una materia específica
def calcular_promedio_notas(id_estudiante, id_materia):
    cursor.execute("""
    SELECT AVG(Nota.valor)
    FROM Nota
    WHERE Nota.id_estudiante = %s AND Nota.id_materia = %s
    """, (id_estudiante, id_materia))
    promedio = cursor.fetchone()
    print(promedio)

# Función para actualizar la información de un estudiante
def actualizar_estudiante(id, nombre_completo, fecha_nacimiento, carrera):
    cursor.execute("""
    UPDATE Estudiantes
    SET nombre_completo = %s, fecha_nacimiento = %s, carrera = %s
    WHERE id = %s
    """, (nombre_completo, fecha_nacimiento, carrera, id))
    connection.commit()

# Función para eliminar un estudiante de la base de datos
def eliminar_estudiante(id):
    cursor.execute("DELETE FROM Estudiantes WHERE id = %s", (id,))
    connection.commit()

def eliminar_materia(id):
    cursor.execute("DELETE FROM Materias WHERE id = %s", (id,))
    connection.commit()

def main():
    while True:
        print("\n1. Registrar un nuevo estudiante y sus materias")
        print("2. Ver la lista de estudiantes registrados")
        print("3. Ver las materias en las que está inscrito un estudiante específico")
       #print("4. Calcular el promedio de notas de un estudiante en una materia específica")
        print("4. Ver las notas de un estudiante específico")  # Nueva opción

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
            id_estudiante = registrar_estudiante(nombre_completo, fecha_nacimiento,
                                                 carrera)  # Guarda el id del estudiante registrado

            materias = input("Ingrese los nombres de las materias, separados por comas: ").split(',')
            creditos_list = input(
                "Ingrese los créditos de las materias, en el mismo orden y separados por comas: ").split(',')
            notas = input("Ingrese las notas de las materias, en el mismo orden y separados por comas: ").split(',')

            id_materias = []  # Crear una lista vacía para almacenar los IDs de las materias

            for i in range(len(materias)):
                nombre_materia = materias[i].strip()
                creditos = creditos_list[i].strip()

                id_materia = registrar_materia(nombre_materia, creditos)  # Guarda el id de la materia registrada
                id_materias.append(id_materia)  # Agrega el id de la materia a la lista

                inscribir_estudiante(id_estudiante, id_materia)  # Inscribir al estudiante en la materia

            # Agregar una calificación a cada materia
            for i in range(len(materias)):
                id_materia = id_materias[i]  # Obtener el id de la materia
                calificacion = notas[i].strip()  # Obtener la calificación de la materia

                agregar_nota(id_materia, calificacion)  # Agregar la calificación a la materia

            print(f"IDs de las materias registradas: {id_materias}")

        elif opcion == "2":
            ver_estudiantes()
        elif opcion == "3":
            id_estudiante = input("Ingrese el id del estudiante: ")
            ver_materias_estudiante(id_estudiante)
            ver_notas_estudiante(id_estudiante)
        elif opcion == "4":
            id_estudiante = input("Ingrese el id del estudiante: ")
            id_materia = input("Ingrese el id de la materia: ")
            calcular_promedio_notas(id_estudiante, id_materia)
        #elif opcion == "4":  # Nueva opción
        #    id_estudiante = input("Ingrese el id del estudiante: ")
        #    ver_notas_estudiante(id_estudiante)
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
            id = input("Ingrese el id del estudiante: ")
            eliminar_estudiante(id)
        elif opcion == "8":
            id = input("Ingrese el id de la materia: ")
            eliminar_materia(id)
        elif opcion == "9":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()

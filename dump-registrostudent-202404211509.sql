select * from inscripciones i  ; 

-- cambiar el orden
SELECT id_inscripcion, id_nota, nota
FROM Notas
ORDER BY id_inscripcion, id_nota, nota;

----------------------------------------------------
SELECT id_materia, nombre_materia, creditos
FROM public.materias;

SELECT id_inscripcion, id_estudiante, id_materia
FROM public.inscripciones;

SELECT id_estudiante, nombre_completo, fecha_nacimiento, carrera
FROM public.estudiantes;

create table Notas(
	id_nota SERIAL primary key,
	nota numeric not null,
	id_inscripcion integer not null,
	foreign key(id_inscripcion) references inscripciones(id_inscripcion)
);
------------------------------------------------------------------------------
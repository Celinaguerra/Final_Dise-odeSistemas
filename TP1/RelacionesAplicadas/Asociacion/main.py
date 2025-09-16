from profesor import Profesor
from estudiante import Estudiante

profesor = Profesor("Juan Pérez")
estudiante_ana = Estudiante("Ana Gómez")
estudiante_luis = Estudiante("Luis García")

profesor.agregar_estudiante(estudiante_ana)
profesor.agregar_estudiante(estudiante_luis)

print(f"El profesor {profesor.nombre} tiene {len(profesor.estudiantes)} estudiantes.")
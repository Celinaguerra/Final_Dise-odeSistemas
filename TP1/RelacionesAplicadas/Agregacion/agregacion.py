from departamento import Departamento
from empleado import Empleado

empleado1 = Empleado("Carlos Sanchez")
empleado2 = Empleado("Laura Méndez")

departamento_ti = Departamento("Tecnologías de la Información")
departamento_ti.agregar_empleado(empleado1)
departamento_ti.agregar_empleado(empleado2)

# Si el departamento se elimina, los objetos Empleado siguen existiendo.
del departamento_ti
print(f"El empleado {empleado1.nombre} todavía existe.")
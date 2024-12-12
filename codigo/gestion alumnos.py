# codigo para la gestion de alumnos y registro en cursos

Ncurso = []
Nnombre = []

print("GESTION DE ALUMNOS Y REGISTRO EN CURSOS")
print("---------------------------------------------------")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print("¿Desea registrarse en un curso? (S/N): ")
registro = input().upper()
if registro == "S":
    curso = input("Ingrese el nombre del curso: ")
    Ncurso.append(curso)
    Nnombre.append(nombre)
    print(f"¡Bienvenido {nombre} a {curso}!")
    
else:
    print("¡Hasta luego!")
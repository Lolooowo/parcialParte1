class evaluacion:
    def __init__(self, puntualidad, equipo, productividad):
        self.productividad = productividad
        self.puntualidad = puntualidad
        self.equipo = equipo
    def promedio(self):
        promedio = 0
        promedio = (puntualidad+productividad+equipo) / 3
        return promedio

def estado(promedio):
    if promedio >= 7:
        return 'Satisfactorio'
    else:
        return 'Mejorar'

class Empleado:
    def __init__(self, nombre, departamento, antiguedad, evaluacion, informacion):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad
        self.evaluacion = evaluacion
        self.inforamcion = informacion
class Informacion:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo
empleados = {}
numEmpleados = int(input("Cuantos empleados desea ingresar: "))
for i in range(numEmpleados):
    codigoEmpleado = i+1
    print(f"Empledo No. {codigoEmpleado}")
    nombre = input("Ingrese el nombre del empleado: ")
    departamento = input("Ingrese el departamento del empleado: ")
    antiguedad = input("Ingrese la antiguedad: ")
    print("\t Ingrese la evalucion del empleado en un rango de 0-10:")
    productividad = int(input("Ingrese el productividad del empleado: "))
    puntualidad = int(input("Ingrese la puntualidad del empleado: "))
    equipo = int(input("Ingrese el trabajo en equipo del empleado: "))
    NuevaEvaluacion = evaluacion(puntualidad, equipo, productividad)
    print("\t Ingrese el contacto del empleado:")
    telefono = input("Ingrese el numero del telefono del empleado: ")
    correo = input("Ingrese el correo del empleado: ")
    informacion = Informacion(telefono, correo)
    nuevoEmpleado = Empleado(nombre, departamento, antiguedad, NuevaEvaluacion, informacion)
    promedio = nuevoEmpleado.evaluacion.promedio()
    NuevoEstado = estado(promedio)
    empleados[codigoEmpleado] = {
        "nombre": nuevoEmpleado.nombre,
        "departamento": nuevoEmpleado.departamento,
        "antiguedad": nuevoEmpleado.antiguedad,
        "evaluacion": {
            "equipo": nuevoEmpleado.evaluacion.equipo,
            "productividad": nuevoEmpleado.evaluacion.productividad,
            "puntualidad": nuevoEmpleado.evaluacion.productividad,
            "promedio": nuevoEmpleado.evaluacion.promedio(),
            "Estado": NuevoEstado
        },
        "informacion": {
            "telefono": nuevoEmpleado.inforamcion.telefono,
            "correo": nuevoEmpleado.inforamcion.correo,
        }
    }
for i in range(10):
    print("\n")

#Mostrar Informacin de todos los empleados

for clave, valor in empleados.items():
    print(f"\t Empleado: {clave}")
    print(f"Nombre: {valor['nombre']}")
    print(f"Departamento: {valor['departamento']}")
    print(f"Antiguedad: {valor['antiguedad']}")
    print(f"\t Evaluacion. ")
    print(f"Trabajo en equipo: {valor['evaluacion']['equipo']}")
    print(f"Productividad: {valor['evaluacion']['productividad']}")
    print(f"Puntualidad: {valor['evaluacion']['puntualidad']}")
    print(f"Promedio: {valor['evaluacion']['promedio']}")
    print(f"Estado: {valor['evaluacion']['Estado']}")
    print("\t Informacion.")
    print(f"Telefono: {valor['informacion']['telefono']}")
    print(f"Correo: {valor['informacion']['correo']}")

#Buscar Un Empleado

print("\n")
buscar= int(input("Ingrese el codigo del empleado para buscarlo: "))
empleado = empleados[buscar]
print(f"\t Empleado: {buscar}")
print(f"Nombre: {empleado['nombre']}")
print(f"Departamento: {empleado['departamento']}")
print(f"Antiguedad: {empleado['antiguedad']}")
print(f"\t Evaluacion. ")
print(f"Trabajo en equipo: {empleado['evaluacion']['equipo']}")
print(f"Productividad: {empleado['evaluacion']['productividad']}")
print(f"Puntualidad: {empleado['evaluacion']['puntualidad']}")
print(f"Promedio: {empleado['evaluacion']['promedio']}")
print(f"Estado: {empleado['evaluacion']['Estado']}")
print("\t Informacion.")
print(f"Telefono: {empleado['informacion']['telefono']}")
print(f"Correo: {empleado['informacion']['correo']}")

#Mostrar el total de "Satisfactorios en los empleados

contSatisfactorio = 0
for clave, valor in empleados.items():
    if valor["evaluacion"]["Estado"] == "Satisfactorio":
        contSatisfactorio += 1
print(f"Total de personas con una calificacion de (Satisfactorio): {contSatisfactorio}")

#Quien tiene el promedio mayor


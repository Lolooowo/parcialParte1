class evaluacion:
    def __init__(self, puntualidad, equipo, productividad):
        self.productividad = productividad
        self.puntualidad = puntualidad
        self.equipo = equipo
    def promedio(self):
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
    codigoEmpleado = i
    nombre = input("Ingrese el nombre del empleado: ")
    departamento = input("Ingrese el departamento del empleado: ")
    antiguedad = input("Ingrese la antiguedad: ")
    print("\t Ingrese la evalucion del empleado en un rango de 0-10:")
    productividad = int(input("Ingrese el productividad del empleado: "))
    puntualidad = int(input("Ingrese la puntualidad del empleado: "))
    equipo = int(input("Ingrese el trabajo en equipo del empleado: "))
    evaluacion = evaluacion(puntualidad, equipo, productividad)
    print("\t Ingrese el contacto del empleado:")
    telefono = input("Ingrese el numero del telefono del empleado: ")
    correo = input("Ingrese el correo del empleado: ")
    informacion = Informacion(telefono, correo)
    nuevoEmpleado = Empleado(nombre, departamento, antiguedad, evaluacion, informacion)
    promedio = nuevoEmpleado.evaluacion.promedio()
    estado = estado(promedio)
    empleados[codigoEmpleado] = {
        "nombre": nuevoEmpleado.nombre,
        "departamento": nuevoEmpleado.departamento,
        "antiguedad": nuevoEmpleado.antiguedad,
        "evaluacion": {
            "equipo": nuevoEmpleado.evaluacion.equipo,
            "productividad": nuevoEmpleado.evaluacion.productividad,
            "puntualidad": nuevoEmpleado.evaluacion.productividad,
            "promedio": nuevoEmpleado.evaluacion.promedio(),
            "Estado": estado
        },
        "informacion": {
            "telefono": nuevoEmpleado.inforamcion.telefono,
            "correo": nuevoEmpleado.inforamcion.correo,
        }
    }
for i in range(10):
    print("  ")
print("HOlas")



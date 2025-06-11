course_list = []
students_list = []
close_system = False

""" 
Funcionalidad que se encarga de validar si el documento ya fue registrado
y de registrar un estudiante en el sistema
"""
def append_user(username, document, sexo):
    student_registered = False
    # Recorro todos los estudiantes
    for student in students_list:
        # Valido si el documento ingresado ya está en mis registros
        if student[1] == document:
            # En caso de encontrarlo, imprimo que ya está registrado
            print("Estudiante ya registrado.")
            # Termino el loop
            student_registered = True
            break

    # Si no está registardo, lo registro
    if not student_registered:
        students_list.append([username, document, sexo, []])

    # Devuelvo si el estudiante ya fue registrado o no.
    return student_registered

"""
Función que se encarga de validar si el curso ya existe y de registrarlo en el sistema
"""
def append_course(course_name, course_max_users):
    register_course = True
    # Recorro todos los cursos
    for course in course_list:
        if not course[3]:
            continue

        # Valido si el nombre ya se encuentra registrado y si el curso sigue disponible => sigue con cupos
        if course[0] == course_name:
            # Si el curso ya fue registrado, valido si quedan cupos
            if course[1] != course[2]:
                # No debo registrar un nuevo curso porque quedan cupos
                register_course = False
                print("Este curso ya existe y tiene cupos disponibles")
                break
            else:
                # Debo registrar un nuevo curso porque no quedan cupos
                course[3] = True
                break

    # Registro el curso
    if register_course:
        # Ingreso nombre del curso, máxima cantidad de usuarios, cantidad de usuarios registrados y si se visibiliza el registro (display)
        register = [course_name, course_max_users, 0, True]
        # Agrego el cusro al listado de cursos
        course_list.append(register)

"""
Función que muestra el listado de estudiantes.
"""
def show_students():
    # Valido si hay estudiantes ingresados
    if len(students_list) == 0:
        # SI no hay estudiantes, imprimo un mensaje mostrando que no hay estudiantes
        print("El sistema todavía no tiene estudiantes cargados.\n")
        # No ejecuto el resto de la función
        return False

    for student in students_list:
        # Armo un string con todos los cursos del estudiante separados por coma.
        curso_string = ""
        for course_id in student[3]:
            course_name = get_course_name(course_id)
            if course_name is not None:
                curso_string += f"{course_name}, "

        # Elimino los últimos dos caracteres, debreían ser siempre una coma y un espacio al pedo.
        final_string = curso_string[:-2]

        # Imprimo cada estudiante, su documento, su sexo y sus cursos.
        print(f"Nombre: {student[0]}, Documento: {student[1]}, Sexo: {student[2]}, Cursos: {final_string}")

    return True

def get_course_name(course_id):
    for key, value in enumerate(course_list):
        if key == course_id:
            return value[0]

    print("No course found for that id.")
    return None

"""
Función que muestra el listado de cursos.
"""
def show_courses() -> bool:
    # Valido que hayan cursos registrados
    if len(course_list) == 0:
        print("El sistema todavía no tiene cursos cargados.\n")
        return False

    # Contador para validarq que se haya imprreso al menos un curso
    amount_printed = 0
    # Recorro todos los cursos por key (posición) value (registro/curso)
    for key, value in enumerate(course_list):
        # Si la tercer posición (display) es verdadera, verifico si hay que mostrarlo o ya se llenó
        if value[3]:
            # Valido si ya está lleno el curso
            if int(value[2]) >= int(value[1]):
                course_list[key][3] = False
            else:
                # Si no está lleno, lo listo y muestro su información correspondiente
                amount_printed += 1
                print(f"[{key}] {value[0]}. {value[2]}/{value[1]} cupos disponibles.")

    return amount_printed > 0

"""
Función que vincula un estudiante a un curso.
"""
def validate_course_availability(course_id) -> bool:
    # Valido si existe el registro con el id ingresado.
    if not course_list[course_id]:
        print("El curso no existe, por favor ingrese un id valido.")
        return False
    # VAlido que el curso tenga cupos disponibles
    if int(course_list[course_id][2]) == int(course_list[course_id][1]):
        # Si no hay cupos, dejo de mostrarlo en el listado de cursos.
        course_list[course_id][3] = False
        # Comento que no hay más cupos.
        print("Ya no hay cupos disponibles para este curso")
        # Retorno falso
        return False

    # Retorno el nombre del curso
    return course_list[course_id][0]

"""
Función que se encarga de agregar el curso al listado de cursos de un estudiante
"""
def add_course_to_course_list(student_id, course_id) -> bool:
    for student in students_list:
        print(student)
        if int(student[1]) == student_id:
            student[3].append(course_id)
            return True

    return False

def append_user_to_course(course_id = -1, student_id = -1):
    # Valido que haya cursos registrados.
    if len(course_list) == 0:
        print("No hay cursos disponibles en este momento, por favor ingrese cursos.")
        return

    # Valido que haya estudiantes registrados.
    if len(students_list) == 0:
        print("No hay estudiantes registrados, por favor ingrese estudiantes.")

    # Busca recuperar el nombre de un curso con espacios validos
    coursename = None
    while course_id == -1:
        print("Ingrese el identificador del curso al que desea ingresar el estudiante: ")
        # Imprimo y valido que haya cursos con cupos disponibles.
        if not show_courses():
            print("No hay cursos con vacantes en este momento, por favor cree un nuevo curso.")
            return

        # Solicito que ingresen un id de curso
        course_id = int(input())
        # Valido que el curso exista y que tenga espacios disponibles
        coursename = validate_course_availability(course_id)
        if not coursename:
            course_id = -1

    # Recorro hasta que ingresen un documento de esutidantes valido
    while student_id == -1:
        # Muestro el listado de estudiantes.
        show_students()
        student_id = int(input("Ingrese el documento del estudiante:"))

        # Intengo registrar el curso al listado de cursos del estudiante ingresado
        if not add_course_to_course_list(student_id, course_id):
            student_id = -1

    course_list[course_id][2] += 1
    print("Estudiante inscripto corretamente")

def modify_user_data(user_document):
     for student in students_list:
         if student[1] == user_document:
            print("Ingrese el nuevo nombre del estudiante: ")
            student[0] = input()
            print("Ingrese el nuevo sexo del estudiante: ")
            student[2] = input()
            return True

     print("No se ha encontrado ese documento en el listado de usuarios.")
     return None

def modify_course_data(course_id):
    for key, value in enumerate(course_list):
        if key == course_id:
            print("Ingrese el nuevo nombre del curso:")
            value[0] = input()

            valid_max_users = False
            while not valid_max_users:
                print("Ingrese el nuevo cupo máximo de usuarios")
                new_max_users = int(input())
                if new_max_users >= value[2]:
                    valid_max_users = True
                    value[1] = new_max_users
                else:
                    print("El curso tiene más inscriptos del cupo que quiere definir, por favor ingrese otro monto.")

            return True

    print("No se ha encontrado ese id en el listado de cursos.")
    return False

def show_user_inscription_percentage():
    for course in course_list:
        percentage = int(course[2])/int(course[1])*100
        print(f"Se ha ocupado un {percentage}% del curso {course[0]}")

"""
Función que visibiliza el menú de navegación en la aplicación.
"""
def start():
    print("Por favor ingrese que acción quiere ejecutar")
    print("[1] Cargar estudiante")
    print("[2] Cargar curso")
    print("[3] Inscribir estudiante a curso")
    print("[4] Modificar datos estudiante")
    print("[5] Modificar datos curso")
    print("[7] Ver porcentaje de inscritos al curso")
    print("[8] Ver listado de cursos")
    print("[9] Ver listado de estudiantes")
    print("[-1] Salir del programa")

    return int(input())

print("Bienvenido a nuestro gestor de cursos y estudiantes")
while not close_system:
    action = start()
    if action == -1:
        close_system = True
        break

    # Se fija que acción ingreso el usuario
    match action:
        # Crear estudiante
        case 1:
            if append_user(input("Ingrese el nombre del estudiante que desea ingresar: "), input("Ingrese el documento del estudiante: "), input("Ingrese el sexo del estudiante: ")):
                append_user_to_course(student_id = students_list[-1][1])
        # Crear curso
        case 2:
            append_course(input("Ingrese el nombre del curso: "), input("Ingrese la cantidad máxima de usuarios: "))
        # Vincular el usuario a un curso
        case 3:
            append_user_to_course()
        case 4:
            user_modified = None
            while user_modified is None:
                show_students()
                user_modified = modify_user_data(input("Ingrese el documento del estudiante que desea modificar: "))
        case 5:
            course_modified = None
            while course_modified is None:
                if not show_courses():
                    print("No hay cursos validos para modificar.")
                    continue

                course_modified = modify_course_data(int(input("Ingrese el identificador del curso que desea modificar: ")))
        case 7:
            show_user_inscription_percentage()
        # Ver listado de cursos
        case 8:
            show_courses()
        # Ver listado de estudiantes
        case 9:
            show_students()

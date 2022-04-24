import sqlite3
import getpass
from typing import Tuple


def main():


    '''nombre = input("Ingrese el alumno: ")

    apellido = input("Ingrese el apellido: ")

    if crear_alumno(nombre,apellido):
        print("Ingreso el alumno correctamente")

    else:
        print("No ingreso correctamente")'''
 
    #Consultar alumno
    nombre = input("Cual alumno buscas: ")
    apellido = input("Apellido del alumno: ")

    consultar_alumno(nombre,apellido) 


def crear_alumno(nombre,apellido):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

#insertar nuevo alumno    
    
    query = f"INSERT INTO student VALUES(NULL,'{nombre}','{apellido}')"
    print("Query a ejecuar: ", query)
    rows = cursor.execute(query)
    
 
    nombre = rows.fetchone()


    
    conn.commit() 
    cursor.close()
    conn.close()

    if nombre == None:
        return True

    return False



   

  

def consultar_alumno(nombre,apellido):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    

    query = f"SELECT id FROM student WHERE nombre='{nombre}' AND apellido='{apellido}'"

    print('query ejecutar; ', query)

    rows = cursor.execute(query)
    usuario = rows.fetchone()
    print(usuario)

    
    cursor.close()
    conn.close()


    if usuario == usuario and usuario != None:
        print(f"se encuentra registrado '{nombre}','{apellido}'")
        

    else:
        print('no registrado')

    

               
        
if __name__ == "__main__":
    main()


try:
    n= float(input("Introduce un número "))
    5/n
except TypeError:
    print("No se puede dividir el número por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede divir por cero, prueba otro número")
except Exception as e:
    print( type(e)._name_)

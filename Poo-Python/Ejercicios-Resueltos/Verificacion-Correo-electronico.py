#Verificacion del correo electronico 

correo = input("Ingresa un correo electronico: ")

if correo.count('@') == 1:
    print("El correo electronico es valido")
else:
    print("El correo electronico no es valido")
    
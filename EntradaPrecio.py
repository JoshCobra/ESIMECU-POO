#Programa Calcula el Precio de la entrada segun la Edad
#DE LA ROSA VAZQUEZ JOSUE

e=1
while e==1:

    edad = int(input("Cual es tu edad?:"))

    if edad < 4:
        print("La entrada es Gratis")
    elif 4 <= edad <= 18:
        print("Debes Pagar 5 Euros")
    else:
        print("El precio de la entrada es 10 Euros")
    e = int(input("Volver a Ingresar? si=1/no=otro:"))

else:
    print("Programa Terminado")

#clave

secreto = 'ESIME'
clave = input("Dime la clave:")

while clave != secreto:
    print("Clave incorrecta!!!")
    otra = input("Quieres introducir otra clave (s/n)?:")
    if otra.upper()=="n":
        break;
    clave = input("Dime la clave:")
    if clave == secreto:
        print("Bienvenido!!!")
        print("Porgrama terminado")
        
print("\n")
print("Programa 2 \n")


#programa2
"""Continue: The continue statement in Python is used to skip
the remaining code inside a loop for the current iteration only"""

cont = 0
while cont < 10:
    cont = cont + 1 #( cont+ = 1 )
    if cont %2 != 0:
        continue
    print(cont)

    
        

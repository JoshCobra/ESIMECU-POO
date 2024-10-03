#Promedio de edades por Turno

mañana = []
for i in range(5):
    edad_M=int(input("introduce la edad del alumno de la mañana: "))
    i+1

tarde = []
for i in range(6):
    edad_T=int(input("introduce la edad del alumno de la tarde: "))
    i+1

noche = []
for i in range(11):
    edad_N = int(input("introduce la edad del alumno de la noche: "))
    i+1

promedio_M = sum(edad_M)/ len(edad_M)
promedio_T = sum(edad_T)/ len(edad_T)
promedio_N = sum(edad_N)/ len(edad_N)

print("Promedios de la Mañana: ", promedio_M)
print("Promedios de la Tarde: ", promedio_T)
print("Promedio de la Noche: ", promedio_N)

if promedio_M > promedio_T and promedio_M > promedio_N:
    print("El turno de la mañana tiene el mejor")
elif promedio_T > promedio_M and promedio_T > promedio_N:
    print("El promedio de la tarde es el mejor")
else:
    print("El promedio de la noche tiene el mayor promedio")
    


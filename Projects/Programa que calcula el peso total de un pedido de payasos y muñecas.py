
# Programa que calcula el peso total de un pedido de payasos y muñecas
#DE LA ROSA VAZQUEZ JOSUE

peso_payaso = 112  # gramos
peso_muñeca = 75  # gramos

num_payasos = int(input("Introduce el numero de payasos vendidos: "))
num_muñecas = int(input("Introduce el numero de muñecas vendidas: "))

peso_total = (peso_payaso * num_payasos) + (peso_muñeca * num_muñecas)

print("El peso total del paquete es:", peso_total," gramos")

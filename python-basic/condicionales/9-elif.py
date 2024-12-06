"""Se debe validar el ingreso mensual, y mostrar
lo siguiente dependiendo del salario
salario > 10000 , nostrar ganas bien en cualquier parte del mundo
si salrio >1000, estas bien en surameria, de lo contrario mostrar eres pobre
"""

salario = 5000
if (salario > 10000):
# se valida esta condicion si se cumple entra si no se evaluda la condicion de abajo
    print("ganas bien en cualquier parte del mundo")
elif (salario > 1000):
# se valida esta condicion si se cumple entra si no se evaluda la condicion de abajo
    print("ganas bien en sur america")
else:
#Si no se cumple niguna condicion se imprime este bloque
    print("Eres pobre")
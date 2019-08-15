# Sitio de Craigslist que será consultado
site = input("Ingrese el sitio de Craigslist que será consultado\n")
area = input("Ingrese el area en donde se hará la busqueda\n")

# Ajustes de la busqueda
min_price = input("Ingrese el precio minimo que está dispuesto a pagar\n")
max_price = input("Ingrese el maximo precio que está dispuesto a pagar\n")
limit = int(input("Ingrese el numero de resultados que desea obtener\n"))

# Vecindarios
num = int(input("Ingrese el numero de vecindarios que quiere consultar\n"))
VECINDARIOS = []
while num > 0:
	vec = input("Ingrese el nombre de un vecindario\n")
	VECINDARIOS.append(vec)
	num -= 1

# Formato en el que se desea obtener los resultados
formato = input("Ingrese el formato en el que quiere los resultados (csv/txt)\n")
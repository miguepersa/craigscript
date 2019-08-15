# Se importa CraigslistHousing como clh
from craigslist import CraigslistHousing as clh
from ajustes import *

print("\nBuscando...")

# Inicializacion de CraigslistHousing
cl = clh(
	site=site, 
	area=area, 
	category='apa',
	filters={'max_price': max_price, 'min_price': min_price})

# Obtencion de los resultados
resultados = cl.get_results(sort_by='newest', limit=limit)

# Lista en donde serán almacenados los 
# resultados filtrados
res_filtrados = []

# Filtro de resultados por ubicación
for res in resultados:
	for vec in VECINDARIOS:
		if vec in str(res["where"]).lower():
			res_filtrados.append(res)

# Items importantes de cada resultado
items = ["name", "where", "price", "area", "url"]

# Se abre el archivo en el cual se escribirán los resultados
# obtenidos del proceso de busqueda

# Ciclo para escribir los resultados con el formato deseado
# en el archivo
for resultado in res_filtrados:
    res = ""
    # Los resultados se guardaran en un archivo .csv
    if formato == "csv":
        apts = open("apartamentos.csv", 'a')
        for item in items:
        	it = ""
        	# Filtro de comas
        	for i in str(resultado[item]):
        		if i != ",":
        			it = it + i
        	res = res + it + ","
        res = res[:len(res)-1] + "\n"
        apts.write(res)
    # Los resultados se guardarán en un archivo .txt
    elif formato == "txt":
        apts = open("apartamentos.txt", 'a')
        res = ""
        for item in items:
            res = res + str(resultado[item]) + " | "
        res = res[:len(res)-3] + "\n"
        apts.write(res)

# Se cierra el archivo luego del proceso de escritura
apts.close()

print("Fin de la ejecución")
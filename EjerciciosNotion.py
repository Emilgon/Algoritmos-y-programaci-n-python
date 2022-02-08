#Variables

#C2E1
volumen_reservorio = 4.445e8
lluvia = 5e6
porcentaje_disminuido_de_lluvia= 10
porcentaje_aumento_reservorio= 5
porcentaje_disminuido_reservorio= 2
resta= 2.5e5
aumento_reservorio= volumen_reservorio*(porcentaje_aumento_reservorio/100)
print(aumento_reservorio)
disminución_lluvias=lluvia*(porcentaje_disminuido_de_lluvia/100)
lluvia_disminuida=lluvia-disminución_lluvias
print(lluvia_disminuida)
disminución_reservorio=volumen_reservorio*(porcentaje_disminuido_reservorio/100)
reservorio_disminuido=volumen_reservorio-disminución_reservorio
print(reservorio_disminuido)
regiones_aridas=volumen_reservorio-resta
print(regiones_aridas)

#C2E2
username = "Ana"
timestamp = "07:00"
url = "https://petshop.com/pets/reptiles/pythons"
print(f"{username} ingresó al sitio {url} a las {timestamp} A.M")

#Condicionales

#C3E1
# q=input("Ingrese un número para saber si es par o impar: ")
# if int(q)%2==0:
#     print(f"El número {q} es par")
# else:
#     print(f"El número {q} impar")

#C3E2
# nombre_p=input("Ingrese su nombre: ")
# edad_p=input("Ingrese su edad: ")
# precio_1= 0.00
# precio_2= 1.50
# precio_3= 1
# precio_4= 2.00
# if int(edad_p)<=4:
#     print(f"El cliente: {nombre_p} tiene: {edad_p} años y su entrada de cine cuesta: ${precio_1}")
# elif int(edad_p)<=18:
#     print(f"El cliente: {nombre_p} tiene: {edad_p} años y su entrada de cine cuesta: ${precio_2}")
# elif int(edad_p)>=60:
#     print(f"El cliente: {nombre_p} tiene: {edad_p} años y su entrada de cine cuesta: ${precio_3}")
# elif 18<int(edad_p)<60:
#     print(f"El cliente: {nombre_p} tiene: {edad_p} años y su entrada de cine cuesta: ${precio_4}")

#C3E3
# premio_2="Bronze"
# premio_3="Plata"
# premio_4="Oro"
# premio= input("Ingrese sus puntos: ")
# if (1<=int(premio)<=50):
#     print(f"No hay premios para {premio} pts")
# if (51<=int(premio)<=150):
#     print(f"Felicitaciones, Ganaste la medalla de {premio_2} por haber tenido {premio} pts!")
# if (151<=int(premio)<=180):
#     print(f"Felicitaciones, Ganaste la medalla de {premio_3} por haber tenido {premio} pts!")
# if (181<=int(premio)<=200):
#     print(f"Felicitaciones, Ganaste la medalla de {premio_4} por haber tenido {premio} pts!")

#Lista y ciclos

#C4E1
oración=["Estoy", "imprimiendo", "una", "lista", "línea", "por", "línea"]
for i in oración:
    print(i)

#C4E2
for i in range(5,31,5):
    print(i)

#C4E3
students = ["Emmie Grey",
"Andre Hills",
"Gurpreet Atherton",
"Johan Stewart",
"Joseff Hurst",
"Margot Conrad",
"Matteo Whitaker",
"Mekhi Hussain",
"Sherry Macdonald",
"Mathew Cano",
"Cara O'Moore",
"Kush Gonzalez",
"Soren Clark",
"Inaayah Broadhurst",
"Ruth Lawrence",
"Nafisa Nairn",
"Zachariah Velasquez"]

for i in students:
    print(i.lower().replace(" ","_"))









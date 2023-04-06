#---------------------
#escribir en consola
print("hola")
#----------------------------------
#como escribir variables

#frase_bienvenida no empezar la varible por numeros o carcateristicas
#solo se puede empezar la variable con la caracteristica guion bajo
#no se recomienda usar acentos

frase_bienvenida = "primer dia en python."

print (frase_bienvenida)

#-----------------
#reasignar variables a variables mediante otras variables
variable_1 = "variable 1"

variable_2 = variable_1

print(variable_1)

#--------------------------
#reasignar valores a variables
a = "primer valor"
print(a)

a = "segundo valor"
print(a)

#-------------------------------
#finalizacion de instrucciones

#se le puede poner ; al final de cada instruccion
#si esto no se hace no pasa nada
#esto sirve si queres poner varias instrucciones en un renglon

#-----------------------------------
#espacios en blanco
#los espacios se ignoran, osea es lo mismo
#variable = "hola"
#variable          =            "hola"

#-----------------------------------
#entrada, salida y almacenaje de datos al programa
# input()

nombre = input("di tu nombre:\n")
#variable = instruccion("texto")
#La salida esta en la parte de concatenacion

#-----------------------------------
#salto de linea
# \n 
#para hacer "la barra invertida"( \ ) apretar Alt+92

#-----------------------------------
#concatenacion ( + )
#unir dos trozos de texto
print ("Bienvenido/a " + nombre + ".")

#--------------------------------------
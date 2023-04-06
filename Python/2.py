#print (""Blue" es azul ").
#esto no se puede debido a que se abre y se cierra entre las primeras comillas.

#se puede usar comillas simples o dobles al igual que en las ecuaciones el {[()]}.
#print ('"Blue" es azul')
#esto si se puede.

#--------------------------------
#funcion len() devuelve el numero de caracteres que tiene un print.


print(len("amarillo")) #nos comenta cuantos caracteres tiene "amarillo" = 8; se puede acceder a cualquier posicion, se empieza a contar desde el 0, osea.

# A M A R I L L O
# 0 1 2 3 4 5 6 7

#para acceder a ellos es de la siguiente manera.
color = "Amarillo"

print(color[0]) #al ser "0" el numero que pusimos, la letra que mostrara sera la A.

#--------------------------------------
#integer

numero_1 = 100
numero_2 = 400

#los numeros en las variables al no estar entre comillas se convierten en numeros camapces de realizar cuentas matematicas. si los pusieramos entre comillas se convertirian en texto legible.

#sumas.
print(numero_1 + numero_2)

#simbolos: suma + ; resta - ; multiplicacion * ; division / ;
#exponentes ** ; Ejemplo 2**3 = 8;  2*2*2 = 8;

#Hay que utilizar python como si fuera una calculadora a la hora de utilizar las matematicas; Osea hay que utilizar los { [ ( ) ] }.



#Para numeros largos como este: 9123456789123456789; es mejor escribirlos de la siguiente manera:9_123_456_789_123_456_789; Para asi poder ver las separaciones.


#-------------------------------
#tipos de datos.


#Los numeros decimales se expresan con "."; Ej: 18.49; este es un numero de tipo "float".

#Tipo de dato Booleano, solo puede ser verdadero o falso, se escriben así.
# nombre_de_variable = True;
# nombre_de_variable = False;
#Es importante que la primer letra de True o de False este en mayuscula.

#----------------------------------
#funcion Type.

entero = 4
float = 58.47
texto = "TEXTO"
decision = True

print(type(entero))
print(type(float))
print(type(texto))
print(type(decision))

#En consola al igual que con la funcion "len"(la cual te indica la cantidad de caracteres); La funcion "(type)" (te indica el tipo/clase de variable que es).

#--------------------------------------
#Función len con numeros


#si intentamos poner lo siguiente:

#numero = 123456789
#print(len(numero))

#nos saltara un error, debido a que "len" no puede leer caracteres de tipo entero.
#Por lo tanto si queremos leer cuantos caracteres posee la variable "numero" tendremos que hacer lo siguente:

#numero = "123456789"
#print(len(numero))

#Al agregar las comillas pasa a ser texto y la funcion len si lo puede leer.

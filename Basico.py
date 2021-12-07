# hola a todos hoy les voy a enseñar un poco de python de como estar 
# y lo primero que les enseñare sera la forma de usar print
"cuando queremos mostrar una indicacion en python usamos print"  
print("hola mundo")
#Se usamos comillas para que se escriba el hola mundo para no tener errores

#Tambien se pueden poner otros valores para eso definiremos las siguiente funcion

a=3
print(a)
#Se a definico una funcion para mostrar el uso de print, aunque esta datos se clasifican en mas valores ahora solo les enseñaremos:
# Numeros enteros que se les conoce en python como int
a=3
print(a)
 # los numeros decimales que se les llama float, que son de la siguente manera
b=3.3
print(b)    
# para saber con que datos estas trabajando se ocupa la funcion
type(a)
#ahora intentelo con b
#como en en la aritmetica python tambien tiene operaciones para relacionar numeros como:
# el operador == que es para decir si son iguales los valores entre si

4==4

4==5

"hola mundo"=="hola mundo"

"hola"=="hola mundo"    
#tambien se puede ocupar para valores como el de arriba
# te enseñare ahora cuando son valores distinto se usa !=

2!=3

2!=2

# < y > que ayuda para las desigualdades

2 > 3

3 > 2

2 < 3

3 < 2
 
# Se usa  casi de la misma manera el <= solo que se ocupa para mayor
# o igual al lado izquierdo

3 <= 4

#pasa casi igual para el  >= pero del lado derecho

3 >= 4

#Ahora trabajaremos con operaciones como +, -, /, y *
# primero definos dos funciones
a=3
b=4
c=a/b
d=a*b
e=a+b
print(c)
print(d)
print(e)
# aunque tambien se puede hacer de la siguiete manera como una calculadora
x=3/2
print(x)
# ahora una operacion que causa confucion si se quiere elevar un numero a una potencia se ocupa
# de la siguiente forma 2**3 que se agrega un * mas que en la multiplicacion
r=2**3
print(r)
#Por ultimo agregaremos los condiccionales logicos como son
# primero la condicion if que solo acepta valores ciertos o falso
# y para este ejemplo ocuparemos lo vistoa arriba de las operaciones 

mi_numero= 3
if mi_numero==3:
    print("ese es mi numero")
#como se ve primero se compara un objeto y despues se ocupa el if "variable que se analiza" "operacion":
#y al final para mostrar el objeto se pone un print() auque seadentro del if 
#ahora el caso en que es falso
mi_numero= 3
if mi_numero==4:
    print("ese es mi numero")
#como vez no se agrago nada ya que el valor fue falso y por lo tanto no escribimos 
# la forma en que el codigo pudiera tener mas opciones asi que ocuparemos un print
# fuera del if y sera todo, pero por ahora
mi_numero= 3
if mi_numero==4:
    print("ese es mi numero")
print("rayos")

#El error de arriba se arregla de la siguiente manera y eso agregado un else
# nos ayuda a darno otra opcion cuando es contraria a la afromacion que pensabamos
mi_numero= 3
if mi_numero==4:
    print("ese es mi numero")
else:    
    print("rayos")
# pero si es verdadero no afectara a nuestro codigo
mi_numero= 3
if mi_numero==3:
    print("ese es mi numero")
else:    
    print("rayos")
#Y por ultimo el elif que nos da mas opciones al momento de hacer codigo
mi_numero= 3
if mi_numero==4:
    print("ese es mi numero")
elif mi_numero==3:
    print("la segunda es la vencida")
else:    
    print("rayos")
# asi es lo mas basico que necesitas para saber 
#saludos
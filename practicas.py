# Inmutables = Numeros, String, Tuplas y los Sets.
# Mutables = Listas, Diccionarios

print("Python Unidad 1")

while True:
    try:
        s = int(input("Ingrese una variable de tipo Entero: "))
        if s != "":
            print("Correcto", type(s))
            break        
    except ValueError:
        print("No es correcto, esa variable es String")


j = 'Tomas'
l = list(j)
print(l)

l[0] = 'C'
print(l)

''.join(l)
print(''.join(l))

print(help(j.find))  # Nota: Los métodos pueden concatenarse 

                   
#Reasignacion en listas!

f1 = [0,1,2]
f2 = f1
print(f1,f2)


# en este caso si cambia el valor de uno el otro tambien lo hara
f1[0] = 3
print(f1,f2)

# para que no suceda se usa copy.copy
import copy

f2 = copy.copy(f1)
f1[0] = 0
print(f1,f2)



lista = ['a','b','c',['d','e','f',['g','h','i']]]


print(lista)
print("---------------------------------------")
for a in lista:
    if isinstance(a,list):
        for b in a:
            print(b)
    else:
        print(a)
print("---------------------------------------")
for a in lista:
    if isinstance(a,list):
        for b in a:
            if isinstance(b,list):
                for c in b:
                    print(c)
            else:
                print(b)
    else:
        print(a)
print("---------------------------------------")

def recorrer(item):
    for x in item:
        if isinstance(x,list):
            recorrer(x)
        else:
            print(x)

recorrer(lista)


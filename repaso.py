# Pida un número. Si el número es mayor a cero, verifique si es par o impar. Si el número es igual a cero, diga que es neutro.
#5
# numero=float(input("digite un numero" ))
#1
# if numero > 0 and numero % 2== 0:
#     print(f"el numero {numero}es par ")
# else: 
#     print(f"el numero {numero}es impar ")

# if numero == 0:
#     print("el numero es neutro")

# #anidado

# if numero > 0:
#     if numero % 2==0:
#         print("el numero es par")
#     else:
#         print("el numero es impar")

# elif numero ==0:
#     print("el numero es neutro")

# else:
#     print("usted digito un numero negativo")
    

# Lea la temperatura. Si es menor a 10 grados diga "Frío". Si está entre 10 y 25 diga "Templado". Si es mayor a 25 diga "Calor".

# temperatura=float(input("digite la temperatura"))

# if temperatura < 10:
#     print("frio")

# elif temperatura >=10 and temperatura <=25:
#     print("templado")

# elif temperatura > 25:
#     print("caliente")

# Pida un usuario y una clave. Si el usuario es "estudiante", verifique la clave. Si la clave es "123", diga "Acceso", si no, "Error de clave".

usuario=input("Digite el usuario ")
clave=input("Digite la clave ")

if usuario =="estudiante":
    if clave=="123":
        print("Acceso")
    else:
        print("Error en la clave")
else:
    print("Usuario incorrecto")
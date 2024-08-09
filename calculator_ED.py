
def sum(a, b):
    return a+b;

def rest(a, b):
    return a-b;

def multi(a, b):
    return a*b;

def divid(a, b):
    return a/b;



def calc():
    print("Bienvenido a la calculadora de Edwin");
    user=input("Por favor escribe tu contraseña para usar la Calculadora: ");
    pass_valid=["edwin", "pas"]
    if user not in pass_valid:
        print("No tienes acceso");
        
    else:
        while True:
            print("Estas son las operaciones permitidas, elige una: ");
            print("1. Suma");
            print("2. Resta");
            print("3. Multiplicacion");
            print("4. Division");
            print("5. Salir")
            opcion=int(input("Aqui elige la opcion: "))
            
            if opcion==1:
                valor1=int(input("Inserte el valor1: "));
                valor2=int(input("Inserte el valor2: "));
                print("Tu resultado es: ", sum(valor1, valor2))

            if opcion==2:
                valor1=int(input("Inserte el valor1: "));
                valor2=int(input("Inserte el valor2: "));
                print("Tu resultado es: ", rest(valor1, valor2)) 

            if opcion==3:
                valor1=int(input("Inserte el valor1: "));
                valor2=int(input("Inserte el valor2: "));
                print("Tu resultado es: ", multi(valor1, valor2)) 

            if opcion==4:
                valor1=int(input("Inserte el valor1: "));
                valor2=int(input("Inserte el valor2: "));
                print("Tu resultado es: ", divid(valor1, valor2))   

            elif opcion==5:
                print("Saliendo del programa.....")
                break;
            
calc()
        

#Este es un confesionario de Autos de Lujo.

class Auto:
    def __init__(self, marca, modelo,color):
        self.marca=marca;
        self.modelo=modelo;
        self.color=color;
        self.disponible=True;

    def Rentar(self):
        if self.disponible==True:
            self.disponible=False;
            print(f"El auto {self.modelo} esta sido rentado.")
        else:
            print(f"No se puede rentar el auto {self.modelo}.")

    def Devolver(self):
        self.disponible=True;
        print(F"El auto {self.modelo} ya esta disponible.")


class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre=nombre;
        self.cedula=cedula;
        self.auto_rentados=[];

    def Rentar_auto(self, auto):
        if auto.disponible:
            auto.Rentar();
            self.auto_rentados.append(auto);
        else:
            print(f"El auto {self.modelo} no esta disponible");

    def Devolver_auto(self, auto):
        if auto in self.auto_rentados:
            auto.Devolver()
            self.auto_rentados.remove(auto);
        else:
            print(f"El auto {self.modelo} no esta disponible.")


class Edwin_auto_import:
    def __init__(self):
        self.autos=[]
        self.clientes=[];

    def Rentando_auto(self, auto):
        self.autos.append(auto);
        print(f"Has rentado el auto {auto.modelo}")
        #Aqui no se busca el constructor si no la lsita 
        #de los carrros registados.

    def Registro_cliente(self, cliente):
        self.clientes.append(cliente);
        print(f"El cliente {cliente.nombre} ha sido registrado")

    def Carros_disponibles(self):
        print("Autos Disponibles");
        for auto in self.autos:
            if auto.disponible:
                print(f"{auto.modelo}");

#Creando objetos:
carro1=Auto("Honda", "Civic", "Blanco");
carro2=Auto("Toyota", "Rav4", "Negro");

cliente1=Cliente("Edwin", "12345");
cliente2=Cliente("Ramon", "402");

#Rentando autos:
auto_import=Edwin_auto_import();
auto_import.Rentando_auto(carro1);
auto_import.Rentando_auto(carro2);

auto_import.Registro_cliente(cliente1);
auto_import.Registro_cliente(cliente2);

#mostras carros disponibles
auto_import.Carros_disponibles()

#vamos a rentar el auto
cliente1.Rentar_auto(carro1);

#mostras carros disponibles
auto_import.Carros_disponibles()

cliente1.Devolver_auto(carro1);
#mostras carros disponibles
auto_import.Carros_disponibles()

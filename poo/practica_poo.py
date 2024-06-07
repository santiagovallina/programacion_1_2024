# Santiago Vallina  

# Crear una clase Persona que tenga las características nombre y edad. La persona debe poder
# mostrar un mensaje saludando presentándose con su nombre y edad. Se debe crear la clase e
# implementarla.

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

santi = Persona(nombre = "santi", edad = 24)
# santi.saludar()


# Crear una clase Libro que tenga las características título, autor y año de publicación. Del libro se
# debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase
# e implementarla.

class Libro:
    def __init__(self, titulo, autor, año) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    def mostrar_datos_libro(self):
        return print(f"Libro: {self.titulo}. \nAutor: {self.autor}. \nAño: {self.año}.")

libro = Libro(titulo = "Narnia", autor= "Pepe argento", año = 2009)

# libro.mostrar_datos_libro()


# Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe
# poder calcular el área y el perímetro. Se debe crear la clase e implementarla.

class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = self.base * self.altura
        return print(area)
    
    def calcular_perimetro(self):
        perimetro = self.base + self.altura
        return print(perimetro)

rectangulo = Rectangulo(base = 5, altura = 2)
# rectangulo.calcular_area()
# rectangulo.calcular_perimetro()


# Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. Se debe
# crear la clase e implementarla.

class Calculadora:
    def __init__(self, operador_a, operador_b) -> None:
        self.operador_a = operador_a
        self.operador_b = operador_b
    
    def sumar(self):
        return print(self.operador_a + self.operador_b)
    
    def restar(self):
        return print(self.operador_a - self.operador_b)
    
    def multiplicar(self):
        return print(self.operador_a * self.operador_b)
    
    def dividir(self):
        return print(self.operador_a // self.operador_b)


numeros = Calculadora(operador_a = 50, operador_b = 25 )
# numeros.sumar()
# numeros.restar()
# numeros.multiplicar()
# numeros.dividir()


# Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal
# las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las
# características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que
# realizan. Se debe crear la clase e implementarla.

class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
class Perro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.nombre = nombre
    
    def ladrar(self):
        return print(f"El perro {self.nombre} hace guau guau.")

class Gato(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.nombre = nombre
    
    def maullar(self):
        return print(f"El gato {self.nombre} hace miau.")

perro = Perro(nombre = "Coco")
#perro.ladrar()
gato = Gato(nombre = "Michi")
#gato.maullar()


# Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. De la
# cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue
# exitoso). Se debe crear la clase e implementarla.

class Cuenta_bancaria:
    def __init__(self, titular, saldo_encapsulado) -> None:
        self.__titular = titular
        self.__saldo_encapsulado = saldo_encapsulado
    
    def obtener_saldo(self):
        saldo = self.__saldo_encapsulado
        return print(f"Su saldo es {saldo}")
    
    def depositar(self):
        saldo = self.__saldo_encapsulado
        numero = int(input("Ingrese cuanto desea depositar: "))
        nuevo_saldo = saldo + numero
        return print(f"Moivimiento exitoso. \nUsted depositó ${numero}. Ahora tiene ${nuevo_saldo}")
    
    def retirar(self):
        saldo = self.__saldo_encapsulado
        numero = int(input("Ingrese cuanto desea retirar: "))
        if numero > saldo:
            numero = int(input("No tiene suficiente saldo, ingrese de nuevo: "))
        nuevo_saldo = saldo - numero
        return print(f"Moivimiento exitoso. \nUsted retiró ${numero}. Ahora tiene ${nuevo_saldo}")

cuenta = Cuenta_bancaria(titular= "santi", saldo_encapsulado= 45000)
# cuenta.obtener_saldo()
# cuenta.depositar()
# cuenta.retirar()
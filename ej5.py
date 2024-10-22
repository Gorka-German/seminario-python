class Calculadora:
    def __init__(self):
        # Atributo privado para almacenar el estado interno de la calculadora.
        self.__estado = 0

    # Método privado para validar si el valor es un entero.
    def __validar_entero(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El valor debe ser un número entero.")

    # Método para sumar.
    def suma(self, valor):
        self.__validar_entero(valor)
        self.__estado += valor

    # Método para restar.
    def resta(self, valor):
        self.__validar_entero(valor)
        self.__estado -= valor

    # Método para multiplicar.
    def multiplicacion(self, valor):
        self.__validar_entero(valor)
        self.__estado *= valor

    # Método para la división entera.
    def division(self, valor):
        self.__validar_entero(valor)
        if valor == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        self.__estado //= valor

    # Método para establecer el estado interno.
    def set(self, valor):
        self.__validar_entero(valor)
        self.__estado = valor

    # Método para reiniciar el estado a 0.
    def reset(self):
        self.__estado = 0

    # Método para obtener el estado interno.
    def get_resultado(self):
        return self.__estado

    # Método interactivo para realizar operaciones.
    def run(self):
        print("Calculadora interactiva. Introduzca 'salir' para terminar.")
        while True:
            try:
                operacion = input("Ingrese la operación (suma, resta, multiplicacion, division, set, reset, resultado): ").strip().lower()
                
                if operacion == "salir":
                    print("Saliendo de la calculadora.")
                    break
                
                if operacion == "reset":
                    self.reset()
                    print("Estado reiniciado a 0.")
                    continue
                
                if operacion == "resultado":
                    print(f"Estado actual: {self.get_resultado()}")
                    continue
                
                # Para las operaciones que requieren un valor.
                if operacion in ["suma", "resta", "multiplicacion", "division", "set"]:
                    valor = input("Ingrese un valor entero: ").strip()
                    try:
                        valor = int(valor)
                    except ValueError:
                        print("Error: El valor debe ser un número entero.")
                        continue

                    # Realizar la operación correspondiente.
                    if operacion == "suma":
                        self.suma(valor)
                    elif operacion == "resta":
                        self.resta(valor)
                    elif operacion == "multiplicacion":
                        self.multiplicacion(valor)
                    elif operacion == "division":
                        try:
                            self.division(valor)
                        except ZeroDivisionError as e:
                            print(f"Error: {e}")
                            continue
                    elif operacion == "set":
                        self.set(valor)

                    # Mostrar el resultado después de la operación.
                    print(f"Resultado: {self.get_resultado()}")
                else:
                    print("Operación no válida. Intente de nuevo.")
            
            except Exception as e:
                print(f"Se produjo un error: {e}")


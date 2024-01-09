import os
import platform
import random
import sys

class LabraxtorInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        try:
            lines = code.split('\n')
            for line in lines:
                self.execute(line.strip())
        except Exception as e:
            print(f"Se produjo un error durante la interpretación: {e}")

    def execute(self, line):
        try:
            if line.endswith(','):
                if line.startswith('mostrar'):
                    self.handle_print(line)
                elif line.startswith('detener'):
                    self.handle_stop()
                elif line.startswith('fin'):
                    self.handle_end()
                elif line.startswith('agregar'):
                    self.handle_add(line)
                elif line.startswith('definir'):
                    self.handle_define(line)
                elif line.startswith('salto'):
                    self.handle_line_break()
                elif line.startswith('aleatorio'):
                    self.handle_random(line)
        except Exception as e:
            print(f"Se produjo un error durante la ejecución: {e}")

    def handle_random(self, line):
        try:
            max_range = int(line.split(' ')[1])
            numero_aleatorio = random.randint(1, max_range)
            self.variables['resultado_aleatorio'] = numero_aleatorio
            print(f"{numero_aleatorio}")
        except (ValueError, IndexError):
            print("Error: Formato de declaración inválido")

    def handle_print(self, line):
        try:
            partes = line.split('\'')
            if len(partes) >= 2:
                texto = partes[1]
                for nombre_var, valor_var in self.variables.items():
                    texto = texto.replace(f'#{nombre_var}', str(valor_var))
                print(texto, end=' ')
            else:
                print("Error: Formato de declaración de impresión inválido")
        except Exception as e:
            print(f"Se produjo un error durante el manejo de la impresión: {e}")

    def handle_stop(self):
        try:
            input("Presiona Enter para continuar...")
        except Exception as e:
            print(f"Se produjo un error durante el manejo de la parada: {e}")

    def handle_end(self):
        try:
            sys.exit()
        except SystemExit:
            pass
        except Exception as e:
            print(f"Se produjo un error durante el manejo del fin: {e}")

    def handle_add(self, line):
        try:
            nombre_archivo = line.split('\'')[1]
            with open(nombre_archivo, 'r') as archivo:
                codigo_incluido = archivo.read()
                self.interpret(codigo_incluido)
        except FileNotFoundError:
            print(f"Error: Archivo '{nombre_archivo}' no encontrado")
        except Exception as e:
            print(f"Se produjo un error durante el manejo de la adición: {e}")

    def handle_define(self, line):
        try:
            partes = line.split('=')
            if len(partes) == 2:
                nombre_var = partes[0].strip()
                valor_var = partes[1].strip().strip(',')
                self.variables[nombre_var] = valor_var
            else:
                print("Error: Formato de definición de variable inválido")
        except Exception as e:
            print(f"Se produjo un error durante el manejo de la definición: {e}")

    def handle_line_break(self):
        try:
            print()
        except Exception as e:
            print(f"Se produjo un error durante el manejo del salto de línea: {e}")



if len(sys.argv) > 1:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = input("Archivo a ejecutar: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        codigo = archivo.read()

    interprete = LabraxtorInterpreter()
    interprete.interpret(codigo)
except FileNotFoundError:
    print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
except Exception as e:
    print(f"Se produjo un error: {e}")

class LabraxtorInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        lines = code.split('\n')
        for line in lines:
            self.execute(line.strip())

    def execute(self, line):
        if line.endswith(','):
            if line.startswith('pt'):
                self.handle_print(line)
            elif line.startswith('sp'):
                self.handle_stop()
            elif line.startswith('ed'):
                self.handle_end()
            elif line.startswith('add'):
                self.handle_add(line)
            elif line.startswith('def'):
                self.handle_define(line)
            elif line.startswith('sl'):
                self.handle_line_break()
       

    def handle_print(self, line):
        parts = line.split('\'')
        if len(parts) >= 2:
            text = parts[1]
            for var_name, var_value in self.variables.items():
                text = text.replace(f'#{var_name}', str(var_value))
            print(text, end=' ')
        else:
            print("Error: Invalid print statement format")

    def handle_stop(self):
        input("Press Enter to continue...")

    def handle_end(self):
        exit()

    def handle_add(self, line):
        filename = line.split('\'')[1]
        try:
            with open(filename, 'r') as file:
                included_code = file.read()
                self.interpret(included_code)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_define(self, line):
        parts = line.split('=')
        if len(parts) == 2:
            var_name = parts[0].strip()
            var_value = parts[1].strip().strip(',')
            self.variables[var_name] = var_value
        else:
            print("Error: Invalid variable definition format")

    def handle_line_break(self):
        print()  # Print a new line


# Example usage
interpreter = LabraxtorInterpreter()
filename = input("File (example: test.lx): ")
with open(filename, 'r') as file:
    code = file.read()

interpreter.interpret(code)

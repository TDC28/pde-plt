from itertools import combinations_with_replacement

from variables import Variable, VariableList


class FirstOrderTime:
    def __init__(self):
        self.variables = VariableList()
        self.pde_order = self.get_pde_order()

        n_vars = int(input("Number of independent variables (Min 1, max 4): "))

        for i in range(n_vars):
            if i == 0:
                print("\nt selected as variable 1")
                timestep = self.get_stepsize("t")
                time_range = self.get_variable_range("t")
                self.variables.append(Variable("t", 1, timestep, time_range))
                continue

            symbol = self.get_variable_symbol(i)
            highest_order = self.get_highest_order(symbol)
            stepsize = self.get_stepsize(symbol)
            var_range = self.get_variable_range(symbol)

            self.variables.append(Variable(symbol, highest_order, stepsize, var_range))

        self.get_pde()
        self.get_initial_condition()
        # self.get_boundary_conditions()

    def get_pde_order(self):
        while True:
            try:
                order = int(input("Enter the order of the PDE (Max 3): "))
                return order

            except:
                print("Invalid input. Enter an integer.")

    def get_variable_symbol(self, i):
        while True:
            variable = input(f"\nInput symbol for variable {i+1}: ")

            if (
                variable not in self.variables
                and variable != "f"
                and " " not in variable
                and "." not in variable
            ):
                return variable

            print("Variable already exists or is invalid. Enter a different symbol.")

    def get_highest_order(self, symbol):
        while True:
            try:
                highest_order = int(
                    input(f"Highest order of a derivative with respect to {symbol}: ")
                )
                return highest_order

            except ValueError:
                print("Invalid Input. Enter an integer.")

    def get_stepsize(self, variable):
        while True:
            try:
                stepsize = float(input(f"Select stepsize d{variable}: "))
                return stepsize

            except ValueError:
                print("Invalid input. Enter a number.")

    def get_variable_range(self, symbol):
        while True:
            try:
                lower = float(input(f"Minimum {symbol} value: "))
                upper = float(input(f"Maximum {symbol} value: "))
                return lower, upper

            except:
                print("Invalid input. Enter numbers.")

    def get_pde(self):
        pde = "f_t "
        symbols = self.variables.list_variables()
        derivatives = []

        for i in range(self.pde_order):
            derivatives += list(
                combinations_with_replacement(self.variables[1:], i + 1)
            )

        for i in range(len(derivatives)):
            pde += f"+ g{i+1}({symbols}) * f_{"".join(str(derivatives[i]))} "

        pde += f"= k({symbols})"
        print("\nPDE has form", pde)
        return NotImplemented

    def get_initial_condition(self):
        while True:
            try:
                symbols = self.variables.list_variables()
                ic = f"lambda {symbols[3:]}: " + input(
                    f"\nEnter initial condition f(0, {symbols[3:]})\nf(0, {symbols[3:]}) = lambda {symbols[3:]}: "
                )
                self.ic = eval(ic)
                return

            except:
                print("Invalid input. Make sure the input is a valid lambda function.")

    def get_boundary_conditions(self):
        return NotImplemented

from conditions import DirichletBC, InitialCondition, NeumannBC, RobinBC
from functions import Function, FunctionList
from variables import Variable, VariableList


class PDE:
    def __init__(self):
        self.variables = VariableList()
        self.cfs = FunctionList()
        self.ics = FunctionList()
        self.bcs = FunctionList()

        self.get_variables()
        self.get_pde()
        self.get_ics()
        self.get_bcs()

    def get_variables(self):
        n_vars = int(input("Number of independent variables (Min 1, max 4): "))

        print("\nt selected as variable 1")

        timestep = self.get_stepsize("t")
        time_range = self.get_variable_range("t")

        self.variables.append(Variable("t", 1, timestep, time_range))

        for i in range(1, n_vars):
            symbol = self.get_variable_symbol(i)
            highest_order = self.get_highest_order(symbol)
            stepsize = self.get_stepsize(symbol)
            var_range = self.get_variable_range(symbol)

            self.variables.append(Variable(symbol, highest_order, stepsize, var_range))

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

    def get_pde(self):
        while True:
            try:
                self.pde_order = int(input("\nEnter the order of the PDE: "))
                break

            except:
                print("Invalid input.")

        pde_form = ""
        symbols = ", ".join(self.variables.symbols)
        derivatives = self.generate_derivatives()

        for i in range(len(derivatives)):
            pde_form += f"g{i+1}({symbols}) * f_{"".join(derivatives[i])} + "

        pde_form = pde_form[:-2]
        pde_form += f"= k({symbols})"
        print("\nPDE has form", pde_form, "\n")

        for i in range(len(derivatives)):
            while True:
                try:
                    pde_text = input(f"g{i+1}({symbols}) = lambda {symbols}: ")
                    pde = eval(f"lambda {symbols}: " + pde_text)
                    break

                except:
                    print("Invalid input. Make sure input is a valid lambda function.")

            self.cfs.append(Function(pde))

    def generate_derivatives(self):
        derivatives = []

        def backtrack(i=0, curr=[]):
            if len(curr) == self.pde_order:
                return

            for j in range(i, len(self.variables)):
                var = self.variables[j]

                if curr.count(var.symbol) == var.highest_order:
                    continue

                curr.append(var.symbol)
                derivatives.append(curr.copy())
                backtrack(j, curr)
                curr.pop()

        backtrack()
        derivatives.sort(key=len, reverse=True)
        derivatives.sort(key=lambda x: x.count("t"), reverse=True)
        return derivatives

    def get_ics(self):
        for order in range(self.variables[0].highest_order):
            ic = InitialCondition(order)
            ic.get_initial_condition(self.variables.symbols)
            self.ics.append(ic)

    def get_bcs(self):
        for var in self.variables:
            if var.highest_order == 0 or var.symbol == "t":
                continue

            print(f"\nInput {var.highest_order} boundary conditions for variable {var}")

            for _ in range(var.highest_order):
                bc = self.input_bc(var)
                self.bcs.append(bc)

    def input_bc(self, var):
        while True:
            try:
                print("\nSelect BC type")
                print("1 - Dirichlet")
                print("2 - Neumann")
                print("3 - Robin")

                choice = int(input())

                match choice:
                    case 1:
                        bc = DirichletBC(var)

                    case 2:
                        bc = NeumannBC(var)

                    case 3:
                        bc = RobinBC(var)

                    case _:
                        raise Exception("Enter a valid input")

                break

            except:
                print("Enter a valid input.")

        bc.get_bc(self.variables.symbols)
        return bc

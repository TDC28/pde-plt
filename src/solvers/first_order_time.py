from itertools import combinations_with_replacement


class FirstOrderTime:
    def __init__(self):
        self.variables = ["t"]
        self.highest_derivative_orders = [1]
        self.stepsizes = []
        self.pde_order = self.get_pde_order()

        n_vars = int(input("Number of independent variables (Min 1, max 4): "))

        for i in range(n_vars):
            if i == 0:
                print("\nt selected as variable 1")
                dt = self.get_stepsize("t")

                self.stepsizes.append(dt)
                continue

            variable = self.get_variable_symbol(i)
            highest_order = self.get_highest_order(variable)
            stepsize = self.get_stepsize(variable)

            self.variables.append(variable)
            self.highest_derivative_orders.append(highest_order)
            self.stepsizes.append(stepsize)

        self.get_pde()
        # self.get_initial_condition()
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
            ):
                return variable

            print("Variable already exists or is invalid. Enter a different symbol.")

    def get_highest_order(self, variable):
        while True:
            try:
                highest_order = int(
                    input(f"Highest order of a derivative w.r.t. {variable}: ")
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

    def get_pde(self):
        pde = "f_t "
        variables = ", ".join(self.variables)
        derivatives = []

        for i in range(self.pde_order):
            derivatives += list(
                combinations_with_replacement(self.variables[1:], i + 1)
            )

        for i in range(len(derivatives)):
            pde += f"+ g{i+1}({variables}) * f_{"".join(derivatives[i])} "

        pde += f"= k({variables})"
        print("\nPDE has form", pde)
        return NotImplemented

    def get_initial_condition(self):
        while True:
            try:
                variables = ", ".join(self.variables)
                ic = input(
                    f"\nEnter initial condition f(0, {variables[3:]})\n\nlambda {variables[3:]}: "
                )

                return NotImplemented

            except:
                print("Invalid input. Make sure the input is a valid lambda function.")

    def get_boundary_conditions(self):
        return NotImplemented

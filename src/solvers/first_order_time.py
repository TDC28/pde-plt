class FirstOrderTime:
    def __init__(self):
        self.indep_vars = ["t"]
        self.highest_derivative_orders = [1]
        self.stepsizes = []

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

            self.indep_vars.append(variable)
            self.highest_derivative_orders.append(highest_order)
            self.stepsizes.append(stepsize)

    def get_variable_symbol(self, i):
        while True:
            variable = input(f"\nInput symbol for variable {i+1}: ")

            if variable not in self.indep_vars and variable != "f":
                return variable

            print("Variable already exists or is invalid. Enter a different symbol")

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

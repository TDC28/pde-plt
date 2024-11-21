from functions import Function


class BoundaryCondition(Function):
    def __init__(self, var):
        super().__init__(None)
        self.var = var


class DirichletBC(BoundaryCondition):
    def get_bc(self, variables):
        print("Choose a boundary")
        print(
            f"\n1 - ({self.var} = {self.var.value_span[0]})\n2 - ({self.var} = {self.var.value_span[1]})"
        )

        while True:
            try:
                choice = int(input())

                self.boundary = self.var.value_span[choice - 1]
                break

            except:
                print("Invalid input.")

        var_index = variables.index(self.var.symbol)

        input_symbols = variables.copy()
        input_symbols[var_index] = str(self.var.value_span[choice - 1])
        inputs = ", ".join(input_symbols)

        lambda_vars = variables.copy()
        lambda_vars.pop(var_index)
        lambda_inputs = ", ".join(lambda_vars)

        while True:
            try:
                bc_input = input(f"f({inputs}) = lambda {lambda_inputs}: ")
                bc_func = eval(f"lambda {lambda_inputs}:" + bc_input)
                break

            except:
                print("Invalid input. Make sure input is a valid lambda function.")

        self.func = bc_func


class NeumannBC(BoundaryCondition):
    def get_bc(self, variables):
        print("Choose a boundary")
        print(
            f"\n1 - ({self.var} = {self.var.value_span[0]})\n2 - ({self.var} = {self.var.value_span[1]})"
        )

        while True:
            try:
                choice = int(input())

                self.boundary = self.var.value_span[choice - 1]
                break

            except:
                print("Invalid input.")

        var_index = variables.index(self.var.symbol)

        input_symbols = variables.copy()
        input_symbols[var_index] = str(self.var.value_span[choice - 1])
        inputs = ", ".join(input_symbols)

        lambda_vars = variables.copy()
        lambda_vars.pop(var_index)
        lambda_inputs = ", ".join(lambda_vars)

        while True:
            try:
                bc_input = input(f"f_t({inputs}) = lambda {lambda_inputs}: ")
                bc_func = eval(f"lambda {lambda_inputs}:" + bc_input)
                break

            except:
                print("Invalid input. Make sure input is a valid lambda function.")

        self.func = bc_func


class RobinBC(BoundaryCondition):
    def get_bc(self, variables):
        pass


class InitialCondition(Function):
    def __init__(self, order):
        super().__init__(None)
        self.order = order

    def get_initial_condition(self, variables):
        while True:
            try:
                symbols = variables[1:]
                inputs = ", ".join(symbols)
                func = (
                    f"f(0, {inputs})"
                    if self.order == 0
                    else f"f_{'t'*self.order}(0, {inputs})"
                )
                ic = f"lambda {inputs}: " + input(
                    f"\nEnter initial condition {func}\nf(0, {inputs}) = lambda {inputs}: "
                )
                self.fn = eval(ic)
                return

            except:
                print("Invalid input. Make sure the input is a valid lambda function.")

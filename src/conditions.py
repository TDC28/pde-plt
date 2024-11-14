class BoundaryCondition:
    def __init__(self, var):
        self.var = var


class BCList:
    def __init__(self):
        self.bcs = []

    def __itr__(self):
        return iter(self.bcs)

    def append(self, bc):
        self.bcs.append(bc)


class DirichletBC(BoundaryCondition):
    def get_bc(self):
        pass


class NeumannBC(BoundaryCondition):
    def get_bc(self):
        pass


class RobinBC(BoundaryCondition):
    def get_bc(self):
        pass


class InitialCondition:
    def __init__(self, order):
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
                self.ic = eval(ic)
                return

            except:
                print("Invalid input. Make sure the input is a valid lambda function.")


class ICList:
    def __init__(self):
        self.ics = []

    def __itr__(self):
        return iter(self.ics)

    def append(self, ic):
        self.ics.append(ic)

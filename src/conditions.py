class BoundaryCondition:
    def __init__(self, var):
        self.var = var


class BCList:
    pass


class DirichletBC(BoundaryCondition):
    pass


class NeumannBC(BoundaryCondition):
    pass


class RobinBC(BoundaryCondition):
    pass


class InitialCondition:
    pass


class ICList:
    pass

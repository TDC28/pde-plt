import solvers


class CLI:
    def __init__(self):
        print("Welcome to PDE-PLT, the linear partial differential equation plotter.\n")

        order = input("Enter the order of the PDE (max 2): ")
        n_vars = input("Enter the number of independant variables (max 2): ")
        highest_dt_order = input("Enter the highest order of a time derivative: ")

        assert order.isnumeric() and 0 <= int(order) <= 2
        assert n_vars.isnumeric() and 0 <= int(n_vars) <= 2
        assert highest_dt_order.isnumeric() and 0 <= int(highest_dt_order) <= int(order)

        self.order = int(order)
        self.n_vars = int(n_vars)
        self.highest_dt_order = int(highest_dt_order)

        if self.order == 1:
            self.solver = solvers.FirstOrder()

        elif self.highest_dt_order == 1:
            self.solver = solvers.SecondOrder_OneTime()

        elif self.highest_dt_order == 2:
            self.solver = solvers.SecondOrder_OneTime()

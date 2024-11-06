import solvers


class CLI:
    def __init__(self):
        print("Welcome to PDE-PLT, the linear partial differential equation plotter.\n")

        highest_dt_order = input("Enter the highest order of a time derivative: ")
        self.highest_dt_order = int(highest_dt_order)

        match self.highest_dt_order:
            case 1:
                self.solver = solvers.FirstOrderTime()

            case _:
                return

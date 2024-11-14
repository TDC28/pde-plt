import solvers

if __name__ == "__main__":
    print("Welcome to PDE-PLT, the linear partial differential equation plotter.\n")

    highest_dt_order = int(input("Enter the highest order of a time derivative: "))

    match highest_dt_order:
        case 1:
            solver = solvers.FirstOrderTime()

        case _:
            print("Not implemented")
            solver = None

    if solver:
        solver.solve()

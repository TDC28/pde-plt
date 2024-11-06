class SecondOrder_OneTime:
    pass


class SecondOrder_TwoTime:
    def __init__(self):
        print(
            "\nPDE of the form u_tt + f(t, x) u_t + g(t, x) u_xx + h(t, x) u_x = k(t, x)"
        )

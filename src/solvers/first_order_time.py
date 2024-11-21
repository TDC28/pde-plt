import numpy as np

from pde import PDE


class FirstOrderTime:
    def __init__(self):
        self.pde = PDE()

        v1 = self.pde.variables[0]

        if len(self.pde.variables) == 1:
            self.f = np.array([0 for _ in range(v1.n_vals)], dtype=np.float64)
            # Probably will get deleted as this is not interesting

        elif len(self.pde.variables) == 2:
            v2 = self.pde.variables[1]
            self.f = np.array(
                [[0 for _ in range(v2.n_vals)] for _ in range(v1.n_vals)],
                dtype=np.float64,
            )

        elif len(self.pde.variables) == 3:
            v2, v3 = self.pde.variables[1:3]
            self.f = np.array(
                [
                    [[0 for _ in range(v3.n_vals)] for _ in range(v2.n_vals)]
                    for _ in range(v1.n_vals)
                ],
                dtype=np.float64,
            )

    def solve(self):
        vars = self.pde.variables

        if len(vars) == 2:
            self.f[0] = self.pde.ics[0](vars[1].values)

            for bc in self.pde.bcs:
                self.apply_bc(bc, 0)

        elif len(vars) == 3:
            return NotImplemented

    def apply_bc(self, t, *args):
        return NotImplemented

    def plot_solution(self):
        pass

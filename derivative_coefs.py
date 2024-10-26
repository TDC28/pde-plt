import numpy as np


def coefs(n):
    coefs = [1, -1]

    for _ in range(n - 1):
        coefs.append(0)

        for j in range(len(coefs) - 2, -1, -1):
            coefs[j + 1] -= coefs[j]

    return np.array(coefs)

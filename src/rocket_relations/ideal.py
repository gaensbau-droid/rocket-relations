import numpy as np

def c_star(gamma, R, T0):

    if gamma <= 1 or R <= 0 or T0 <= 0:
        raise ValueError("Invalid inputs")
    return (1 / np.sqrt(gamma)) * np.sqrt(((2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1))) * R * T0)


def c_f(gamma, Pe_P0, Pa_P0, Ae_At):

    if gamma <= 1 or Pe_P0 <= 0 or Ae_At <= 1:
        raise ValueError("Invalid inputs")
    term1 = np.sqrt(
        (2 * gamma**2 / (gamma - 1))
        * (2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1))
        * (1 - Pe_P0 ** ((gamma - 1) / gamma))
    )
    term2 = (Pe_P0 - Pa_P0) * Ae_At
    return term1 + term2
        

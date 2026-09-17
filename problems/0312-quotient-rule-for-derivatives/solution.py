import numpy as np
def quotient_rule_derivative(g_coeffs, h_coeffs, x):

    g = np.polyval(g_coeffs, x)
    h = np.polyval(h_coeffs, x)

    g_prime = np.polyval(np.polyder(g_coeffs), x)
    h_prime = np.polyval(np.polyder(h_coeffs), x)

    if h == 0:
        raise ValueError("Denominator cannot be zero")

    return float((g_prime * h - g * h_prime) / h**2)
import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    """

    gradient = np.array(gradient, dtype=float)

    magnitude = np.linalg.norm(gradient)

    if magnitude == 0:
        direction = np.zeros_like(gradient)
        descent_direction = np.zeros_like(gradient)
    else:
        direction = gradient / magnitude
        descent_direction = -direction

    return {
        'magnitude': magnitude,
        'direction': direction,
        'descent_direction': descent_direction
    }
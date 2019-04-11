import numpy as np

def free_wave_packet_potential(length):
    """Makes a potential for the free wave packet.

    Arguments
    ---------
        length: int
            number of simulated positions

    Returns
    -------
        free wave packet potential
    """
    return np.zeros((length), dtype=complex)

def infinite_sqare_well_potential(length, infinity=10e10, start=None, end=None):
    """Makes a potential for the infinite square well.

    Arguments
    ---------
        length: int
            number of simulated positions

        infinity: float
            the numerical value used to represent infinity (default: 10e10)

        start: int
            beginning of the well (default: length // 4)

        end: int
            end of the well (default: length - (length // 4))

    Returns
    -------
        infinite square well potential
    """
    if start is None:
        start = length // 4

    if end is None:
        end = length - length // 4

    index = np.arange(start, end)
    potential = np.full((length), infinity)
    potential[index] = 0
    return potential

def harmonic_oscillator_potential(length, dx, a=1.0, center=None):
    """Make the Harmonic Oscillator Potential.
    TODO
    """
    pass

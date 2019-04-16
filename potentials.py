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
    Arguments
    ---------
        length: int 
            number of simulated positions
        dx: float
            the distance between each point defined on the potential
            (not used, didn't know if we wanted an ulterior motive with this variable)
        a: float
            the max-value of the potential
        center: float
            The x-value of the center of the parabola and where it is the lowest potential value
        
    """
    """k is the spring constant, which is set to 1 for now"""
    k = 1.0
    potential = np.zeros(length)
    for i in range(0, length):
        x = i - center
        energy = 1/2 * k * x**2
        if x <= a and x >= -a:
            potential[i] = energy
        else:
            potential[i] = a
           
        
    return potential
    pass

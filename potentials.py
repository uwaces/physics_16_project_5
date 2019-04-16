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
    potential = np.full((length), infinity, dtype=complex)
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
            (not used, didn't know if we wanted an ulterior motive with
            this variable)

        a: float
            the max-value of the potential

        center: float
            The x-value of the center of the parabola and where it is the
            lowest potential value (defaults to length * dx / 2)

    Returns
    -------
        Returns the Harmonic Potential
    """
    if center is None: center = length * dx / 2
    k = 1.0 # k is the spring constant, which is set to 1 for now
    potential = np.zeros(length, dtype=complex)

    for i in range(0, length):
        x = i - center
        energy = 1/2 * k * x**2
        if energy <= a and energy >= -a:
            potential[i] = energy
        else:
            potential[i] = a

    return potential

def barrier_potential(length, height=10.0, start=None, end=None):
    """Makes a potential for the barrier with given height.

    Arguments
    ---------
        length: int
            number of simulated positions

        height: float
            the height of the barrier (default 10.0) #TODO see if there is a
            better default

        start: int
            beginning of the barrier (default: length // 4)

        end: int
            end of the barrier (default: length - (length // 4))

    Returns
    -------
        height of barrier
    """
    if start is None:
        start = length // 4

    if end is None:
        end = length - length // 4

    index = np.arange(start, end)
    potential = np.zeros((length))
    potential[index] = height
    return potential

def triangle_well_potential(length, dx, center_index=None, slope=1.0):
    """Make a triangle well.

    Arguments
    ---------
        length : int
            number of simulated positions

        dx : float
            distance between adjacent space samples

        center_index : int (0 <= center_index < length)
            bottom of the triangle well

        slope : float
            Left of center_index slope is `-slope`, to the right `slope`

    Returns
    -------
        Numpy array (length,) with triangle well
    """
    if center_index is None: center_index = length // 2
    left_height = dx * center_index * -1.0 * slope
    left_of_center = np.linspace(left_height, 0,
                                 num=center_index,
                                 endpoint=False,
                                 dtype=complex)
    elems_right = length - center_index
    right_of_center = np.linspace(0, dx * elems_right * slope,
                                  num=elems_right,
                                  dtype=complex)
    return np.append(left_of_center, right_of_center)

def question6a_potential(length, dx, L=10.0, infinity=10e10):
    """Implements the the first non-Hermitian V(x) in question 6.

    Arguments
    ---------
        length : int
            number of simulated positions

        dx : float
            distance between adjacent space samples

        L : float
            limits of complex well

        infinity : float
            what passes for infty here
    """
    space = np.linspace(-length*dx/2.0, length*dx/2.0, num=length, dtype=complex)
    mask = np.logical_and((space > -L), (space < L))
    space[mask] = 1j * space[mask]
    space[np.logical_not(mask)] = infinity
    return space

def question6b_potential(length, dx, L=10.0, infinity=10e10):
    """Implements the the second non-Hermitian V(x) in question 6.

    Arguments
    ---------
        length : int
            number of simulated positions

        dx : float
            distance between adjacent space samples

        L : float
            limits of complex well

        infinity : float
            what passes for infty here
    """
    space = np.linspace(-length*dx/2.0, length*dx/2.0, num=length, dtype=complex)
    mask = np.logical_and((space > -L), (space < L))
    space[mask] = 1j * space[mask] + space[mask]
    space[np.logical_not(mask)] = infinity
    return space
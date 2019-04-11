
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from   matplotlib.animation import FFMpegWriter 




n = 100
def banner (b):
    print('+'+'-'*79)
    print('| ' + b)
    print('+'+'-'*79)


def next_complex_array (i, i_per_period):
    i /= 30
    c = (2 * np.pi / i_per_period)
    rl = np.sin(np.linspace(i*c,i*c+2*np.pi,n))
    im = np.cos(np.linspace(-i*c,-i*c+2*np.pi,n))
    return np.vectorize(complex)(rl, im)

banner('generating complex array')
y = [next_complex_array(i,10) for i in range(0,200)]


def separate_complex_components (cmplx):
    """
    takes an array of complex numbers and returns the array split into 
    its real, imaginary, and square magnitude components.

    Arguments
    ---------

        psi: numpy.complex array (num_positions)

    Returns
    -------
    
        real: float array (num_positions)

        imaginary: float array (num_positions)

        square_magnitude: float array (num_positions)

    returns (real, imaginary, square_magnitude)

    """
    return (np.real(cmplx), np.imag(cmplx), np.absolute(cmplx))

def animate_psi(psi, potential, dt, dx, repeat=True, repeat_delay=1000,
                rewind=False, rewind_speed=5,
                real_vis = {'color': 'firebrick', 'alpha':'0.5'},
                imag_vis = {'color': 'gold',      'alpha':'0.5'},
                smag_vis = {'color': 'slategrey', 'alpha':'0.5'}):
    """ 

    Arguments
    ---------
        psi: array-like (num_frames, num_positions) 

        potential: array-like ()

        dt: float
            the time simulated between the arrays of complex numbers in 

        dx: float 
            physical distance between the complex numbers in the internal 
            arrays of complex number in psi

        repeat: bool
            true if the 
                
        repeat_delay: float
            the delay in milliseconds before repeating the animation 
                  should repeat be set to true.

    Returns
    -------

        None

    """


    if rewind: psi = np.concatenate((psi, psi[::-rewind_speed]))

    num_frames, num_positions = np.shape(psi)

    # setup plot
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    # set axes boundaries
    ax.set_ylim(-2,2)
    ax.set_xlim(0,(num_positions-1)*dx)




    ## TODO clean up    
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='red', alpha=0.5)

    # place a text box in upper left in axes coords
    time_display = ax.text(0.05, 0.95, 's', transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    ## TODO clean up    



    # setup some garbage

    x = np.linspace(0,(num_positions-1)*dx, num_positions)
    #x = np.linspace(0,1, n)
    

    potential_line, = ax.plot(x, potential, linewidth = 10)
    # CURRENTLY A DUMMY GENERATING IRRELEVANT COMPLEX ARRAY

    def next_arrays_to_visualize (i): 
        rl, im, mag = separate_complex_components(psi[i])
        return rl, im, np.square(mag)

    def init(): return animate(0)
    
    def animate(i):
        ax.collections.clear()
        real, imag, smag = next_arrays_to_visualize(i)
        real_area = ax.fill_between  (x, real, **real_vis)
        imag_area = ax.fill_between  (x, imag, **imag_vis)
        smag_area = ax.fill_between  (x, smag, **smag_vis)
        time_display.set_text('time: {}'.format(np.round(dt*i,3)))
        return (real_area, imag_area, smag_area, time_display)


    ani = animation.FuncAnimation(fig, animate, frames=num_frames, 
            init_func=init, interval=int(dt/1000), blit=True, 
            repeat_delay=repeat_delay, repeat=repeat, save_count=50)

    plt.show()

# To save the animation, use e.g.
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

animate_psi(y, np.sin(np.linspace(0,7,len(y[0]))), 1/300, 1);


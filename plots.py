import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors as mcolors


color_names = np.array(list(mcolors.CSS4_COLORS.keys()))
color_size = len(color_names)


# Plot complex numbers in Argand-Gauss plane.
#
def plot_complex(n):
    plt.stem(np.real(n), np.imag(n))
    plt.Circle((0,0), radius=1)
    plt.show()


# Simple wrapper for pyplot.
#
def plot(*args, **kwargs):
    plt.plot(*args, **kwargs)
    plt.show()


# Plot axis split vertical-wise.
#
def vertical_plots(curves, labels, title="Vertical Plots"):
    n = len(curves)
    fig, axs = plt.subplots(n)
    fig.suptitle(title)
    for i in range(len(axs)):
        axs[i].plot(*curves[i], label=labels[i])
        axs[i].grid(True)
    plt.show()


def plot_twin_axis(x1_axis, y1_axis, x2_axis, y2_axis, n, 
	x1_label, x2_label, y_label, fig_name, plot_title):
    fig, zax = plt.subplots()
    zax.plot(x1_axis, y1_axis, 'b.')
    zax.set_ylabel(y_label, color='b')

    # Make the x-axis label, ticks and tick labels match the line color.
    zax.set_xlabel(x1_label, color='b')
    zax.tick_params('x', colors='b')

    bax = zax.twiny()
    bax.plot(x2_axis, y2_axis, 'r.')
    bax.set_xlabel(x2_label, color='r')
    bax.tick_params('x', colors='r')

    plt.grid(True)
    plt.title(plot_title, y=1.16)
    fig.tight_layout()
    plt.savefig(fig_name)

def loglog_twins(x1_axis, y1_axis, x2_axis, y2_axis, n, 
    x1_label, x2_label, y_label, fig_name, plot_title):
    fig, zax = plt.subplots()
    zax.loglog(x1_axis, y1_axis, 'b.')
    zax.set_ylabel(y_label, color='b')

    # Make the x-axis label, ticks and tick labels match the line color.
    zax.set_xlabel(x1_label, color='b')
    zax.tick_params('x', colors='b')

    bax = zax.twiny()
    bax.loglog(x2_axis, y2_axis, 'r.')
    bax.set_xlabel(x2_label, color='r')
    bax.tick_params('x', colors='r')

    plt.title(plot_title, y=1.16)
    plt.grid(True)
    fig.tight_layout()
    plt.savefig(fig_name)



# Plot mutliple curves sharing the same axis with different colors. If a tuple
#  of curves is an element of color_axis, all the curves inside that tuple will
#  have the same color.
def plot_color_curves(x_axis, color_axis, labels=None, fig_name="figure.png",
                      plot_title=None, x_label=None, y_label=None,
                      savefig = True):
    
    color_curves_artist(
        x_axis, color_axis, labels, plot_title, x_label, y_label)

    plt.grid(True) # coller
    if savefig:
        plt.savefig(fig_name)
        plt.clf()
    else:
        plt.show()



def color_curves_artist(x_axis, color_axis, labels=None, 
                        plot_title=None, x_label=None, y_label=None):

    num_curves = len(color_axis)
    colors = ['C' + str(c) for c in range(num_curves)]
    # colors = color_names[:num_curves]
    plots = list()

    for c in range(num_curves):
        curves = color_axis[c]
        kwargs = {'color': colors[c]}

        if isinstance(curves, (np.ndarray, tuple)):
            for curve in curves[1:]:
                print(curve)
                plot, = plt.plot(x_axis, curve, **kwargs)
                plots.append(plot)
            curves = curves[0]

        if labels is not None:
            kwargs['label'] = labels[c]

        plot, = plt.plot(x_axis, curves, **kwargs)
        plots.append(plot)

    if plot_title is not None:
        plt.title(plot_title)
    if x_label is not None:
        plt.xlabel(x_label)
    if y_label is not None:
        plt.ylabel(y_label)
    if labels is not None:
        plt.legend(handles=plots)



def generic_curves(color_axis, labels=None, fig_name="figure.png",
                      plot_title=None, x_label=None, y_label=None,
                      plot_function=plt.plot, savefig=True):
    fig = plt.figure()
    num_curves = len(color_axis)
    colors = ['C' + str(c) for c in range(num_curves)]
    plots = list()

    for c in range(num_curves):
        curves = color_axis[c]
        c_color = colors[c]
        c_label = labels[c]
        plots.append(plot_function(
                     curves[0], curves[1], color=c_color, label=c_label))

    if plot_title != None:
        plt.title(plot_title, y=1.16)
    if x_label != None:
        plt.xlabel(x_label)
    if y_label != None:
        plt.ylabel(y_label)
    plt.title(plot_title)#, y=1.16)
    plt.legend()
    plt.grid(True) # coller

    if savefig:
        plt.savefig(fig_name)
        plt.clf()
    else:
        plt.show()

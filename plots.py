import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors as mcolors

__all__ = ["plot_twin_axis", "loglog_twins"]

color_names = np.array(list(mcolors.CSS4_COLORS.keys()))
color_size = len(color_names)

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
                      plot_title=None, x_label=None, y_label=None, savefig = True):
    num_curves = len(color_axis)
    colors = ['C' + str(c) for c in range(num_curves)]
    plots = list()

    for c in range(num_curves):
        curves = color_axis[c]
        c_color = colors[c]
        c_label = labels[c]
        if isinstance(curves, tuple):
            for curve in curves[1:]:
                plot, = plt.plot(x_axis, curve, color=c_color)
                plots.append(plot)
            curves = curves[0]

        plot, = plt.plot(x_axis, curves, color=c_color, label=c_label)
        plots.append(plot)

    if plot_title is not None:
        plt.title(plot_title)
    if x_label is not None:
        plt.xlabel(x_label)
    if y_label is not None:
        plt.ylabel(y_label)
    plt.legend(handles=plots)
    plt.grid(True) # coller

    if savefig:
        plt.savefig(fig_name)
        plt.clf()
    else:
        plt.show()




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
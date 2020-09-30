from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import json
import numpy as np

# %matplotlib inline
# plt.rcParams['axes.unicode_minus'] = False

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    # print([z_middle - plot_radius, z_middle + plot_radius], "ttttt")
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def plot_package(ax, x, y, z, dx, dy, dz, name="", color='red', transparent=0.125, surface_color=True, border_tickness=1):
    # draw border line
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color, 'linewidth':border_tickness}
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)

    if surface_color:
        # draw box surface
        xx = np.linspace(x, x+dx, 2)
        yy = np.linspace(y, y+dy, 2)
        zz = np.linspace(z, z+dz, 2)
        
        xx, yy = np.meshgrid(xx, yy)
        ax.plot_surface(xx, yy, np.atleast_2d(z), color=color, shade=False, alpha=transparent)
        ax.plot_surface(xx, yy, np.atleast_2d(z+dz), color=color, shade=False, alpha=transparent)

        yy, zz = np.meshgrid(yy, zz)
        ax.plot_surface(x, yy, zz, color=color, shade=False, alpha=transparent)
        ax.plot_surface(x+dx, yy, zz, color=color, shade=False, alpha=transparent)

        xx, zz = np.meshgrid(xx, zz)
        ax.plot_surface(xx, y, zz, color=color, shade=False, alpha=transparent)
        ax.plot_surface(xx, y+dy, zz, color=color, shade=False, alpha=transparent)

    # put test in box
    if name != "":
        ax.text(x+dx/2, y+dy/2, z+dz/2, name, color="black", fontsize=8)


def plot_multiple_package(data, title, num, scale=True):
    # read json data
    # data = json.loads(data)
    
    fig = plt.figure(num, figsize=(14,8))

    # draw container
    ax = Axes3D(fig)
    ax.set_xlim3d(0, data['width'])
    ax.set_ylim3d(0, data['height'])
    ax.set_zlim3d(0, data['length'])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    if scale:
        set_axes_equal(ax)

    # color item by name
    unique_name = set([item['name'] for item in data['placement']])
    name_color = {}
    for name in unique_name:
        name_color[name] = np.random.rand(3,)

    # plot package
    for item in data['placement']:
        color = name_color[item['name']]
        plot_package(
            ax, item['x'], item['y'], item['z'], 
            item['width'], item['height'], item['length'], item['name'], 
            color=color
        )
    
    # plot container
    plot_package(
        ax, 0, 0, 0, 
        data['width'], data['height'], data['length'],
        color=[0, 0, 0],
        surface_color=False,
        border_tickness=2
    )

    ax.legend()
    plt.title(title)
    return plt


def plot_multiple_package_from_file(data_path, title, num, scale):
    data = {}
    with open(data_path) as json_file:
        data = json.load(json_file)
        return plot_multiple_package(data, title, num, scale)


if __name__ == "__main__":
    # plt1 = plot_multiple_package_from_file('./simple.json', 'Packages', 1)
    # plt2 = plot_multiple_package_from_file('./multiple.json', 'Packages', 2)
    # plt1.show()
    # plt2.show()

    plt1 = plot_multiple_package_from_file('./test.json', 'Packages', 1, scale=True)
    plt2 = plot_multiple_package_from_file('./test.json', 'Packages', 2, scale=False)
    plt3 = plot_multiple_package_from_file('./test2.json', 'Packages', 3, scale=True)
    plt4 = plot_multiple_package_from_file('./test2.json', 'Packages', 4, scale=False)
    
    plt1.show()
    plt2.show()
    plt3.show()
    plt4.show()
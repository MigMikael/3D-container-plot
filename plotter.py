from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import json
import numpy as np

# %matplotlib inline
# plt.rcParams['axes.unicode_minus'] = False


def plot_package(ax, x, y, z, dx, dy, dz, name='', color='red', transparent=0.2):
    # draw border line
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)

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
    ax.text(x+dx/2, y+dy/2, z+dz/2, name, color="black", fontsize=8)


def plot_multiple_package(data_path):
    # read json data
    data = {}
    with open(data_path) as json_file:
        data = json.load(json_file)
    fig = plt.figure(figsize=(10,7))

    # draw container
    ax = Axes3D(fig)
    ax.set_xlim3d(0, data['width'])
    ax.set_ylim3d(0, data['length'])
    ax.set_zlim3d(0, data['height'])
    
    # plot package
    for item in data['placement']:
        color = np.random.rand(3,)
        plot_package(
            ax, item['x'], item['y'], item['z'], 
            item['width'], item['length'], item['height'], item['name'], 
            color=color
        )
        
    plt.title('Packages')
    plt.show()


if __name__ == "__main__":
    plot_multiple_package('./simple.json')
    plot_multiple_package('./multiple.json')
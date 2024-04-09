import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

def create_affine_functions(coeff_dict, method=1):
    functions = []
    probabilities = []

    for name, coeffs in coeff_dict.items():  
        if method == 1:
            a, b, c, d, e, f, p = coeffs
            affine_function = lambda x, y, a=a, b=b, c=c, d=d, e=e, f=f: (a * x + b * y + e, 
                                                                          c * x + d * y + f) 
        else:  # for the 2nd version of the fractal tree 
            r, s, theta, phi, e, f, p = coeffs
            affine_function = lambda x, y, r=r, s=s, theta=theta, phi=phi, e=e,f=f: (r*np.cos(theta)*x - s*np.sin(phi)*y + e, 
                                                                                    r*np.sin(theta)*x + s*np.cos(phi)* y + f)
        functions.append(affine_function)
        probabilities.append(p)

    return functions, probabilities

def generate_fractal(coeff_dict, filename, points=10000, method=1, frames=100):
    functions, probabilities = create_affine_functions(coeff_dict, method=method)
    
    fig, ax = plt.subplots()
    scatter = ax.scatter([], [], s=0.2)
    
    x_list = []
    y_list = []

    def update(frame):
        nonlocal x_list, y_list
        x, y = 0, 0

        for _ in range(points):
            function = np.random.choice(functions, p=probabilities)
            x, y = function(x, y)
            x_list.append(x)
            y_list.append(y)

        scatter.set_offsets(np.vstack((x_list, y_list)).T)
        ax.set_xlim(min(x_list) - 0.5, max(x_list) + 0.5)
        ax.set_ylim(min(y_list) - 0.5, max(y_list) + 0.5)

    ani = FuncAnimation(fig, update, frames=frames, blit=False)

    if not os.path.exists('gifs'):
        os.makedirs('gifs')
    
    gif_path = os.path.join('gifs', filename)
    ani.save(gif_path, writer='pillow', fps=10)
    plt.show() #don't need ?

coeff_dict1 = {
    'set1': (0.1400, 0.0100, 0.0000, 0.5100, -0.0800, -1.3100, 0.25),
    'set2': (0.4300, 0.5200, -0.4500, 0.5000, 1.4900, -0.7500, 0.25),
    'set3': (0.4500, -0.4900, 0.4700, 0.4700, -1.6200, -0.7400, 0.25),
    'set4': (0.4900, 0.0000, 0.0000, 0.5100, 0.0200, 1.6200, 0.25)
}
coeff_dict2 = {
    'set1': (0.787879, -0.424242, 0.242424, 0.859848, 1.758647, 1.408065, 0.90),
    'set2': (-0.121212, 0.257576, 0.151515, 0.053030, -6.721654, 1.377236, 0.05),
    'set3': (0.181818, -0.136364, 0.090909, 0.181818, 6.086107, 1.568035, 0.05)
}
coeff_dict3 = {
    'set1': (0.2020, 0.8050, -0.6890, -0.3420, -0.3730, -0.6530, 0.5),
    'set2': (0.1380, 0.6650, -0.5020, -0.2220, 0.6600, -0.2770, 0.5) 
}
coeff_dict4 = {
    'set1': (0.0500, 0.0000, 0.0000, 0.4000, -0.0600, -0.4700, 1/7),
    'set2': (-0.0500, 0.0000, 0.0000, -0.4000, -0.0600, -0.4700, 1/7),
    'set3': (0.0300, -0.1400, 0.0000, 0.2600, -0.1600, -0.0100, 1/7),
    'set4': (-0.0300, 0.1400, 0.0000, -0.2600, -0.1600, -0.0100, 1/7),
    'set5': (0.5600, 0.4400, -0.3700, 0.5100, 0.3000, 0.1500, 1/7),
    'set6': (0.1900, 0.0700, -0.1000, 0.1500, -0.2000, 0.2800, 1/7),
    'set7': (-0.3300, -0.3400, -0.3300, 0.3400, -0.5400, 0.3900, 1/7)
}
coeff_dict5 = {               #theta  #phi
    'set1': (0.0500, 0.6000, 0.0000, 0.0000, 0.0000, 0.0000, 1/6),
    'set2': (0.0500, -0.5000, 0.0000, 0.0000, 0.0000, 1.0000, 1/6),
    'set3': (0.6000, 0.5000, 0.6980, 0.6980, 0.0000, 0.6000, 1/6),
    'set4': (0.5000, 0.4500, 0.3490, 0.3492, 0.0000, 1.1000, 1/6),
    'set5': (0.5000, 0.5500, -0.5240, -0.5240, 0.0000, 1.0000, 1/6),
    'set6': (0.5500, 0.4000, -0.6980, -0.6980, 0.0000, 0.7000, 1/6)
}
coeff_dict6 = {
    'set1': (0.0100, 0.0000, 0.0000, 0.4500, 0.0000, 0.0000, 0.25),
    'set2': (-0.0100, 0.0000, 0.0000, -0.4500, 0.0000, 0.4000, 0.25),
    'set3': (0.4200, -0.4200, 0.4200, 0.4200, 0.0000, 0.4000, 0.25),
    'set4': (0.4200, 0.4200, -0.4200, 0.4200, 0.0000, 0.4000, 0.25)
}
coeff_dict7 = {
    'set1': (0.1950, -0.4880, 0.3440, 0.4430, 0.4431, 0.2452, 0.2),
    'set2': (0.4620, 0.4140, -0.2520, 0.3610, 0.2511, 0.5692, 0.2),
    'set3': (-0.6370, 0.0000, 0.0000, 0.5010, 0.8562, 0.2512, 0.2),
    'set4': (-0.0350, 0.0700, -0.4690, 0.0220, 0.4884, 0.5069, 0.2),
    'set5': (-0.0580, -0.0700, 0.4530, -0.1110, 0.5976, 0.0969, 0.2)
}
coeff_dict8 = {
    'set1': (0.0000, 0.2439, 0.0000, 0.3053, 0.0000, 0.0000, 0.25),
    'set2': (0.7248, 0.0337, -0.0253, 0.7426, 0.2060, 0.2538, 0.25),
    'set3': (0.1583, -0.1297, 0.3550, 0.3676, 0.1383, 0.1750, 0.25),
    'set4': (0.3386, 0.3694, 0.2227, -0.0756, 0.0679, 0.0826, 0.25)
}
coeff_dict9 = {
    'set1': (0.38200, 0.00000, 0.00000, 0.38200, 0.30900, 0.57000, 1/6),
    'set2': (0.11800, -0.36330, 0.36330, 0.11800, 0.36330, 0.33060, 1/6),
    'set3': (0.11800, 0.36330, -0.36330, 0.11800, 0.51870, 0.69400, 1/6),
    'set4': (-0.30900, -0.22450, 0.22450, -0.30900, 0.60700, 0.30900, 1/6),
    'set5': (-0.30900, 0.22450, -0.22450, -0.30900, 0.70160, 0.53350, 1/6),
    'set6': (0.38200, 0.00000, 0.00000, -0.38200, 0.30900, 0.67700, 1/6)
}
coeff_dict10 = {
    'set1': (0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.25),
    'set2': (0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.25),
    'set3': (-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.25),
    'set4': (0.75, 0.04, -0.04, 0.85, 0.0, 1.6, 0.25)
}
coeff_dict11 = {
    'set1': (0.824074, 0.281428, -0.212346, 0.864198, -1.882290, -0.110607, 0.8),
    'set2': (0.088272, 0.520988, -0.463889, -0.377778, 0.785360, 8.095795, 0.2)
}
coeff_dict12 = {
    'set1': (0, 0.053, -0.429, 0, -7.083, 5.43, 1/19),
    'set2': (0.143, 0, 0, -0.053, -5.619, 8.513, 1/19),
    'set3': (0.143, 0, 0, 0.083, -5.619, 2.057, 1/19),
    'set4': (0, 0.053, 0.429, 0, -3.952, 5.43, 1/19),
    'set5': (0.119, 0, 0, 0.053, -2.555, 4.536, 1/19),
    'set6': (-0.0123806, -0.0649723, 0.423819, 0.00189797, -1.226, 5.235, 1/19),
    'set7': (0.0852291, 0.0506328, 0.420449, 0.0156626, -0.421, 4.569, 1/19),
    'set8': (0.104432, 0.00529117, 0.0570516, 0.0527352, 0.976, 8.113, 1/19),
    'set9': (-0.00814186, -0.0417935, 0.423922, 0.00415972, 1.934, 5.37, 1/19),
    'set10': (0.093, 0, 0, 0.053, 0.861, 4.536, 1/19),
    'set11': (0, 0.053, -0.429, 0, 2.447, 5.43, 1/19),
    'set12': (0.119, 0, 0, -0.053, 3.363, 8.513, 1/19),
    'set13': (0.119, 0, 0, 0.053, 3.363, 1.487, 1/19),
    'set14': (0, 0.053, 0.429, 0, 3.972, 4.569, 1/19),
    'set15': (0.123998, -0.00183957, 0.000691208, 0.0629731, 6.275, 7.716, 1/19),
    'set16': (0, 0.053, 0.167, 0, 5.215, 6.483, 1/19),
    'set17': (0.071, 0, 0, 0.053, 6.279, 5.298, 1/19),
    'set18': (-0.121, 0, 0, 0.053, 5.941, 1.487, 1/19),
    'set19': (0, 0, 0, 0.053, 5.298, 1.487, 1/19)
}
coeff_dict13 = {
    'set1': (0.387, 0.430, 0.430, -0.387, 0.2560, 0.5220, 1/3),
    'set2': (0.441, -0.091, -0.009, -0.322, 0.4219, 0.5059, 1/3),
    'set3': (-0.468, 0.020, -0.113, 0.015, 0.4, 0.4, 1/3)
}
coeff_dict14 = {
    'set1': (0.0, -0.5, 0.5, 0.0, 0.5, 0.0, 1/3),
    'set2': (0.0, 0.5, -0.5, 0.0, 0.5, 0.5, 1/3),
    'set3': (0.5, 0.0, 0.0, 0.5, 0.25, 0.5, 1/3)
}

generate_fractal(coeff_dict1, filename='Maple_leaf.gif', points=1000, frames=100)
generate_fractal(coeff_dict2, filename='Spiral.gif', points=1000, frames=100)
generate_fractal(coeff_dict3, filename='Mandelbrot-like.gif', points=1000, frames=100)
generate_fractal(coeff_dict4, filename='Fractal_tree.gif', points=1000, frames=100)
generate_fractal(coeff_dict5, filename='Fractal_tree2.gif', points=1000, frames=100, method=2)
generate_fractal(coeff_dict6, filename='Fractal_tree3.gif', points=1000, frames=100)
generate_fractal(coeff_dict7, filename='Fractal_tree4.gif', points=1000, frames=100)
generate_fractal(coeff_dict8, filename='Leaf.gif', points=1000, frames=100)
generate_fractal(coeff_dict9, filename='Sand_dollar-snowflake.gif', points=1000, frames=100)
generate_fractal(coeff_dict10, filename='Fern.gif', points=1000, frames=100)
generate_fractal(coeff_dict12, filename='IFS_Chaos_Text.gif', points=1000, frames=100)
generate_fractal(coeff_dict11, filename='IFS_Dragon.gif', points=1000, frames=100)
generate_fractal(coeff_dict13, filename='IFS_Branch.gif', points=1000, frames=100) #
generate_fractal(coeff_dict14, filename='IFS_fir_tree.gif', points=1000, frames=100)#


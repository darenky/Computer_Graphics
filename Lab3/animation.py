import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def test_tur(axiom, rules, max_iter, fi):
    for _ in range(max_iter):
        new_axiom = []
        for j in axiom:
            new_axiom.append(rules.get(j, j))
        axiom = ''.join(new_axiom)
    return axiom

def plot_axiom(ax, axiom, fi, dfi, l): 
    n = len(axiom)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    for i in range(n):
        x[i+1] = x[i]
        y[i+1] = y[i]
        if axiom[i] == 'F':
            x[i+1] = x[i+1] + l*np.cos(fi)
            y[i+1] = y[i+1] + l*np.sin(fi)
        elif axiom[i] == '+':
            fi += dfi
        elif axiom[i] == '-':
            fi -= dfi
    ax.plot(x, y, 'b')  

def animate_fractal(axiom, rules, min_angle, max_angle, num_frames, max_iter, filename):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()  
        current_angle = min_angle + (max_angle - min_angle) * frame / num_frames
        result = test_tur(axiom, rules, max_iter, current_angle)  
        plot_axiom(ax, result, 0, current_angle, 1)
        ax.set_title(f"Angle: {current_angle:.2f}") 

    writer = PillowWriter(fps=10)   # fps = frames per second
    anim = FuncAnimation(fig, update, frames=num_frames, repeat=False)
    anim.save(filename, writer=writer)  
    plt.close(fig)  


num_frames = 30 
max_iter = 5
fi = 0

fractals = [
     ("Koch Snowflake", "F++F++F", {"F": "F-F++F-F"}, np.pi/3),
    ("Sierpinski Cross", "F+XF+F+XF", {"X": "XF-F+F-XF+F+XF-F+F-X"}, np.pi/2),
    ("Crystal Snowflake", "F+F+F+F", {"F": "FF+F++F+F"}, np.pi/2),
    ("Fractal Star", "X+X+X+X+X+X+X+X", {"X": "X+YF++YF-FX--FXFX-YF+X", "Y": "-FX+YFYF++YF+FX--FX-YF"}, np.pi/4),
    ("Serpinski Arrowhead", "YF", {"X": "YF+XF+Y", "Y": "XF-YF-X"}, np.pi/3),
    ("Fractal Basin", "-D--D", {"A": "F++FFFF--F--FFFF++F++FFFF--F", "B": "F--FFFF++F++FFFF--F--FFFF++F", "C": "BFA--BFA", "D": "CFC--CFC"}, np.pi/4),
    ("Fractal Rings", "F+F+F+F", {"F": "FF+F+F+F+F+F-F"}, np.pi/2),
    ("Dragon Curve", "FX", {"X": "X+YF+", "Y": "-FX-Y"}, np.pi/2)
 ]


for name, axiom, rules, dfi in fractals:
    filename = f"{name.replace(' ', '_')}.gif"
    animate_fractal(axiom, rules, 0, dfi, num_frames, max_iter, filename)
    print(f"Animation saved as {filename}")
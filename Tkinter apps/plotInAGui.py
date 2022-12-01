# Explore how to plot in a gui with matplotlib and tkinter.
# to do: Expand the canvas with the widget area.
import tkinter 
from tkinter import ttk
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

# Peak voltage
VmaxPk = 2

# Actual sinusoidal frequency.
Fi = 2010

# Nominal sinusoidal frequency.
Fn = 2000

# Sample frequency.
Fs = 50e3

# Duration of the sinusoid
Tstop = 50e-3

# Time input vector
N = int(Tstop/(1/Fs))
t = np.linspace(0, Tstop, N)

inputVmax = VmaxPk*np.sin(2*np.pi*Fi*t)
input2 = VmaxPk/2*np.sin(2*np.pi*2*Fi*t)
input4 = VmaxPk/3*np.sin(2*np.pi*4*Fi*t)
input6 = VmaxPk/6*np.sin(2*np.pi*6*Fi*t)

ran = np.ones(len(t))
for i in range(len(t)):
    ran[i] = random.random()*VmaxPk/8
inputVmax = input2 + input4 + input6 + ran + inputVmax

# GUI
root = tkinter.Tk()
root.title("Plot")
root.geometry("700x1000")

# add a frame to the root. The frame holds every widget.
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = ttk.Frame(mainframe)
frame1.grid(column=0, row=0, sticky="nsew")

# Create a figure that has axis. Axis holds the plots.
fig1 = matplotlib.figure.Figure(dpi=100)
ax1 = fig1.add_subplot()
ax1.plot(t, inputVmax)

# From the figure object create a canvas that is draws the plot in the
# widget.
canvas1 = FigureCanvasTkAgg(figure=fig1, master=frame1)
canvas1.draw()

# Second plot.
frame2 = ttk.Frame(mainframe)
frame2.grid(column=0, row=1, sticky="nsew")

fig2 = matplotlib.figure.Figure(dpi=100)
ax2 = fig2.add_subplot()
ax2.plot(t, -inputVmax)

canvas2 = FigureCanvasTkAgg(figure=fig2, master=frame2)
canvas2.draw()

mainframe.pack()

canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
root.mainloop()

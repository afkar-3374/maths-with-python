import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ---------- DATA ----------
x_deg = np.linspace(0, 360, 1000)
x_rad = np.radians(x_deg)

y_sin = np.sin(x_rad)
y_cos = np.cos(x_rad)

# ---------- FIGURE ----------
fig, ax = plt.subplots(figsize=(8, 5))
plt.subplots_adjust(bottom=0.25)

# Curves
ax.plot(x_deg, y_sin, label="sin x")
ax.plot(x_deg, y_cos, label="cos x")

# Axis settings
ax.set_xlim(0, 360)
ax.set_ylim(-1.1, 1.1)
ax.set_xticks(np.arange(0, 361, 30))
ax.set_yticks(np.arange(-1, 1.1, 0.2))
ax.grid(True)

# Initial dots
sin_dot, = ax.plot([0], [0], 'go', markersize=10)
cos_dot, = ax.plot([0], [1], 'ro', markersize=10)

# Labels
ax.set_xlabel("Angle (degrees)")
ax.set_ylabel("Value")
ax.legend()

# ---------- SLIDER ----------
slider_ax = plt.axes([0.15, 0.1, 0.7, 0.05])
angle_slider = Slider(slider_ax, "Angle (°)", 0, 360, valinit=0)

# ---------- UPDATE FUNCTION ----------
def update(angle):
    rad = np.radians(angle)

    sin_dot.set_data([angle], [np.sin(rad)])
    cos_dot.set_data([angle], [np.cos(rad)])

    fig.canvas.draw_idle()

angle_slider.on_changed(update)

# ---------- SHOW ----------
plt.show()

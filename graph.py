import matplotlib.pyplot as plt
import numpy as np


def show_temp_range(rows):

    name = [r[0] for r in rows]
    temp_min = [r[1] for r in rows]
    temp_max = [r[2] for r in rows]

    width = [max_t - min_t for min_t, max_t in zip(temp_min, temp_max)]
    gradient = np.linspace(0, 1, 500)
    gradient = np.vstack((gradient, gradient))

    fig, ax = plt.subplots()
    ax.imshow(
        gradient,
        extent=[-20, 50, -1, len(name)],
        aspect="auto",
        cmap="coolwarm",
        alpha=0.3,
    )
    ax.barh(y=name, left=temp_min, width=width, color="skyblue")

    plt.xlabel("Temperature (°C)")
    plt.show()

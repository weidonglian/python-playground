import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

def fibonacci(length: int) -> list[int]:
    """Generate Fibonacci sequence.

    :param length: The length of the Fibonacci sequence.
    :return: The Fibonacci sequence of length.
    """
    if length <= 0:
        return []

    if length == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

def draw_fibonacci_squares(ax, sequence):
    """Draw Fibonacci squares with different colors."""
    x, y = 0, 0
    dx, dy = 1, 0  # Initial direction (right)
    colors = plt.cm.viridis(np.linspace(0, 1, len(sequence)))

    for i in range(len(sequence)):
        size = sequence[i]
        rect = patches.Rectangle((x, y), size * dx, size * dy, linewidth=2, edgecolor='black', facecolor=colors[i])
        ax.add_patch(rect)

        # Move to the next position
        if dx == 1:  # Right
            x += size
            dy = 1
            dx = 0
        elif dy == 1:  # Up
            y += size
            dx = -1
            dy = 0
        elif dx == -1:  # Left
            x -= sequence[i-1] if i > 0 else 0
            dy = -1
            dx = 0
        elif dy == -1:  # Down
            y -= sequence[i-1] if i > 0 else 0
            dx = 1
            dy = 0

def update(frame, ax, sequence):
    """Update function for animation."""
    ax.clear()
    ax.set_xlim(-sequence[-1], sequence[-1]*1.5)
    ax.set_ylim(-sequence[-1], sequence[-1]*1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    draw_fibonacci_squares(ax, sequence[:frame+1])

    angles = np.linspace(0, frame * np.pi / 2, num=frame * 10)
    radius = np.array([sequence[int(angle / (np.pi / 2))] if int(angle / (np.pi / 2)) < len(sequence) else sequence[-1] for angle in angles])
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    ax.plot(x, y, color='blue', linewidth=2)

def animate_fibonacci(length: int):
    """Animate Fibonacci squares and spiral."""
    sequence = fibonacci(length)
    fig, ax = plt.subplots(figsize=(8, 8))
    ani = animation.FuncAnimation(fig, update, frames=len(sequence), fargs=(ax, sequence), interval=500, repeat=False)
    plt.show()

def main():
    while True:
        try:
            length = int(input("Enter the length of the Fibonacci sequence: "))
            if length < 1:
                print("Please enter a positive integer greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    animate_fibonacci(length)

if __name__ == "__main__":
    main()

import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Initialize the 5x5 grid
def initialize_grid():
    grid = [['.' for _ in range(5)] for _ in range(5)]
    # Place the treasure at a random position
    treasure_row = random.randint(0, 4)
    treasure_col = random.randint(0, 4)
    grid[treasure_row][treasure_col] = 'X'
    return grid, [treasure_row, treasure_col]


# Move the position based on the direction
def move(position, direction):
    row, col = position
    if direction == 'right':
        col += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'up':
        row -= 1

    # Ensure the new position is within the grid boundaries
    if 0 <= row < 5 and 0 <= col < 5:
        return [row, col]
    else:
        return position  # Invalid move, stay in the same position


# Calculate the distance to the treasure
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


# Plot the grid and path
def plot_grid_path(grid, path, treasure_position):
    fig, ax = plt.subplots()

    # Plot the grid
    for row in range(5):
        for col in range(5):
            rect = patches.Rectangle((col, 4 - row), 1, 1, linewidth=1, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            if grid[row][col] == 'X':
                ax.text(col + 0.5, 4 - row + 0.5, 'X', ha='center', va='center', fontsize=12, color='red')

    # Plot the path
    path_x, path_y = zip(*path)
    ax.plot(path_x, path_y, marker='o', color='blue', linestyle='-', markersize=8, label='Path')

    # Plot the starting point and treasure
    ax.plot(path[0][1], path[0][0], marker='o', color='green', markersize=12, label='Start')
    ax.plot(treasure_position[1], treasure_position[0], marker='o', color='red', markersize=12, label='Treasure')

    # Set the plot limits and labels
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels(range(5))
    ax.set_yticklabels(range(5)[::-1])
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.set_title('Treasure Hunt Path')
    ax.legend()
    ax.grid(True)

    plt.gca().invert_yaxis()  # To match the grid orientation
    plt.show()


def main():
    grid, treasure_position = initialize_grid()
    current_position = [0, 0]
    path = [current_position.copy()]

    print("Starting grid:")
    for row in grid:
        print(' '.join(row))
    print()

    print("You are at position [0, 0]. Find the treasure!")

    while current_position != treasure_position:
        # Get user input
        command = input("Enter command (right, left, up, down): ").strip().lower()

        if command in ['right', 'left', 'up', 'down']:
            new_position = move(current_position, command)
            if new_position == current_position:
                print("Invalid move! Try a different direction.")
                continue

            current_position = new_position
            path.append(current_position.copy())
            distance = calculate_distance(current_position, treasure_position)
            print(f"Current position: {current_position}")
            print(f"Distance to treasure: {distance}")

            if current_position == treasure_position:
                print("Treasure found!")
                break
        else:
            print("Invalid command. Please enter 'right', 'left', 'up', or 'down'.")

    # Plot the path taken and treasure location
    plot_grid_path(grid, path, treasure_position)


if __name__ == "__main__":
    main()

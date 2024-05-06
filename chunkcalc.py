def calculate_chunk_coordinates(x, y, z):
    chunk_size = 16
    min_x = (x // chunk_size) * chunk_size
    min_y = (y // chunk_size) * chunk_size
    min_z = (z // chunk_size) * chunk_size
    max_x = min_x + chunk_size
    max_y = min_y + chunk_size
    max_z = min_z + chunk_size
    return min_x, min_y, min_z, max_x, max_y, max_z

while True:
    x_input = input("Enter the x coordinate (or type 'exit' to quit): ")
    if x_input.lower() == "exit":
        break

    y_input = input("Enter the y coordinate (or type 'exit' to quit): ")
    if y_input.lower() == "exit":
        break

    z_input = input("Enter the z coordinate (or type 'exit' to quit): ")
    if z_input.lower() == "exit":
        break

    try:
        x = int(x_input)
        y = int(y_input)
        z = int(z_input)

        min_x, min_y, min_z, max_x, max_y, max_z = calculate_chunk_coordinates(x, y, z)
        print(f"Chunk coordinates: ({min_x}, {min_y}, {min_z}) / ({max_x}, {max_y}, {max_z})")
        print()  # Add an empty line for readability
    except ValueError:
        print("Invalid input. Please enter valid integer coordinates.")
        print()  # Add an empty line for readability
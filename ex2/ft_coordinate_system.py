import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        coordinates = []
        len_coor = 0
        user_in = input("Enter new coordinates as floats in format 'x,y,z': ")
        if user_in.count(",") != 2:
            print("Invalid syntax")
            continue
        for coord in user_in.split(","):
            try:
                coordinates.append(float(coord))
            except Exception as e:
                print(f"Error on parameter '{coord}': {e}")
            else:
                len_coor += 1
        if len_coor == 3:
            return (tuple(coordinates))


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    coordinates1 = get_player_pos()
    print(f"Got a first tuple: {coordinates1}")
    X1 = coordinates1[0]
    Y1 = coordinates1[1]
    Z1 = coordinates1[2]
    print(f"It includes: X={X1}, Y={Y1}, Z={Z1}")
    d_to_center = math.sqrt(X1**2 + Y1**2 + Z1**2)
    print(f"Distance to center: {round(d_to_center,4)}")
    print("\nGet a second set of coordinates")
    coordinates2 = get_player_pos()
    X2 = coordinates2[0]
    Y2 = coordinates2[1]
    Z2 = coordinates2[2]
    d_between_coords = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2 + (Z2 - Z1)**2)
    print("Distance between the 2 sets of coordinates:", end=' ')
    print(f"{round(d_between_coords,4)}")

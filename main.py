PAINT_CAN_COST = 25
PAINT_SQ_FEET = 350

DOOR_SQ_FEET = 14.5
WINDOW_SQ_FEET = 9


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Sorry, your response must be a positive number.")
        except ValueError:
            print("Sorry, I didn't understand that. Please enter a number.")


def roomDimensions():
    room_length_input = get_positive_float("Please enter the room length: ")
    room_width_input = get_positive_float("Please enter the room width: ")
    room_height_input = get_positive_float("Please enter the room height: ")
    room_dimensions = room_length_input * room_width_input * room_height_input
    print(f"The dimensions of your room are: {room_dimensions} sq feet.")

    paint_cieling_input = ""
    while paint_cieling_input.lower() not in ["yes", "no"]:
        paint_cieling_input = input("Do you want to paint the ceiling (yes/no): ").lower()
        if paint_cieling_input.lower() not in ["yes", "no"]:
            print("Sorry, please enter 'yes' or 'no'.")

    if paint_cieling_input.lower() == "yes":
        ceiling_length_input = get_positive_float("What is the ceiling length: ")
        ceiling_width_input = get_positive_float("What is the ceiling width: ")
        ceiling_dimensions = ceiling_width_input * ceiling_length_input
        print(f"The dimensions of your ceiling are: {ceiling_dimensions}")
    else:
        ceiling_dimensions = 0  # If not painting the ceiling, its dimensions are 0

    return room_dimensions, ceiling_dimensions


def roomCost(room_dimensions, ceiling_dimensions):
    total_dimensions = room_dimensions + ceiling_dimensions
    total_cost = total_dimensions / PAINT_SQ_FEET * PAINT_CAN_COST
    print(f"Total cost to paint is ${total_cost}")


def main():
    room_dimensions, ceiling_dimensions = roomDimensions()
    roomCost(room_dimensions, ceiling_dimensions)


if __name__ == "__main__":
    main()

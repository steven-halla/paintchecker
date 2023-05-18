import math

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
    DOOR_SQ_FEET = 14.5
    WINDOW_SQ_FEET = 9

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




import math

def roomCost(room_dimensions, ceiling_dimensions):
    PAINT_CAN_COST = 25
    PAINT_SQ_FEET = 350
    BASE_LABOR_COST = 100
    LABOR_DIVIDER = 500

    total_dimensions = room_dimensions + ceiling_dimensions
    cans_needed = math.ceil(total_dimensions / PAINT_SQ_FEET)
    paint_cost = cans_needed * PAINT_CAN_COST

    labor_cost = math.ceil(total_dimensions / LABOR_DIVIDER) * BASE_LABOR_COST

    total_cost = paint_cost + labor_cost

    print(f"The user's total square feet is {total_dimensions}, labor cost is {labor_cost}, and the paint cost is {paint_cost}. Total cost is {total_cost}.")






def main():
    room_dimensions, ceiling_dimensions = roomDimensions()
    roomCost(room_dimensions, ceiling_dimensions)


if __name__ == "__main__":
    main()

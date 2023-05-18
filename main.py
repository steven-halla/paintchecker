

import math

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Sorry, your response must be a positive number.")
        except ValueError:
            print("Sorry, please enter a number.")


def roomDimensions() -> tuple[float, float, float, int, int, int]:
    PAINT_CAN_COST: float = 25
    PAINT_SQ_FEET: int = 350
    BASE_LABOR_COST: int = 100
    LABOR_DIVIDER: int = 500

    door_sq_feet: float = 14.5
    window_sq_feet: float = 9

    room_length_input: float = get_positive_float("Please enter the room length: ")
    room_width_input: float = get_positive_float("Please enter the room width: ")
    room_height_input: float = get_positive_float("Please enter the room height: ")
    room_dimensions: float = room_length_input * room_width_input * room_height_input

    door_number: int = -1
    while door_number < 0:
        try:
            door_number = int(input("Please enter the number of doors in the room: "))
            if door_number < 0:
                print("Sorry, the number of doors must be a non-negative integer.")
        except ValueError:
            print("Sorry, the number of doors must be a non-negative integer.")

    window_number: int = -1
    while window_number < 0:
        try:
            window_number = int(input("Please enter the number of windows in the room: "))
            if window_number < 0:
                print("Sorry, the number of windows must be a non-negative integer.")
        except ValueError:
            print("Sorry, the number of windows must be a non-negative integer.")

    total_door_sqft: float = door_number * door_sq_feet
    total_window_sqft: float = window_number * window_sq_feet

    room_dimensions -= total_door_sqft + total_window_sqft

    print(f"The dimensions of your room after subtracting doors and windows are: {room_dimensions} sq feet.")

    paint_ceiling_input: str = ""
    while paint_ceiling_input.lower() not in ["yes", "no"]:
        paint_ceiling_input = input("Do you want to paint the ceiling (yes/no): ").lower()
        if paint_ceiling_input.lower() not in ["yes", "no"]:
            print("Sorry, please enter 'yes' or 'no'.")

    if paint_ceiling_input.lower() == "yes":
        ceiling_length_input: float = get_positive_float("What is the ceiling length: ")
        ceiling_width_input: float = get_positive_float("What is the ceiling width: ")
        ceiling_dimensions: float = ceiling_width_input * ceiling_length_input
        print(f"The dimensions of your ceiling are: {ceiling_dimensions}")
    else:
        ceiling_dimensions: float = 0  # If not painting the ceiling, its dimensions are 0

    return room_dimensions, ceiling_dimensions, PAINT_CAN_COST, PAINT_SQ_FEET, BASE_LABOR_COST, LABOR_DIVIDER


def roomCost(
    room_dimensions: float,
    ceiling_dimensions: float,
    PAINT_CAN_COST: float,
    PAINT_SQ_FEET: int,
    BASE_LABOR_COST: int,
    LABOR_DIVIDER: int
) -> None:
    TAX: float = 0.105
    total_dimensions: float = room_dimensions + ceiling_dimensions
    cans_needed: int = math.ceil(total_dimensions / PAINT_SQ_FEET)
    paint_cost: float = cans_needed * PAINT_CAN_COST

    labor_cost: int = math.ceil(total_dimensions / LABOR_DIVIDER) * BASE_LABOR_COST

    subtotal_cost: float = paint_cost + labor_cost
    total_cost: float = subtotal_cost + (subtotal_cost * TAX)

    print(
        f"The user's total square feet is {total_dimensions}, labor cost is {labor_cost}, paint cost is {paint_cost}.")
    print(f"Subtotal cost (before tax) is {subtotal_cost}, and the total cost (including tax) is {total_cost}.")


def main() -> None:
    room_dimensions, ceiling_dimensions, PAINT_CAN_COST, PAINT_SQ_FEET, BASE_LABOR_COST, LABOR_DIVIDER = roomDimensions()
    roomCost(room_dimensions, ceiling_dimensions, PAINT_CAN_COST, PAINT_SQ_FEET, BASE_LABOR_COST, LABOR_DIVIDER)


if __name__ == "__main__":
    main()


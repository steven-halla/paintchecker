# Steven Halla
# paint project
# Intro to programming CS 115

################################################################
# Project: pain project
# File: paint.py
# Description: This program asks for user input for their home dimensions.
# Author: Steven Halla
# Version: 1.0
# Date: May 17, 2023
################################################################

import math

################################################################
# Function: getPositiveFloat
# Description:  error handling so user input is a number
# Return:   float-value
# params    prompt:str
# Author: Steven halla
################################################################
def getPositiveFloat(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Sorry, your response must be a positive number.")
        except ValueError:
            print("Sorry, please enter a number.")

################################################################
# Function: roomDimensions
# Description:  get user inputs for room dimensions as well as ceiling
#               while loop to help with error handling
# Return:   tuple[float,float,float,int,int,int]
#           room_dimensions, ceiling_dimensions, PAINT_CAN_COST, PAINT_SQ_FEET,
#           BASE_LABOR_COST, LABOR_DIVIDER
# Author: Steven halla
################################################################

def roomDimensions() -> tuple[float, float, float, int, int, int]:
    PAINT_CAN_COST: float = 25
    PAINT_SQ_FEET: int = 350
    BASE_LABOR_COST: int = 100
    LABOR_DIVIDER: int = 500

    DOOR_SQ_FEET: float = 14.5
    WINDOW_SQ_FEET: float = 9

    room_length_input: float = getPositiveFloat("Please enter the room "
                                                "length: ")
    room_width_input: float = getPositiveFloat("Please enter the room"
                                               " width: ")
    room_height_input: float = getPositiveFloat("Please enter the room"
                                                " height: ")
    room_dimensions: float = room_length_input * room_width_input * \
                             room_height_input

    door_number: int = -1
    while door_number < 0:
        try:
            door_number = int(input("Please enter the number of doors in"
                                    " the room: "))
            if door_number < 0:
                print("Sorry, the number of doors must be a non-negative"
                      " integer.")
        except ValueError:
            print("Sorry, the number of doors must be a non-negative integer.")

    window_number: int = -1
    while window_number < 0:
        try:
            window_number = int(input("Please enter the number of windows "
                                      "in the room: "))
            if window_number < 0:
                print("Sorry, the number of windows must be a non-negative"
                      " integer.")
        except ValueError:
            print("Sorry, the number of windows must be a non-negative "
                  "integer.")

    total_door_sqft: float = door_number * DOOR_SQ_FEET
    total_window_sqft: float = window_number * WINDOW_SQ_FEET

    room_dimensions -= total_door_sqft + total_window_sqft

    print(f"The dimensions of your room after subtracting doors and windows"
          f" are: {room_dimensions} sq feet.")

    paint_ceiling_input: str = ""
    while paint_ceiling_input.lower() not in ["yes", "no"]:
        paint_ceiling_input = input("Do you want to paint the "
                                    "ceiling (yes/no): ").lower()
        if paint_ceiling_input.lower() not in ["yes", "no"]:
            print("Sorry, please enter 'yes' or 'no'.")

    if paint_ceiling_input.lower() == "yes":
        ceiling_length_input: float = getPositiveFloat("What is the ceiling "
                                                       "length: ")
        ceiling_width_input: float = getPositiveFloat("What is the ceiling "
                                                      "width: ")
        ceiling_dimensions: float = ceiling_width_input * ceiling_length_input
        print(f"The dimensions of your ceiling are: {ceiling_dimensions}")
    else:
        ceiling_dimensions: float = 0

    return room_dimensions, ceiling_dimensions, PAINT_CAN_COST, PAINT_SQ_FEET,\
        BASE_LABOR_COST, LABOR_DIVIDER

################################################################
# Function: roomCost
# Description:  calculates total cost based on labor, paint cans used,
#               and taxes.
# params:       room_dimensions, ceiling_dimensions,PAINT_CAN_COST,
#               PAINT_SQ_FEET, BASE_LABOR_COST, LABOR_DIVIDER
# Author: Steven halla
################################################################

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


    labor_cost: int = math.ceil(total_dimensions / LABOR_DIVIDER) *\
                      BASE_LABOR_COST

    subtotal_cost: float = paint_cost + labor_cost
    total_cost: float = subtotal_cost + (subtotal_cost * TAX)

    print(
        f"The user's total square feet is {total_dimensions}, labor cost is "
        f"{labor_cost},total cans of paint used is {cans_needed}, and the  "
        f"paint cost is {paint_cost}.")
    print(f"Subtotal cost (before tax) is {subtotal_cost}, and the total "
          f"cost (including tax) is {total_cost}.")


################################################################
# Function: main
# Description:  fires up our function calls in our program
# Author: Steven halla
################################################################
def main() -> None:
    room_dimensions, ceiling_dimensions, PAINT_CAN_COST, PAINT_SQ_FEET,\
        BASE_LABOR_COST, LABOR_DIVIDER = roomDimensions()
    roomCost(room_dimensions, ceiling_dimensions, PAINT_CAN_COST,
             PAINT_SQ_FEET, BASE_LABOR_COST, LABOR_DIVIDER)


if __name__ == "__main__":
    main()


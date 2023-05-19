# Steven Halla
# bowling
# Intro to programming CS 115

################################################################
# Project: bowling
# File: bowling.py
# Description: Ask user for 3 bowling scores,user validation included
# Author: Steven Halla
# Version: 1.0
# Date: May 18, 2023
################################################################


import math

################################################################
# Function: validateInput
# Description:  error handling so user input is a number not above or below
#               300
# params    prompt:int
# Author: Steven halla
################################################################
def validateInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 300:
                return value
            else:
                print("Invalid input. Please enter a number between 0 and 300.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


################################################################
# Function: getUserScore
# Description:  user enters 3 scrores
# return:       score_one, score_two, score_three
# Author: Steven halla
################################################################
def getUserScore():
    score_one = validateInput("Enter score 1: "
                               "Please enter a number between 0-300: ")
    score_two = validateInput("Enter score 2:"
                               " Please enter a number between 0-300: ")
    score_three = validateInput("Enter score "
                                 "3: Please enter a number between 0-300: ")
    print(f"Your scores entered are: Score 1:"
          f" {score_one}, Score 2: {score_two}, Score 3: {score_three}")
    return score_one, score_two, score_three

################################################################
# Function: getScoreAverage
# Description:  takes 3 scores, math ceiling, and averages them
# param:       score_one, score_two, score_three
# Author: Steven halla
################################################################
def getScoreAverage(score_one, score_two, score_three):
    score_average = math.ceil((score_one + score_two + score_three) / 3)
    print(f"Your average score is: {score_average}")

################################################################
# Function: main
# Description:  fires up our program
# Author: Steven halla
################################################################

def main():
    scores = getUserScore()
    getScoreAverage(scores[0], scores[1], scores[2])


if __name__ == "__main__":
    main()


import math

def get_user_score():
    score_one = int(input("Enter score 1: Please enter a number between 0-300 "))
    score_two = int(input("Enter score 2: Please enter a number between 0-300 "))
    score_three = int(input("Enter score 3: Please enter a number between 0-300 "))
    print(f"Your scores entered are: Score 1: {score_one}, Score 2: {score_two}, Score 3: {score_three}")
    return score_one, score_two, score_three


def get_score_average(score_one, score_two, score_three):
    score_average = math.ceil((score_one + score_two + score_three) / 3)
    print(f"Your average score is: {score_average}")


def main():
    scores = get_user_score()
    get_score_average(scores[0], scores[1], scores[2])


if __name__ == "__main__":
    main()

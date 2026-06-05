import random


players = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]


def main() -> None:
    print(f"Initial list of players: {players}")
    c_players = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {c_players}")
    c_only = [x for x in players if x.capitalize() == x]
    print(f"New list of capitalized names only: {c_only}")
    score_dict = {k: random.randint(0, 1000) for k in c_players}
    print(f"Score dict: {score_dict}")
    average_score = sum(score_dict.values()) / len(score_dict.values())
    print(f"Score average is {round(average_score, 2)}")
    high_score = {k: v for k, v in score_dict.items() if v > average_score}
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()

import random

achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                "Collector Supreme", "Untouchable", "Boss Slayer",
                "Strategist", "Unstoppable", "Speed Runner",
                "Survivor", "Treasure Hunter", "First Steps",
                "Sharp Mind"]


def gen_player_achievements() -> set[str]:
    achvs: set[str] = set()
    ach_len = len(achievements)
    low_ach_possible = round(ach_len/2)
    big_ach_possible = round(ach_len)
    n_ach = random.randint(low_ach_possible, big_ach_possible)
    i = 0
    while i < n_ach:
        rand_ach = achievements[random.randint(0, ach_len - 1)]
        achvs.add(rand_ach)
        i += 1
    return achvs


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player_list: list[list[str | set[str]]] = [["Alice", set()],
                                               ["Bob", set()],
                                               ["Charlie", set()],
                                               ["Dylan", set()]]
    union_achvs: set[str] = set()
    common_achvs = set(achievements)
    for player in player_list:
        player[1] = gen_player_achievements()
        print(f"Player {player[0]}: {player[1]}")
        union_achvs = union_achvs.union(player[1])
        common_achvs = common_achvs.intersection(player[1])
    print(f"\nAll distinct achievements: {union_achvs}")
    print(f"\nCommon achievements: {common_achvs}")
    print("")
    for player1 in player_list:
        unique_achvs: set[str] = set()
        unique_achvs = set(player1[1])
        for player2 in player_list:
            if player1[0] != player2[0]:
                unique_achvs = unique_achvs.difference(player2[1])
        print(f"Only {player1[0]} has: {unique_achvs}")
    all_achvs = set(achievements)
    print("")
    for player in player_list:
        print(f"{player[0]} is missing: {all_achvs.difference(player[1])}")

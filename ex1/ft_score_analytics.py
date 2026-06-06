import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    total_players = len(scores)
    if total_players > 0:
        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {sum(scores)}")
        # average_score = sum(scores) / total_players
        print(f"Average score: {sum(scores) / total_players}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")
    else:
        print("No scores provided.", end=' ')
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")

import typing
import random


players = ["bob", "alice", "dylan", "charlie"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players_len = len(players)
    actions_len = len(actions)
    while True:
        rand_player = players[random.randint(0, players_len - 1)]
        rand_action = actions[random.randint(0, actions_len - 1)]
        yield (rand_player, rand_action)


def consume_event(event_list:
                  list[tuple[str, str]]) -> typing.Generator[tuple[str, str],
                                                             None, None]:
    while event_list:
        event_id = random.randint(0, len(event_list) - 1)
        rand_event = event_list[event_id]
        event_list.remove(rand_event)
        yield rand_event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for i in range(1000):
        next_event = next(event)
        print(f"Event {i}: Player {next_event[0]} did action {next_event[1]}")
    event_list = []
    event_num = 10
    for i in range(event_num):
        event_list.append(next(event))
    print(f"Built list of {event_num} events: {event_list}")
    for rand_event in consume_event(event_list):
        print(f"Got event from list: {rand_event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()

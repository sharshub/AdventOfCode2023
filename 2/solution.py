from collections import defaultdict

TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14


def main():
    result1 = 0
    result2 = 0

    with open("./2/input.txt") as f:
        lines = f.readlines()

        for line in lines:
            game_id, game_outcomes = get_game_and_outcomes(line)

            if is_reveals_possible(game_outcomes):
                result1 += game_id

            result2 += get_game_power(game_outcomes)

    print("answer1:", result1)
    print("answer2:", result2)


def get_game_and_outcomes(line: str) -> tuple[int, list[defaultdict[str, int]]]:
    idx_colon = line.find(":")
    game_id = int(line[:idx_colon].split(" ")[1])

    game_reveal_strs = line[idx_colon + 1 :].split(";")

    reveals = get_game_reveals(game_reveal_strs)

    return [game_id, reveals]


def get_game_reveals(game_reveal_strs):
    result = []
    for s in game_reveal_strs:
        reveals = s.strip().split(", ")
        reveal_result = defaultdict(int)
        for reveal in reveals:
            count_str, color = reveal.split(" ")
            count = int(count_str)
            reveal_result[color] = count
        result.append(reveal_result)
    return result


def is_reveals_possible(reveals: list[defaultdict[str, int]]) -> bool:
    res = True
    for reveal in reveals:
        count_red = reveal["red"]
        count_green = reveal["green"]
        count_blue = reveal["blue"]
        res = (
            res
            and (count_red <= TOTAL_RED)
            and (count_green <= TOTAL_GREEN)
            and (count_blue <= TOTAL_BLUE)
        )
    return res


def get_game_power(game_outcomes: list[defaultdict[str, int]]) -> int:
    red_max = 0
    green_max = 0
    blue_max = 0

    for game_outcome in game_outcomes:
        red_max = max(red_max, game_outcome["red"])
        green_max = max(green_max, game_outcome["green"])
        blue_max = max(blue_max, game_outcome["blue"])

    return red_max * green_max * blue_max


main()
